p='/workspace/toledo-safety-digest/email-2026-10-14.txt'
t=open(p).read()
def rep(a,b):
    global t
    assert a in t, a[:70]
    t=t.replace(a,b)
rep("  - Also: Vermilion coal car spill Oct 6 (not hazmat); Ecorse MI train strike Oct 4 (child died).\n","  - Also (context): Vermilion coal spill Oct 6; Ecorse MI train strike Oct 4.\n")
rep("(Blade Oct 13; paywalled, extent and dates unconfirmed; check OHGO)","(Blade Oct 13; details unconfirmed; check OHGO)")
rep("requires registration of Class 1 and 2 e-bikes for bike-only and shared-use paths starting Thu Oct 15, non-residents included; free, in-person inspection.","requires Class 1-2 e-bike registration for its paths from Thu Oct 15 (non-residents too; free, in-person).")
rep(", weather permitting; takeoffs and landings until 10 p.m., with flares. Planned training, not an emergency."," until 10 p.m., with flares. Planned training, not an emergency.")
rep("All 88 Ohio counties quarantined; SE Michigan including Monroe has confirmed populations. Scrape egg masses into soapy water/alcohol; check vehicles/firewood/gear.","Ohio-wide quarantine; Monroe MI has populations. Scrape egg masses into soapy water; check vehicles and firewood.")
rep("Full lot-code lists and extended detail: ","Full details: ")
open(p,'w').write(t); print(len(t))
