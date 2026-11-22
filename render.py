"""The World Brief — deterministic editorial poster generator (21 Nov 2026).

Draws at 2048x2048 (supersampled) and downscales to the contest size
1024x1024. All randomness comes from a fixed seed; no timestamps.
Requires Pillow + Liberation fonts.
"""
import math
import os
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SS = 2  # supersample factor
W = 1024 * SS
SEED = 20261121

FONT_DIR = os.environ.get(
    "LIBERATION_FONTS", "/usr/share/fonts/truetype/liberation"
)


def font(name, size):
    return ImageFont.truetype(str(Path(FONT_DIR) / name), int(size * SS))


SERIF_B = "LiberationSerif-Bold.ttf"
SERIF = "LiberationSerif-Regular.ttf"
SANS_B = "LiberationSans-Bold.ttf"
SANS = "LiberationSans-Regular.ttf"

# palette
PAPER = (246, 239, 220)
PAPER_D = (238, 228, 200)
INK = (18, 26, 48)
NAVY = (16, 32, 64)
NAVY2 = (27, 48, 92)
GOLD = (192, 148, 44)
GOLD_L = (232, 196, 106)
RED = (178, 34, 40)
RED_D = (128, 22, 30)
CREAM_TXT = (250, 245, 228)
TEAL = (14, 92, 96)
TEAL_D = (8, 52, 62)


def X(v):
    return v * SS


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def vgrad(d, box, top, bot):
    x0, y0, x1, y1 = [X(v) for v in box]
    h = max(1, y1 - y0)
    for i in range(h):
        d.line([(x0, y0 + i), (x1, y0 + i)], fill=lerp(top, bot, i / h))


def text_c(d, cx, y, s, fnt, fill, spacing=0):
    """Centered text with optional letter spacing (drawn char by char)."""
    if spacing:
        widths = [d.textlength(ch, font=fnt) for ch in s]
        total = sum(widths) + spacing * SS * (len(s) - 1)
        x = X(cx) - total / 2
        for ch, w in zip(s, widths):
            d.text((x, X(y)), ch, font=fnt, fill=fill)
            x += w + spacing * SS
        return
    w = d.textlength(s, font=fnt)
    d.text((X(cx) - w / 2, X(y)), s, font=fnt, fill=fill)


def text_l(d, x, y, s, fnt, fill):
    d.text((X(x), X(y)), s, font=fnt, fill=fill)


def wrap(d, s, fnt, maxw):
    words, lines, cur = s.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if d.textlength(t, font=fnt) <= X(maxw) or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def spark(d, cx, cy, r, col):
    cx, cy, r = X(cx), X(cy), X(r)
    for a in range(0, 360, 45):
        dx, dy = math.cos(math.radians(a)), math.sin(math.radians(a))
        d.line([(cx, cy), (cx + dx * r, cy + dy * r)], fill=col, width=2 * SS)
    d.ellipse([cx - r * 0.28, cy - r * 0.28, cx + r * 0.28, cy + r * 0.28],
              fill=col)


def tower(d, cx, base, h, col, wtop=10, wbot=30):
    """Transmission tower silhouette."""
    cx, base, h = X(cx), X(base), X(h)
    wt, wb = X(wtop), X(wbot)
    d.line([(cx - wb, base), (cx - wt, base - h)], fill=col, width=3 * SS)
    d.line([(cx + wb, base), (cx + wt, base - h)], fill=col, width=3 * SS)
    d.line([(cx - wb, base), (cx + wt, base - h)], fill=col, width=2 * SS)
    d.line([(cx + wb, base), (cx - wt, base - h)], fill=col, width=2 * SS)
    for t in (0.35, 0.6, 0.85):
        y = base - h * t
        half = wb + (wt - wb) * t
        d.line([(cx - half, y), (cx + half, y)], fill=col, width=2 * SS)
    for arm_y, arm_w in ((0.97, 44), (0.82, 36)):
        y = base - h * arm_y
        d.line([(cx - X(arm_w), y), (cx + X(arm_w), y)], fill=col, width=3 * SS)
        for sx in (-1, 1):
            d.line([(cx + sx * X(arm_w), y), (cx + sx * X(arm_w), y + X(9))],
                   fill=col, width=2 * SS)


def build():
    rng = random.Random(SEED)
    img = Image.new("RGB", (W, W), PAPER)
    d = ImageDraw.Draw(img, "RGBA")

    # paper grain (deterministic)
    for _ in range(5200):
        gx, gy = rng.randrange(W), rng.randrange(W)
        tone = rng.choice([(232, 222, 192), (252, 247, 232), (240, 231, 205)])
        d.point((gx, gy), fill=tone)

    # outer frame
    d.rectangle([X(10), X(10), X(1014), X(1014)], outline=NAVY, width=3 * SS)
    d.rectangle([X(17), X(17), X(1007), X(1007)], outline=GOLD, width=1 * SS)

    # ---------- masthead ----------
    text_c(d, 512, 26, "INDEPENDENT DAILY PICTURE EDITION · ONE DAY · ONE PAGE",
           font(SANS_B, 10.5), RED, spacing=2)
    text_c(d, 512, 42, "THE WORLD BRIEF", font(SERIF_B, 63), INK)
    d.line([(X(28), X(116)), (X(996), X(116))], fill=RED, width=3 * SS)
    d.line([(X(28), X(121)), (X(996), X(121))], fill=GOLD, width=1 * SS)
    # dateline bar
    d.rectangle([X(28), X(127), X(996), X(153)], fill=NAVY)
    text_l(d, 40, 133, "SATURDAY · 21 NOVEMBER 2026", font(SANS_B, 13.5), GOLD_L)
    r = "40 SOURCED STORIES · 9 REGIONS · 6 ILLUSTRATED"
    f = font(SANS_B, 13.5)
    d.text((X(984) - d.textlength(r, font=f), X(133)), r, font=f, fill=CREAM_TXT)

    # ---------- hero scene ----------
    hx0, hy0, hx1, hy1 = 28, 161, 996, 341
    split = 592
    # left: Bahrain night — missiles over the Gulf
    vgrad(d, (hx0, hy0, split, hy1), (8, 12, 34), (52, 40, 66))
    # right: COP31 dawn, Antalya
    vgrad(d, (split, hy0, hx1, hy1), (16, 84, 96), (238, 178, 92))
    # stars (left only)
    for _ in range(80):
        sx = rng.randrange(X(hx0 + 8), X(split - 8))
        sy = rng.randrange(X(hy0 + 6), X(hy0 + 84))
        d.point((sx, sy), fill=(220, 228, 250))
        if rng.random() < 0.3:
            d.point((sx + 1, sy), fill=(180, 195, 235))
    # crescent moon (left)
    d.ellipse([X(64), X(174), X(96), X(206)], fill=(232, 234, 220))
    d.ellipse([X(76), X(170), X(104), X(202)], fill=(14, 20, 44))
    # sun (right)
    d.ellipse([X(872), X(190), X(968), X(286)], fill=(250, 205, 92))
    d.ellipse([X(884), X(202), X(956), X(274)], fill=(252, 220, 130))
    # globe arc (right)
    gx, gy, gr = 700, 262, 58
    d.ellipse([X(gx - gr), X(gy - gr), X(gx + gr), X(gy + gr)],
              outline=(240, 240, 230), width=2 * SS)
    for k in (-0.6, 0.0, 0.6):
        d.arc([X(gx - gr * (1 - abs(k)) - 4), X(gy - gr),
               X(gx + gr * (1 - abs(k)) + 4), X(gy + gr)], 90, 270,
              fill=(240, 240, 230), width=1 * SS)
        d.arc([X(gx - gr * (1 - abs(k)) - 4), X(gy - gr),
               X(gx + gr * (1 - abs(k)) + 4), X(gy + gr)], 270, 450,
              fill=(240, 240, 230), width=1 * SS)
    for off in (-28, 0, 28):
        d.line([(X(gx - gr + 4), X(gy + off)), (X(gx + gr - 4), X(gy + off))],
               fill=(240, 240, 230), width=1 * SS)

    # --- left scene details: radar, missiles, plant, sea ---
    # radar mast + dome (far left)
    d.line([(X(150), X(302)), (X(150), X(238))], fill=(6, 9, 18), width=4 * SS)
    d.line([(X(118), X(302)), (X(150), X(262))], fill=(6, 9, 18), width=3 * SS)
    d.line([(X(182), X(302)), (X(150), X(262))], fill=(6, 9, 18), width=3 * SS)
    d.pieslice([X(122), X(196), X(178), X(246)], 180, 360, fill=(16, 22, 42),
               outline=(190, 200, 225), width=1 * SS)
    d.line([(X(150), X(222)), (X(196), X(200))], fill=(190, 200, 225),
           width=2 * SS)
    for rr in (26, 40, 54):
        d.arc([X(150 - rr), X(222 - rr), X(150 + rr), X(222 + rr)], 300, 380,
              fill=(150, 190, 235), width=1 * SS)
    # missile trails: quadratic arcs from top-right down to targets
    def missile(x0, y0, xc, yc, x1, y1, col):
        pts = []
        for i in range(41):
            t = i / 40
            px = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * xc + t ** 2 * x1
            py = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * yc + t ** 2 * y1
            pts.append((X(px), X(py)))
        d.line(pts, fill=col, width=2 * SS)
        spark(d, x1, y1, 9, (255, 190, 80))
    missile(566, 168, 470, 190, 428, 282, (255, 170, 90))
    missile(540, 166, 400, 200, 300, 292, (255, 150, 80))
    missile(500, 170, 330, 210, 208, 296, (255, 200, 110))
    # intercept bursts mid-sky
    spark(d, 372, 226, 12, (240, 244, 255))
    spark(d, 470, 248, 9, (240, 244, 255))
    # coastline + industrial plant (left bottom)
    d.polygon([(X(hx0), X(302)), (X(210), X(302)), (X(260), X(292)),
               (X(split), X(296)), (X(split), X(318)), (X(hx0), X(318))],
              fill=(8, 11, 22))
    for bx, bw, bh in [(268, 52, 26), (330, 34, 18), (452, 60, 22)]:
        d.rectangle([X(bx), X(302 - bh), X(bx + bw), X(302)], fill=(24, 30, 52))
    d.rectangle([X(398), X(252), X(408), X(302)], fill=(24, 30, 52))  # chimney
    d.rectangle([X(516), X(266), X(526), X(302)], fill=(24, 30, 52))
    for wx, wy in [(278, 288), (292, 282), (306, 290), (462, 290), (478, 286),
                   (492, 292), (338, 292)]:
        d.rectangle([X(wx), X(wy), X(wx + 3), X(wy + 4)], fill=(255, 205, 110))
    # fire at the plant
    d.ellipse([X(392), X(232), X(416), X(254)], fill=(255, 120, 40, 200))
    d.ellipse([X(398), X(238), X(410), X(252)], fill=(255, 190, 70, 230))
    d.ellipse([X(416), X(292), X(486), X(305)], fill=(255, 110, 45, 80))
    # Patriot-style launcher (right of plant)
    d.polygon([(X(528), X(302)), (X(560), X(302)), (X(556), X(282)),
               (X(534), X(282))], fill=(8, 11, 22))
    d.polygon([(X(538), X(284)), (X(574), X(258)), (X(582), X(266)),
               (X(546), X(290))], fill=(8, 11, 22))
    # sea band
    d.rectangle([X(hx0), X(318), X(split), X(hy1)], fill=(10, 22, 44))
    for i in range(26):
        wx = rng.randrange(X(hx0 + 10), X(split - 30))
        wy = rng.randrange(X(322), X(hy1 - 4))
        d.line([(wx, wy), (wx + X(rng.randrange(8, 22)), wy)],
               fill=(90, 120, 170), width=1)

    # Antalya skyline (right bottom): dome + minarets
    sky = TEAL_D
    d.rectangle([X(split), X(310), X(hx1), X(324)], fill=sky)
    d.pieslice([X(748), X(246), X(868), X(324)], 180, 360, fill=sky)
    d.rectangle([X(802), X(232), X(814), X(252)], fill=sky)
    d.polygon([(X(802), X(232)), (X(814), X(232)), (X(808), X(218))], fill=sky)
    for mx in (636, 946):
        d.rectangle([X(mx), X(246), X(mx + 10), X(324)], fill=sky)
        d.polygon([(X(mx - 2), X(246)), (X(mx + 12), X(246)), (X(mx + 5), X(226))],
                  fill=sky)
        d.rectangle([X(mx - 4), X(276), X(mx + 14), X(282)], fill=sky)
    for bx, bw, bh in [(600, 44, 30), (884, 52, 38), (700, 30, 20)]:
        d.rectangle([X(bx), X(324 - bh), X(bx + bw), X(324)], fill=sky)
    # ground line both sides
    d.rectangle([X(hx0), X(324), X(hx1), X(hy1)], fill=(10, 14, 26))
    # hero frame + divider
    d.line([(X(split), X(hy0)), (X(split), X(hy1))], fill=GOLD, width=2 * SS)
    d.rectangle([X(hx0), X(hy0), X(hx1), X(hy1)], outline=INK, width=2 * SS)
    # hero tags
    d.rectangle([X(hx0), X(hy0), X(268), X(hy0 + 24)], fill=RED)
    text_l(d, hx0 + 10, hy0 + 4, "LEAD · IRAN STRIKES BAHRAIN", font(SANS_B, 11.5),
           CREAM_TXT)
    d.rectangle([X(772), X(hy0), X(hx1), X(hy0 + 24)], fill=TEAL_D)
    text_l(d, 782, hy0 + 4, "CLIMATE · COP31 OVERTIME", font(SANS_B, 11.5),
           CREAM_TXT)
    return img, d


# ---------------- panels ----------------

def icon_radar(d, x, y, w, h):
    vgrad(d, (x, y, x + w, y + h), (12, 18, 44), (44, 36, 66))
    cx, base = x + w / 2, y + h - 10
    d.line([(X(cx), X(base)), (X(cx), X(y + 34))], fill=(8, 10, 20), width=3 * SS)
    d.arc([X(cx - 22), X(y + 10), X(cx + 22), X(y + 46)], 180, 360,
          fill=(235, 238, 245), width=3 * SS)
    d.arc([X(cx - 22), X(y + 16), X(cx + 22), X(y + 46)], 180, 360,
          fill=(235, 238, 245), width=1 * SS)
    d.line([(X(cx - 22), X(y + 28)), (X(cx + 22), X(y + 28))],
           fill=(235, 238, 245), width=2 * SS)
    d.line([(X(cx), X(y + 28)), (X(cx + 24), X(y + 15))], fill=(235, 238, 245),
           width=2 * SS)
    d.ellipse([X(cx + 22), X(y + 13), X(cx + 27), X(y + 18)], fill=(235, 238, 245))
    for rr in (14, 24, 34):
        d.arc([X(cx - rr), X(y + 28 - rr), X(cx + rr), X(y + 28 + rr)], 300, 390,
              fill=(160, 200, 240), width=1 * SS)
    # incoming missile + burst
    d.line([(X(x + w - 8), X(y + 8)), (X(cx + 18), X(y + 52))],
           fill=(255, 170, 90), width=2 * SS)
    spark(d, cx + 18, y + 56, 9, (255, 190, 80))
    d.rectangle([X(x + 6), X(base), X(x + w - 6), X(base + 4)], fill=(8, 10, 20))


def icon_raid(d, x, y, w, h):
    vgrad(d, (x, y, x + w, y + h), (30, 44, 84), (196, 120, 60))
    # Sinaloa mountains
    d.polygon([(X(x), X(y + h)), (X(x + 26), X(y + 44)), (X(x + 48), X(y + h))],
              fill=(52, 40, 34))
    d.polygon([(X(x + 30), X(y + h)), (X(x + 58), X(y + 30)), (X(x + w), X(y + h))],
              fill=(40, 30, 26))
    # helicopter silhouette (pale halo so it reads against the dusk sky)
    hx, hy = x + w / 2 + 2, y + 20
    d.ellipse([X(hx - 30), X(hy - 17), X(hx + 42), X(hy + 15)],
              fill=(235, 205, 150, 110))
    d.ellipse([X(hx - 17), X(hy - 7), X(hx + 17), X(hy + 8)], fill=(10, 10, 12))
    d.polygon([(X(hx + 13), X(hy - 3)), (X(hx + 34), X(hy - 9)), (X(hx + 34), X(hy - 3)),
               (X(hx + 14), X(hy + 3))], fill=(10, 10, 12))
    d.line([(X(hx - 24), X(hy - 12)), (X(hx + 24), X(hy - 12))], fill=(10, 10, 12),
           width=2 * SS)
    d.line([(X(hx), X(hy - 12)), (X(hx), X(hy - 7))], fill=(10, 10, 12), width=2 * SS)
    d.line([(X(hx - 8), X(hy + 8)), (X(hx - 10), X(hy + 13))], fill=(10, 10, 12),
           width=2 * SS)
    d.line([(X(hx + 8), X(hy + 8)), (X(hx + 10), X(hy + 13))], fill=(10, 10, 12),
           width=2 * SS)
    # badge star
    star(d, x + 16, y + h - 18, 9, GOLD_L)
    # roadblock fire dots
    spark(d, x + w - 16, y + h - 14, 7, (255, 140, 60))


def star(d, cx, cy, r, col):
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((X(cx + rr * math.cos(ang)), X(cy + rr * math.sin(ang))))
    d.polygon(pts, fill=col)


def icon_tower(d, x, y, w, h):
    vgrad(d, (x, y, x + w, y + h), (14, 22, 52), (56, 48, 84))
    # city blocks
    for bx, bw, bh in [(6, 16, 34), (26, 13, 48), (58, 18, 28)]:
        d.rectangle([X(x + bx), X(y + h - 8 - bh), X(x + bx + bw), X(y + h - 8)],
                    fill=(10, 13, 26))
    for i in range(9):
        wx = x + 9 + (i % 3) * 6 + (18 if i > 5 else 0)
        wy = y + h - 20 - (i // 3) * 12
        d.rectangle([X(wx), X(wy), X(wx + 2.5), X(wy + 3)], fill=(255, 214, 130))
    # missile streak + impact glow
    d.line([(X(x + w - 6), X(y + 6)), (X(x + 44), X(y + 40))],
           fill=(255, 160, 80), width=2 * SS)
    spark(d, x + 42, y + 44, 11, (255, 170, 70))
    d.ellipse([X(x + 28), X(y + h - 22), X(x + 58), X(y + h - 8)],
              fill=(255, 110, 45, 130))


def icon_globe(d, x, y, w, h):
    vgrad(d, (x, y, x + w, y + h), (14, 92, 96), (240, 186, 96))
    cx, cy, r = x + w / 2, y + h / 2 + 2, 28
    d.ellipse([X(cx - r), X(cy - r), X(cx + r), X(cy + r)], fill=(20, 110, 110),
              outline=(245, 242, 225), width=2 * SS)
    for off in (-14, 0, 14):
        d.line([(X(cx - r + 3), X(cy + off)), (X(cx + r - 3), X(cy + off))],
               fill=(245, 242, 225), width=1 * SS)
    d.arc([X(cx - 11), X(cy - r), X(cx + 11), X(cy + r)], 90, 270,
          fill=(245, 242, 225), width=1 * SS)
    d.arc([X(cx - 11), X(cy - r), X(cx + 11), X(cy + r)], 270, 450,
          fill=(245, 242, 225), width=1 * SS)
    d.pieslice([X(x + w - 38), X(y + h - 28), X(x + w + 2), X(y + h + 12)],
               180, 360, fill=TEAL_D)


def icon_market(d, x, y, w, h):
    vgrad(d, (x, y, x + w, y + h), (40, 14, 20), (96, 26, 34))
    pts = [(8, 16), (24, 24), (38, 20), (52, 36), (66, 32), (78, 50)]
    for i in range(len(pts) - 1):
        d.line([(X(x + pts[i][0]), X(y + pts[i][1])), (X(x + pts[i + 1][0]),
               X(y + pts[i + 1][1]))], fill=(255, 120, 110), width=2 * SS)
    for (px, py) in pts:
        d.line([(X(x + px), X(y + py - 10)), (X(x + px), X(y + py + 10))],
               fill=(255, 150, 140), width=1 * SS)
        d.rectangle([X(x + px - 3), X(y + py - 6), X(x + px + 3), X(y + py + 6)],
                    fill=(255, 90, 84))
    d.polygon([(X(x + 78), X(y + 56)), (X(x + 86), X(y + 44)), (X(x + 88), X(y + 58))],
              fill=(255, 90, 84))
    cx0, cy0 = x + w - 32, y + h - 34
    d.rectangle([X(cx0), X(cy0), X(cx0 + 22), X(cy0 + 22)], outline=GOLD_L,
                width=2 * SS)
    d.rectangle([X(cx0 + 6), X(cy0 + 6), X(cx0 + 16), X(cy0 + 16)], fill=GOLD_L)
    for p in (4, 11, 18):
        d.line([(X(cx0 + p), X(cy0 - 5)), (X(cx0 + p), X(cy0))], fill=GOLD_L,
               width=2 * SS)
        d.line([(X(cx0 + p), X(cy0 + 22)), (X(cx0 + p), X(cy0 + 27))],
               fill=GOLD_L, width=2 * SS)


def icon_quake(d, x, y, w, h):
    vgrad(d, (x, y, x + w, y + h), (36, 60, 100), (150, 130, 105))
    # Andes ridge
    d.polygon([(X(x), X(y + h)), (X(x + 22), X(y + 34)), (X(x + 40), X(y + 52)),
               (X(x + 58), X(y + 26)), (X(x + w), X(y + h))], fill=(44, 40, 44))
    d.polygon([(X(x + 52), X(y + 34)), (X(x + 58), X(y + 26)), (X(x + 65), X(y + 36))],
              fill=(245, 244, 238))
    d.polygon([(X(x + 17), X(y + 42)), (X(x + 22), X(y + 34)), (X(x + 27), X(y + 43))],
              fill=(245, 244, 238))
    # seismic arcs from epicentre
    ex, ey = x + w / 2, y + h - 14
    for rr in (12, 22, 32):
        d.arc([X(ex - rr), X(ey - rr), X(ex + rr), X(ey + rr)], 180, 360,
              fill=(255, 120, 60), width=2 * SS)
    d.ellipse([X(ex - 3), X(ey - 3), X(ex + 3), X(ey + 3)], fill=(255, 120, 60))
    # crack
    pts = [(x + 12, y + h - 6), (x + 26, y + h - 16), (x + 34, y + h - 10),
           (x + 48, y + h - 22), (x + 60, y + h - 14)]
    for i in range(len(pts) - 1):
        d.line([(X(pts[i][0]), X(pts[i][1])), (X(pts[i + 1][0]), X(pts[i + 1][1]))],
               fill=(20, 16, 16), width=2 * SS)


PANELS = [
    ("01 · MIDEAST — GULF WAR", RED, icon_radar, "AL JAZEERA · EURONEWS",
     "Iran strikes US bases in Bahrain; plant ablaze",
     "Guards claim Patriot radars hit at Al-Riffa & Awali; Manama says a civilian site burned — no injuries."),
    ("02 · LATIN AM — CARTEL RAID", (146, 84, 22), icon_raid, "BBC · FBI · 21 NOV",
     "Mexico captures FBI most-wanted 'Chapo Isidro'",
     "Special forces seize cartel boss Meza Flores in Guasave, Sinaloa, with US help; clashes kill 11+."),
    ("03 · EUROPE — WAR", NAVY2, icon_tower, "AL JAZEERA · FRANCE 24",
     "Russian missile kills 2 in Zelenskyy's hometown",
     "Ballistic strike on Kryvyi Rih wounds ~60; Russian missiles also came down in Poland."),
    ("04 · CLIMATE — TÜRKIYE", TEAL, icon_globe, "BBC · FRANCE 24",
     "COP31 deadlocked past deadline on fossil fuels",
     "Nearly 200 nations in Antalya still split on fuels, finance and targets as talks run over."),
    ("05 · MARKETS — AI ROUT", RED_D, icon_market, "GUARDIAN · BBC",
     "AI sell-off pushes US stocks into correction",
     "S&P and Dow correct; Nasdaq wipes out 2026 gains as Anthropic's record IPO stumbles."),
    ("06 · LATIN AM — DISASTER", (30, 90, 140), icon_quake, "UPI · USGS",
     "M6.7 earthquake shakes Peru's Andes",
     "Deep quake in central Peru felt in Lima; counts report 1 dead, 16 hurt, ~850 affected."),
]


WIRE = [
    ("EUROPE", "Drones hit Russian cargo ship Sparta II in Gulf of Finland"),
    ("EUROPE", "Estonia to shut Russia border crossings from 1 December"),
    ("EUROPE", "Denmark expels Russian diplomat over alleged murder plot"),
    ("EUROPE", "Cost-of-living protests in France & Portugal; 144 arrested"),
    ("EUROPE", "CERN finds first evidence of an ultra-rare particle decay"),
    ("EUROPE", "EU & Indonesia sign trade deal; 98.5% of tariffs cut"),
    ("MIDEAST", "Tankers struck by projectiles in the Strait of Hormuz"),
    ("MIDEAST", "Houthis & Saudi coalition trade strikes; Riyadh missiles downed"),
    ("MIDEAST", "Israeli strike kills 3 in Gaza food vehicle"),
    ("MIDEAST", "Basra power-station fire kills 4, injures 35"),
    ("MIDEAST", "Saudi Arabia to triple crude stored in Japan — stockpile deal"),
    ("AFRICA", "Funeral boat capsizes in Nigeria's Bayelsa; at least 24 dead"),
    ("AFRICA", "Uganda restricts gatherings & travel over Ebola fears"),
    ("AFRICA", "Tanzania opposition leader Lissu convicted of sedition"),
    ("AFRICA", "Fighting widens in eastern DR Congo, truce at risk"),
    ("AFRICA", "700,000 displaced in southern Ethiopia"),
    ("AFRICA", "Kenya begins onshore crude drilling in Turkana"),
    ("N AMERICA", "FBI crime database reportedly hacked; probe opens"),
    ("N AMERICA", "Man convicted of arson over deadly Palisades fire"),
    ("N AMERICA", "Virginia child dies of measles, state's first of 2026"),
    ("N AMERICA", "Mamdani sets 2032 date to close Rikers Island jail"),
    ("N AMERICA", "GTA VI earns $3.8bn on day one — entertainment record"),
    ("GLOBAL", "BepiColombo enters Mercury orbit after 8-year flight"),
    ("LATIN AM", "Bolsonaro in intensive care with bowel obstruction"),
    ("LATIN AM", "Salvadoran troops fight gangs in Haiti's capital"),
    ("LATIN AM", "Argentina bonds slide into distressed territory"),
    ("LATIN AM", "Wolbachia mosquitoes cut dengue among Brazil's children"),
    ("S ASIA", "Nepal PM Balendra Shah to visit India, first foreign trip"),
    ("E ASIA", "South Korea ruling party moves to impeach chief justice"),
    ("E ASIA", "Japan feels sidelined by US–China–Russia summit"),
    ("SE ASIA", "M6.8 quake strikes sea off Timor-Leste, near Dili"),
    ("OCEANIA", "Melbourne teen accused of organising arsons on Signal"),
    ("OCEANIA", "Air Niugini jet lands safely in Philippines; 146 safe"),
    ("SPORT", "Alcaraz to face Zverev in ATP Finals title match"),
]


def panels_and_wire(img, d):
    # hero caption strip
    cy = 349
    d.rectangle([X(28), X(cy), X(996), X(cy + 40)], fill=INK)
    text_l(d, 40, cy + 4, "MANAMA — Guards claim US radar hits; a civilian",
           font(SANS_B, 12.5), CREAM_TXT)
    text_l(d, 40, cy + 20, "plant burns, no injuries · Hormuz tankers hit",
           font(SANS_B, 12.5), CREAM_TXT)
    text_l(d, 620, cy + 4, "ANTALYA — COP31 deadlocked past deadline",
           font(SANS_B, 12.5), GOLD_L)
    text_l(d, 620, cy + 20, "over fossil fuels, finance & targets",
           font(SANS_B, 12.5), GOLD_L)

    # panels 3 x 2
    px0, py0, pw, ph, gap = 28, 397, 309, 146, 6
    for i, (tag, col, icon, src, head, summ) in enumerate(PANELS):
        cx = px0 + (i % 3) * (pw + gap)
        cyy = py0 + (i // 3) * (ph + gap)
        d.rectangle([X(cx), X(cyy), X(cx + pw), X(cyy + ph)], fill=(255, 253, 244),
                    outline=INK, width=1 * SS)
        d.rectangle([X(cx), X(cyy), X(cx + pw), X(cyy + 22)], fill=col)
        text_l(d, cx + 9, cyy + 4, tag, font(SANS_B, 11), CREAM_TXT)
        _sf = font(SANS_B, 9)
        _sw = d.textlength(src, font=_sf)
        d.text((X(cx + pw - 9) - _sw, X(cyy + 6)), src, font=_sf,
               fill=(255, 240, 210))
        # icon scene
        ix, iy, iw, ih = cx + 9, cyy + 29, 82, 108
        icon(d, ix, iy, iw, ih)
        d.rectangle([X(ix), X(iy), X(ix + iw), X(iy + ih)], outline=INK,
                    width=1 * SS)
        # headline + summary
        tx = cx + 101
        tw = pw - 101 - 9
        hl = wrap(d, head, font(SANS_B, 15), tw)
        yy = cyy + 31
        for ln in hl[:3]:
            text_l(d, tx, yy, ln, font(SANS_B, 15), INK)
            yy += 20
        yy += 2
        for ln in wrap(d, summ, font(SANS, 12), tw)[:4]:
            text_l(d, tx, yy, ln, font(SANS, 12), (52, 56, 66))
            yy += 15.5

    # world wire
    wy = 703
    d.rectangle([X(28), X(wy), X(996), X(wy + 24)], fill=RED)
    text_l(d, 40, wy + 4,
           "THE WORLD WIRE — 34 MORE STORIES FIRST REPORTED SATURDAY 21 NOV 2026",
           font(SANS_B, 12.5), CREAM_TXT)
    colw, row0, rowh = 474, wy + 32, 14.0
    for i, (region, head) in enumerate(WIRE):
        col = i // 17
        row = i % 17
        x = 36 + col * (colw + 12)
        y = row0 + row * rowh
        text_l(d, x, y, f"{i + 7:02d}", font(SANS_B, 10.5), RED)
        text_l(d, x + 23, y, region, font(SANS_B, 10.5), NAVY)
        rw = d.textlength(region, font=font(SANS_B, 10.5)) / SS
        text_l(d, x + 29 + rw, y, "· " + head, font(SANS, 11), INK)
        if row < 16:
            d.line([(X(x), X(y + 12)), (X(x + colw - 8), X(y + 12))],
                   fill=(216, 206, 178), width=1)

    # footer / date check
    fy = 982
    d.line([(X(28), X(fy - 6)), (X(996), X(fy - 6))], fill=GOLD, width=1 * SS)
    text_c(d, 512, fy,
           "DATE CHECK — ALL 40 ITEMS FIRST REPORTED SATURDAY 21 NOVEMBER 2026 · "
           "FULL SOURCES IN THE REPOSITORY (SOURCES.MD)", font(SANS_B, 10.5), NAVY)
    text_c(d, 512, fy + 15,
           "No news photographs — every image on this page is original drawn geometry.",
           font(SANS, 10), (90, 88, 78))


def main():
    img, d = build()
    panels_and_wire(img, d)
    out = img.resize((1024, 1024), Image.LANCZOS)
    dest = Path(__file__).with_name("entry.png")
    out.save(dest, format="PNG", optimize=True)
    print(f"wrote {dest} {dest.stat().st_size} bytes")


if __name__ == "__main__":
    main()
