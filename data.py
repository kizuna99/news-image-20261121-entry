"""Day data — Saturday 21 November 2026 (all items verified as reported that
day; see SOURCES.md). Consumed by render.py."""

DAY = {
    "date_long": "Saturday 21 November 2026",
    "dayline": "DAY 325 OF 2026",
    "ticker": "Iran strikes Bahrain as tankers hit in Hormuz  ◆  Drones set "
              "Russian cargo ship ablaze off Finland  ◆  COP31 deadlocked "
              "over fossil fuels in overtime",
    "count_line": "40 STORIES · 9 REGIONS · EVERY ONE DATED SATURDAY "
                  "21 NOVEMBER 2026",
    "stats": [
        ("2", "tankers attacked off Khasab, Hormuz", "UKMTO"),
        ("130+", "countries want fossil fuels named", "AFP"),
        ("730m", "people in the EU–Indonesia trade area", "EU COMMISSION"),
        ("700k", "people displaced in southern Ethiopia", "FRANCE 24"),
        ("$5m", "FBI reward on ‘El Chapo Isidro’", "FBI"),
        ("8 yrs", "BepiColombo’s flight to Mercury", "ESA"),
    ],
    "regions": [
        ("Europe", 9), ("Middle East", 4), ("Americas", 11), ("Africa", 6),
        ("South Asia", 1), ("East Asia", 3), ("South-East Asia", 1),
        ("Oceania", 2), ("Global", 3),
    ],
    "timeline": [
        (0.01, "00:09 M6.7 Junín"),
        (0.28, "06:50 Sparta II alarm"),
        (0.40, "09:42 M6.8 Banda Sea"),
        (0.52, "12:12 EU–Indonesia signing"),
        (0.76, "18:24 BepiColombo orbit"),
        (0.93, "22:00 COP31 pause"),
    ],
    "leads": [
        {
            "art": "gulf", "chip": "IRAN STRIKES BAHRAIN",
            "chip_r": "2 TANKERS HIT",
            "kicker": "1 · BAHRAIN / HORMUZ · CONFLICT", "badge": "CONFIRMED",
            "headline": "Iran strikes Bahrain as tankers hit in Hormuz",
            "summary": "An Iranian attack set a civilian industrial site "
                       "ablaze — no one hurt. IRGC says it hit US positions; "
                       "two tankers attacked off Khasab.",
            "sources": "AL JAZEERA · REUTERS · AFP",
        },
        {
            "art": "ship", "chip": "06:50 UTC · TWO DRONES, CREW TAKEN OFF",
            "chip_r": "",
            "kicker": "2 · GULF OF FINLAND · CONFLICT", "badge": "CONFIRMED",
            "headline": "Drones set Russian cargo ship ablaze off Finland",
            "summary": "Sparta II, bound for Kaliningrad, was hit about "
                       "06:50 UTC and drifted into Finnish waters; crew "
                       "evacuated. Finland: Ukraine likely behind it.",
            "sources": "BBC · FRANCE 24 · MOSCOW TIMES",
        },
        {
            "art": "cop", "chip": "COP31 · ANTALYA", "chip_r": "OVERTIME",
            "kicker": "3 · COP31, ANTALYA · CLIMATE", "badge": "CONFIRMED",
            "headline": "COP31 deadlocked over fossil fuels in overtime",
            "summary": "A day past deadline, talks paused overnight. EU "
                       "and Pacific states reject a draft omitting fossil "
                       "fuels; 130+ want them named.",
            "sources": "BBC · AFP · FRANCE 24",
        },
    ],
    "cards": [
        {"n": 4, "tag": "SINALOA · SECURITY", "badge": "CONFIRMED",
         "stat": "11", "note": "DEAD",
         "headline": "Mexico seizes ‘El Chapo Isidro’",
         "detail": "Army raid in Sinaloa; 11 dead in clashes",
         "sources": "GUARDIAN · DW · NYT"},
        {"n": 5, "tag": "KRYVYI RIH · WAR", "badge": "CONFIRMED",
         "stat": "2", "note": "KILLED",
         "headline": "Missile kills 2 in Zelenskyy’s hometown",
         "detail": "Ballistic strike on the city centre wounds ~60",
         "sources": "AL JAZEERA · FRANCE 24"},
        {"n": 6, "tag": "WALL STREET · MARKETS", "badge": "CONFIRMED",
         "stat": "10%", "note": "CORRECTION",
         "headline": "AI sell-off puts US stocks in correction",
         "detail": "S&P, Dow correct; Anthropic IPO stumbles",
         "sources": "GUARDIAN · BBC · UPI"},
        {"n": 7, "tag": "JUNÍN, PERU · QUAKE", "badge": "OFFICIAL",
         "stat": "M6.7", "note": "00:09 UTC",
         "headline": "Deep quake shakes Peru’s Andes",
         "detail": "Felt in Lima; 1 dead, 16 hurt, ~850 affected",
         "sources": "USGS · UPI"},
        {"n": 8, "tag": "BRUSSELS · TRADE", "badge": "CONFIRMED",
         "stat": "98.5%", "note": "OF TARIFFS LIFTED",
         "headline": "EU and Indonesia sign trade pact",
         "detail": "After 10 years; 730m people in the area",
         "sources": "DW · AFP · ANTARA"},
        {"n": 9, "tag": "FRANCE · PROTEST", "badge": "CONFIRMED",
         "stat": "144", "note": "ARRESTED",
         "headline": "Cost-of-living protests: France & Portugal",
         "detail": "Sixth Saturday of marches in France",
         "sources": "AL JAZEERA · FRANCE 24"},
        {"n": 10, "tag": "BAYELSA · DISASTER", "badge": "CONFIRMED",
         "stat": "24", "note": "DEAD",
         "headline": "Nigeria funeral boat toll reaches 24",
         "detail": "Capsized Fri; toll given Sat (NEMA)",
         "sources": "DW · AP · SKY NEWS"},
        {"n": 11, "tag": "MERCURY · SCIENCE", "badge": "OFFICIAL",
         "stat": "18:24", "note": "UTC · ORBIT",
         "headline": "BepiColombo enters orbit around Mercury",
         "detail": "Europe–Japan probe; 8 years out",
         "sources": "ESA · AP · SPACE.COM"},
        {"n": 12, "tag": "BANDA SEA · QUAKE", "badge": "OFFICIAL",
         "stat": "M6.8", "note": "09:42 UTC",
         "headline": "Deep quake shakes Timor-Leste and Darwin",
         "detail": "132 km deep, 106 km north-east of Lospalos",
         "sources": "USGS · ABC AUSTRALIA"},
        {"n": 13, "tag": "TWICKENHAM · RUGBY", "badge": "CONFIRMED",
         "stat": "37–12", "note": "FULL TIME",
         "headline": "England beat All Blacks by record margin",
         "detail": "25 points: their biggest win over New Zealand",
         "sources": "BBC · REUTERS · STUFF"},
    ],
    "also_head": "ALSO ON SATURDAY 21 NOVEMBER — 27 MORE STORIES, IN ORDER "
                 "OF CONSEQUENCE",
    "also": [
        ("Estonia", "to shut Russia border crossings from 1 December", "ST"),
        ("Denmark", "expels Russian defence attaché over alleged plot", "BBC"),
        ("CERN", "first evidence of an ultra-rare particle decay", "PHYS.ORG"),
        ("Riyadh", "Houthi & Saudi coalition trade strikes; missiles downed", "MEE"),
        ("Gaza City", "Israeli strike on food vehicle kills three", "AJ"),
        ("Basra", "power-station fire: 4 dead, 35 injured", "REUTERS"),
        ("Tokyo", "Saudi Arabia to triple crude stored in Japan", "JAPAN TODAY"),
        ("Uganda", "restricts gatherings & travel over Ebola fears", "GUARDIAN"),
        ("Tanzania", "opposition leader Lissu convicted of sedition", "BBC"),
        ("DR Congo", "fighting widens in the east, truce at risk", "ASHARQ"),
        ("Ethiopia", "about 700,000 displaced in the south", "FRANCE 24"),
        ("Kenya", "begins onshore crude drilling in Turkana", "ALLAFRICA"),
        ("Washington", "FBI probes reported breach of crime database", "BBC · CBC"),
        ("Los Angeles", "man convicted of arson over Palisades fire", "BBC · UPI"),
        ("Virginia", "child dies of measles, state’s first of 2026", "GUARDIAN"),
        ("New York", "Mamdani sets 2032 date to close Rikers Island jail", "BBC"),
        ("Global", "GTA VI earns $3.8bn on day one — a record", "BBC BIZ"),
        ("Brasília", "Bolsonaro in intensive care, bowel obstruction", "AJ"),
        ("Haiti", "Salvadoran troops fight gangs in the capital", "GUARDIAN"),
        ("Argentina", "bonds slide into distressed territory", "BA TIMES"),
        ("Brazil", "Wolbachia mosquitoes cut dengue in children", "ST"),
        ("Nepal", "PM Shah’s first foreign trip: to India, 22–23 Nov", "BBC"),
        ("Seoul", "ruling party moves to impeach chief justice", "YONHAP"),
        ("Japan", "feels sidelined by US–China–Russia summit", "JAPAN TIMES"),
        ("Melbourne", "teen accused of organising arsons on Signal", "GUARDIAN"),
        ("Philippines", "Air Niugini jet lands safely; all 146 safe", "REPORTS"),
        ("Turin", "Alcaraz beats Shelton, faces Zverev in ATP final", "BBC SPORT"),
    ],
    "date_check": "Left out as other days’ news: the Russian missiles that "
                  "came down in Poland (Fri 20 Nov) · Verstappen wins Las "
                  "Vegas, the new COP31 draft text and India’s 720-9 "
                  "declaration (Sun 22 Nov) · the Bayelsa boat capsized Fri — "
                  "its toll was given on Saturday, card 10.",
    "footer": "Every story here happened or was first reported on Saturday "
              "21 November 2026 (UTC), told as the named outlets reported it. "
              "All maps and drawings are original vector work.",
    "how_sure": "HOW SURE — CONFIRMED: carried by 2+ major outlets · "
                "OFFICIAL: on the record: agency, ministry, federation · "
                "REPORTED: one major outlet",
    "seed": 20261121,
    "out_name": "entry.png",
}

# Pins for the map: (story number, lon, lat, region)
PINS = [
    (1, 50.5, 26.2, "Middle East"), (2, 24.0, 60.0, "Europe"),
    (3, 30.7, 36.9, "Middle East"), (4, -107.8, 24.8, "Americas"),
    (5, 33.4, 47.9, "Europe"), (6, -74.0, 40.7, "Americas"),
    (7, -75.5, -11.5, "Americas"), (8, 4.35, 50.85, "Europe"),
    (9, 2.35, 48.85, "Europe"), (10, 6.0, 4.9, "Africa"),
    (12, 129.0, -5.5, "South-East Asia"), (13, -0.1, 51.5, "Europe"),
    (14, 25.0, 59.0, "Europe"), (15, 10.0, 56.0, "Europe"),
    (16, 6.1, 46.2, "Europe"), (17, 45.0, 15.5, "Middle East"),
    (18, 34.3, 31.4, "Middle East"), (19, 47.8, 30.5, "Middle East"),
    (20, 138.0, 37.0, "East Asia"), (21, 32.5, 1.3, "Africa"),
    (22, 35.0, -6.0, "Africa"), (23, 25.0, -2.0, "Africa"),
    (24, 39.0, 9.0, "Africa"), (25, 37.5, 3.0, "Africa"),
    (26, -77.0, 38.9, "Americas"), (27, -118.2, 34.0, "Americas"),
    (28, -78.5, 37.5, "Americas"), (29, -74.0, 40.7, "Americas"),
    (30, -51.9, -14.2, "Americas"), (31, -47.9, -15.8, "Americas"),
    (32, -72.3, 18.5, "Americas"), (33, -63.6, -38.4, "Americas"),
    (34, -51.9, -14.2, "Americas"), (35, 84.0, 28.2, "South Asia"),
    (36, 127.0, 37.5, "East Asia"), (37, 138.0, 37.0, "East Asia"),
    (38, 145.0, -37.8, "Oceania"), (39, 122.0, 13.0, "Oceania"),
    (40, 7.7, 45.1, "Europe"),
]
