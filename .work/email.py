E = open('/workspace/toledo-safety-digest/email-2026-10-13.txt').read().split('\n')
def L(a,b): return '\n'.join(E[a-1:b])
LINK='https://github.com/coattails-droid/toledo-safety-digest/blob/main/digest-2026-10-14.txt'
needs = L(7,96).replace('digest-2026-10-13.txt','digest-2026-10-14.txt')
needs = needs.replace("- Amazon Basic Care Extra Strength Acetaminophen 500 mg - discolored tablets (ongoing; FDA Oct 2)","- Amazon Basic Care Extra Strength Acetaminophen 500 mg - discolored tablets (ongoing; FDA Oct 2; news reminders Oct 13, no new FDA action)")
needs = needs.replace("  - FDA matched supplier lot W4105 to the outbreak strain: 32 sick in six states, 3 hospitalized (advisory updated Oct 9). https://www.medicaldaily.com/broccoli-sprouting-seed-recall-salmonella-outbreak-w4105-479826",
 "  - FDA matched supplier lot W4105 to the outbreak strain: 32 sick in six states, 3 hospitalized (advisory still dated Oct 9; unchanged Oct 14). https://www.fda.gov/food/outbreaks-foodborne-illness/outbreak-investigation-salmonella-sprouts-september-2026")
needs = needs.replace("(ongoing; last city update Oct 2)","(ongoing; last city update Oct 2; nothing newer Oct 14)")
head = open('/workspace/toledo-safety-digest/digest-2026-10-14.txt').read().split('\nMEASLES')[0]
body = head + """
MEASLES (top priority; ongoing, no new NW Ohio sites)
- Ohio statewide (ongoing; no new ODH count today)
  - 231 confirmed cases in 2026 (WOIO, Oct 11); ODH Oct 8: 228 in 21 counties (Geauga 50, Wayne 45, Ashtabula 41). Medina first case Oct 9; new Wayne and Morrow cases Oct 12. Next ODH update expected Thu Oct 15.
  - Reliability note: a Signal Cleveland story dated Oct 13-14 citing "180 cases in 14 counties" uses outdated Sep 23 figures.
  - Central Ohio context only: Kraft House No. 5, Powell, Oct 4, 11 a.m.-4 p.m. (watch to ~Oct 25).
  - Sources: https://www.cleveland19.com/2026/10/11/measles-cases-ohio-top-230-medina-county-reports-first-case-year/
    https://odh.ohio.gov/know-our-programs/infectious-diseases/statistics/statistics
- NW Ohio exposure sites still open (no new sites; Lucas, Wood, Hancock and Monroe MI checked Oct 14)
  - Wood County: BGSU Overman and/or Physical Science buildings, Sep 23, 9 a.m.-6:30 p.m. and Pagliai's Restaurant, Sep 23, 5-9 p.m. (watch ENDS TODAY, Oct 14); Wood County Hospital Emergency Department, Sep 24 8:30 p.m.-Sep 25 1:30 a.m. and Sep 25 6:30 a.m.-2:15 p.m. (watch to ~Oct 15-16); Falcon Health Center, Sep 28, 10 a.m.-2 p.m. (watch to ~Oct 19). Form: https://woodcountyhealth.org/measles-resources/
  - Hancock County (Findlay): NWO Urgent Care, Sep 29, 2:30-5:30 p.m.; Blanchard Valley Hospital Emergency Department, Sep 29, 3:30-6:30 p.m. (watch to ~Oct 20). Close Contact Investigation Form at hancockph.com.
  - Lucas County: nothing new (Amtrak Train 41 monitoring ended Oct 5). Monroe County, MI: no current exposures.
  - Full site details: """ + LINK + """
- What to do: watch for fever, runny nose, cough, red eyes, then rash, up to 21 days after exposure. Call ahead before going to a clinic or ER. Check your MMR status.

NEEDS ATTENTION
""" + needs + """

WORTH KNOWING (TOLEDO)
- Recalls by category (daily checklist)
  - Medications and supplements: NEW Par Health Argatroban Injection 250 mg/2.5 mL (Oct 13) - particles in 22 lots; could cause life-threatening clots or vessel blockage if injected. Hospital-only blood thinner (NDC 42023-182-01 / -89), shipped Dec 30, 2024-May 5, 2026; not sold in stores. Hospitals return via Inmar 1-855-648-7909; questions Par Health 1-800-828-9393. Lot codes and full details: """ + LINK + """
    - Source: https://specgx.mediaroom.com/2026-10-13-Par-Health-Issues-Voluntary-Nationwide-Recall-of-Argatroban-Injection-Due-to-the-Presence-of-Particulate-Matter
    - Ongoing: gripe water, eye drops, acetaminophen (above); RAPTURE pre-workout with DMAA (below).
  - Food and beverages: nothing new for OH/MI from FDA, USDA FSIS or Ohio Agriculture Oct 12-14; ongoing items above and below.
  - Children's toys and products: no new CPSC posts (latest Oct 8); ongoing kids' items above.
  - Car seats and strollers: no new NHTSA or CPSC recalls.
  - Electronics with battery or fire risk: nothing new; ongoing hand warmers, balloon pumps, floor lamps (above).
  - Household appliances: nothing new; ongoing Snow Peak fireplace inserts (below), DR Power mowers (above).
  - Clothing, footwear and wearables: no new recalls found.
  - All clear for quiet categories: no new food, kids' product, car seat/stroller, battery/fire electronics, appliance or clothing recalls Oct 12-14 (CPSC usually posts Thursdays). https://www.cpsc.gov/Recalls

- Toyota and Lexus recalls (first day of this section; recent recalls included)
  - NEW to digest: 2026 Toyota RAV4 Plug-In Hybrid - loss of drive power (Oct 7)
    - About 31,000 U.S. vehicles. A plug-in hybrid ECU fault can cut power or shut the system down at higher speeds, raising crash risk.
    - Remedy: free ECU software update; owner letters by early December. NHTSA 26V659000. Not a do-not-drive warning.
    - Check VIN: https://www.nhtsa.gov/recalls or https://www.toyota.com/recall (Toyota 1-800-331-4331).
    - Source: https://pressroom.toyota.com/toyota-recalls-certain-my2026-toyota-rav4-plug-in-hybrid-electric-vehicles/
  - NEW to digest: 2026 Grand Highlander (incl. Hybrid) and Lexus RX350/RX350h/RX500h/TX350/TX500h - front steering knuckles may crack (filed Sep 17)
    - 617 vehicles; loss of steering control risk. Dealers inspect and replace free; owner letters Nov 2. NHTSA 26V598000. Not a do-not-drive warning.
    - Check VIN: https://www.nhtsa.gov/recalls
    - Source: https://www.usatoday.com/recalls/automotive/NHTSA-26V598000/
  - Awareness: 2026 C-HR braking/battery software (~10,000, Sep 2); 2021-2025 Highlander second-row recliner expansion (~690,000, updated Sep 9). https://pressroom.toyota.com/toyota-recalls-certain-model-year-2026-c-hr-vehicles/

""" + L(110,114).replace('digest-2026-10-13.txt','digest-2026-10-14.txt').replace("  - No new FDA/CPSC recalls since Oct 12.","  - No new FDA/CPSC consumer recalls since Oct 12 (checked Oct 14).") + """

""" + L(116,118).replace("(ongoing; last update Oct 2)","(ongoing; last update Oct 2; nothing newer Oct 14)") + """

- Rail: fatal train-pickup crash, Albon Rd near Airport Hwy, Springfield Twp (ongoing; Sun Oct 11; no new OSHP update Oct 14)
  - OSHP: southbound pickup drove through lowered gates into a westbound train; driver Michael Jones, 57, of Monclova, died (no seatbelt). Investigation ongoing. Not a derailment; no hazmat or evacuation.
  - Never go around lowered gates.
  - Source: https://www.13abc.com/2026/10/12/man-killed-railroad-crash-albon-road/
- Rail context (updated): Michigan State Police say the Oct 7 Genoa Twp, MI incident (Coon Lake Rd closure) was a train striking and killing a 79-year-old pedestrian near Chilson and Brighton roads; not a derailment or hazmat. https://x.com/MSPFirstDist/status/2108201127644717395
  - Also: Vermilion NS coal car spill Oct 6 (coal, not hazmat); Ecorse MI pedestrian train strike Oct 4 (child died). Never cross between stopped trains.

""" + L(127,129) + """
  - No new poison center kids' product warnings Oct 12-14. https://www.poisoncenters.org/news-alerts
  - Reliability note: Ohio "bloody diarrhea outbreak" shigella headlines are overblown; CDC data show no Ohio surge (WOIO fact-check Oct 12). https://www.13abc.com/2026/10/12/flushing-out-facts-ohio-is-not-going-through-bloody-diarrhea-outbreak/

- Lake Erie (updated; NOAA HAB model Oct 14 6 a.m. ET)
  - Western-basin bloom still present; size not measured (clouds/wind). New Oct 13 satellite image added; band of low-medium concentrations Monroe MI to Leamington ON, patches possible near the MI/OH shore including Maumee Bay. Toxins below recreational limit; avoid scum.
  - Source: https://cdn.coastalscience.noaa.gov/hab-data/forecasts/LErie_forecast/web_latest/current_bulletin.pdf
  - Toledo tap water: city says safe; no boil advisory; microcystin tested weekly at Collins Park. https://toledo.oh.gov/residents/water/quality
  - Maumee Bay State Park beach: algal toxin advisory since mid-Sept (Sep 15 sample 24.4 µg/L); BeachGuard couldn't be re-checked today, so confirm before swimming. https://publicapps.odh.ohio.gov/beachguardpublic/beaches/153/advisories
  - No new U.S. EPA, Ohio EPA or EGLE western Lake Erie notices.

""" + L(137,140) + """

- Air (today)
  - (updated) 7 a.m. Oct 14: MODERATE, PM2.5 AQI 65 (ozone and PM10 Good). Sensitive people should ease heavy outdoor exertion. No Toledo AQI forecast posted for today or tomorrow. No ozone action day, smoke, refinery flaring or airborne hazmat notice. No outdoor mold count published (not guessing).
  - Weather: storms possible early, then cloudy, high ~70; storms Thursday night; windy showers Friday (gusts ~37 mph).
  - Source: https://www.airnow.gov/?city=Toledo&state=OH&country=USA

- Water mains and sewers
  - (updated) Lucas County Common Pleas Courthouse: leak found early Mon Oct 12, court closed Tue Oct 13; the Blade reports it will reopen after the repair, but no reopening time was confirmed. Check the court website or your notice before going. https://www.toledoblade.com/local/courts/2026/10/13/courthouse-reopen-after-water-repair/stories/20261013096
  - No other verified new main breaks, sewer collapses or sinkholes.

- Roadwork (next 7 days)
  - NEW: utility work closes part of Hamilton Street (Blade Oct 13; paywalled, extent and dates unconfirmed; check OHGO). https://www.toledoblade.com/local/transportation/2026/10/13/utility-work-closes-part-of-hamilton-street/stories/20261013090
  - NEW: Perrysburg requires registration of Class 1 and 2 e-bikes for bike-only and shared-use paths starting Thu Oct 15, non-residents included; free, in-person inspection. https://www.13abc.com/2026/10/13/perrysburg-require-registration-some-e-bikes-starting-thursday/
  - Wood County ODOT (ongoing): OH 199 north of US 6 closed through Fri Oct 16 (detour OH 105, Bowling Green Rd, US 6); SB I-75 near Bays Rd right lane through mid-Nov; US 20/Conant Perrysburg-Maumee bridge one lane each way; OH 235 at Kellogg all-way stop Oct 27. https://bgindependentmedia.org/odot-lists-road-and-bridge-projects-underway-in-wood-county/
  - Starts Fri: UT Stadium Drive closed morning Fri Oct 16 to morning Wed Oct 21 (South Glass Bowl Dr to Area 10 north entrance); Area 5 via Douglas Rd. https://news.utoledo.edu/index.php/10_09_2026/stadium-drive-to-close-oct-16-21-for-paving
  - US 20A/Strayer Rd roundabout, Monclova: still listed to reopen Fri Oct 16 (detour I-475, SR 2). https://livetrafik.com/us/report/5099533-road-work-planned-on-20a-at-strayer
  - Ongoing: Woodville Rd work zone near I-280; Toledo street reconstruction closures; Huron St downtown (Spitzer); Turnpike WB Maumee River bridge redecking through ~Nov 15; Executive Pkwy median; Arlington Ave Detroit-Woodsdale closed through 2028; Alexis Rd night resurfacing; Lucas Co roundabout Archbold-Whitehouse / Providence-Neapolis-Swanton into late Oct. Live: https://ohgo.com/

- Other local notices
  - NEW: 180th Fighter Wing F-16 night training through Thu Oct 15, weather permitting; takeoffs and landings until 10 p.m., with flares. Planned training, not an emergency. https://bgindependentmedia.org/ohio-air-national-guards-180th-fighter-wing-to-conduct-nighttime-training-flights-this-week/
  - NEW: Lucas County EMA survey on sirens, Wireless Emergency Alerts and Lucas County Alerts: https://arcg.is/X0uWi1 (via https://www.13abc.com/2026/10/13/lucas-co-wants-know-what-you-think-about-emergency-alert-system/)

""" + L(155,155) + """
  - No new local detections.

- Lawsuits (info only, not legal advice; ongoing)
  - Kroger Rx pricing settlement: exclusion by Oct 22, 2026 (8 days); claims by Dec 21; fairness hearing Jan 11, 2027. https://www.krogersavingsclubsettlement.com/
""" + L(159,159) + """

- Protests / civic (next 7 days)
  - No verified road-closing marches through Oct 21. Coca-Cola Teamsters picket ongoing (workplace, not street march).
  - NEW: Thu Oct 15, VP JD Vance midterm rally at LevelUp Training Complex, Monroe, MI; starts noon, remarks ~1:20 p.m.; RSVP required. Expect security and traffic near the venue; no road-closure notice. https://www.13abc.com/2026/10/12/vice-president-vance-speak-midterm-rally-monroe-thursday/
  - Sat Oct 17, 10 a.m.-noon: "No Kings: Vote Early Edition" sidewalk demo, Monroe St along Monroe between Harvest and Flanders (near Talmadge); billed peaceful. No police traffic notice yet. https://lucascountydemocraticparty.com/new-events/2026/10/17/no-kings-no-thrones-no-crowns
  - NEW: Sun Oct 18, 1-3 p.m.: "Immigration Solidarity Walk" (Toledo Immigrant Alliance), Sofia Quintero Art and Cultural Center, 1222 Broadway St. Route and size not given; no closure notice. Reliability: event listing only. https://allevents.in/toledo/immigration-solidarity-walk/200030798132112
  - Early voting ongoing: 3737 W. Sylvania Ave (Entrance C). https://toledovotes.com/early-absentee-voting-info/

EMERGING TECH WATCH
- Geoengineering
  - Ohio HB 290 / Michigan HB 4304: no new committee action (checked Oct 14). https://ohiohouse.gov/legislation/136/hb290/status
  - NEW: ARIA-funded sun-dimming governance simulations ended with no deal (WIRED Oct 12; report Oct 1). 35 players acting as governments, NGOs and companies; rivalry and sovereignty drove talks more than climate. Research exercise only; the plane, plume and Stardust "test" happened only in the game. Stardust's no-outdoor-tests pledge is the company's own claim. https://www.wired.com/story/they-war-gamed-dimming-the-sun-it-went-even-worse-than-you-think/
  - (updated) IMO announcement (Oct 13) restates the Oct 9 marine geoengineering precautionary frameworks; research only. https://www.energylivenews.com/2026/10/13/new-rules-make-marine-geoengineering-research-safer-for-sea-life/
  - Ongoing: Malaysia Johor haze cloud seeding Oct 13 (weather mod, not SRM); EU Horizon call to detect rogue SRM (~€35M); ACP marine cloud brightening modeling paper; UK no deployment while ARIA research continues; Alaska Rainmaker context; Idaho/Missouri/Oklahoma cloud-seeding laws; federal H.R. 7452 (no floor action).
  - Recycled: the UK Ministry of Defence sun-dimming research report is from Sep 13. "White House blocking sunlight" posts recycle the June 2023 research plan.

- Smart Dust
  - Ongoing: seed-sized injectable, battery-free wireless nerve stimulator (Science Advances, Oct 10; NYU Abu Dhabi + Cleveland Clinic Abu Dhabi). Preclinical only; no new follow-up. https://www.eegsignal.com/articles/seed-sized-injectable-stimulator-delivers-wireless-peripheral-neuromodulation-36f885a2
  - DustNet remains lab/animal stage. Reliability: claims of a first human "neural dust" implant in Jan 2026 remain unverified.

- 6G Cellular
  - NEW: 3GPP Release 20 6G study meetings Oct 12-16 (Jeju and Prague) on AI in the 6G core, voice-on-5G with data-on-6G, base-station sleep signals and 7 GHz carriers. Nothing decided this week; core architecture due November, first 6G work item planned for Feb 2027. https://3gpp-explorer.com/articles/6g-october-2026-meetings-preview/
  - NEW: network sensing (ISAC) moving into live trials (Mobile World Live Oct 12): Ericsson commits $100M; Pentagon FutureG office eyeing drone-swarm tracking; Verizon's FCC test license for a Los Angeles trial pending. Verizon says sensing can't identify individuals (company claim). Pre-6G trials. https://www.mobileworldlive.com/network-tech/feature-why-isac-is-moving-beyond-labs-to-live-trials/
  - Recycled: an Oct 13 Telecom Gazette "6G ISAC trial" piece rewrites September's Samsung/Verizon Dallas 5G trial (AI-generated summary). Also thin, low-reliability reports: Nokia weighing Nvidia 6G chips; Samsung AI-RAN deals with KT and SK Telecom.
  - Ongoing: FCC Oct 29 meeting agenda unchanged (25 MHz mid-band FNPRM, satellite-to-phone spectrum, 800 MHz for drones). https://www.fcc.gov/October2026 . Also 6G core debate, Tejas/Qualcomm ISAC demo, NTIA 7 GHz study by Dec, Auction 115 Apr 27, 2027.

ALL CLEAR / NO CHANGE
- Missing persons: no AMBER Alert in Ohio and no Endangered Missing alerts or police requests in Toledo, Lucas, Wood, NW Ohio or Monroe County, MI in the last 7 days. https://ohioamberplan.org/
- Recall categories with nothing new: food and beverages, children's products, car seats and strollers, battery/fire electronics, household appliances, clothing.
- Gas leaks: no new Columbia Gas emergencies, line strikes or explosions in Lucas/Wood. https://www.columbiagasohio.com/services/alert-center
- Hazmat: no new releases, shelter-in-place or evacuations.
- Rail: no derailments or rail hazmat releases in NW Ohio / SE Michigan.
- Drinking water and crops: no Toledo boil or do-not-drink advisory; no crop or livestock notices. https://toledo.oh.gov/residents/water/boil-advisories
- DUI checkpoints: no announced OVI checkpoints or saturation patrols in Lucas or Wood through Oct 21.
- Maumee River: no new incidents; dredging and Swan Creek advisory continue (above).
- Lake Erie: bloom still present; toxins below recreational limit; city water safe (above).
- Air: Moderate (PM2.5 AQI 65); no ozone, smoke or hazmat alerts; no mold count published.
- Smart Dust: nothing new in 48 hours.
- Geoengineering (Ohio/Michigan): HB 290 and HB 4304 unchanged.
- 6G (local): no Toledo, Ohio or Michigan tower or small-cell news.

SKY
- Moon: waxing crescent ~17% lit; sets 8:49 p.m. ET, low in the WSW near Antares. First Quarter Sun Oct 18.
- Aurora: none expected; NOAA max Kp 3.67 through Oct 16 (needs Kp 6). https://services.swpc.noaa.gov/text/3-day-forecast.txt
- ISS: best passes Sat Oct 17, 6:39-6:45 a.m. (very bright, up to 70°, WSW to NE) and Sun Oct 18, 5:54-5:57 a.m. (high in the east).
- Planets: Saturn all evening and night; Jupiter with Mars above it in the east before dawn.
- Orionids: peak mornings Oct 20-22, best Oct 21; watch from moonset (2:45 a.m. Oct 21) until dawn. https://science.nasa.gov/solar-system/meteors-meteorites/orionids/
- Clouds (correcting yesterday's "clear tonight"): mostly cloudy tonight; showers Thursday into Friday; Saturday night and Sunday morning look clearest. https://forecast.weather.gov/MapClick.php?lat=41.66&lon=-83.56

Full lot-code lists and extended detail: """ + LINK + "\n"
open('/workspace/toledo-safety-digest/email-2026-10-14.txt','w').write(body)
print(len(body))
