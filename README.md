# toledo-safety-digest

This repo is a reference copy of the standing directive behind C T's daily Toledo, Ohio safety digest, which Raenie (Grok Bot) runs every morning at 7:30 AM ET.

The directive itself is in [DIRECTIVE.md](DIRECTIVE.md).

## Automated run (GitHub Actions)

The digest is moving off the Grok Bot routine to the workflow [`.github/workflows/daily-digest.yml`](.github/workflows/daily-digest.yml), which runs [`scripts/run_digest.py`](scripts/run_digest.py) (Python 3 standard library only).

**How it works**
- Cron fires at 11:30 and 12:30 UTC every day. A gate step continues only when the New York local hour is 7, so exactly one run proceeds around 7:30 AM ET in both EDT and EST. GitHub can delay scheduled runs, sometimes 5–30+ minutes.
- If today's `digest-YYYY-MM-DD.txt` (New York date) already exists, the run skips, so nothing is sent twice.
- `generate` reads `DIRECTIVE.md` and the latest prior digest (for ongoing items), asks the chosen LLM (with web search) for the subject, the email body (under 25,000 characters) and the full digest, checks the result (length, link, no placeholders), and writes `digest-`, `email-` and `email-subject-YYYY-MM-DD.txt`.
- The workflow commits and pushes those files as `github-actions[bot]`, then `send` emails the body through Gmail SMTP (smtp.gmail.com:465).
- If a required secret is missing, the run ends green with a "Missing secret(s)" warning and sends nothing.

**Secrets** (Settings > Secrets and variables > Actions > Secrets)
- One LLM key matching the provider: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` or `XAI_API_KEY`
- `GMAIL_USER` (the sending Gmail address) and `GMAIL_APP_PASSWORD` (a Google app password; needs 2-Step Verification on the account)

**Variables** (same page, Variables tab; all optional)
- `DIGEST_PROVIDER`: `openai` (default), `anthropic` or `xai`
- `DIGEST_MODEL`: model override. Defaults: openai `gpt-5.5`, anthropic `claude-opus-5-5`, xai `grok-4.7`
- `DIGEST_TO`: recipient address (repo secret; falls back to GMAIL_USER)

**Manual run:** Actions tab > "Daily Toledo digest" > Run workflow. `dry_run` writes and commits the files without emailing. `force` regenerates even if today's file exists (and, without `dry_run`, emails again). From the CLI: `gh workflow run daily-digest.yml -f dry_run=true`.

**Local test without keys:** `DIGEST_MOCK=1 FORCE=true python3 scripts/run_digest.py generate` (overwrites today's files with mock text; don't commit them).
