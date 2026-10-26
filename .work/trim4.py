p='/workspace/toledo-safety-digest/email-2026-10-14.txt'
t=open(p).read()
def rep(a,b):
    global t
    assert a in t, a[:70]
    t=t.replace(a,b)
rep("- 6G (local):","- Smart Dust: nothing new in 48 hours.\n- 6G (local):")
rep(" White or black wood, ~27.6×15.6×43.2 in.","")
rep(" Models 8911304, 8911305, 8911308, 8929130.","")
rep(" Never leave a baby unattended in a bath.","")
rep("  - Hit-and-run Sep 20; gasoline line leak + broken sewer lateral found; station closed; EPA/city oversight continues. No newer update.\n","  - Hit-and-run Sep 20; leak and broken sewer lateral found; station closed; EPA/city oversight continues.\n")
rep("  - Reliability note: a Signal Cleveland story dated Oct 13-14 citing \"180 cases in 14 counties\" uses outdated Sep 23 figures.\n","  - Reliability note: a new story citing \"180 cases in 14 counties\" uses outdated Sep 23 figures.\n")
rep("  - Central Ohio context only: Kraft House No. 5, Powell, Oct 4, 11 a.m.-4 p.m. (watch to ~Oct 25).\n","")
rep("; starts noon, remarks ~1:20 p.m.; RSVP required. Expect security and traffic near the venue; no road-closure notice.","; starts noon; expect security and traffic, no closure notice.")
rep(" sidewalk demo, Monroe St along Monroe between Harvest and Flanders (near Talmadge); billed peaceful. No police traffic notice yet."," sidewalk demo on Monroe St between Harvest and Flanders; billed peaceful; no traffic notice.")
rep(" (Toledo Immigrant Alliance), Sofia Quintero Art and Cultural Center, 1222 Broadway St. Route and size not given; no closure notice. Reliability: event listing only."," at Sofia Quintero Center, 1222 Broadway; no closure notice. Reliability: event listing only.")
rep("(very bright, up to 70°, WSW to NE)","(very bright, WSW to NE)")
rep("; SB I-75 near Bays Rd right lane through mid-Nov; US 20/Conant Perrysburg-Maumee bridge one lane each way; OH 235 at Kellogg all-way stop Oct 27.","; SB I-75 near Bays Rd right lane to mid-Nov; US 20 Perrysburg-Maumee bridge one lane each way; OH 235 at Kellogg all-way stop Oct 27.")
rep(" Older recalls still need action if you own the items."," Older recalls still active.")
open(p,'w').write(t); print(len(t))
