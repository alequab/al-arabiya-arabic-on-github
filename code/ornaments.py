"""Arabic manuscript ornaments as SVG pictures for README files (transparent, for light and dark pages).

    python code/ornaments.py --out-dir docs/assets/ornaments --title "دليل الكتابة العربية"

Writes shamsa.svg (sun rosette), interlace.svg (woven border), arabesque.svg (vine scroll divider), arcade.svg (row of
pointed arches) and, with --title, cartouche.svg (title panel; the Amiri font is built into the picture).
--gold and --blue change the two colours.
"""
import argparse
import math
import os
import sys
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from typing_svg import font_face  # noqa: E402

DARK = "#7A5C1E"


def svg(w, h, label, body):
    return (f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='{w}' height='{h}' role='img' "
            f"aria-label='{escape(label)}'>\n<title>{escape(label)}</title>\n" + "\n".join(body) + "\n</svg>\n")


def pt(cx, cy, ang, r):
    return f"{cx + r * math.cos(ang):.1f},{cy + r * math.sin(ang):.1f}"


def petals(cx, cy, n, r1, r2, offset, fill, stroke, opacity):
    out = []
    d = math.pi / n
    for i in range(n):
        a = offset + 2 * math.pi * i / n
        out.append(f"<path d='M{pt(cx, cy, a - d, r1)} Q{pt(cx, cy, a - d * 0.25, r2 * 0.86)} {pt(cx, cy, a, r2)} "
                   f"Q{pt(cx, cy, a + d * 0.25, r2 * 0.86)} {pt(cx, cy, a + d, r1)} Z' fill='{fill}' "
                   f"fill-opacity='{opacity}' stroke='{stroke}' stroke-width='1.5' stroke-linejoin='round'/>")
    return out


def star(cx, cy, r, gold, blue):
    """Eight-pointed star (two squares)."""
    sq = f"x='{cx - r:.1f}' y='{cy - r:.1f}' width='{2 * r:.1f}' height='{2 * r:.1f}'"
    return [f"<rect {sq} fill='{blue}' fill-opacity='0.5' stroke='{gold}' stroke-width='2'/>",
            f"<rect {sq} transform='rotate(45 {cx} {cy})' fill='{blue}' fill-opacity='0.5' stroke='{gold}' "
            f"stroke-width='2'/>"]


def shamsa(gold, blue):
    w, h = 220, 240
    cx, cy = 110, 120
    b = petals(cx, cy, 16, 44, 98, -math.pi / 2, blue, gold, 0.35)
    b += petals(cx, cy, 16, 44, 78, -math.pi / 2 + math.pi / 16, gold, gold, 0.3)
    b += [f"<circle cx='{cx}' cy='{cy}' r='44' fill='none' stroke='{gold}' stroke-width='2.5'/>",
          f"<circle cx='{cx}' cy='{cy}' r='39' fill='none' stroke='{gold}' stroke-width='1'/>"]
    b += star(cx, cy, 24, gold, blue)
    b.append(f"<circle cx='{cx}' cy='{cy}' r='7' fill='{gold}'/>")
    for y, s in ((cy - 104, -1), (cy + 104, 1)):   # finials above and below, as on manuscript shamsas
        b.append(f"<path d='M{cx},{y} q-7,{8 * -s} 0,{16 * -s} q7,{-8 * -s} 0,{-16 * -s} Z' fill='{gold}'/>")
        b.append(f"<line x1='{cx}' y1='{y + 16 * s}' x2='{cx}' y2='{y + 26 * s}' stroke='{gold}' stroke-width='2'/>")
    return svg(w, h, "شمسة · Shamsa (sun rosette)", b)


def interlace(gold, blue, w=840, h=56, period=56, amp=14):
    """Two strands woven over and under each other, with blue dots in the eyes."""
    cy = h / 2

    def seg(sign, x0, x1):
        n = 12
        pts = " ".join(f"{x0 + (x1 - x0) * i / n:.1f},{cy + sign * amp * math.sin(2 * math.pi * (x0 + (x1 - x0) * i / n) / period):.1f}"
                       for i in range(n + 1))
        return pts

    b = [f"<line x1='0' y1='3' x2='{w}' y2='3' stroke='{gold}' stroke-width='2'/>",
         f"<line x1='0' y1='{h - 3}' x2='{w}' y2='{h - 3}' stroke='{gold}' stroke-width='2'/>"]
    k = 0
    x = 0.0
    while x <= w:
        under, over = (1, -1) if k % 2 else (-1, 1)
        for sign in (under, over):
            pts = seg(sign, max(0, x - period / 4), min(w, x + period / 4))
            b += [f"<polyline points='{pts}' fill='none' stroke='{DARK}' stroke-width='9' stroke-linecap='butt'/>",
                  f"<polyline points='{pts}' fill='none' stroke='{gold}' stroke-width='6' stroke-linecap='butt'/>",
                  f"<polyline points='{pts}' fill='none' stroke='{blue}' stroke-width='1.4'/>"]
        if x + period / 4 < w:
            b.append(f"<circle cx='{x + period / 4:.1f}' cy='{cy}' r='3.5' fill='{blue}'/>")
        x += period / 2
        k += 1
    return svg(w, h, "ضفيرة · Interlace border", b)


def arabesque(gold, blue, w=640, h=90):
    """Vine scroll from a central rosette out to both ends, with curls and leaves (mirror halves)."""
    cy = h / 2
    half, period, amp = w / 2 - 40, 96, 12
    stem = " ".join(f"{x:.1f},{cy + amp * math.sin(2 * math.pi * x / period):.1f}"
                    for x in [36 + i * 2 for i in range(int((half - 36) / 2) + 1)])
    g = [f"<polyline points='{stem}' fill='none' stroke='{gold}' stroke-width='2.4' stroke-linecap='round'/>"]
    x = 36 + period / 4
    up = True
    while x < half - 10:
        y = cy + amp * math.sin(2 * math.pi * x / period)
        s = -1 if up else 1
        spiral = " ".join(
            f"{x + 4 + 15 * (1 - t * 0.75) * math.cos(math.pi + t * 1.7 * math.pi * s * -1):.1f},"
            f"{y + s * 15 + 15 * (1 - t * 0.75) * math.sin(math.pi + t * 1.7 * math.pi * s * -1) * s:.1f}"
            for t in [i / 24 for i in range(25)])
        g.append(f"<polyline points='{spiral}' fill='none' stroke='{gold}' stroke-width='1.8' stroke-linecap='round'/>")
        lx = x + period / 4
        ly = cy + amp * math.sin(2 * math.pi * lx / period)
        g.append(f"<path d='M{lx:.1f},{ly:.1f} q8,{s * 4} 16,{s * 14} q-12,{-s * 2} -16,{-s * 14} Z' fill='{blue}' "
                 f"fill-opacity='0.6' stroke='{gold}' stroke-width='1.2'/>")
        x += period / 2
        up = not up
    b = [f"<g>{''.join(g)}</g>", f"<g transform='translate({w} 0) scale(-1 1)'>{''.join(g)}</g>"]
    b += petals(w / 2, cy, 8, 10, 26, -math.pi / 2, blue, gold, 0.45)
    b.append(f"<circle cx='{w / 2}' cy='{cy}' r='10' fill='{gold}'/>")
    for ex in (18, w - 18):
        b.append(f"<circle cx='{ex}' cy='{cy}' r='4' fill='{gold}'/>")
    return svg(w, h, "رقش · Arabesque vine divider", b)


def arcade(gold, blue, w=840, h=96, bay=70):
    """Row of pointed arches on columns."""
    b = [f"<line x1='0' y1='{h - 6}' x2='{w}' y2='{h - 6}' stroke='{gold}' stroke-width='2.5'/>"]
    n = int(w // bay)
    left = (w - n * bay) / 2
    for i in range(n):
        x0, x1 = left + i * bay + 6, left + (i + 1) * bay - 6
        xm = (x0 + x1) / 2
        b.append(f"<path d='M{x0:.1f},{h - 6} V46 Q{x0:.1f},20 {xm:.1f},12 Q{x1:.1f},20 {x1:.1f},46 V{h - 6}' "
                 f"fill='{blue}' fill-opacity='0.3' stroke='{gold}' stroke-width='2' stroke-linejoin='round'/>")
        b.append(f"<path d='M{x0 + 8:.1f},{h - 6} V50 Q{x0 + 8:.1f},30 {xm:.1f},24 Q{x1 - 8:.1f},30 {x1 - 8:.1f},50 "
                 f"V{h - 6}' fill='none' stroke='{gold}' stroke-width='1'/>")
        b.append(f"<circle cx='{xm:.1f}' cy='6' r='3' fill='{gold}'/>")
    return svg(w, h, "قناطر · Arcade of pointed arches", b)


def cartouche(title, gold, blue, font="Amiri", w=620, h=120):
    """Title panel with pointed side tabs, a double frame and corner dots; the text is in the picture."""
    face = font_face(font, title)
    m = 40
    b = [f"<style>{face}</style>",
         f"<path d='M{m},10 H{w - m} C{w - 12},10 {w - 12},{h / 2 - 22} {w - 4},{h / 2} C{w - 12},{h / 2 + 22} "
         f"{w - 12},{h - 10} {w - m},{h - 10} H{m} C12,{h - 10} 12,{h / 2 + 22} 4,{h / 2} C12,{h / 2 - 22} 12,10 {m},10 Z' "
         f"fill='{blue}' fill-opacity='0.25' stroke='{gold}' stroke-width='2.5'/>",
         f"<rect x='{m + 6}' y='18' width='{w - 2 * m - 12}' height='{h - 36}' rx='6' fill='none' stroke='{gold}' "
         f"stroke-width='1'/>"]
    for x, y in ((m + 14, 26), (w - m - 14, 26), (m + 14, h - 26), (w - m - 14, h - 26)):
        b.append(f"<circle cx='{x}' cy='{y}' r='3' fill='{gold}'/>")
    b.append(f"<text x='{w / 2}' y='{h / 2}' text-anchor='middle' dominant-baseline='central' direction='rtl' "
             f"font-family=\"'{font}', serif\" font-size='42' fill='{gold}' stroke='{DARK}' stroke-width='0.7' "
             f"paint-order='stroke'>{escape(title)}</text>")
    return svg(w, h, title, b)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--out-dir", required=True)
    p.add_argument("--title", help="text for cartouche.svg (needs internet for the font)")
    p.add_argument("--gold", default="#C9A24D")
    p.add_argument("--blue", default="#2B6A8F")
    a = p.parse_args(argv)
    os.makedirs(a.out_dir, exist_ok=True)
    files = {"shamsa.svg": shamsa(a.gold, a.blue), "interlace.svg": interlace(a.gold, a.blue),
             "arabesque.svg": arabesque(a.gold, a.blue), "arcade.svg": arcade(a.gold, a.blue)}
    if a.title:
        files["cartouche.svg"] = cartouche(a.title, a.gold, a.blue)
    for name, text in files.items():
        with open(os.path.join(a.out_dir, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        print(name, len(text))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
