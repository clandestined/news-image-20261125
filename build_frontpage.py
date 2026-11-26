#!/usr/bin/env python3
"""Build the news-image-20261125 front page.

Draws a dense one-day newspaper front page for Wednesday, 25 November 2026
with Pillow and saves it as entry.png next to this script.

All stories were verified against live reporting of 25 November 2026
(Reuters, Al Jazeera, AP via CNA, Kyiv Post, Times of Israel, Nature,
Arab News, and others). See README.md for the fact-check notes.

Run:  python3 build_frontpage.py
Needs: Pillow (pip install pillow). Output is deterministic.
"""

import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
M = 26  # side margin

BG = (247, 244, 236)      # warm newsprint
INK = (20, 20, 20)
RED = (158, 27, 27)
GRAY = (85, 85, 85)
LIGHT_RULE = (170, 170, 170)
NAVY = (31, 43, 70)
ORANGE = (217, 119, 6)

FONT_DIR = "/usr/share/fonts/truetype"
SERIF_B = os.path.join(FONT_DIR, "dejavu/DejaVuSerif-Bold.ttf")
SERIF = os.path.join(FONT_DIR, "dejavu/DejaVuSerif.ttf")
SANS_B = os.path.join(FONT_DIR, "dejavu/DejaVuSans-Bold.ttf")
SANS = os.path.join(FONT_DIR, "dejavu/DejaVuSans.ttf")
COND_B = os.path.join(FONT_DIR, "noto/NotoSerif-CondensedBold.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if fnt.getlength(trial) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_rule(d, x, y, w, px=1, color=INK):
    d.rectangle([x, y, x + w - 1, y + px - 1], fill=color)


def spaced(text):
    """Letterspace a kicker: 'TRADE WAR' -> 'T R A D E   W A R'."""
    return " ".join(list(text.replace(" ", "  ")))


def draw_panel(d, x, y, w, h, kicker, headline, deck, strip=None):
    draw_rule(d, x, y, w, 2, INK)
    # kicker
    kf = font(SANS_B, 13)
    d.text((x, y + 8), spaced(kicker), font=kf, fill=RED)
    # headline (max 2 lines)
    hf = font(COND_B, 27)
    lines = wrap(headline, hf, w)
    assert len(lines) <= 2, "headline too long: %r -> %r" % (headline, lines)
    hy = y + 30
    for ln in lines:
        d.text((x, hy), ln, font=hf, fill=INK)
        hy += 31
    # deck
    df = font(SERIF, 14)
    max_deck_lines = 2 if strip else 3
    dlines = wrap(deck, df, w)
    assert len(dlines) <= max_deck_lines, "deck too long: %r -> %r" % (deck, dlines)
    dy = y + 30 + 2 * 31 + 6
    for ln in dlines:
        d.text((x, dy), ln, font=df, fill=INK)
        dy += 18
    # optional picture strip at the bottom
    if strip == "rocket":
        draw_rocket_strip(d, x, y + h - 30, w, 30)
    elif strip == "spark":
        draw_spark_strip(d, x, y + h - 30, w, 30)


def draw_rocket_strip(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], fill=NAVY)
    # stars
    for sx, sy, r in [(30, 8, 1), (70, 20, 1), (120, 7, 1), (180, 18, 1),
                      (230, 9, 1), (280, 21, 1), (300, 8, 1)]:
        d.ellipse([x + sx - r, y + sy - r, x + sx + r, y + sy + r], fill=(255, 255, 255))
    # rocket (simple flat silhouette), nose up, at left
    rx, ry = x + 14, y + 4
    d.polygon([(rx + 5, ry), (rx + 10, ry + 7), (rx, ry + 7)], fill=(255, 255, 255))
    d.rectangle([rx, ry + 7, rx + 10, ry + 19], fill=(255, 255, 255))
    d.polygon([(rx, ry + 19), (rx - 4, ry + 24), (rx, ry + 19)], fill=RED)
    d.polygon([(rx + 10, ry + 19), (rx + 14, ry + 24), (rx + 10, ry + 19)], fill=RED)
    d.polygon([(rx + 3, ry + 19), (rx + 7, ry + 19), (rx + 5, ry + 26)], fill=ORANGE)
    # label
    lf = font(SANS_B, 12)
    d.text((x + 40, y + 9), "SHENZHOU-24  •  TIANGONG", font=lf, fill=(255, 255, 255))


def draw_spark_strip(d, x, y, w, h):
    d.rectangle([x, y, x + w - 1, y + h - 1], outline=LIGHT_RULE, width=1)
    pts = [(x + 8, y + 7), (x + 55, y + 9), (x + 105, y + 8), (x + 155, y + 15),
           (x + 205, y + 13), (x + 255, y + 21), (x + w - 8, y + 25)]
    d.line(pts, fill=RED, width=2)
    d.ellipse([pts[-1][0] - 3, pts[-1][1] - 3, pts[-1][0] + 3, pts[-1][1] + 3],
              fill=RED)
    lf = font(SANS_B, 11)
    d.text((x + 8, y + 8), "ANT  $74", font=lf, fill=GRAY)


def draw_hero_chart(d, x, y, w):
    """Horizontal bars: proposed capped tariff rates, %."""
    tf = font(SANS_B, 13)
    d.text((x, y), "PROPOSED RATES, %", font=tf, fill=INK)
    rows = [("China", 20), ("Vietnam", 20), ("India", 17), ("EU", 15), ("Japan", 15)]
    lf = font(SANS, 13)
    vf = font(SANS_B, 13)
    by = y + 24
    for name, val in rows:
        d.text((x, by), name, font=lf, fill=INK)
        bx = x + 72
        bw = int(val * 10.5)  # 20% -> 210 px
        d.rectangle([bx, by + 1, bx + bw - 1, by + 14], fill=RED if val >= 20 else INK)
        d.text((bx + bw + 6, by), "%d%%" % val, font=vf, fill=INK)
        by += 26
    cf = font(SANS, 11)
    cap = wrap("Capped rates under trade deals. Hearing Jan. 25; China rises to "
               "40% if the truce fails.", cf, w)
    cy = by + 2
    for ln in cap:
        d.text((x, cy), ln, font=cf, fill=GRAY)
        cy += 14


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # ---------- masthead ----------
    mf = font(SERIF_B, 54)
    title = "THE WORLD TODAY"
    d.text(((W - mf.getlength(title)) / 2, 12), title, font=mf, fill=INK)
    df = font(SANS_B, 19)
    date = "WEDNESDAY, NOVEMBER 25, 2026"
    d.text(((W - df.getlength(date)) / 2, 76), date, font=df, fill=RED)
    draw_rule(d, M, 102, W - 2 * M, 3, INK)
    draw_rule(d, M, 107, W - 2 * M, 1, INK)

    # ---------- ticker ----------
    tf = font(SANS_B, 14)
    ticker = ("TARIFFS ON 14 NATIONS  •  TIANGONG'S FIRST FOREIGNER  •  "
              "EUROPE JOINS UKRAINE TALKS  •  76 FREED IN CARTAGENA  •  "
              "LEAVE IRAN NOW")
    while tf.getlength(ticker) > W - 2 * M and tf.size > 11:
        tf = font(SANS_B, tf.size - 1)
    d.text(((W - tf.getlength(ticker)) / 2, 114), ticker, font=tf, fill=INK)
    draw_rule(d, M, 134, W - 2 * M, 1, LIGHT_RULE)

    # ---------- hero: tariffs ----------
    hx, hy = M, 142
    hw = 642  # text column width; chart takes the rest
    kf = font(SANS_B, 13)
    d.text((hx, hy), spaced("TRADE WAR"), font=kf, fill=RED)
    hf = font(COND_B, 44)
    for i, ln in enumerate(["TRUMP HITS 14 PARTNERS", "WITH NEW TARIFFS"]):
        d.text((hx, hy + 26 + i * 48), ln, font=hf, fill=INK)
    deck = ("The U.S. Trade Representative proposes duties of up to 40% on China "
            "to fight excess factory capacity. "
            "The EU, Japan and India are also targeted.")
    df2 = font(SERIF, 16)
    dy = hy + 26 + 2 * 48 + 8
    for ln in wrap(deck, df2, hw):
        d.text((hx, dy), ln, font=df2, fill=INK)
        dy += 21
    draw_hero_chart(d, 690, hy, W - M - 690)
    draw_rule(d, M, 326, W - 2 * M, 2, INK)

    # ---------- story rows ----------
    panels = [
        # row A
        ("SPACE", "FIRST FOREIGNER ABOARD TIANGONG",
         "Pakistan's Muhammad Zeeshan Ali, 40, is the first foreigner aboard "
         "Tiangong.", "rocket"),
        ("MIDDLE EAST", "U.S. TELLS CITIZENS: LEAVE IRAN NOW",
         "Washington warns hostilities could escalate fast. Iran says two "
         "tankers hit mines in the Strait of Hormuz.",
         None),
        ("EUROPE", "EUROPE JOINS NEXT UKRAINE TALKS",
         "Von der Leyen: a strong European team will join the next round; "
         "Moscow has not agreed. EU unveils 22nd sanctions.", None),
        # row B
        ("AMERICAS", "76 FREED IN CARTAGENA SIEGE",
         "Police say 76 were held, far more than first reported. All freed "
         "after a 17-hour standoff; one gunman killed.", None),
        ("MIDDLE EAST", "2ND HAMAS SECURITY CHIEF KILLED",
         "Muhammad Abu al-Awf, 47, his wife and two daughters die in a Shati "
         "strike, a day after the security chief was killed.", None),
        ("AFRICA", "AT LEAST 30 KILLED IN NIGERIA",
         "Gunmen burn homes in Niger state villages in a reprisal raid. Police "
         "confirm 30 dead and reject a claim of 64.", None),
        # row C
        ("TECH", "ANTHROPIC SLIDES BELOW IPO PRICE",
         "Shares fall toward $74, about 30% below their debut high.", "spark"),
        ("TECH", "HUANG'S RETURN FUELS CHIP-WAR FIGHT",
         "Nvidia shares slide 6% a day after the CEO's reinstatement. "
         "Lawmakers demand tighter China chip curbs.", None),
        ("LAW", "HUAWEI TO APPEAL 10 GUILTY VERDICTS",
         "A Brooklyn jury convicts Huawei on fraud and Iran-sanctions counts, "
         "clearing it of racketeering.",
         None),
    ]
    pw = 316
    pxs = [M, 354, 682]
    pys = [334, 502, 670]
    ph = 160
    for i, (kicker, headline, deck, strip) in enumerate(panels):
        x = pxs[i % 3]
        y = pys[i // 3]
        draw_panel(d, x, y, pw, ph, kicker, headline, deck, strip)
        if i % 3 < 2:  # vertical separator
            draw_rule(d, x + pw + 6, y + 4, 1, ph - 8, LIGHT_RULE)
    for y in (494, 662):
        draw_rule(d, M, y, W - 2 * M, 1, LIGHT_RULE)

    # ---------- IN BRIEF ----------
    by = 838
    bf = font(SANS_B, 15)
    d.text((M, by), spaced("IN BRIEF"), font=bf, fill=INK)
    draw_rule(d, M, by + 22, W - 2 * M, 1, INK)
    briefs = [
        ("UKRAINE STRIKES RUSSIAN AIR BASE", "Kyiv says five planes damaged."),
        ("34 NATIONS URGE RUSSIA", "to stop tear-gas use in Ukraine."),
        ("POLAND PLANS NO-FLY ZONE", "along its border with Ukraine."),
        ("CAIRO BLAZE KILLS 31", "after a fuel truck overturns; 21 hurt."),
        ("KENYA CULT LEADER CONVICTED", "of new charges over mass killings."),
        ("SECOND JUDGE BLOCKS", "Trump's order curtailing birthright citizenship."),
        ("INDIA CONDEMNS", "the Riyadh drone strike that wounded 11."),
        ("COP31: EU WANTS", "climate summits rebuilt after Antalya collapse."),
        ("POUNDLAND INTO ADMINISTRATION", "12,000 jobs at risk in the UK."),
        ("MURMANSK GOVERNOR HELD", "in a corruption inquiry in Russia."),
        ("GIULIANI AWARDED", "the Medal of Freedom by President Trump."),
        ("IS ATTACK KILLS TWO", "Syrian security staff in Hasaka."),
        ("LEBANON TO OPEN", "a second airport next month."),
        ("THANKSGIVING TOMORROW", "America heads home for the holiday."),
    ]
    lf = font(SANS_B, 12)
    rf = font(SANS, 12)
    col_w = 474
    col_x = [M, 524]
    iy = by + 34
    for col in range(2):
        for row in range(7):
            lead, rest = briefs[col * 7 + row]
            text = lead + " " + rest
            assert lf.getlength(lead) + rf.getlength(" " + rest) <= col_w, \
                "brief too long: %r" % text
            yy = iy + row * 17
            d.text((col_x[col], yy), lead, font=lf, fill=INK)
            d.text((col_x[col] + lf.getlength(lead), yy), " " + rest, font=rf,
                   fill=INK)
    draw_rule(d, M, 994, W - 2 * M, 1, INK)

    # ---------- footer ----------
    ff = font(SANS_B, 12)
    foot = ("MARKETS  •  S&P 500 -0.25%  •  NVIDIA -5.9%  •  ANTHROPIC $74  •  "
            "THE WORLD TODAY — WEDNESDAY, NOVEMBER 25, 2026")
    d.text(((W - ff.getlength(foot)) / 2, 1002), foot, font=ff, fill=GRAY)

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote %s (%d bytes)" % (out, os.path.getsize(out)))


if __name__ == "__main__":
    main()
