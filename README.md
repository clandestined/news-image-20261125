# THE WORLD TODAY — Wednesday, November 25, 2026

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/clandestined/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/clandestined/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

A dense one-day newspaper front page summing up the world's news of
Wednesday, 25 November 2026. One hero story (U.S. tariffs on 14 trading
partners), nine panels and fourteen briefs, 25 stories in all, across trade,
space, war and diplomacy, crime, tech and markets.

## Files

- `entry.png` — the front page, 1024x1024, the image the entry submits.
- `main.py` — the entrypoint: copies `entry.png` to the output directory
  (standard library only, deterministic).
- `build_frontpage.py` — the script that draws `entry.png` with Pillow.
  Run `python3 build_frontpage.py` to regenerate it (needs Pillow).
  Every story in it was verified against live reporting of 25 November 2026.

## Stories

Hero: Trump proposes new tariffs on 14 partners (USTR, Section 301; China
20%, Vietnam 20%, India 17%, EU and Japan 15%; hearing Jan. 25).

Panels: Shenzhou-24 carries the first foreigner to Tiangong (Pakistan's
Muhammad Zeeshan Ali, 40) · U.S. tells citizens to leave Iran now; Iran says
two tankers hit mines in Hormuz · Europe joins the next Ukraine talks, Moscow
has not agreed; EU unveils a 22nd sanctions package · 76 freed in the
Cartagena supermarket siege · second Hamas security chief killed in Gaza in
24 hours · at least 30 killed in a Nigeria reprisal raid · Anthropic slides
below its IPO price · Huang's return fuels the chip-war fight · Huawei to
appeal 10 guilty verdicts.

In brief: Ukraine strikes a Russian air base · 34 nations urge Russia to stop
tear-gas use · Poland plans a no-fly zone · Cairo blaze kills 31 · Kenya cult
leader convicted · second judge blocks the birthright order · India condemns
the Riyadh drone strike · COP31: EU wants climate summits rebuilt · Poundland
into administration · Murmansk governor held · Giuliani awarded the Medal of
Freedom · IS attack kills two in Hasaka · Lebanon to open a second airport ·
Thanksgiving tomorrow.

Markets: S&P 500 -0.25%, Nvidia -5.9%, Anthropic about $74.

## Fact-check notes (25 Nov 2026)

- Cartagena: police later said 76 people were held, not the ~30 first
  reported; the page uses 76.
- Gaza: the Hamas security chief (Naim Abu Nahal) was killed on 24 Nov; the
  25 Nov strike killed his likely successor, Muhammad Abu al-Awf, 47, with
  his wife and two daughters. The page says exactly that.
- Nigeria: police confirmed 30 dead and rejected a claim of 64; the page
  uses 30 and names the dispute.
- The Houthi drone strike on Riyadh's PIF tower happened on 24 Nov, so it
  appears only as India's 25 Nov condemnation in the briefs.
- The Huawei verdict was delivered on Tuesday 24 Nov; the page frames it on
  the 25 Nov development, Huawei's appeal, and notes the racketeering
  acquittal.
- Microsoft's "Code Red" was reported on 24 Nov, so it is not in the paper.
- The COP31 collapse itself was Sunday 22 Nov; the page carries only the
  EU's push to rebuild the summit rules.
- Thanksgiving falls on Thursday 26 Nov; the page marks it as tomorrow.

## Verification (26 Nov 2026)

- `entry.png`: 1024x1024 PNG, 193,856 bytes (limit 1 MiB), SHA-256
  `e84a2276c9d9a52df1060b2b2d839d36615cd638c96148ebd375b5b14964265c`.
- `main.py` run twice with different output dirs writes byte-identical
  files; re-running `build_frontpage.py` reproduces the same SHA-256.
- Read at 300 px across, the masthead, date, hero headline, panel
  headlines and tariff chart all stay legible.

## License

MIT — see LICENSE.
