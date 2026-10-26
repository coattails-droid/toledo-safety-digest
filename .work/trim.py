p='/workspace/toledo-safety-digest/email-2026-10-14.txt'
t=open(p).read()
import re
def rep(a,b):
    global t
    assert a in t, a[:60]
    t=t.replace(a,b)
# 1 summary
s0=t.index('SUMMARY\n')+8; s1=t.index('\nMEASLES')
t=t[:s0]+"""- Nothing needs shelter-in-place, evacuation or a water order today, and there are no AMBER or endangered missing-person alerts. Measles: no new Ohio count until about Thu Oct 15 and no new NW Ohio sites; the watch for Wood County's Sep 23 sites ends today. Air is Moderate (PM2.5 AQI 65). New: a hospital-only argatroban recall, two recent Toyota/Lexus recalls (2026 RAV4 Plug-In Hybrid power loss; Grand Highlander and Lexus RX/TX steering knuckles), F-16 night flights through Thu, a VP Vance rally in Monroe, MI Thu, and Perrysburg e-bike path registration from Oct 15. Older recalls still need action if you own the items. Sky: cloudy tonight; best viewing Saturday night.
"""+t[s1:]
# 2 checklist quiet categories
a=t.index("  - Food and beverages: nothing new for OH/MI"); b=t.index("- Toyota and Lexus recalls")
t=t[:a]+"""  - Quiet categories (one all-clear): no new food and beverage, children's toys and products, car seat and stroller, battery/fire electronics, household appliance or clothing recalls Oct 12-14 (CPSC usually posts Thursdays); ongoing items above and below. https://www.cpsc.gov/Recalls

"""+t[b:]
rep("    - Ongoing: gripe water, eye drops, acetaminophen (above); RAPTURE pre-workout with DMAA (below).\n","")
# 3 Toyota
rep("  - Awareness: 2026 C-HR braking/battery software (~10,000, Sep 2); 2021-2025 Highlander second-row recliner expansion (~690,000, updated Sep 9). https://pressroom.toyota.com/toyota-recalls-certain-model-year-2026-c-hr-vehicles/\n","  - Older (awareness): 2026 C-HR braking software (Sep 2); 2021-2025 Highlander seat recliner expansion (Sep 9). Details in the full file.\n")
rep("    - Check VIN: https://www.nhtsa.gov/recalls or https://www.toyota.com/recall (Toyota 1-800-331-4331).\n","    - Check VIN at nhtsa.gov/recalls or toyota.com/recall (1-800-331-4331).\n")
rep("    - Check VIN: https://www.nhtsa.gov/recalls\n","")
# 4 rail
rep("  - Also: Vermilion NS coal car spill Oct 6 (coal, not hazmat); Ecorse MI pedestrian train strike Oct 4 (child died). Never cross between stopped trains.\n","  - Also: Vermilion coal car spill Oct 6 (not hazmat); Ecorse MI train strike Oct 4 (child died).\n")
# 5 lake erie
rep("  - Maumee Bay State Park beach: algal toxin advisory since mid-Sept (Sep 15 sample 24.4 µg/L); BeachGuard couldn't be re-checked today, so confirm before swimming. https://publicapps.odh.ohio.gov/beachguardpublic/beaches/153/advisories\n","  - Maumee Bay State Park beach: algal toxin advisory since mid-Sept; confirm on BeachGuard before swimming. https://publicapps.odh.ohio.gov/beachguardpublic/beaches/153/advisories\n")
# 6 roadwork ongoing
a=t.index("  - Ongoing: Woodville Rd work zone near I-280;"); b=t.index("\n",a)
t=t[:a]+"  - Ongoing: Woodville Rd near I-280; Toledo reconstruction closures; Huron St (Spitzer); Turnpike Maumee River bridge to ~Nov 15; Arlington Ave closed through 2028; Alexis Rd nights; Lucas Co roundabouts into late Oct. Live: https://ohgo.com/"+t[b:]
# 7 tech
rep("  - Recycled: an Oct 13 Telecom Gazette \"6G ISAC trial\" piece rewrites September's Samsung/Verizon Dallas 5G trial (AI-generated summary). Also thin, low-reliability reports: Nokia weighing Nvidia 6G chips; Samsung AI-RAN deals with KT and SK Telecom.\n","  - Recycled: an Oct 13 Telecom Gazette \"6G ISAC trial\" piece rewrites September's Samsung/Verizon 5G trial. Thin, low-reliability reports (Nokia/Nvidia, Samsung AI-RAN) are in the full file.\n")
rep("  - Ongoing: Malaysia Johor haze cloud seeding Oct 13 (weather mod, not SRM); EU Horizon call to detect rogue SRM (~€35M); ACP marine cloud brightening modeling paper; UK no deployment while ARIA research continues; Alaska Rainmaker context; Idaho/Missouri/Oklahoma cloud-seeding laws; federal H.R. 7452 (no floor action).\n","  - Ongoing: Malaysia Johor cloud seeding Oct 13 (weather mod, not SRM); EU call to detect rogue SRM (~€35M); ACP cloud brightening modeling paper; UK ARIA research, no deployment; state cloud-seeding laws; federal H.R. 7452 stalled.\n")
# 8 all clear trims
rep("- Recall categories with nothing new: food and beverages, children's products, car seats and strollers, battery/fire electronics, household appliances, clothing.\n","")
open(p,'w').write(t); print(len(t))
