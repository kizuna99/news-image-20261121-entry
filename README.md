[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/kizuna99/news-image-20261121-entry/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/kizuna99/news-image-20261121-entry/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

# The World in One Day — Saturday 21 November 2026: 40 stories, 9 regions, every one dated

An original editorial broadsheet poster for [make.fun](https://make.fun/bounty/news-image-20261121): the whole of Saturday 21 November 2026's world news on one 1024 × 1024 page — a giant dated masthead, the day in UTC on a timeline, six key numbers, three illustrated lead stories (a Strait of Hormuz map, the Sparta II burning in the Gulf of Finland, COP31 in overtime), ten numbered story cards, a pin map of where it happened, and 27 more dated stories in the "Also on Saturday" column. A date-check box names the famous stories left out because they belong to another day. No news photography: every picture, map and icon is original geometry drawn by `render.py` (Pillow, deterministic, supersampled 2048 → 1024). Full source list: see `SOURCES.md`.

![The World in One Day for Saturday 21 November 2026 — 40 dated stories, 9 regions](entry.png)

## The three illustrated leads

1. **Bahrain / Hormuz.** Iran's Revolutionary Guards claimed strikes on US positions in Bahrain; Bahrain said a civilian industrial site was ablaze with no injuries, and UKMTO reported two tankers attacked off Khasab in the Strait of Hormuz. (Al Jazeera, Reuters, AFP, UKMTO, 21 Nov 2026)
2. **Gulf of Finland.** Two drones hit the Russian cargo ship Sparta II at about 06:50 UTC; the crew was taken off and the ship drifted into Finnish waters. (BBC, France 24, Moscow Times, 21 Nov 2026)
3. **COP31, Antalya.** A day past deadline, the climate talks paused overnight deadlocked: a draft text omitted fossil fuels while 130+ countries wanted them named. (BBC, AFP, France 24, 21 Nov 2026)

## The ten cards

Mexico seizes 'El Chapo Isidro' in an army raid (Guardian, DW, NYT) · A Russian missile kills 2 in Zelenskyy's hometown Kryvyi Rih (Al Jazeera, France 24) · The AI sell-off pushes US stocks into correction (Guardian, BBC, UPI) · A M6.7 quake shakes Junín, Peru (USGS, UPI) · The EU and Indonesia sign their trade pact after ten years (DW, AFP, Antara) · Sixth Saturday of cost-of-living marches in France (AFP, France 24, Le Monde) · A funeral boat capsizes in Nigeria's Bayelsa State, toll 24 (DW, AP, Sky News) · BepiColombo enters orbit around Mercury after eight years (ESA, AP, Space.com) · A deep M6.8 quake shakes Timor-Leste and Darwin (USGS, ABC Australia) · England beat the All Blacks by a record margin at Twickenham (BBC, Reuters, Stuff).

## Also on Saturday (27 more)

Estonia to shut Russia border crossings from 1 December · Denmark expels a Russian attaché · CERN's first evidence of an ultra-rare decay · Houthi and Saudi coalition trade strikes · An Israeli strike kills three in a Gaza food vehicle · Basra power-station fire kills four · Saudi Arabia to triple crude stored in Japan · Uganda restricts gatherings over Ebola fears · Tanzania's Lissu convicted of sedition · Fighting widens in eastern DR Congo · About 700,000 displaced in southern Ethiopia · Kenya begins onshore crude drilling in Turkana · The FBI probes a reported breach of its crime database · A man is convicted of arson over the Palisades fire · A Virginia child dies of measles, the state's first of 2026 · Mamdani sets 2032 to close Rikers Island jail · GTA VI earns $3.8bn on day one · Bolsonaro in intensive care in Brasília · Salvadoran troops fight gangs in Haiti's capital · Argentina's bonds slide into distress · Wolbachia mosquitoes cut dengue among Brazil's children · Nepal's PM Balendra Shah to visit India · South Korea's ruling party moves to impeach the chief justice · Japan feels sidelined by the Shenzhen summit · A Melbourne teen accused of organising arsons on Signal · An Air Niugini jet lands safely in the Philippines, 146 safe · Alcaraz beats Shelton and faces Zverev in the ATP Finals final.

## Run locally

`MAKEFUN_OUTPUT_DIR=out python3 main.py` writes the committed PNG (the contest program: standard library only, validates the PNG chunk by chunk). To regenerate the artwork: `python3 render.py` (requires Pillow and Liberation/Noto fonts).

## License

MIT — see `LICENSE`.
