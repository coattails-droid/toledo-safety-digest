#!/usr/bin/env python3
"""Toledo daily safety digest, run from GitHub Actions (no Grok Bot usage).

Standard library only. Two subcommands:
  generate  research + write digest-YYYY-MM-DD.txt, email-YYYY-MM-DD.txt,
            email-subject-YYYY-MM-DD.txt (America/New_York date)
  send      email today's email-*.txt via Gmail SMTP (run AFTER the files are pushed)

Env:
  DIGEST_PROVIDER  openai | anthropic | xai   (default openai)
  DIGEST_MODEL     optional model override
  OPENAI_API_KEY / ANTHROPIC_API_KEY / XAI_API_KEY
  GMAIL_USER, GMAIL_APP_PASSWORD, DIGEST_TO (all from repo secrets)
  FORCE=true       regenerate even if today's digest file already exists
  DIGEST_MOCK=1    skip the LLM call and use canned text (local testing only)
  GITHUB_OUTPUT    (set by Actions) receives status=generated|skipped|error
"""
import datetime as dt
import glob
import json
import os
import re
import smtplib
import ssl
import sys
import urllib.error
import urllib.request
from email.message import EmailMessage
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_URL = "https://github.com/coattails-droid/toledo-safety-digest/blob/main"
EMAIL_LIMIT = 25000
DEFAULT_MODELS = {"openai": "gpt-5.5", "anthropic": "claude-opus-5-5", "xai": "grok-4.3"}
KEY_VARS = {"openai": "OPENAI_API_KEY", "anthropic": "ANTHROPIC_API_KEY", "xai": "XAI_API_KEY"}
PLACEHOLDER_RE = re.compile(r"\b(TODO|TBD|PLACEHOLDER|lorem ipsum|\[insert|XX:XX)\b", re.I)


def log(msg):
    print(msg, flush=True)


def set_output(key, value):
    path = os.environ.get("GITHUB_OUTPUT")
    if path:
        with open(path, "a") as f:
            f.write(f"{key}={value}\n")


def today_ny():
    return dt.datetime.now(ZoneInfo("America/New_York")).date()


def paths(day):
    s = day.isoformat()
    return (os.path.join(ROOT, f"digest-{s}.txt"),
            os.path.join(ROOT, f"email-{s}.txt"),
            os.path.join(ROOT, f"email-subject-{s}.txt"))


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def prior_digest(day):
    files = sorted(f for f in glob.glob(os.path.join(ROOT, "digest-20*.txt"))
                   if os.path.basename(f) < f"digest-{day.isoformat()}.txt")
    return (os.path.basename(files[-1]), read(files[-1])) if files else ("(none)", "")


def build_prompt(day, directive, prior_name, prior_text):
    s = day.isoformat()
    pretty = day.strftime("%A, %B %-d, %Y")
    subj_date = day.strftime("%b %-d, %Y")
    link = f"{REPO_URL}/digest-{s}.txt"
    return f"""You write C T's daily Toledo, Ohio safety digest for {pretty} (America/New_York).
Follow the DIRECTIVE below exactly: every numbered section in it (currently 1-25), the priority layout
(summary; Measles right after the summary when measles news is active, with only AMBER/endangered
missing-person alerts ahead of it; Needs attention; Worth knowing (Toledo); Emerging Tech Watch;
All clear / no change, which always lists Maumee River, Lake Erie, Air and Fog; Sky last), the rules
and the style. Use web search thoroughly for news from the last 24-48 hours. Never invent
incidents, readings, closures, cases or events; if you could not confirm something, say so.
Carry forward every still-active item from the PRIOR DIGEST, marked "(ongoing)" or "(updated)",
and re-verify it. Every item needs a source URL. Fully bulleted with sub-bullets, no paragraphs.

Produce THREE parts, in this order, each starting with its marker line exactly:
===SUBJECT===
One line: "Toledo Daily Digest - {subj_date} - <n> new items" (or "- all clear" on a quiet day,
or "- ACTION: <thing>" when something needs action today).
===EMAIL===
The plain-text email body, UNDER {EMAIL_LIMIT - 1500} characters. First line:
"Toledo Daily Digest + Emerging Tech Watch - {pretty}". Long lot/UPC/NDC/model/VIN lists,
long exposure-site lists and extended background go ONLY in the full digest; in the email write
"Lot codes and full details: {link}". Include that link in the SUMMARY section.
===DIGEST===
The full digest file (no length limit), same structure with all details, codes and sources.

No placeholder text. No commentary outside the three parts.

===== DIRECTIVE.md =====
{directive}

===== PRIOR DIGEST ({prior_name}) =====
{prior_text}
"""


def http_json(url, headers, payload, timeout=1500):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST",
                                 headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"HTTP {e.code} from {url}: {e.read().decode(errors='replace')[:2000]}")


def responses_api(base, key, model, prompt, tools, extra=None):
    """OpenAI Responses API; xAI exposes the same shape at api.x.ai/v1/responses."""
    payload = {"model": model, "input": prompt}
    if tools:
        payload["tools"] = tools
    payload.update(extra or {})
    data = http_json(f"{base}/responses", {"Authorization": f"Bearer {key}"}, payload)
    text = data.get("output_text") or "".join(
        c.get("text", "") for item in data.get("output", []) if item.get("type") == "message"
        for c in item.get("content", []) if c.get("type") == "output_text")
    log(f"usage: {json.dumps(data.get('usage', {}))}")
    return text


def xai_api(key, model, prompt, use_search):
    """xAI Chat Completions with Live Search, streamed.

    The Responses-API path failed twice in production testing: grok-4.3
    returned a ~1k-char stub through it, and grok-4.7 hung until the socket
    timed out at 1500s. Chat Completions + search_parameters is xAI's
    classic Live Search shape (one clean content string), and streaming
    keeps bytes flowing during long searches so nothing idles to death.
    """
    payload = {"model": model,
               "messages": [{"role": "user", "content": prompt}],
               "max_tokens": 16000,
               "stream": True,
               "stream_options": {"include_usage": True}}
    if use_search:
        payload["search_parameters"] = {
            "mode": "on", "return_citations": True, "max_search_results": 30,
            "sources": [{"type": "web"}, {"type": "news"}, {"type": "x"}]}
    req = urllib.request.Request(
        "https://api.x.ai/v1/chat/completions",
        data=json.dumps(payload).encode(), method="POST",
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {key}"})
    parts, usage = [], {}
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            for raw in r:
                line = raw.decode("utf-8", "replace").strip()
                if not line.startswith("data:"):
                    continue
                data = line[5:].strip()
                if data == "[DONE]":
                    break
                try:
                    chunk = json.loads(data)
                except ValueError:
                    continue
                if chunk.get("usage"):
                    usage = chunk["usage"]
                for choice in chunk.get("choices", []):
                    piece = (choice.get("delta") or {}).get("content")
                    if piece:
                        parts.append(piece)
    except urllib.error.HTTPError as e:
        raise RuntimeError(
            f"HTTP {e.code} from xAI chat completions: "
            f"{e.read().decode(errors='replace')[:2000]}")
    log(f"usage: {json.dumps(usage)}")
    return "".join(parts)


def anthropic_api(key, model, prompt, use_search):
    headers = {"x-api-key": key, "anthropic-version": "2023-06-01"}
    messages = [{"role": "user", "content": prompt}]
    tools = [{"type": "web_search_20250305", "name": "web_search", "max_uses": 40,
              "user_location": {"type": "approximate", "city": "Toledo", "region": "Ohio",
                                "country": "US", "timezone": "America/New_York"}}] if use_search else []
    out = []
    for _ in range(6):  # handle pause_turn continuations
        payload = {"model": model, "max_tokens": 32000, "messages": messages}
        if tools:
            payload["tools"] = tools
        data = http_json("https://api.anthropic.com/v1/messages", headers, payload)
        log(f"usage: {json.dumps(data.get('usage', {}))}")
        out = data.get("content", [])
        if data.get("stop_reason") != "pause_turn":
            break
        messages = [messages[0], {"role": "assistant", "content": out}]
    return "".join(b.get("text", "") for b in out if b.get("type") == "text")


def call_llm(prompt, use_search=True):
    if os.environ.get("DIGEST_MOCK") == "1":
        return mock_output()
    provider = os.environ.get("DIGEST_PROVIDER", "openai").strip().lower() or "openai"
    model = os.environ.get("DIGEST_MODEL", "").strip() or DEFAULT_MODELS[provider]
    key = os.environ[KEY_VARS[provider]]
    log(f"provider={provider} model={model} search={use_search}")
    if provider == "openai":
        tools = [{"type": "web_search", "user_location": {"type": "approximate", "city": "Toledo",
                  "region": "Ohio", "country": "US", "timezone": "America/New_York"}}] if use_search else None
        return responses_api("https://api.openai.com/v1", key, model, prompt, tools,
                             {"reasoning": {"effort": "medium"}})
    if provider == "xai":
        return xai_api(key, model, prompt, use_search)
    if provider == "anthropic":
        return anthropic_api(key, model, prompt, use_search)
    raise ValueError(f"unknown DIGEST_PROVIDER {provider!r}")


def split_parts(text):
    m = re.search(r"===SUBJECT===\s*(.*?)\s*===EMAIL===\s*(.*?)\s*===DIGEST===\s*(.*)\Z", text, re.S)
    if not m:
        raise RuntimeError("model output missing ===SUBJECT===/===EMAIL===/===DIGEST=== markers")
    subject = m.group(1).strip().splitlines()[0].strip()
    return subject, m.group(2).strip() + "\n", m.group(3).strip() + "\n"


def problems(subject, email, digest, link):
    errs = []
    if not subject.startswith("Toledo Daily Digest - "):
        errs.append(f"bad subject: {subject!r}")
    if len(email) >= EMAIL_LIMIT:
        errs.append(f"email is {len(email)} chars (limit {EMAIL_LIMIT})")
    if link not in email:
        errs.append("email lacks the digest link")
    for name, body in (("email", email), ("digest", digest)):
        if PLACEHOLDER_RE.search(body):
            errs.append(f"{name} contains placeholder text: {PLACEHOLDER_RE.search(body).group(0)!r}")
    if len(digest) < 2000:
        errs.append(f"digest suspiciously short ({len(digest)} chars)")
    return errs


def _attempt(prompt, link):
    text = call_llm(prompt)
    log(f"raw model output: {len(text)} chars; head: {text[:240]!r}")
    subject, email, digest = split_parts(text)
    errs = problems(subject, email, digest, link)
    if any("chars (limit" in e for e in errs):  # one cheap no-search shortening pass
        log("email too long; asking the model to shorten it")
        short = call_llm(f"Shorten this email body to under {EMAIL_LIMIT - 2000} characters. Keep every "
                         f"item, bullets and source links; move lists and background out (they are in "
                         f"{link}). Return only the email body.\n\n{email}", use_search=False)
        email = short.strip() + "\n"
        errs = problems(subject, email, digest, link)
    return subject, email, digest, errs


def generate():
    day = today_ny()
    digest_p, email_p, subj_p = paths(day)
    force = os.environ.get("FORCE", "").lower() == "true"
    if os.path.exists(digest_p) and not force:
        log(f"{os.path.basename(digest_p)} already exists; skipping (use force to regenerate).")
        set_output("status", "skipped")
        return 0
    link = f"{REPO_URL}/digest-{day.isoformat()}.txt"
    prior_name, prior_text = prior_digest(day)
    prompt = build_prompt(day, read(os.path.join(ROOT, "DIRECTIVE.md")), prior_name, prior_text)
    try:
        subject, email, digest, errs = _attempt(prompt, link)
    except Exception as e:  # a dead API call becomes a failed attempt, not a dead run
        subject, email, digest = "", "", ""
        errs = [f"generation call failed: {e}"]
    if errs:  # one full retry with the required format spelled out (model output varies run to run)
        log("first attempt failed checks; retrying once with the format reinforced:\n  " + "\n  ".join(errs))
        retry_prompt = (prompt + "\n\n===== FORMAT REMINDER (a previous attempt failed validation) =====\n"
                        "Return EXACTLY three sections, in order, marked ===SUBJECT===, ===EMAIL===, "
                        "===DIGEST===. The subject line must begin 'Toledo Daily Digest - '. The EMAIL "
                        f"section is the short summary and must stay under {EMAIL_LIMIT} characters; put "
                        "the full detail in the DIGEST section (the long version). Never put a markdown "
                        "bold marker on its own line.")
        try:
            subject, email, digest, errs = _attempt(retry_prompt, link)
        except Exception as e:
            errs = errs + [f"retry call failed: {e}"]
    if errs:
        log("ERROR: output failed checks, nothing written:\n  " + "\n  ".join(errs))
        set_output("status", "error")
        return 1
    for p, body in ((digest_p, digest), (email_p, email), (subj_p, subject + "\n")):
        with open(p, "w", encoding="utf-8") as f:
            f.write(body)
    log(f"wrote {os.path.basename(digest_p)} ({len(digest)} chars), email {len(email)} chars, subject: {subject}")
    set_output("status", "generated")
    return 0


def send():
    day = today_ny()
    _, email_p, subj_p = paths(day)
    user, pw = os.environ.get("GMAIL_USER", ""), os.environ.get("GMAIL_APP_PASSWORD", "")
    to = os.environ.get("DIGEST_TO", "").strip() or user
    if not (user and pw):
        log("ERROR: missing secret GMAIL_USER or GMAIL_APP_PASSWORD; not sending.")
        return 1
    msg = EmailMessage()
    msg["From"], msg["To"], msg["Subject"] = user, to, read(subj_p).strip()
    msg.set_content(read(email_p))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as s:
        s.login(user, pw.replace(" ", ""))
        s.send_message(msg)
    log(f"sent '{msg['Subject']}' to the DIGEST_TO recipient")
    return 0


def mock_output():
    day = today_ny()
    link = f"{REPO_URL}/digest-{day.isoformat()}.txt"
    bullets = "".join(f"- Mock item {i}\n  - What: mock test entry\n  - Source: https://example.org/{i}\n"
                      for i in range(60))
    return (f"===SUBJECT===\nToledo Daily Digest - {day.strftime('%b %-d, %Y')} - 0 new items\n"
            f"===EMAIL===\nToledo Daily Digest + Emerging Tech Watch - {day:%A}\n\nSUMMARY\n"
            f"- Mock run.\n- Full details: {link}\n\n{bullets}"
            f"===DIGEST===\nFULL DIGEST (mock)\n\n{bullets}")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "generate":
        provider = os.environ.get("DIGEST_PROVIDER", "openai").strip().lower() or "openai"
        if os.environ.get("DIGEST_MOCK") != "1":
            if provider not in KEY_VARS:
                log(f"ERROR: DIGEST_PROVIDER must be openai, anthropic or xai (got {provider!r}).")
                set_output("status", "error")
                sys.exit(1)
            if not os.environ.get(KEY_VARS[provider]):
                log(f"ERROR: missing secret {KEY_VARS[provider]}; nothing generated.")
                set_output("status", "error")
                sys.exit(1)
        sys.exit(generate())
    if cmd == "send":
        sys.exit(send())
    print(__doc__)
    sys.exit(2)
