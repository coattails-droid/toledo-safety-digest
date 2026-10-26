import re
Y = open('/workspace/toledo-safety-digest/digest-2026-10-13.txt').read().split('\n')
def L(a,b): return '\n'.join(Y[a-1:b])
LINK='https://github.com/coattails-droid/toledo-safety-digest/blob/main/digest-2026-10-14.txt'

needs = L(7,133).replace('digest-2026-10-13.txt', 'digest-2026-10-14.txt')
needs = needs.replace("- Amazon Basic Care Extra Strength Acetaminophen 500 mg - discolored tablets (ongoing; FDA enforcement report Oct 2)",
 "- Amazon Basic Care Extra Strength Acetaminophen 500 mg - discolored tablets (ongoing; FDA enforcement report Oct 2; news reminders Oct 13, no new FDA action)")
needs = needs.replace("  - (updated from prior days) FDA outbreak advisory (last updated Oct 9, per Medical Daily Oct 11)",
 "  - (ongoing; FDA advisory still dated Oct 9, checked Oct 14, cases unchanged) FDA outbreak advisory")
needs = needs.replace("  - Source (update): https://www.medicaldaily.com/broccoli-sprouting-seed-recall-salmonella-outbreak-w4105-479826",
 "  - Source (outbreak): https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026")
needs = needs.replace("(ongoing; last city update Oct 2; no newer update found this morning)","(ongoing; last city update Oct 2; no newer update found Oct 14)")
needs = needs.replace("No new city update since Oct 2.","No new city update since Oct 2 (checked Oct 14).")

T = {}
T['head'] = """Toledo Daily Digest + Emerging Tech Watch - Wednesday, October 14, 2026

SUMMARY
- Nothing needs shelter-in-place, evacuation, or a water order today, and there are no AMBER or endangered missing-person alerts for the area. Measles is still active statewide (231 cases, no new Ohio count until about Thu Oct 15); no new NW Ohio exposure sites, and the watch for Wood County's Sep 23 BGSU and Pagliai's sites ends today. Air is Moderate (PM2.5 AQI 65). New today: a hospital-only argatroban injection recall, two recent Toyota/Lexus recalls (2026 RAV4 Plug-In Hybrid power loss; 2026 Grand Highlander and Lexus RX/TX steering knuckles), F-16 night training flights from Toledo's 180th Fighter Wing through Thu Oct 15, a VP Vance rally in Monroe, MI on Thu Oct 15, and Perrysburg e-bike path registration starting Oct 15. Active recalls (dressers, bikes, bath seats, swings, gripe water, eye drops, acetaminophen, broccoli seeds and more) still need action if you own them. Weather turns wet: storms early today, heavy showers Thursday night, windy Friday. Tech: ARIA-funded sun-dimming governance simulations ended with no deal (research exercise only); 3GPP 6G study meetings run Oct 12-16. Sky: cloudy tonight; best viewing Saturday night; ISS bright pass Sat Oct 17, 6:39 a.m.
"""
T['measles'] = """MEASLES (top priority; ongoing, no new NW Ohio sites)
- Ohio statewide (ongoing; no new ODH count today)
  - Latest: 231 confirmed cases in 2026 (WOIO, Oct 11), more than five times 2025's 45. ODH's Oct 8 tally was 228 in 21 counties; Geauga (50), Wayne (45) and Ashtabula (41) lead. Medina confirmed its first case Oct 9; Mansfield News Journal (Oct 12) reported new cases in Wayne and Morrow counties.
  - ODH's dashboard updates weekly, usually Thursday afternoon, so the next count is expected Thu Oct 15. The ODH statistics page did not load this morning.
  - Reliability note: a Signal Cleveland story dated Oct 13-14 cites "180 confirmed cases in 14 counties." That figure comes from Sep 23 meeting notes and is outdated.
  - Central Ohio context (not NW Ohio): Delaware County exposure at Kraft House No. 5, 5 S. Liberty St., Powell, Sun Oct 4, 11 a.m.-4 p.m.; watch through about Oct 25.
  - Sources: https://www.cleveland19.com/2026/10/11/measles-cases-ohio-top-230-medina-county-reports-first-case-year/
    https://www.dispatch.com/story/news/2026/10/08/measles-cases-ohio-grow-again-400-percent-rise-2025-numbers/92156056007/
    https://focalnews.org/columbus-oh/local/delaware-county-urges-powell-diners-to-watch-for-measles-symptoms-after-oct-4-exposure
    https://odh.ohio.gov/know-our-programs/infectious-diseases/statistics/statistics
- NW Ohio exposure sites still within their 21-day watch (no new sites; Lucas, Wood and Hancock health departments and Monroe County, MI checked Oct 14)
  - Wood County (Bowling Green) - form and updates at https://woodcountyhealth.org/measles-resources/
    - BGSU Overman and/or Physical Science buildings, Wed Sep 23, 9 a.m.-6:30 p.m. Watch ENDS TODAY, Oct 14 (last listing).
    - Pagliai's Restaurant, Wed Sep 23, 5-9 p.m. Watch ENDS TODAY, Oct 14 (last listing).
    - Wood County Hospital Emergency Department, Sep 24 8:30 p.m. to Sep 25 1:30 a.m., and Sep 25 6:30 a.m.-2:15 p.m. Watch through about Oct 15-16.
    - Falcon Health Center, Mon Sep 28, 10 a.m.-2 p.m. Watch through about Oct 19.
    - Source: https://woodcountyhealth.org/wp-content/uploads/2026/09/WCHD_Media-Release_Measles_UPDATED_93026.pdf
  - Hancock County (Findlay) - submit the Measles Close Contact Investigation Form at hancockph.com
    - NWO Urgent Care, Tue Sep 29, 2:30-5:30 p.m. Watch through about Oct 20.
    - Blanchard Valley Hospital Emergency Department, Tue Sep 29, 3:30-6:30 p.m. Watch through about Oct 20.
    - Source: https://www.hancockph.com/_files/ugd/e16ad6_36fc3f814bda4359b54cf0c429931109.pdf
  - Lucas County: nothing new. The Sep 13 Amtrak Train 41 traveler notice (Toledo station ~11:40 p.m.) ended its contact monitoring Oct 5; no spread announced. https://lucascountyhealth.com/
  - Monroe County, MI: no new exposure; its only 2026 notice (April) is long expired. https://www.co.monroe.mi.us/943/Measles
- What to do
  - Watch for fever, runny nose, cough and red watery eyes, then a rash from the hairline down, up to 21 days after exposure. People are contagious four days before and after the rash.
  - If symptoms start, call your doctor or the ER before going in. Check that your MMR vaccination is up to date.
"""
T['wk1'] = """WORTH KNOWING (TOLEDO)
- Recalls by category (daily checklist)
  - Medications and supplements
    - Par Health Argatroban Injection 250 mg/2.5 mL - particulate matter (NEW; announced Oct 13)
      - What happened: voluntary nationwide recall of 22 lots after particles (cellulose, polystyrene, PET, stopper material, possibly stainless steel) were found. Injecting it could cause life-threatening blood-vessel blockages, lung clots, organ damage or vein inflammation. No adverse events reported.
      - Product: argatroban, a hospital blood thinner (for heparin-induced thrombocytopenia and heart procedures); NDC 42023-182-01 and 42023-182-89. Hospital injectable only, not sold in stores.
      - Where and when: shipped nationwide to wholesalers and hospitals Dec 30, 2024 through May 5, 2026.
      - What to do: hospitals and wholesalers stop use and return through Inmar (1-855-648-7909, rxrecalls@inmar.com). Patients have no action unless their care team contacts them; medical questions to Par Health 1-800-828-9393.
      - Lot numbers: see "Argatroban lots" below.
      - Source: https://specgx.mediaroom.com/2026-10-13-Par-Health-Issues-Voluntary-Nationwide-Recall-of-Argatroban-Injection-Due-to-the-Presence-of-Particulate-Matter
    - Ongoing (above or below): Babies' Magic Tea gripe water, K.C. Pharmaceuticals store-brand eye drops, Amazon Basic Care acetaminophen (Needs attention); RAPTURE pre-workout with DMAA (below).
  - Food and beverages: nothing new from FDA, USDA FSIS or the Ohio Department of Agriculture Oct 12-14 for Ohio or Michigan. Ongoing items are listed in Needs attention (berries, broccoli and alfalfa seeds, Bettergoods Alfredo, Graziers cheese) and below.
  - Children's toys and products: no new CPSC posts (latest batch still Oct 8). Ongoing kids' items are in Needs attention.
  - Car seats and strollers: no new NHTSA or CPSC recalls.
  - Electronics with battery or fire risk: no new CPSC posts. Ongoing: HotHands and Gobi Heat rechargeable hand warmers, Dollar Tree balloon pumps, Cupcakes and Cashmere floor lamps.
  - Household appliances: no new CPSC posts. Ongoing: Snow Peak propane fireplace inserts (below), DR Power trimmer mowers (above).
  - Clothing, footwear and wearable accessories: no new CPSC, Health Canada or retailer recalls found.
  - Quiet categories all-clear: no new food and beverage, children's product, car seat or stroller, battery/fire electronics, household appliance or clothing recalls posted Oct 12-14 (CPSC usually posts Thursdays).
  - Source index: https://www.fda.gov/safety/recalls-market-withdrawals-safety-alerts
    https://www.cpsc.gov/Recalls
    https://www.fsis.usda.gov/recalls

- Toyota and Lexus recalls (first day of this section; recent recalls included)
  - 2026 Toyota RAV4 Plug-In Hybrid - loss of drive power (NEW to digest; announced Oct 7)
    - Models: certain model year 2026 RAV4 Plug-In Hybrid. About 31,000 U.S. vehicles.
    - Defect and risk: a fault in the plug-in hybrid system's electronic control unit (motor generator ECU) can cut power or shut the system down at higher speeds, raising crash risk.
    - Remedy: dealers update the ECU software free. Owner letters by early December 2026.
    - NHTSA campaign: 26V659000. Not a do-not-drive or park-outside warning.
    - Check your VIN: https://www.nhtsa.gov/recalls or https://www.toyota.com/recall ; Toyota 1-800-331-4331.
    - Sources: https://pressroom.toyota.com/toyota-recalls-certain-my2026-toyota-rav4-plug-in-hybrid-electric-vehicles/
      https://www.usatoday.com/recalls/automotive/NHTSA-26V659000/
  - 2026 Toyota Grand Highlander and Lexus RX/TX - front steering knuckles may crack (NEW to digest; filed Sep 17; owner letters Nov 2)
    - Models: 2026 Grand Highlander and Grand Highlander Hybrid; 2026 Lexus RX350, RX350h, RX500h, TX350, TX500h. 617 vehicles.
    - Defect and risk: a manufacturing error can let the front steering knuckles crack and break, causing loss of steering control.
    - Remedy: dealers inspect and replace the knuckles as needed, free. Owner letters expected Nov 2, 2026 (Toyota 26TA19, Lexus 26LA09).
    - NHTSA campaign: 26V598000. Not a do-not-drive warning.
    - Check your VIN: https://www.nhtsa.gov/recalls or https://www.toyota.com/recall
    - Source: https://www.usatoday.com/recalls/automotive/NHTSA-26V598000/
  - Older recent Toyota recalls (awareness): 2026 C-HR regenerative braking / battery overcharge software, about 10,000 vehicles (Sep 2; owners notified by early November) https://pressroom.toyota.com/toyota-recalls-certain-model-year-2026-c-hr-vehicles/ ; 2021-2025 Highlander second-row seat recliner expansion, about 690,000 total (updated Sep 9) https://pressroom.toyota.com/toyota-recalls-certain-my2021-2024-toyota-highlander-vehicles/

- Other ongoing recalls
"""
recalls_ongoing = L(154,180)
T['wk2'] = """  - No new FDA or CPSC consumer recalls posted since Oct 12 other than the hospital argatroban item (checked Oct 14).

- Hazmat
""" + L(184,188).replace('(ongoing; last update Oct 2; no newer update)','(ongoing; last update Oct 2; no newer update Oct 14)') + """

- Rail
  - Fatal train-pickup crash, Albon Road near Airport Highway, Springfield Township (ongoing; Sun Oct 11; no new OSHP update Oct 14)
    - What happened: per the Ohio State Highway Patrol, a southbound pickup drove through the lowered crossing gates and hit a westbound train. The driver, Michael Jones, 57, of Monclova, died; he was not wearing a seatbelt. OSHP is investigating (vehicle data download, toxicology).
    - Not a derailment; no hazmat release or evacuation reported.
    - What to do: never go around or through lowered gates.
    - Sources: https://www.13abc.com/2026/10/12/man-killed-railroad-crash-albon-road/
      https://www.wilx.com/2026/10/12/driver-killed-after-truck-strikes-train-railroad-crossing/
  - Genoa Township, Livingston County, MI rail incident (updated; Oct 7)
    - Michigan State Police say a 79-year-old Genoa Township woman was killed when struck by a train around 10:30 a.m. Oct 7 near Chilson Rd and Brighton Rd (the CSX incident that closed Coon Lake Rd). Not a derailment or hazmat. About 80 miles north of Toledo.
    - Source: https://x.com/MSPFirstDist/status/2108201127644717395
""" + L(197,199) + "\n" + L(203,205) + """

- Kids / Poison Control
""" + L(208,213) + """
  - No new America's Poison Centers, Ohio or Michigan poison center kids' product warnings Oct 12-14. https://www.poisoncenters.org/news-alerts
  - Reliability note (WOIO fact-check, Oct 12): headlines about an Ohio "bloody diarrhea" shigella outbreak are overblown; CDC data show no Ohio surge. https://www.13abc.com/2026/10/12/flushing-out-facts-ohio-is-not-going-through-bloody-diarrhea-outbreak/

- Lake Erie (updated)
  - NOAA HAB bulletin (model updated Oct 14, 6 a.m. ET)
    - Cyanobacteria bloom still in western Lake Erie; clouds or winds kept NOAA from measuring its size. The bulletin now includes an Oct 13 satellite image; forecast positions are given for Oct 15 and Oct 18.
    - Where: band of low to medium concentrations from Monroe, MI to Leamington, ON; patches may be near the Michigan and Ohio shore, including Maumee Bay.
    - Toxins detected below the recreational limit; scums can be highly concentrated.
    - What to do: keep yourself and pets out of any water with scum.
    - Source: https://cdn.coastalscience.noaa.gov/hab-data/forecasts/LErie_forecast/web_latest/current_bulletin.pdf
  - Toledo drinking water (ongoing): city says water is safe to drink; microcystin sampled weekly and analyzed Tuesdays at Collins Park. No boil advisory found.
    - Source: https://toledo.oh.gov/residents/water/quality
  - Maumee Bay State Park beach (ongoing): recreational algal toxin advisory since mid-September (latest indexed sample Sep 15: 24.4 µg/L microcystin). BeachGuard could not be re-checked this morning; confirm live status before swimming.
    - Source: https://publicapps.odh.ohio.gov/beachguardpublic/beaches/153/advisories
""" + L(226,227) + """
  - No new U.S. EPA, Ohio EPA or Michigan EGLE notices for western Lake Erie found.

- Maumee River (ongoing)
  - No new spill, fish kill or sewage notice in the last 48 hours.
""" + L(231,238) + """

- Air (today)
  - (updated) AirNow, 7 a.m. Oct 14: MODERATE, PM2.5 AQI 65 (main pollutant). Ozone 24 and PM10 26, both Good. Sensitive people should ease heavy outdoor exertion. TMACOG has not posted a forecast for today or tomorrow, so none is given here. No ozone action day, no smoke alert, no active NWS air alerts.
  - No refinery flaring or airborne hazmat notice for Toledo or Oregon.
  - Mold: no outdoor spore count published for Toledo today; not guessing.
  - Sources: https://www.airnow.gov/?city=Toledo&state=OH&country=USA
    https://files.airnowtech.org/airnow/today/reportingarea.dat

- Water mains and sewers
  - Lucas County Common Pleas Courthouse water leak (updated)
    - A significant water leak was found on the courthouse grounds early Mon Oct 12 and the court closed Tue Oct 13. The Blade reports the courthouse will reopen after the repair; no confirmed reopening time was found. Check the court website or your notice before going.
    - Sources: https://www.toledoblade.com/local/courts/2026/10/13/courthouse-reopen-after-water-repair/stories/20261013096
      https://wbnowqct.com/lucas-co-common-pleas-court-closed-today/
  - No other verified new main breaks, sewer collapses or sinkholes in Toledo's service area.

- Roadwork (next 7 days and ongoing)
  - Hamilton Street partly closed for utility work (NEW; Blade Oct 13)
    - Only the headline is available (paywalled); extent and dates not confirmed. Check OHGO before driving.
    - Source: https://www.toledoblade.com/local/transportation/2026/10/13/utility-work-closes-part-of-hamilton-street/stories/20261013090
  - Perrysburg e-bike registration for paths starts Thu Oct 15 (NEW; 13abc Oct 13)
    - Class 1 and 2 e-bikes must be registered before riding on Perrysburg's bike-only or shared-use paths, including non-residents. Registration is free but needs an in-person inspection.
    - Source: https://www.13abc.com/2026/10/13/perrysburg-require-registration-some-e-bikes-starting-thursday/
""" + L(256,262).replace("    - Overnight I-75 → I-475 ramp closure (2:30–5 a.m. Tue) has already passed.\n","") + """
  - University of Toledo Stadium Drive paving closure (ongoing; starts Fri)
    - Closed morning of Fri Oct 16 through morning of Wed Oct 21, from South Glass Bowl Drive to the north entrance of Area 10. Enter Area 5 from Douglas Road. Questions: Dan Perry, 419-530-1428.
    - Source: https://news.utoledo.edu/index.php/10_09_2026/stadium-drive-to-close-oct-16-21-for-paving
""" + L(267,278) + """
  - US 20A at Strayer Rd roundabout, Monclova Township near Maumee (ongoing; closed since Aug 17; still listed to reopen Fri Oct 16)
    - Detour: I-475 to SR 2/Airport Hwy and back to US 20A.
    - Source: https://livetrafik.com/us/report/5099533-road-work-planned-on-20a-at-strayer
""" + L(281,285) + """

- Other local notices
  - 180th Fighter Wing F-16 night training flights (NEW; Oct 13-15)
    - Ohio Air National Guard F-16s at Toledo Express are flying nighttime training through Thu Oct 15, weather permitting, with takeoffs and landings as late as 10 p.m. and use of flares. Planned training, not an emergency; expect jet noise in the evening.
    - Source: https://bgindependentmedia.org/ohio-air-national-guards-180th-fighter-wing-to-conduct-nighttime-training-flights-this-week/
  - Lucas County EMA emergency-alert survey (NEW)
    - The county wants feedback on sirens, Wireless Emergency Alerts and Lucas County Alerts through an online survey: https://arcg.is/X0uWi1
    - Source: https://www.13abc.com/2026/10/13/lucas-co-wants-know-what-you-think-about-emergency-alert-system/

- Invasive species (ongoing)
""" + L(288,291) + """
  - No new NW Ohio, Lake Erie or SE Michigan detections (the Oct 7 red swamp crayfish find is in Cass County, SW Michigan).

- Lawsuits and claim deadlines (information only, not legal advice; ongoing)
""" + L(294,299).replace("exclusion by Oct 22, 2026 (9 days away)","exclusion by Oct 22, 2026 (8 days away)") + """

- Protests, demonstrations and civic events (next 7 days)
  - No verified marches, rallies or strikes expected to close major Toledo-area roads through Oct 21.
  - VP JD Vance midterm rally, Monroe, MI (NEW; Thu Oct 15)
    - LevelUp Training Complex in Monroe; event starts at noon, remarks expected around 1:20 p.m.; RSVP required; hosted by the Trump 47 Committee. Expect security and traffic around the venue; no road-closure notice found.
    - Source: https://www.13abc.com/2026/10/12/vice-president-vance-speak-midterm-rally-monroe-thursday/
""" + L(303,304) + """
  - "Immigration Solidarity Walk" (NEW; Sun Oct 18, 1-3 p.m.)
    - Organized by Toledo Immigrant Alliance at the Sofia Quintero Art and Cultural Center, 1222 Broadway St; described as an interactive walk with stories about immigrant experiences. Route and size not given; no road-closure notice.
    - Reliability note: event listing only, not confirmed by police or organizer press.
    - Source: https://allevents.in/toledo/immigration-solidarity-walk/200030798132112
""" + L(305,308) + "\n"

T['tech'] = """EMERGING TECH WATCH
- Geoengineering
  - Ohio and Michigan bills (background, flagged first; no new action; checked Oct 14)
    - Ohio HB 290 Atmosphere Protection Act: still in House Natural Resources Committee (last action May 21, 2025). https://ohiohouse.gov/legislation/136/hb290/status
    - Michigan HB 4304: still in Regulatory Reform Committee (last action Mar 26, 2025). https://www.legislature.mi.gov/Bills/Bill?ObjectName=2025-HB-4304
  - Sun-dimming governance simulations end with no deal (NEW; WIRED Oct 12; report dated Oct 1)
    - What: in three two-day crisis simulations of solar radiation modification governance run by the University of Leeds, Queen Mary University of London and Imperial College and funded by the UK research agency ARIA, 35 academics and practitioners played governments, NGOs and companies. They never reached an agreement; the report says strategic competition and sovereignty drove the talks more than climate concerns, and misinformation broke down consensus.
    - Status: research exercise only. The plane, plume and Stardust "test" in the article happened only inside the game.
    - Confirmed vs. claimed: published report plus credible reporting (confirmed). Stardust's statement that it won't run large outdoor tests before global governance exists is the company's own claim.
    - Sources: https://www.wired.com/story/they-war-gamed-dimming-the-sun-it-went-even-worse-than-you-think/
      https://cfg.eu/negotiating-solar-radiation-modification-governance/
  - Marine geoengineering frameworks (updated; IMO announcement covered Oct 13)
    - Restates the Oct 9 London Convention/Protocol decision: precautionary assessment frameworks for ocean fertilization, ocean alkalinity enhancement and biomass sinking. Research only, not deployment.
    - Sources: https://www.energylivenews.com/2026/10/13/new-rules-make-marine-geoengineering-research-safer-for-sea-life/
      https://www.ciel.org/news/lc-lp-advances-precautionary-regime-marine-geoengineering/
  - Malaysia cloud seeding in Johor for haze (ongoing; Oct 13): weather modification, not SRM. https://www.thestar.com.my/news/nation/2026/10/13/haze-cloud-seeding-conducted-in-johor
  - EU Horizon Europe tender on detecting rogue sun-blocking efforts (ongoing; opened Oct 6): about €35 million for monitoring, detection and attribution of SRM; field experiments out of scope. https://www.energyconnects.com/news/renewables/2026/october/eu-wants-to-track-potential-rogue-efforts-to-block-out-sun/
  - Peer-reviewed marine cloud brightening modeling study (ongoing; ACP Oct 9): modeling only. https://doi.org/10.5194/acp-26-14111-2026
  - UK ARIA £56.8 million Exploring Climate Cooling research continues; no UK deployment planned (ongoing).
  - Recycled-story note: the report that the UK Ministry of Defence paid a consultancy to research sun-dimming (mentioned by WIRED) is from Sep 13, not this week. https://observer.co.uk/news/science-technology/article/mod-revealed-to-be-funding-research-into-sun-dimming-technology
""" + L(331,334) + """

- Smart Dust
""" + L(337,343).replace("(ongoing; Science Advances, published Oct 10; no new follow-up found this morning)","(ongoing; Science Advances, published Oct 10; no new follow-up Oct 14)") + """

- 6G Cellular
  - Ohio and Michigan: no new Toledo, Lucas County, Ohio or Michigan 6G sites, towers or small-cell permits found.
  - 3GPP 6G study meetings this week, Oct 12-16 (NEW)
    - Radio groups in Jeju, South Korea and core-network groups in Prague are working on Release 20 6G studies: where AI sits in the 6G core, letting phones keep voice on 5G while data runs on 6G, base-station sleep signals, and 200-400 MHz carriers at 7 GHz.
    - Status: in progress; nothing decided this week. The core architecture is due by November, the voice question at the December plenaries, and the first 6G work item is planned for approval in February 2027.
    - Confirmed vs. claimed: meeting schedule and proposals from public 3GPP document lists, per an independent explainer site; company positions are proposals, not votes.
    - Source: https://3gpp-explorer.com/articles/6g-october-2026-meetings-preview/
  - Network sensing (ISAC) moving into live trials (NEW; Mobile World Live Oct 12)
    - Ericsson has committed $100 million to integrated sensing and communication and expects a product within two years. The Pentagon's FutureG office is focused on using cell networks to track drone swarms. Verizon's request for an FCC experimental license for an Ericsson sensing test near Los Angeles is still pending.
    - Privacy angle: Verizon says the sensing returns shape, movement and size, not identity. That is the company's own claim.
    - Status: 5G-Advanced pre-6G trials, not a 6G launch. The $100 million and timelines are company statements.
    - Source: https://www.mobileworldlive.com/network-tech/feature-why-isac-is-moving-beyond-labs-to-live-trials/
    - Recycled-story note: a Telecom Gazette piece dated Oct 13 calling the Samsung/Verizon sensing trial "6G" rewrites the September Dallas 5G trial; the site labels its summaries AI-generated.
  - FCC Oct 29 open meeting (ongoing; agenda unchanged Oct 14)
    - FNPRM to auction 25 MHz of mid-band spectrum (1675-1695 and 2020-2025 MHz; terrestrial, direct-to-device or hybrid). Also on the agenda: satellite-to-phone (Supplemental Coverage from Space) spectrum, opening part of the 800 MHz band for drones, and limits on test labs in non-reciprocal countries. Votes not yet taken.
    - Source: https://www.fcc.gov/October2026
""" + L(350,357) + """
  - Low-weight reports (reliability note: AI-generated summaries on Telecom Gazette, thin detail): Nokia reportedly weighing Nvidia chips for 6G radios (Nokia confirms only that it is evaluating); Samsung AI-RAN agreements with KT and SK Telecom (no details disclosed).
    - https://telecomgazette.com/articles/nokia-weighs-nvidia-partnership-for-6g-radio-development-dece836b
"""
T['clear'] = """ALL CLEAR / NO CHANGE
- Missing persons: no AMBER Alert in Ohio (none issued in 2026) and no Endangered Missing alerts or police requests in Toledo, Lucas or Wood counties, NW Ohio or Monroe County, MI in the last 7 days.
  - Sources: https://ohioamberplan.org/
    https://www.ohioattorneygeneral.gov/Law-Enforcement/Local-Law-Enforcement/Ohio-Missing-Persons/Missing-Persons-Alerts
- Recall categories with nothing new: food and beverages, children's toys and products, car seats and strollers, battery/fire electronics, household appliances, clothing (details above).
- Kids / Poison Control: no new kids' product warnings (ongoing items above).
- Gas leaks: no new Columbia Gas emergencies, line strikes or gas explosions in Lucas or Wood counties (the Oct 12 line strike was in Upper Arlington near Columbus).
  - Source: https://www.columbiagasohio.com/services/alert-center
- Hazmat: no new releases, shelter-in-place or evacuations; Cherry Oil and Brent Industries unchanged (above).
- Rail: no derailments or rail hazmat releases in NW Ohio or SE Michigan.
- Drinking water and crops: no boil or do-not-drink advisory for Toledo found; no crop or livestock contamination notices. (The Oct 13 boil advisory in search results is Buckeye Water in eastern Ohio.)
  - Sources: https://toledo.oh.gov/residents/water/boil-advisories
- DUI checkpoints: no officially announced OVI checkpoints or saturation patrols in Lucas or Wood counties through Oct 21.
  - Source: https://statepatrol.ohio.gov/media/all-news
- Invasive species: no new local detections (lanternfly reminder above).
- Maumee River: no new incidents; dredging and the Swan Creek advisory continue (above).
- Lake Erie: bloom still present; toxins below recreational limit; city water safe (above).
- Air: Moderate this morning (PM2.5 AQI 65); no ozone, smoke or hazmat alerts; no mold count published (above).
- Smart Dust: nothing new in 48 hours; the Oct 10 stimulator paper is still the latest (above).
- Geoengineering (Ohio and Michigan): HB 290 and HB 4304 unchanged.
- 6G (local): no Toledo, Ohio or Michigan tower or small-cell news.

SKY
- Moon: waxing crescent, about 17% lit; sets 8:49 p.m. ET tonight, low in the west-southwest after sunset near the star Antares. First Quarter Sun Oct 18 at 12:13 p.m.; Full Hunter's Moon Oct 26 at 12:11 a.m.
  - Source: https://www.timeanddate.com/moon/usa/toledo
- Aurora: none expected. NOAA's highest forecast Kp through Oct 16 is 3.67 with no storms expected, well under the Kp 6 needed for northern Ohio.
  - Source: https://services.swpc.noaa.gov/text/3-day-forecast.txt
- ISS: best passes Sat Oct 17, 6:39-6:45 a.m. (very bright, rising WSW to 70° high, setting NE) and Sun Oct 18, 5:54-5:57 a.m. (appears high in the east). Thursday's 6:36 a.m. pass will likely be clouded out.
  - Source: https://www.heavens-above.com/PassSummary.aspx?satid=25544&lat=41.6639&lng=-83.5552&loc=Toledo&alt=180&tz=EST
- Planets: Saturn up all evening and night (rings well placed after its Oct 4 opposition); bright Jupiter with red Mars above it in the east before dawn. Naked eye.
- Orionid meteors: peak mornings of Oct 20-22, best Oct 21 (10-20 per hour under dark skies). A bright Moon washes out the hours after midnight, so watch from moonset (2:45 a.m. Oct 21, 3:51 a.m. Oct 22) until dawn.
  - Sources: https://earthsky.org/astronomy-essentials/visible-planets-tonight-mars-jupiter-venus-saturn-mercury/
    https://science.nasa.gov/solar-system/meteors-meteorites/orionids/
- Comets: none bright enough for binoculars.
- Clouds (correction to yesterday's "clear tonight"): NWS now says mostly cloudy tonight, low 53. Showers and storms Thursday into Thursday night, windy showers Friday (gusts to about 37 mph), then clear Saturday night and sunny Sunday, the best viewing window this week.
  - Source: https://forecast.weather.gov/MapClick.php?lat=41.66&lon=-83.56
"""
lists = L(386,410) + """

Argatroban lots (Par Health, Oct 13, 2026; lot - expiration):
- NDC 42023-182-01: 83449 (10/2026), 82682 (11/2026), 86714 (02/2027), 87302 (02/2027), 87560 (02/2027), 87753 (03/2027), 88401 (03/2027), 88614 (04/2027), 88836 (04/2027), 90220 (05/2027), 91216 (06/2027), 91219 (06/2027), 92004 (07/2027), 92006 (07/2027), 92009 (08/2027), 92596 (08/2027), 92782 (08/2027), 93107 (08/2027), 93329 (08/2027), 93890 (09/2027)
- NDC 42023-182-89: 84193 (10/2026), 92880 (08/2027)

Sources checked (Oct 14 morning): FDA recalls page and Salmonella sprouts outbreak page (still Oct 9), CPSC (latest Oct 8), USDA FSIS, Par Health press release, Toyota pressroom and NHTSA campaign mirrors, America's Poison Centers, Ohio AMBER Plan, Ohio AG missing-persons alerts, Wood County, Hancock and Lucas County health departments, Monroe County MI, NOAA NCCOS HAB bulletin (Oct 14 6 a.m.), AirNow (PM2.5 AQI 65), NWS Cleveland forecast, SWPC 3-day forecast, timeanddate, EarthSky, NASA, Heavens-Above, Ohio House HB 290 and Michigan HB 4304, WIRED, CFG report, 3GPP meeting explainer, Mobile World Live, FCC October 2026 meeting page, local outlets (13abc, WTOL, BG Independent, Blade headlines). Carry-forward details from digest-2026-10-13.txt. Nothing here is invented; verify recall details on the linked notices before acting.
"""
full = T['head'] + "\n" + T['measles'] + "\nNEEDS ATTENTION\n" + needs + "\n\n" + T['wk1'] + recalls_ongoing + "\n" + T['wk2'] + "\n" + T['tech'] + "\n" + T['clear'] + "\n" + lists.replace('digest-2026-10-13','digest-2026-10-14')
open('/workspace/toledo-safety-digest/digest-2026-10-14.txt','w').write(full)
print(len(full))
