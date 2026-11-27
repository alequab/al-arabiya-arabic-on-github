# AGENTS.md: rules for AI tools writing Arabic on GitHub

Use these rules whenever you write Arabic (or any right-to-left text) for GitHub: README and other Markdown files,
issues, pull requests, comments, release notes, the repo About text, titles, labels and names. Each rule was tested on
github.com (2026-11); phone-app (Android) results come from real screenshots where the lab says so, otherwise
from `code/page_audit.js`, which copies the app. Evidence: `tests/lab.md` (tests T1–T45). Full guide:
`docs/en/guide.md` (English), `docs/ar/guide.md` (Arabic).

## Characters

- RLM = U+200F (`&rlm;` in Markdown). LRM = U+200E (`&lrm;`). RLI = U+2067. PDI = U+2069. No-break space = U+00A0.
- Plain-text fields (About, titles, labels) take no HTML entities: insert the real characters.
- Write text containing these characters from a script into a UTF-8 file and pass the file
  (`gh api ... -F description=@file`, `gh api repos/OWNER/REPO/issues -F title=@title.txt -F body=@body.md`). Windows PowerShell 5.1 mangles them when typed or
  passed as arguments. `code/arabic_text.py` builds them.

## Markdown (README, docs, issue and PR bodies, comments)

1. GitHub sets `dir="auto"` on every paragraph, heading and list item: direction comes from the first strong letter.
   Arabic lines need nothing.
2. If an Arabic line starts with a Latin word (plain, in inline code or in link text), start it with `&rlm;`.
   Numbers and emoji at the start do not matter.
3. If an Arabic line starts with inline math, write `&rlm; ` (with a space) before the `$`. `&rlm;$` breaks the math.
4. Wrap every Arabic section in `<div dir="rtl">` … `</div>`, with a blank line after the opening and before the
   closing tag. The GitHub phone app shows Arabic left to right without it (and ignores `&rlm;`); tables and release
   notes need it on the website too.
5. Close the div before every GitHub alert (`> [!NOTE]` etc.) and every code block, and reopen it after: alerts
   inside the div are not rendered, and code blocks without a language turn right to left in it.
   A code block with a language name takes its direction from its first letter (the div does not matter): if that
   letter is Arabic it shows right to left, so start it with a Latin line (an English comment). That is the website
   only: the phone app has no dir="auto", so there every code block inside the div shows right to left. So close the
   div around every code block, with or without a language.
6. Do not use in Arabic text: `>` quotes (bar stays left), `[^1]` footnotes (list renders left to right),
   italic (`*x*`, `<i>`, `<em>`), `<u>`, `<font>`, `<span style>`, `<bdi>`, `<bdo>` (stripped), task lists `- [ ]`
   (broken in the phone app).
   - **6a.** Keep Arabic lists tight (no blank lines between items): a loose list turns left to right, bullets on the left.
7. Footnotes: by hand. `جملة.<sup>[١](#حاشية-١)</sup>` and, at the end of the section,
   `<a name="حاشية-١"></a>١. نص الحاشية.`
   - **7a.** Numbers in groups inside Arabic text (`050 123 4567`, `10:30 - 11:00`) reverse their groups: put `&#x2066;`
     before and `&#x2069;` after them (T44). `<small>` is removed; `<sub>`/`<sup>` make Arabic 12px (footnote marks only).
   - **7b.** Writing: Arabic punctuation (، ؛ ؟), Modern Standard Arabic, headings and buttons as verbal nouns (التثبيت, not
     ثبّت), one digit system per page (the heritage style keeps Arabic-Indic for verse numbers, footnote marks and the Hijri
     date), product names in Latin letters.
8. Keep Arabic out of code spans and code blocks (the monospace font renders it thin and spaced).
   - **8a.** In Arabic text,
     inline code that starts or ends with a symbol (`&rlm;`, `<br>`, `[^1]`) gets `&lrm;` before and after it; code mixing
     Arabic and Latin letters gets `&#x2066;` before and `&#x2069;` after. Attribute text (`align="left"`) always in code.
9. For bigger text without a rule line use `<h3>`; `#`, `##`, `<h1>`, `<h2>` get a line.
10. Math, colour through math (`$\color{..}\text{..}$`) and Mermaid render on github.com but not in the phone app.
    Mermaid: use `flowchart RL` for Arabic flows.
11. Arabic heading anchors work: `[الرابط](#البدء-السريع)`. Keep vowel marks exactly as in the heading.
12. Pictures: always put the full text in `alt`. The phone app loads only a plain `<img>`: not `<picture>`, not
    `#gh-dark-mode-only`. So use one picture that reads on dark and light (own background, or a colour like GitHub
    blue `#2f81f7`).
    - **12a.** GitHub alerts: write the Arabic text as `> <p dir="rtl">...</p>` (the alert itself must stay outside the div);
      without it the phone app shows it left to right.
    - **12b.** Never `align="right"` for Arabic (the phone app scrambles it): use `dir="rtl"` on a div, `<p>` or heading. A
      centered line that mixes Arabic and English needs `dir="rtl"` on its element (`<h4 dir="rtl">`).
    - **12c.** Justified Arabic paragraphs (both edges straight, like Word's Justify): `<div dir="rtl" align="justify">`
      (test T36). The browser widens spaces (no kashida); best for long paragraphs. Phone app not verified.
13. A chosen Arabic font or an Arabic alert title is only possible as a picture (rule 12), text in `alt`.

## Picture services (banners, badges, cards)

**13a.** Most services draw their pictures left to right. For right-to-left pictures, make them in the repo:
`code/typing_svg.py` (typing text, written from the right, Google font built in), `code/arabic_cards.py` (badge with
the label on the right, stats card, quote card) and `code/ornaments.py` (manuscript ornaments) (tests S3–S5, S7,
S14). Badges: never shields.io (it pulls Arabic letters apart and reverses them); badgen.net and the komarev counter
draw the letters right but put the label on the left. capsule-render banners take Arabic. Stats cards:
streak-stats `locale=ar` is fully RTL. Ornament characters typed as text (S15): `ღ ꕥ ꧁ ꧂ ࿐` are letters of other
scripts, so a line that starts with one turns left to right: start it with `&rlm;`, and type `꧂` before `꧁`.
Picture text that mixes Arabic with a Latin word: wrap it in RLI…PDI (`%E2%81%A7`…`%E2%81%A9` in the URL), or
the Latin word lands on the wrong side (test S13). Details: `docs/en/styles.md`.

## Fields outside Markdown

14. About text: `RLI + Arabic + RLM + " · " + English + LRM + PDI`, with the first ~30 characters of the English
    joined by NBSP;
    Arabic part about 35 letters or less (one line). No new lines (API refuses), no U+2028, no flag emoji.
    `code/arabic_text.py about` builds it.
15. Issue, PR, release and label titles that mix Arabic with Latin words, numbers or brackets: wrap the whole title
    in RLI … PDI; in a bilingual `Arabic · English` title wrap only the Arabic part. `code/arabic_text.py title`
    does both.
    - **15a.** Commit messages: plain left-to-right text, no Markdown, no auto direction, RLM does nothing. Wrap every line that
      has Arabic plus a Latin word, number or full stop in RLI…PDI; in a bilingual title only the Arabic part
      (`code/arabic_text.py commit`). CSV files show as left-to-right tables; notebook Markdown cells ignore
      `dir="rtl"` (tests T37–T39).
    - **15b.** Discussion titles, category names, poll questions and options, Gist descriptions: left-to-right fields, wrap
      the Arabic part in RLI…PDI (T41, T42). Search matches letters exactly: no tatweel or vowel marks in titles or
      words people will search for (T40).
16. Release notes: Arabic part inside `<div dir="rtl">` (release notes get no automatic direction), then `---`, then
    the English part.

## Names

17. Repo names and topics: ASCII only (Arabic becomes `-` in repo names; Arabic topics are refused).
18. Branches, files and folders: prefer ASCII (Arabic works but links become percent-encoded).
19. Tags: `vX.Y.Z` when anything parses versions. If Arabic is wanted: Arabic word + Western digits
    (`إصدار-1.2.0`). Never Arabic-Indic digits in a tag (the zip download loses the version).

## Before you finish

20. Run `python code/check_arabic_md.py <files or folders>` and fix every ERROR and WARN.
    - **20a.** If you can drive a browser: open the page on github.com, paste `code/page_audit.js` into the console, run
      `auditArabic("web")` and `auditArabic("phone")`, and fix every finding.
21. Render with `gh api -X POST markdown -f mode=gfm -F text=@FILE` (or the web page) and check that alerts rendered.
