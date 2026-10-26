p='/workspace/toledo-safety-digest/email-2026-10-14.txt'
t=open(p).read()
def rep(a,b):
    global t
    assert a in t, a[:70]
    t=t.replace(a,b)
rep("  - Limited geography (not OH/MI retail): Starfish Seafood Trio Listeria (NY/FL/GA/MA/NC/SC); Oliva hummus/sesame (CT/MA); Nature's Own Hawaiian Bread milk (AR/LA/NM/OK/TX); Brevital hospital injectable (not OTC).\n","  - Limited-geography items (not OH/MI retail) are listed in the full file.\n")
rep("  - NEW: ARIA-funded sun-dimming governance simulations ended with no deal (WIRED Oct 12; report Oct 1). 35 players acting as governments, NGOs and companies; rivalry and sovereignty drove talks more than climate. Research exercise only; the plane, plume and Stardust \"test\" happened only in the game. Stardust's no-outdoor-tests pledge is the company's own claim.",
    "  - NEW: UK ARIA-funded sun-dimming governance simulations ended with no deal (WIRED Oct 12). Rivalry and sovereignty drove talks more than climate. Research exercise only; the plane, plume and Stardust \"test\" happened only in the game.")
rep("  - Recycled: the UK Ministry of Defence sun-dimming research report is from Sep 13. \"White House blocking sunlight\" posts recycle the June 2023 research plan.\n","  - Recycled: UK MoD sun-dimming research story is from Sep 13; \"White House blocking sunlight\" posts recycle a 2023 plan.\n")
rep(" on AI in the 6G core, voice-on-5G with data-on-6G, base-station sleep signals and 7 GHz carriers. Nothing decided this week; core architecture due November, first 6G work item planned for Feb 2027."," on AI in the 6G core and 7 GHz carriers. Nothing decided; core architecture due November.")
rep(": Ericsson commits $100M; Pentagon FutureG office eyeing drone-swarm tracking; Verizon's FCC test license for a Los Angeles trial pending. Verizon says sensing can't identify individuals (company claim). Pre-6G trials.",": Ericsson commits $100M; Pentagon eyeing drone tracking; Verizon's LA test license pending. Verizon says sensing can't identify people (company claim). Pre-6G.")
rep(" (25 MHz mid-band FNPRM, satellite-to-phone spectrum, 800 MHz for drones). https://www.fcc.gov/October2026 . Also 6G core debate, Tejas/Qualcomm ISAC demo, NTIA 7 GHz study by Dec, Auction 115 Apr 27, 2027."," (25 MHz mid-band, satellite-to-phone, 800 MHz drones). https://www.fcc.gov/October2026 . Also NTIA 7 GHz study by Dec; Auction 115 Apr 27, 2027.")
rep("  - DustNet remains lab/animal stage. Reliability: claims of a first human \"neural dust\" implant in Jan 2026 remain unverified.\n","  - Reliability: claims of a first human \"neural dust\" implant remain unverified.\n")
rep("  - Benadryl Challenge / \"Benny tripping\": high-dose diphenhydramine can cause seizures, heart rhythm problems, coma, death. Lock up OTC meds. Poison Control 1-800-222-1222; 911 for breathing trouble / hard-to-wake / seizures.","  - Benadryl Challenge: high-dose diphenhydramine can cause seizures, heart problems, death. Lock up OTC meds. Poison Control 1-800-222-1222.")
rep("  - Reliability note: Ohio \"bloody diarrhea outbreak\" shigella headlines are overblown; CDC data show no Ohio surge (WOIO fact-check Oct 12). https://www.13abc.com/2026/10/12/flushing-out-facts-ohio-is-not-going-through-bloody-diarrhea-outbreak/\n","  - Reliability note: Ohio shigella \"outbreak\" headlines are overblown; no Ohio surge (WOIO fact-check Oct 12).\n")
rep("- Smart Dust: nothing new in 48 hours.\n","")
rep("- Geoengineering (Ohio/Michigan): HB 290 and HB 4304 unchanged.\n","")
rep("- Hazmat: no new releases, shelter-in-place or evacuations.\n","- Hazmat: nothing new.\n")
rep("  - Toledo Harbor dredging ongoing (began Oct 2; ~750,000 cy into late 2026/early 2027). Give work vessels room.","  - Toledo Harbor dredging ongoing into early 2027; give work vessels room.")
open(p,'w').write(t); print(len(t))
