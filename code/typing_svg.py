"""Typing-text picture that writes Arabic from the right (readme-typing-svg types from the left).

    python code/typing_svg.py --line "مرحبًا بك" --line "سطر ثانٍ" --font Amiri --out docs/assets/typing.svg

Each line is shown whole and uncovered from right to left, then rubbed out again from its end, so letters keep their
joined shapes. --font takes a Google Fonts family: only the letters used are downloaded and built into the picture,
so every reader sees that font. Without --font the reader's own Arabic font is used. --once types the first line a
single time and leaves it shown.
"""
import argparse
import base64
import re
import sys
import urllib.parse
import urllib.request
from xml.sax.saxutils import escape

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
CONTROLS = re.compile("[\u200e\u200f\u202a-\u202e\u2066-\u2069]")


def font_face(family, text, weight=400):
    """@font-face rule with the Google font subset for these letters, as a data URL."""
    chars = "".join(sorted(set(CONTROLS.sub("", text)) - {" ", "\n"}))
    query = urllib.parse.urlencode({"family": f"{family}:wght@{weight}", "text": chars})
    req = urllib.request.Request("https://fonts.googleapis.com/css2?" + query, headers={"User-Agent": UA})
    css = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
    m = re.search(r"url\((https://[^)]+)\)\s*format\('(\w+)'\)", css)
    if not m:
        raise ValueError("no font file in the Google Fonts answer for " + family)
    data = urllib.request.urlopen(urllib.request.Request(m.group(1), headers={"User-Agent": UA}), timeout=30).read()
    mime = "font/woff2" if m.group(2) == "woff2" else "font/" + m.group(2)
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"src:url(data:{mime};base64,{base64.b64encode(data).decode('ascii')}) format('{m.group(2)}');}}")


def build(lines, width=600, height=70, size=34, color="#36BCF7", font=None, face="", type_ms=2200, pause_ms=1600,
          erase_ms=700, once=False):
    """Return the SVG text. face is an @font-face rule (font_face()) or ''."""
    if not lines or not all(x.strip() for x in lines):
        raise ValueError("every line needs text")
    if once:
        lines = lines[:1]
    w, h = width, height
    family = (f"'{font}', " if font else "") + "'Segoe UI', 'Noto Naskh Arabic', Tahoma, sans-serif"
    slot = type_ms + pause_ms + erase_ms
    total = slot * len(lines)
    out = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w} {h}' width='{w}' height='{h}'>"]
    if face:
        out.append(f"<style>{face}</style>")
    for i, line in enumerate(lines):
        clean = CONTROLS.sub("", line)
        est = len(clean) * size * 0.5                     # rough line width; the wipe also covers what lies past it
        right = min(w, w / 2 + est / 2 + size * 0.4)      # where the first letter (the right end) starts
        if once:
            kt, xs, ws = "0;1", f"{right:.1f};0", f"0;{w}"
            timing = f"dur='{type_ms}ms' fill='freeze'"
        else:
            a, b, c, d = (i * slot) / total, (i * slot + type_ms) / total, (i * slot + type_ms + pause_ms) / total, \
                ((i + 1) * slot) / total
            kt = f"0;{a:.4f};{b:.4f};{c:.4f};{d:.4f};1"
            xs = f"{right:.1f};{right:.1f};0;0;{right:.1f};{right:.1f}"
            ws = f"0;0;{w};{w};0;0"
            timing = f"dur='{total}ms' repeatCount='indefinite'"
        out.append(f"<clipPath id='c{i}'><rect y='0' height='{h}' x='{right:.1f}' width='0'>"
                   f"<animate attributeName='x' values='{xs}' keyTimes='{kt}' {timing}/>"
                   f"<animate attributeName='width' values='{ws}' keyTimes='{kt}' {timing}/></rect></clipPath>")
        out.append(f"<text clip-path='url(#c{i})' x='{w / 2}' y='{h / 2}' text-anchor='middle' "
                   f"dominant-baseline='central' direction='rtl' font-family=\"{family}\" font-size='{size}' "
                   f"fill='{escape(color)}'>{escape(line)}</text>")
    out.append("</svg>")
    return "\n".join(out) + "\n"


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--line", action="append", required=True, help="a line of text (repeat for more lines)")
    p.add_argument("--font", help="Google Fonts family, built into the picture (e.g. Amiri)")
    p.add_argument("--weight", type=int, default=400)
    p.add_argument("--size", type=int, default=34)
    p.add_argument("--color", default="#36BCF7")
    p.add_argument("--width", type=int, default=600)
    p.add_argument("--height", type=int, default=70)
    p.add_argument("--once", action="store_true", help="type the first line once and keep it")
    p.add_argument("--out", required=True)
    a = p.parse_args(argv)
    face = font_face(a.font, "".join(a.line), a.weight) if a.font else ""
    svg = build(a.line, a.width, a.height, a.size, a.color, a.font, face, once=a.once)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"{a.out}: {len(svg)} bytes")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
