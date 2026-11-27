"""Build GitHub plain-text fields (About text, titles) with the invisible marks Arabic needs.

GitHub shows the About text and issue / PR / release / label titles left to right, left-aligned.
About text (tested on github.com at widths of 272-420 px and in the GitHub Android app):
  RLI + Arabic + RLM + ' · ' + English (its first ~30 characters joined by no-break spaces) + LRM + PDI
  The whole text is one right-to-left isolate, so the Arabic is read first. The joined start of the English
  is too long to squeeze in beside the Arabic, so the Arabic gets its own line; LRM keeps the
  English full stop at its end; RLM keeps the separator (and a Latin word ending the Arabic, like GitHub)
  with the Arabic. In one-line lists the Arabic sits to the right of the English.
Titles: RLI + title + PDI. A bilingual "Arabic · English" title is wrapped whole, like the About text:
  RLI + Arabic + RLM + ' · ' + English + LRM + PDI, so lists show the Arabic on the right, read first (tests T37,
  T46). English-only titles are left alone.
Commit messages: every line with Arabic in it is marked the same way (GitHub shows commit titles and bodies
  left to right, in a code font, with no automatic direction). Trailers (Signed-off-by: ...) in the last paragraph
  are left alone.
  RLI U+2067, PDI U+2069, LRM U+200E, no-break space U+00A0.

Usage:
  python arabic_text.py about --ar "دليل كتابة العربية" --en "Arabic writing guide." [--out about.txt]
  python arabic_text.py title "README: الجدول لا يظهر من اليمين" [--out title.txt]
  python arabic_text.py commit message.txt --out commit.txt     (then: git commit -F commit.txt)

Then, for example:
  gh api -X PATCH repos/OWNER/REPO -F description=@about.txt
  gh api repos/OWNER/REPO/issues -F title=@title.txt -F body=@body.md

Write to a file with --out: Windows PowerShell 5.1 mangles these characters on the command line and console.
"""
import argparse
import re
import sys

RLI, PDI, LRM, RLM, NBSP = "\u2067", "\u2069", "\u200e", "\u200f", "\u00a0"
MARKS = re.compile("[\u200e\u200f\u202a-\u202e\u2066-\u2069]")
ARABIC_LETTER = re.compile("[ء-يٱ-ۓۺ-ۼ]")
ONE_LINE_LETTERS = 35  # about one line of the About box on the repo page
JOIN_CHARS = 30        # English joined at the start: too long to fit beside the Arabic, even in the phone app


def clean(text: str) -> str:
    """Remove marks already in the text, so they are never doubled."""
    return MARKS.sub("", text).strip()


def isolate(arabic: str) -> str:
    return RLI + clean(arabic) + PDI


BAD_BREAKS = re.compile("[\r\n\u2028\u2029]")
TRAILER = re.compile(r"^[A-Za-z]+(?:-[A-Za-z]+)+: ")   # Signed-off-by:, Co-authored-by: ... are read by tools
NL = chr(10)
SEP = " \u00b7 "


def about(arabic: str, english: str) -> tuple[str, list[str]]:
    notes = []
    ar, en = clean(arabic), clean(english)
    if not ar:
        raise ValueError("the Arabic part is empty")
    if not ARABIC_LETTER.search(ar):
        notes.append("the Arabic part has no Arabic letters")
    if ARABIC_LETTER.search(en):
        notes.append("the English part has Arabic letters")
    if BAD_BREAKS.search(ar) or BAD_BREAKS.search(en):
        raise ValueError("the About text cannot have line breaks (GitHub refuses them)")
    letters = len(ARABIC_LETTER.findall(ar))
    if letters > ONE_LINE_LETTERS:
        notes.append(f"the Arabic part has {letters} letters; above about {ONE_LINE_LETTERS} it wraps, and its "
                     "second line starts on the left")
    if not en:
        result = isolate(ar)
    else:
        words = en.split()
        k = 1
        while k < len(words) and len(" ".join(words[:k])) < JOIN_CHARS:
            k += 1
        en = NBSP.join(words[:k]) + (" " + " ".join(words[k:]) if len(words) > k else "")
        result = RLI + ar + RLM + SEP + en + LRM + PDI
    if len(result) > 350:
        notes.append(f"the About text is {len(result)} characters; GitHub allows 350")
    return result, notes


def _mark_line(line: str) -> str:
    """One line of a title or commit message. "Arabic · English" is wrapped whole, as one right-to-left isolate."""
    if not ARABIC_LETTER.search(line):
        return line
    indent = line[:len(line) - len(line.lstrip())]
    parts = clean(line).split(SEP)
    for i in range(1, len(parts)):
        en = SEP.join(parts[i:])
        if not ARABIC_LETTER.search(en):
            # "Arabic · English" (the Arabic part may have its own separators): RLM keeps the separator, and a
            # Latin word ending the Arabic, with the Arabic; LRM keeps the English full stop at its end
            return indent + RLI + clean(SEP.join(parts[:i])) + RLM + SEP + en + LRM + PDI
    return indent + isolate(line)


def title(text: str) -> str:
    """An issue / PR / release / label title. English-only titles are left alone."""
    return _mark_line(text)


def commit(message: str) -> str:
    """Mark each line of a commit message that has Arabic letters (also Arabic-only lines: a full stop or a number
    at their end moves to the wrong side). English lines, blank lines and the trailers in the last paragraph
    (Signed-off-by:, Co-authored-by:, read by git and GitHub) stay as they are."""
    lines = message.splitlines()
    while lines and not lines[-1].strip():      # blank lines at the end (git drops them) must not hide the trailers
        lines.pop()
    last_blank = max((i for i, x in enumerate(lines) if not x.strip()), default=-1)
    out = []
    for i, x in enumerate(lines):
        trailer = i > 0 and i > last_blank and last_blank >= 0 and TRAILER.match(x)
        out.append(x if trailer else _mark_line(x))
    return NL.join(out) + NL


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("about", help="build the repo About text")
    a.add_argument("--ar", required=True, help="Arabic part")
    a.add_argument("--en", default="", help="English part")
    a.add_argument("--out", help="write to this UTF-8 file instead of printing")
    t = sub.add_parser("title", help="wrap an issue / PR / release / label title")
    t.add_argument("text")
    t.add_argument("--out", help="write to this UTF-8 file instead of printing")
    c = sub.add_parser("commit", help="mark a commit message (a UTF-8 file) for git commit -F")
    c.add_argument("file")
    c.add_argument("--out", help="write to this UTF-8 file instead of printing")
    args = p.parse_args(argv)

    if args.cmd == "about":
        try:
            result, notes = about(args.ar, args.en)
        except ValueError as e:
            print(f"error: {e}", file=sys.stderr)
            return 2
    elif args.cmd == "commit":
        try:
            with open(args.file, encoding="utf-8-sig") as f:   # PowerShell 5.1 writes a BOM
                result, notes = commit(f.read()), []
        except (OSError, UnicodeDecodeError) as e:
            print(f"error: cannot read {args.file}: {e}", file=sys.stderr)
            return 2
    else:
        result, notes = title(args.text), []
    for n in notes:
        print(f"note: {n}", file=sys.stderr)
    if args.out:
        with open(args.out, "w", encoding="utf-8", newline="") as f:
            f.write(result)
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
