p='/workspace/toledo-safety-digest/email-2026-10-14.txt'
t=open(p).read()
LINK='https://github.com/coattails-droid/toledo-safety-digest/blob/main/digest-2026-10-14.txt'
def rep(a,b):
    global t
    assert a in t, a[:70]
    t=t.replace(a,b)
rep("\nMEASLES (top","- Lot codes, site lists and full details: "+LINK+"\n\nMEASLES (top")
rep("  - Full site details: "+LINK+"\n","")
t=t.replace("  - Lot codes and full details: "+LINK+"\n","  - Lot codes and full details: full file (link at top).\n")
rep(" Lot codes and full details: "+LINK," Lots in full file.")
rep(" (advisory still dated Oct 9; unchanged Oct 14). https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026"," (FDA advisory still dated Oct 9; unchanged Oct 14).")
rep(" for refund; dispose. https://www.romorgniz.store/recall.html"," for refund; dispose.")
rep(" email photo to support@theconqueror.events. https://www.cpsc.gov/Recalls/2027/The-Conqueror-Recalls-Avengers-Medals-Due-to-Risk-of-Serious-Injury-or-Death-from-Magnet-Ingestion-Violate-Mandatory-Standard-for-Magnets"," email photo to support@theconqueror.events.")
rep("  - Reliability note: AI aggregator pages dated Oct 11–12 (\"Explosions Rock Brent Industries…\") recycle the Aug 18 blast. No new explosion reported by local news, city or fire. Ignore AI recycles.","  - Reliability note: AI aggregator pages claiming new Brent explosions recycle the Aug 18 blast; no new explosion reported.")
rep(" could cause life-threatening clots or vessel blockage if injected. Hospital-only blood thinner (NDC 42023-182-01 / -89), shipped Dec 30, 2024-May 5, 2026; not sold in stores. Hospitals return via Inmar 1-855-648-7909; questions Par Health 1-800-828-9393."," risk of life-threatening clots or vessel blockage. Hospital-only blood thinner (NDC 42023-182-01/-89), shipped Dec 2024-May 2026; not sold in stores. Hospitals return via Inmar 1-855-648-7909; questions 1-800-828-9393.")
rep(" (via https://www.13abc.com/2026/10/13/lucas-co-wants-know-what-you-think-about-emergency-alert-system/)","")
rep("; the Blade reports it will reopen after the repair, but no reopening time was confirmed. Check the court website or your notice before going.","; Blade says it will reopen after repair (time unconfirmed). Check the court site or your notice.")
rep("  - Weather: storms possible early, then cloudy, high ~70; storms Thursday night; windy showers Friday (gusts ~37 mph).\n","")
rep(" Sensitive people should ease heavy outdoor exertion. No Toledo AQI forecast posted for today or tomorrow."," No AQI forecast posted for today or tomorrow.")
rep("  - Gripe water alcohols and kids' product recalls above remain active. Keep cannabis edibles locked away from candy.\n","  - Kids' recalls above remain active; keep cannabis edibles locked away from candy.\n")
open(p,'w').write(t); print(len(t))
