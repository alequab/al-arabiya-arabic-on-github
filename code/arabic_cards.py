"""Right-to-left README pictures: badge, quote card, GitHub stats card (the usual services draw these left to right).

    python code/arabic_cards.py badge --label "الترخيص" --value MIT --out docs/assets/badge-license.svg
    python code/arabic_cards.py quote --text "من جدّ وجد، ومن زرع حصد" --author "مثل عربي" --out quote.svg
    python code/arabic_cards.py stats --user YOUR-NAME --title "إحصاءات GitHub" --out stats.svg

The label or title sits on the right, values on the left, as Arabic is read. --font takes a Google Fonts family
(default Noto Sans Arabic): only the letters used are built into the picture. The stats card reads GitHub with the
token in GITHUB_TOKEN or from `gh auth token`; it is a still picture, so make it again (by hand or on a schedule in
GitHub Actions) to refresh the numbers. --data file.json gives the numbers instead (keys: stars, commits, prs, issues,
contributed).
"""
import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from xml.sax.saxutils import escape

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from typing_svg import CONTROLS, font_face  # noqa: E402

AR = re.compile("[\u0600-\u06ff]")


def text_width(text, size):
    """Rough width: Arabic letters are narrower than Latin ones in most Arabic fonts."""
    w = 0.0
    for ch in CONTROLS.sub("", text):
        w += size * (0.48 if AR.match(ch) else 0.3 if ch == " " else 0.58)
    return w


def stack(font):
    return (f"'{font}', " if font else "") + "'Segoe UI', 'Noto Sans Arabic', Tahoma, sans-serif"


def svg_open(w, h, face, title):
    head = [f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 {w:.0f} {h:.0f}' width='{w:.0f}' height='{h:.0f}' "
            f"role='img' aria-label='{escape(title)}'>", f"<title>{escape(title)}</title>"]
    if face:
        head.append(f"<style>{face}</style>")
    return head


def badge(label, value, color="#2ea44f", font=None, face="", size=11):
    """Label on the right (grey), value on the left (colour)."""
    pad = 7
    lw, vw = text_width(label, size) + 2 * pad, text_width(value, size) + 2 * pad
    w, h = lw + vw, 20
    out = svg_open(w, h, face, f"{label}: {value}")
    out += [f"<clipPath id='r'><rect width='{w:.0f}' height='{h}' rx='3'/></clipPath><g clip-path='url(#r)'>",
            f"<rect width='{vw:.1f}' height='{h}' fill='{escape(color)}'/>",
            f"<rect x='{vw:.1f}' width='{lw:.1f}' height='{h}' fill='#555'/></g>",
            f"<g font-family=\"{stack(font)}\" font-size='{size}' fill='#fff' text-anchor='middle' "
            f"dominant-baseline='central'>",
            f"<text x='{vw + lw / 2:.1f}' y='{h / 2}' direction='rtl'>{escape(label)}</text>",
            f"<text x='{vw / 2:.1f}' y='{h / 2}' direction='rtl'>{escape(value)}</text></g></svg>"]
    return "\n".join(out) + "\n"


def wrap(text, size, width):
    lines, line = [], ""
    for word in text.split():
        trial = (line + " " + word).strip()
        if line and text_width(trial, size) > width:
            lines.append(line)
            line = word
        else:
            line = trial
    return lines + [line] if line else lines


def quote(text, author, width=500, font=None, face="", size=20, color="#333", accent="#2f80ed", bg="#fffefe"):
    """Quote in «…» on the right, the author under it after a dash."""
    lines = wrap(f"«{text}»", size, width - 60)
    lh = size * 1.7
    h = 30 + lh * len(lines) + 40
    out = svg_open(width, h, face, f"{text} — {author}")
    out.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{h - 1:.0f}' rx='6' fill='{escape(bg)}' "
               f"stroke='#e4e2e2'/>")
    out.append(f"<rect x='{width - 6}' y='14' width='3' height='{h - 28:.0f}' rx='1.5' fill='{escape(accent)}'/>")
    out.append(f"<g font-family=\"{stack(font)}\" direction='rtl' text-anchor='start'>")
    for i, line in enumerate(lines):
        out.append(f"<text x='{width - 24}' y='{30 + lh * i + size:.1f}' font-size='{size}' "
                   f"fill='{escape(color)}'>{escape(line)}</text>")
    out.append(f"<text x='{width - 24}' y='{30 + lh * len(lines) + 18:.1f}' font-size='{size * 0.7:.1f}' "
               f"fill='{escape(accent)}'>— {escape(author)}</text></g></svg>")
    return "\n".join(out) + "\n"


STATS_LABELS = [("stars", "مجموع النجوم"), ("commits", "الإيداعات (العام الماضي)"), ("prs", "طلبات السحب"),
                ("issues", "المشكلات"), ("contributed", "ساهم في (العام الماضي)")]


def fmt_num(n):
    return f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


def stats(data, title, width=450, font=None, face="", title_color="#2f80ed", color="#434d58", bg="#fffefe"):
    """Title on the right; each row: label on the right, number on the left."""
    rows = [(label, fmt_num(int(data[key]))) for key, label in STATS_LABELS if key in data]
    h = 70 + 30 * len(rows)
    out = svg_open(width, h, face, title)
    out.append(f"<rect x='0.5' y='0.5' width='{width - 1}' height='{h - 1}' rx='4.5' fill='{escape(bg)}' "
               f"stroke='#e4e2e2'/>")
    out.append(f"<g font-family=\"{stack(font)}\">")
    out.append(f"<text x='{width - 25}' y='38' direction='rtl' font-size='18' font-weight='600' "
               f"fill='{escape(title_color)}'>{escape(title)}</text>")
    for i, (label, num) in enumerate(rows):
        y = 75 + 30 * i
        out.append(f"<circle cx='{width - 30}' cy='{y - 5}' r='4' fill='{escape(title_color)}'/>")
        out.append(f"<text x='{width - 45}' y='{y}' direction='rtl' font-size='14' fill='{escape(color)}'>"
                   f"{escape(label)}</text>")
        out.append(f"<text x='25' y='{y}' font-size='14' font-weight='700' fill='{escape(color)}'>{num}</text>")
    out.append("</g></svg>")
    return "\n".join(out) + "\n"


QUERY = """query($login:String!){user(login:$login){
  repositories(ownerAffiliations:OWNER, isFork:false, first:100){nodes{stargazerCount}}
  contributionsCollection{totalCommitContributions}
  repositoriesContributedTo(first:1, contributionTypes:[COMMIT,ISSUE,PULL_REQUEST,REPOSITORY]){totalCount}
  pullRequests{totalCount} issues{totalCount}}}"""


def github_stats(user):
    token = os.environ.get("GITHUB_TOKEN") or subprocess.run(
        ["gh", "auth", "token"], capture_output=True, text=True).stdout.strip()
    if not token:
        raise SystemExit("no token: set GITHUB_TOKEN or sign in with gh")
    body = json.dumps({"query": QUERY, "variables": {"login": user}}).encode()
    req = urllib.request.Request("https://api.github.com/graphql", data=body,
                                 headers={"Authorization": "bearer " + token, "Content-Type": "application/json"})
    u = json.load(urllib.request.urlopen(req, timeout=30))["data"]["user"]
    return {"stars": sum(r["stargazerCount"] for r in u["repositories"]["nodes"]),
            "commits": u["contributionsCollection"]["totalCommitContributions"],
            "prs": u["pullRequests"]["totalCount"], "issues": u["issues"]["totalCount"],
            "contributed": u["repositoriesContributedTo"]["totalCount"]}


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="kind", required=True)
    for name in ("badge", "quote", "stats"):
        s = sub.add_parser(name)
        s.add_argument("--font", default="Noto Sans Arabic", help="Google Fonts family, or '' for the reader's font")
        s.add_argument("--out", required=True)
    sub.choices["badge"].add_argument("--label", required=True)
    sub.choices["badge"].add_argument("--value", required=True)
    sub.choices["badge"].add_argument("--color", default="#2ea44f")
    sub.choices["quote"].add_argument("--text", required=True)
    sub.choices["quote"].add_argument("--author", required=True)
    sub.choices["stats"].add_argument("--user")
    sub.choices["stats"].add_argument("--data", help="JSON file with the numbers instead of reading GitHub")
    sub.choices["stats"].add_argument("--title", default="\u2067إحصاءات GitHub\u2069")
    a = p.parse_args(argv)
    if a.kind == "stats":
        if not (a.user or a.data):
            p.error("stats needs --user or --data")
        if a.data:
            with open(a.data, encoding="utf-8") as f:
                data = json.load(f)
        else:
            data = github_stats(a.user)
        texts = a.title + "".join(lbl for _, lbl in STATS_LABELS) + "0123456789.k"
    elif a.kind == "badge":
        texts = a.label + a.value
    else:
        texts = a.text + a.author + "«»—"
    face = font_face(a.font, texts) if a.font else ""
    if a.kind == "badge":
        svg = badge(a.label, a.value, a.color, a.font, face)
    elif a.kind == "quote":
        svg = quote(a.text, a.author, font=a.font, face=face)
    else:
        svg = stats(data, a.title, font=a.font, face=face)
    with open(a.out, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"{a.out}: {len(svg)} bytes")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
