"""Check Markdown files for the Arabic-on-GitHub problems described in docs/en/guide.md.

Usage:
  python check_arabic_md.py README.md docs            (files and folders; folders are searched for *.md)
  python check_arabic_md.py --no-info README.md

Prints one line per finding:  path:line: LEVEL rule-id: message
  ERROR  breaks the rendering on github.com
  WARN   renders, but reads wrong or breaks in the phone app
  INFO   worth knowing (things the phone app does not draw)
Exit code 1 when there is any ERROR or WARN, else 0.

The checks are line-based and simple; they do not parse Markdown fully. Fenced code blocks and inline code are skipped.
Lines between <!-- check-arabic: off --> and <!-- check-arabic: on --> are read (divs and code blocks still count)
but not reported: for examples that are wrong on purpose, such as a "before" next to an "after".
"""
import argparse
import html
import pathlib
import re
import sys

ARABIC = re.compile("[\\u0600-\\u06ff\\u0750-\\u077f\\u08a0-\\u08ff\\ufb50-\\ufdff\\ufe70-\\ufefe]")
ARABIC_LETTER = re.compile("[\\u0621-\\u064a\\u0671-\\u06d3\\u06fa-\\u06fc\\u0750-\\u077f\\u08a0-\\u08ff]")
LATIN_LETTER = re.compile("[A-Za-z\\u00c0-\\u024f]")
RLM_START = re.compile("^(&rlm;|\\u200f|&#x200f;|&#8207;)", re.I)
FENCE = re.compile(r"^\s*(?:>\s*)*(`{3,}|~{3,})")     # also under list items and inside > quotes
ALERT = re.compile(r"^\s*>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]", re.I)
# Block elements that can carry a direction or a centring over several lines.
_BLOCKS = r"(div|table|details|td|th|section|p|h[1-6]|blockquote|center)"
DIV_TAG = re.compile(r"<" + _BLOCKS + r"\b[^>]*>|</" + _BLOCKS + r"\s*>", re.I)
RTL_ATTR = re.compile(r"""dir\s*=\s*["']?rtl""", re.I)
LTR_ATTR = re.compile(r"""dir\s*=\s*["']?ltr""", re.I)
BLOCK_START = re.compile(r"^\s*<(?!/?(?:b|strong|a|code|kbd|sup|sub|ins|mark|del|s|span|br)\b)", re.I)
CENTER_ATTR = re.compile(r"""align\s*=\s*["']?center""", re.I)
PICTURE = re.compile(r"<picture\b|#gh-(dark|light)-mode-only", re.I)
ALIGN_RIGHT = re.compile(r"""align\s*=\s*["']?right""", re.I)
STRIPPED = re.compile(r"<(u|font|bdi|bdo|small)\b|<span\b[^>]*\bstyle\s*=", re.I)
ITALIC_TAG = re.compile(r"<(i|em)\b[^>]*>([^<]*)</\1>", re.I)
ITALIC_MD = re.compile(r"(?<![*\w])\*(?!\*|\s)([^*\n]+?)(?<!\s)\*(?!\*)|(?<![_\w])_(?!_|\s)([^_\n]+?)(?<!\s)_(?![_\w])")
BOLD_ITALIC = re.compile(r"(?<![*_\w])(\*{3}|_{3})(?![*_\s])([^*_\n]+?)(?<!\s)\1(?![*_\w])")   # ***bold and italic***
TASK = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\[[ xX]\]\s")
QUOTE = re.compile(r"^\s*>")
LIST_ITEM = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
TABLE_ROW = re.compile(r"^\s*\|")
FOOTNOTE = re.compile(r"\[\^[^\]]+\]")
CODE_SPAN = re.compile(r"`([^`]+)`")
MATH_INLINE = re.compile(r"(?<!\\)\$[^$\n]+\$")
CODE_EDGE = re.compile(r"`([^`]+)`|<code>(.*?)</code>", re.I)
STRONG_EDGE = re.compile("[A-Za-z0-9\\u0621-\\u064a\\u0660-\\u0669]")
LRM_END = re.compile("(&lrm;|\\u200e)\\s*$", re.I)
LRI_END = re.compile("(&#x2066;|\\u2066)\\s*$", re.I)
LRM_START = re.compile("^\\s*(&lrm;|\\u200e)", re.I)
PDI_START = re.compile("^\\s*(&#x2069;|\\u2069)", re.I)
LATIN_ACROSS = re.compile("[\\u0621-\\u064a]\\s+[A-Za-z][\\w.]*(?:\\s+[A-Za-z][\\w.]*)*\\s*[·—–/]\\s*[A-Za-z]")
# Number groups split by spaces or a spaced / long dash: 050 123 4567, 10:30 - 11:00. A hyphen with no spaces
# (050-123-4567, 2026-11-27) keeps the number whole, so it is not matched.
_NUM = r"\d+(?:[-./,:]\d+)*"
DIGIT_GROUPS = re.compile(r"(?<![\d.,:/-])" + _NUM + r"(?:(?:\s+[-–—]\s+|\s*[–—]\s*|\s+)" + _NUM + r")+")
SHORTCODE = re.compile(r":[a-z0-9_+-]+:")                  # :rocket: is drawn as an emoji
ISOLATED = re.compile("(?:[\\u2066-\\u2068]|&#x206[678];).*?(?:\\u2069|&#x2069;)", re.I)
THEMATIC_BREAK = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")
MUTE = re.compile(r"<!--\s*check-arabic:\s*(off|on)\s*-->", re.I)
LEADING_MARKUP = re.compile(r"^\s*(?:#{1,6}\s+|>\s*|[-*+]\s+(?:\[[ xX]\]\s+)?|\d+[.)]\s+|\|\s*)")


def first_strong(text: str):
    """What decides the direction of a line under dir="auto": 'ar', 'latin', 'math' or None.

    Follows the browser rule: the first strong letter wins; digits, emoji and punctuation do not count. Inline code and
    link text count (their letters are in the paragraph); URLs, HTML tags and image alt text do not.
    """
    s = LEADING_MARKUP.sub("", text, count=1)
    s = ISOLATED.sub("", s)                              # isolated text does not decide the direction
    s = SHORTCODE.sub("", s)
    s = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", s)          # images: their alt text is not shown text
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)        # links: keep the link text
    s = re.sub(r"<[^>]+>", "", s)                        # HTML tags
    s = re.sub(r"&rlm;|&#x200f;|&#8207;", "\u200f", s, flags=re.I)   # the marks are strong letters
    s = re.sub(r"&lrm;|&#x200e;|&#8206;", "\u200e", s, flags=re.I)
    s = re.sub(r"&[a-z]+;|&#\w+;", "", s)                # other entities
    for i, ch in enumerate(s):
        if ch == "$" and s[i + 1:i + 2] != " " and MATH_INLINE.match(s, i):
            return "math"
        if ch == "\u200f":
            return "ar"
        if ch == "\u200e":
            return "latin"
        if ARABIC_LETTER.match(ch):
            return "ar"
        if LATIN_LETTER.match(ch):
            return "latin"
    return None


def check_text(path: str, lines: list[str]):
    findings = []

    def add(n, level, rule, msg):
        findings.append((path, n, level, rule, msg))

    divs = []          # stack of open block elements: (name, "rtl" / "ltr" / "center" / "")
    fence_open = None  # the fence that opened the current code block
    fence_col = 0      # where that fence starts on its line
    alert = False      # inside a GitHub alert
    in_comment = False
    muted, mute = set(), False      # lines between check-arabic: off and on
    for n, raw in enumerate(lines, 1):
        line = raw.rstrip("\n")
        m = MUTE.search(line)
        if m:
            mute = m.group(1).lower() == "off"
        if mute:
            muted.add(n)
        direction = next((d for _, d in reversed(divs) if d in ("rtl", "ltr")), "")
        in_rtl = direction == "rtl"
        in_center = any(d == "center" for _, d in divs)

        fence = FENCE.match(line)
        if fence_open is not None:
            # A closing fence: same character, at least as long, nothing after it, not indented deeper than the
            # opening one plus three spaces (a deeper one is text inside the block).
            closes = (fence and fence.group(1)[0] == fence_open[0] and len(fence.group(1)) >= len(fence_open)
                      and not line[fence.end():].strip() and fence.start(1) <= fence_col + 3)
            if closes:
                fence_open = None
            continue

        # HTML comments are not shown. Text after "-->" on the same line still counts.
        if in_comment or line.lstrip().startswith("<!--"):
            end = line.find("-->")
            if end < 0:
                in_comment = True
                continue
            in_comment = False
            line = line[end + 3:]
            if not line.strip():
                continue
            fence = FENCE.match(line)

        # ```x``` at the start of a text line is inline code: a backtick fence has no backtick after it.
        if fence and fence.group(1)[0] == "`" and "`" in line[fence.end():]:
            fence = None

        if fence:
            fence_open = fence.group(1)
            fence_col = fence.start(1)
            lang = line[fence.end():].strip().split(" ")[0].lower()
            if lang in ("", "text", "txt", "plaintext"):
                # No highlighting: the block takes the direction around it.
                if in_rtl:
                    add(n, "WARN", "code-in-rtl-div", "a code block without a language inside <div dir=\"rtl\"> "
                        "shows right to left: close the div before it")
            else:
                # Highlighted: GitHub sets dir="auto", so the first letter in the block decides.
                letter = ""
                for x in lines[n:]:
                    if FENCE.match(x):
                        break
                    letter = next((c for c in x if ARABIC_LETTER.match(c) or LATIN_LETTER.match(c)), "")
                    if letter:
                        break
                if letter and ARABIC_LETTER.match(letter):
                    add(n, "WARN", "code-starts-arabic", "this code block's first letter is Arabic, so it shows "
                        "right to left: start it with a Latin line (an English comment) or use ```text")
                elif in_rtl and lang != "mermaid":
                    add(n, "WARN", "code-in-rtl-div-phone", "the phone app has no dir=\"auto\", so this code block "
                        "shows right to left there: close the div before it")
            if "mermaid" in line.lower():
                add(n, "INFO", "mermaid-phone", "Mermaid is not drawn in the GitHub phone app")
            continue

        text = CODE_SPAN.sub("", line)  # the line without inline code
        has_ar = bool(ARABIC.search(line))

        # Block elements: every open and close on the line, in order (not those quoted in inline code). A close pops
        # back to the nearest open element of the same name, so an unclosed <td> ends with its </table>.
        for m in DIV_TAG.finditer(text):
            name = (m.group(1) or m.group(2)).lower()
            if m.group(0).startswith("</"):
                for k in range(len(divs) - 1, -1, -1):
                    if divs[k][0] == name:
                        del divs[k:]      # also what was left open inside it (<td>, <p>: no closing tag needed)
                        break
            else:
                tag = m.group(0)
                is_rtl = bool(RTL_ATTR.search(tag))
                divs.append((name, "rtl" if is_rtl else "ltr" if LTR_ATTR.search(tag)
                             else "center" if CENTER_ATTR.search(tag) or name == "center" else ""))
                if (is_rtl and name == "div" and line.strip() == tag and n < len(lines)
                        and lines[n].strip()
                        and not lines[n].lstrip().startswith("<")):
                    add(n, "ERROR", "div-blank-line",
                        "leave a blank line after <div dir=\"rtl\">, or the Markdown inside is not read")

        if ALERT.match(line):
            if in_rtl:
                add(n, "ERROR", "alert-in-rtl-div",
                    "GitHub alerts inside <div dir=\"rtl\"> are not drawn: close the div before the alert")
            alert = True
            continue
        if alert and not QUOTE.match(line):
            alert = False

        if STRIPPED.search(text):
            add(n, "WARN", "stripped-tag", "GitHub removes <u>, <font>, <bdi>, <bdo>, <small> and <span style>")
        if PICTURE.search(text):
            add(n, "WARN", "phone-picture", "the GitHub phone app does not load <picture> or #gh-*-mode-only "
                "pictures: use one plain <img> that reads on dark and light")
        for m in ALIGN_RIGHT.finditer(text):
            # Only on Arabic: on this line, or in the block this tag opens. A floated <img align="right"> is fine.
            opening = text[:m.start()].rfind("<")
            if text[opening:opening + 4].lower() == "<img":
                continue
            after = next((x for x in lines[n:] if x.strip()), "") if line.strip().endswith(">") else ""
            if has_ar or ARABIC.search(after):
                add(n, "WARN", "align-right", "align=\"right\" only moves Arabic to the right; the phone app keeps "
                    "it left to right and scrambles it: use dir=\"rtl\"")
                break

        if not has_ar:
            continue

        # An "Arabic line" has more Arabic than Latin letters in its shown text (no code, URLs, tags, entities or
        # pictures). English lines that only quote an Arabic example are left alone by the direction checks.
        shown = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
        shown = re.sub(r"\]\([^)]*\)", "]", shown)
        shown = re.sub(r"<[^>]*>|&#?\w+;", "", shown)
        arabic_line = len(ARABIC_LETTER.findall(shown)) > len(LATIN_LETTER.findall(shown))

        rtl_here = in_rtl or bool(RTL_ATTR.search(text))
        if rtl_here:
            # Code whose first or last character is a symbol (&rlm;, <div>, --flag): in right-to-left text that
            # symbol moves to the wrong side of the code. &lrm; on both sides keeps the code whole.
            for m in CODE_EDGE.finditer(line):
                # Backtick code shows its text as written; <code> content is HTML.
                body = m.group(1) if m.group(1) is not None else html.unescape(m.group(2))
                if not body.strip():
                    continue
                before, after = line[:m.start()], line[m.end():]
                if LRI_END.search(before) and PDI_START.match(after):
                    continue
                if ARABIC_LETTER.search(body) and LATIN_LETTER.search(body):
                    add(n, "WARN", "code-edge-rtl", f"code {m.group(0)!s:.40} mixes Arabic and Latin, so it is "
                        "scrambled in Arabic text: put &#x2066; before it and &#x2069; after it (a left-to-right "
                        "isolate)")
                elif STRONG_EDGE.match(body[0]) and STRONG_EDGE.match(body[-1]):
                    continue
                elif not (LRM_END.search(before) and LRM_START.match(after)):
                    add(n, "WARN", "code-edge-rtl", f"code {m.group(0)!s:.40} starts or ends with a symbol, which moves "
                        "to the wrong side in Arabic text: put &lrm; before and after it")
            # Digit groups split by spaces or a dash (050 123 4567, 10:30 - 11:00): in Arabic text the groups swap places.
            shown_text = CODE_SPAN.sub(lambda m: " " * len(m.group(0)), line)
            for m in DIGIT_GROUPS.finditer(shown_text):
                if arabic_line and not LRI_END.search(shown_text[:m.start()]):
                    add(n, "WARN", "digit-groups-rtl", f"«{m.group(0)}» in Arabic text shows its groups in reverse order: "
                        "put &#x2066; before it and &#x2069; after it")
            # A Latin word that ends the Arabic part joins the English after a separator (العربية على GitHub · Arabic):
            # GitHub then shows with the English. &rlm; after the Arabic part keeps it there.
            if LATIN_ACROSS.search(re.sub(r"\]\([^)]*\)", "]", text)):
                add(n, "WARN", "latin-across-separator", "a Latin word ending the Arabic part joins the English after "
                    "the separator: put &rlm; after the Arabic part")

        if alert and arabic_line and not rtl_here:
            add(n, "WARN", "alert-arabic-phone", "Arabic in a GitHub alert shows left to right in the phone "
                "app: write it as > <p dir=\"rtl\">...</p>")
        if (arabic_line and not alert and not in_rtl and not in_center and not TABLE_ROW.match(line)
                and not RTL_ATTR.search(text)):
            add(n, "WARN", "outside-rtl-div",
                "Arabic outside <div dir=\"rtl\">: the GitHub phone app shows it left to right")
        if ((in_center or CENTER_ATTR.search(text)) and not rtl_here and ARABIC_LETTER.search(shown)
                and LATIN_LETTER.search(shown)):
            add(n, "WARN", "center-mixed-phone", "a centered line that mixes Arabic and Latin has no direction in the "
                "phone app and comes out scrambled: give its element dir=\"rtl\" (<h4 dir=\"rtl\">)")
        if (arabic_line and LIST_ITEM.match(line) and n >= 3 and not lines[n - 2].strip()
                and LIST_ITEM.match(lines[n - 3])):
            add(n, "WARN", "loose-list", "blank line between Arabic list items: the list turns left to right "
                "(bullets on the left); remove the blank lines")
        if QUOTE.match(line) and arabic_line and not alert:
            add(n, "WARN", "quote", "quote bar stays on the left of Arabic text: avoid > quotes in Arabic")
        if TASK.match(line) and arabic_line:
            add(n, "WARN", "task-list", "task-list checkboxes cover Arabic words in the GitHub phone app")
        if FOOTNOTE.search(text) and arabic_line:
            add(n, "WARN", "footnote", "GitHub's footnote list is left to right: make Arabic footnotes by hand")
        if TABLE_ROW.match(line) and not in_rtl and arabic_line:
            add(n, "WARN", "table-outside-rtl-div",
                "Arabic table outside <div dir=\"rtl\">: its first column will be on the left")
        for m in ITALIC_TAG.finditer(text):
            if ARABIC.search(m.group(2)):
                add(n, "WARN", "italic", "Arabic has no italic; the browser only slants it")
        if not TABLE_ROW.match(line):
            body = LEADING_MARKUP.sub("", text, count=1)                          # not the "* " of a list item
            slanted = [m.group(1) or m.group(2) or "" for m in ITALIC_MD.finditer(body)]
            slanted += [m.group(2) for m in BOLD_ITALIC.finditer(body)]
            for part in slanted:
                if ARABIC.search(part):
                    add(n, "WARN", "italic", "Arabic has no italic; the browser only slants it")
        if arabic_line:
            for m in CODE_SPAN.finditer(line):
                if ARABIC.search(m.group(1)):
                    add(n, "INFO", "arabic-in-code", "Arabic in the code font looks thin and spaced out")
        if MATH_INLINE.search(text) or "$$" in text:
            add(n, "INFO", "math-phone", "math is not drawn in the GitHub phone app")

        # A line that goes on from the line above is part of the same paragraph: its first letter does not decide.
        prev = lines[n - 2] if n >= 2 else ""
        continues = (bool(prev.strip()) and not LIST_ITEM.match(line)
                     and not re.match(r"\s*(#|\||<|>|```|~~~)", prev) and not THEMATIC_BREAK.match(prev)
                     and not re.match(r"\s*(#|\||>|```|~~~)", line))
        stripped = LEADING_MARKUP.sub("", line, count=1)
        if re.match("^(&rlm;|\\u200f)\\$", stripped, re.I) and MATH_INLINE.match(stripped, stripped.index("$")):
            add(n, "ERROR", "rlm-math", "write &rlm; then a space before the math: &rlm;$ stops the math from rendering")
        elif (arabic_line and not continues and not RLM_START.match(stripped) and not TABLE_ROW.match(line)
              and not BLOCK_START.match(line) and not line.lstrip().startswith("$$")):
            kind = first_strong(line)
            if kind in ("latin", "math"):
                what = "a Latin word" if kind == "latin" else "math"
                fix = "&rlm;" if kind == "latin" else "&rlm; (with a space after it)"
                add(n, "WARN", "starts-ltr",
                    f"Arabic line starts with {what}, so it reads left to right: start it with {fix}")
    return [f for f in findings if f[1] not in muted]


def files_from(args):
    for a in args:
        p = pathlib.Path(a)
        if p.is_dir():
            yield from sorted(x for x in p.rglob("*.md")
                              if not any(part.startswith(".") or part == "node_modules"
                                         for part in x.relative_to(p).parts[:-1]))
        else:
            yield p


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("paths", nargs="+")
    ap.add_argument("--no-info", action="store_true", help="hide INFO lines")
    args = ap.parse_args(argv)
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    bad = 0
    for f in files_from(args.paths):
        try:
            lines = f.read_text(encoding="utf-8-sig").splitlines()
        except (OSError, UnicodeDecodeError) as e:
            print(f"{f}: ERROR cannot read: {e}", file=sys.stderr)
            bad += 1
            continue
        for path, n, level, rule, msg in check_text(str(f), lines):
            if level == "INFO" and args.no_info:
                continue
            bad += level != "INFO"
            print(f"{path}:{n}: {level} {rule}: {msg}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
