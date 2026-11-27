# Writing Arabic on GitHub: the guide

[العربية](../ar/guide.md) · [Test page (evidence)](../../tests/lab.md) · [Rules for AI tools](../../AGENTS.md) · [README styles](styles.md) · [Heritage style](heritage.md)

Every rule here was tested on github.com (November 2026). Phone-app (Android) results come from real screenshots
where the test says so, otherwise from `code/page_audit.js`, which copies the app. Most rules link to their test
(`T1`…`T46`) on the [test page](../../tests/lab.md). GitHub can change; if a rule stops working, open an issue.

## Contents

1. [How GitHub decides the direction](#1-how-github-decides-the-direction)
2. [Invisible marks you will need](#2-invisible-marks-you-will-need)
3. [Paragraphs, lists and mixed words](#3-paragraphs-lists-and-mixed-words)
4. [The RTL div: when it helps and when it hurts](#4-the-rtl-div-when-it-helps-and-when-it-hurts)
5. [Elements: what works and what to avoid](#5-elements-what-works-and-what-to-avoid)
6. [Styles, sizes, colour and fonts](#6-styles-sizes-colour-and-fonts)
7. [Fields outside Markdown: About, titles, labels, releases](#7-fields-outside-markdown-about-titles-labels-releases)
8. [Names: repo, topics, branches, tags, files](#8-names-repo-topics-branches-tags-files)
9. [The GitHub phone app](#9-the-github-phone-app)
10. [Checking your page](#10-checking-your-page)

## 1. How GitHub decides the direction

In Markdown files (README, `docs/*.md`), issue and PR bodies and comments, GitHub gives **every paragraph, heading
and list item its own direction, taken from its first letter** (`dir="auto"`). An Arabic first letter makes the line
right to left; a Latin letter (also inside inline code or a link) or math makes it left to right. Numbers and emoji
don't count: `2026 هو العام` stays right to left. ([T1](../../tests/lab.md#t1),
[T2](../../tests/lab.md#t2))

**The GitHub phone app does not do this.** It shows every paragraph left to right unless it is inside
`<div dir="rtl">`, and `&rlm;` does not help there. So wrap every Arabic section in the RTL div (seen on the
GitHub Android app; [T33](../../tests/lab.md#t33) shows each case).

Places that do **not** get this, and stay left to right:

| Place | What to do |
|---|---|
| The repo's About text | [Section 7](#about-text) |
| Issue, PR and release titles in lists | Wrap in RLI…PDI ([section 7](#titles-issues-prs-releases-labels)) |
| Release notes | Put the Arabic inside `<div dir="rtl">` ([section 7](#release-notes)) |
| Wiki pages, sidebar and footer | Put the Arabic inside `<div dir="rtl">`; `&rlm;` does not help. Page names: Arabic only, or the name in RLI…PDI ([T43](../../tests/lab.md#t43)) |
| `.txt` and code files | Shown as code, left to right: write Arabic docs in `.md` ([T28](../../tests/lab.md#t28)) |
| GitHub's own footnote list | Make footnotes by hand ([section 5](#footnotes)) |

## 2. Invisible marks you will need

| Mark | Code point | In Markdown | Use |
|---|---|---|---|
| RLM (right-to-left mark) | U+200F | `&rlm;` | Start of an Arabic line that opens with a Latin word or math |
| LRM (left-to-right mark) | U+200E | `&lrm;` | Keeps the English full stop at the end of the English |
| RLI (right-to-left isolate) | U+2067 | (type the character) | Start of a one-line field: About, titles |
| PDI (pop directional isolate) | U+2069 | (type the character) | End of it |
| No-break space | U+00A0 | `&nbsp;` | Keeps two words on the same line |

Fields like the About text and titles take no HTML entities: the real characters must be in the text. The script
[`code/arabic_text.py`](../../code/arabic_text.py) builds them for you.

## 3. Paragraphs, lists and mixed words

- An Arabic line needs nothing: it sits on the right by itself. ([T1](../../tests/lab.md#t1))
- A line that **starts** with a Latin word (plain, in inline code or in a link) or inline math goes left to right, and
  its full stop and brackets jump. Start it with `&rlm;`. A number or emoji at the start does no harm.
  ([T2](../../tests/lab.md#t2), [T3](../../tests/lab.md#t3), [T30](../../tests/lab.md#t30))

  ```markdown
  &rlm;GitHub يأخذ اتجاه كل فقرة من أول حرف فيها.
  ```

- Math first: `&rlm;` **then a space**: `&rlm; $V = IR$ هي معادلة الجهد.` Without the space (`&rlm;$V`) the math is not
  drawn. ([T14](../../tests/lab.md#t14))
- Inline code that starts or ends with a symbol (`&rlm;`, `<div dir="rtl">`) inside an Arabic line: the symbol jumps to
  the other side. Put `&lrm;` before and after the code. Code that mixes Arabic and Latin letters: put `&#x2066;`
  before it and `&#x2069;` after it (a left-to-right isolate). The checker's rule `code-edge-rtl` finds both.
- Numbers in groups (a phone number `050 123 4567`, a time range `10:30 - 11:00`) inside an Arabic line show their
  groups in reverse order. Put `&#x2066;` before and `&#x2069;` after them. A single number (`2026`, `1.2.0`) is fine.
  Brackets around a Latin term (`(React 18)`) and a colon after one (`Gregorian:`) are fine on GitHub.
  ([T44](../../tests/lab.md#t44))
- Latin words **inside** an Arabic line are fine; a line ending with a Latin word and a full stop is fine too.
  ([T3](../../tests/lab.md#t3), [T11](../../tests/lab.md#t11))
- Bullet and numbered lists put their markers on the right by themselves. ([T4](../../tests/lab.md#t4),
  [T5](../../tests/lab.md#t5))
- Keep Arabic lists **tight**: no blank lines between items. With blank lines GitHub wraps each item in its own
  paragraph, and the list turns left to right: bullets on the left, text on the right. ([T34](../../tests/lab.md#t34))
- `<bdi>` and `<bdo>` (the HTML answer to mixed text) are removed by GitHub. ([T11](../../tests/lab.md#t11))
- `<p dir="rtl">` sets one paragraph right to left, also in the phone app. `align="right"` does not: it only moves
  the text, and the phone app scrambles its order. ([T33](../../tests/lab.md#t33))

### The writing itself

These don't change how GitHub draws the page; they make the Arabic read well (adapted from the bilingual-copy skill of
[Dualkit](https://github.com/dualkit/dualkit), MIT License, Copyright (c) Sam Santos).
- Arabic punctuation: `،` `؛` `؟`. The full stop is the same in both languages.
- Modern Standard Arabic for docs and interface text.
- Headings, links and buttons as verbal nouns, which address no one by gender: «التثبيت», not «ثبّت».
- One digit system per page: Western (`2026`) or Arabic-Indic (`٢٠٢٦`), not both. The heritage style keeps
  Arabic-Indic for verse numbers, margin notes and the Hijri date only.
- Names of products and tools stay in Latin letters (GitHub, React, npm); translate common words (ملف, مجلد, تثبيت).

## 4. The RTL div: when it helps and when it hurts

On the website `<div dir="rtl">` does not change paragraphs (they keep their own direction). Put it around every
Arabic section anyway, because:

- **The phone app needs it**: outside it, the app shows Arabic left to right. ([T33](../../tests/lab.md#t33))
- **Tables need it**: inside it the first column is on the right and the table sits on the right.
  `<table dir="rtl">` gets the column order right but leaves the table on the left. ([T6](../../tests/lab.md#t6))
- **Release notes need it** (they get no automatic direction).

But **close it** around:

- **Code blocks without a language** (plain ``` or ```text): inside the div they show right to left.
  ([T31](../../tests/lab.md#t31))
- **GitHub alerts** (`> [!NOTE]`): inside the div they are not drawn at all; the raw `[!NOTE]` text shows.
  ([T29](../../tests/lab.md#t29))

A code block **with** a language name (```powershell, ```markdown...) ignores the div: GitHub takes its
direction from its first letter. If that letter is Arabic the block shows right to left, so start it with a Latin
line, such as an English comment. ([T31](../../tests/lab.md#t31), [T10](../../tests/lab.md#t10)) That is the website
only: the phone app has no dir="auto", so there a code block inside the div shows right to left even with a
language. So close the div around every code block.

Leave a blank line after `<div dir="rtl">` and before `</div>`, or the Markdown inside is not read.

```markdown
<div dir="rtl">

## التثبيت

| الأداة | الأمر |
|---|---|
| الفحص | `python code/check_arabic_md.py` |

</div>

    ```powershell
    python code/check_arabic_md.py README.md
    ```

<div dir="rtl">

بقية القسم العربي.

</div>
```

## 5. Elements: what works and what to avoid

| Element | On github.com | Note |
|---|---|---|
| Headings and links to them (`#البدء-السريع`) | ✔ also with vowel marks and English words | [T7](../../tests/lab.md#t7) |
| `<details>` / `<summary>` | ✔ arrow on the right | [T9](../../tests/lab.md#t9) |
| Task lists `- [ ]` | ✔ on the website, ✘ in the phone app (checkbox covers the words) | [T12](../../tests/lab.md#t12) |
| Quotes `>` | ✘ the bar stays on the left | [T12](../../tests/lab.md#t12) |
| GitHub alerts `> [!NOTE]` | ✔ outside the div, with the Arabic text in `<p dir="rtl">`; title always in English; ✘ inside the div | [T29](../../tests/lab.md#t29), [T35](../../tests/lab.md#t35) |
| Footnotes `[^1]` | ✘ the list at the bottom is left to right | [T16](../../tests/lab.md#t16) |
| Mermaid diagrams | ✔ Arabic labels; use `flowchart RL`; ✘ phone app | [T13](../../tests/lab.md#t13) |
| CSV files | ⚠ drawn as a left-to-right table (first column on the left); use a Markdown table in the RTL div | [T39](../../tests/lab.md#t39) |
| Jupyter notebooks | ✘ Markdown cells left to right, `dir="rtl"` ignored; keep Arabic notes in `.md` files | [T39](../../tests/lab.md#t39) |
| Math `$...$` | ✔ `\text{عربي}` works; ✘ phone app | [T14](../../tests/lab.md#t14) |
| Emoji at the start of a line | ✔ | [T18](../../tests/lab.md#t18) |
| `<kbd>` | ✔ | [T11](../../tests/lab.md#t11) |
| Vowel marks (tashkeel), kashida (ـ) | ✔ | [T15](../../tests/lab.md#t15), [T27](../../tests/lab.md#t27) |

### Footnotes

Make them by hand, inside the RTL div:

```markdown
<!-- hand-made footnote -->
جملة لها حاشية.<sup>[١](#حاشية-١)</sup>

**الحواشي**

<a name="حاشية-١"></a>١. نص الحاشية. [↩](#اسم-القسم)
```

### Alerts with Arabic text

An alert can't go inside the RTL div (it is not drawn there), so its Arabic text has no direction in the phone app.
Wrap the text in `<p dir="rtl">` (or a `<div dir="rtl">` inside the alert); the website draws both
([T35](../../tests/lab.md#t35)):

```markdown
> [!NOTE]
> <p dir="rtl">ملاحظة: النص العربي هنا.</p>
```

GitHub always writes the title in English ("Note"). For an Arabic title the only way is a picture that looks like the
alert. Make it **one picture that reads on dark and light** (its own background, or a colour like GitHub blue), shown
with a plain `<img>`: the phone app does not load `<picture>` or the `#gh-dark-mode-only` trick
([T32](../../tests/lab.md#t32)).

```html
<img src="docs/alert-note.svg" alt="ملاحظة: النص كاملًا هنا">
```

## 6. Styles, sizes, colour and fonts

| Style | Result | Test |
|---|---|---|
| Bold `**` / `<b>` | ✔ | [T19](../../tests/lab.md#t19) |
| Italic `*` / `<i>` | ✘ Arabic has no italic; the browser slants it. Avoid | [T20](../../tests/lab.md#t20) |
| Strikethrough `~~`, `<ins>` underline, `<mark>` highlight | ✔ | [T21](../../tests/lab.md#t21) |
| `<u>`, `<font>`, `<span style>` | ✘ removed | [T21](../../tests/lab.md#t21), [T25](../../tests/lab.md#t25) |
| `<sub>`, `<sup>` | ⚠ they shrink Arabic to 12px, where dots and vowel marks blur: use them only for footnote marks | [T22](../../tests/lab.md#t22), [T44](../../tests/lab.md#t44) |
| `<small>` | ✘ removed | [T44](../../tests/lab.md#t44) |
| Inline code / code blocks | Arabic shows thin and spaced out in the code font: keep Arabic out of code | [T23](../../tests/lab.md#t23) |
| Justified lines (both edges straight, like Word's Justify): `<div dir="rtl" align="justify">` | ✔ on the website; the browser widens the spaces, it doesn't stretch letters (kashida). Phone app not verified | [T36](../../tests/lab.md#t36) |

**Sizes**: `#` and `##` (and HTML `<h1>`, `<h2>`) get a line under them. `<h3>` is the biggest text without a
line; `<h5>` and `<h6>` are small and grey. ([T8](../../tests/lab.md#t8), [T22](../../tests/lab.md#t22))

**Colour**: only through math, `$\color{green}\text{نص}$`. It uses the math font, is small, and the phone app shows
the raw code. `\colorbox` and `\fcolorbox` are refused. ([T24](../../tests/lab.md#t24))

**Fonts**: GitHub uses the reader's system font. A chosen Arabic font is only possible as a picture: one plain
`<img>` in a colour that reads on dark and light (the phone app can't switch pictures by theme), with the text in the
alt text. [T26](../../tests/lab.md#t26) shows one heading in eight Windows fonts,
made by [`code/make-font-samples.ps1`](../../code/make-font-samples.ps1). [`code/typing_svg.py`](../../code/typing_svg.py)
builds a Google font into the picture and writes from the right; badges and cards come from
[`code/arabic_cards.py`](../../code/arabic_cards.py), manuscript ornaments from [`code/ornaments.py`](../../code/ornaments.py)
([styles](styles.md), [heritage](heritage.md)).

## 7. Fields outside Markdown: About, titles, labels, releases

### About text

The About box is always left to right and lined up on the left, on the website and in the phone app. You can get the
order right, not the side.

- Build it as **one right-to-left piece**: `RLI` + Arabic + `RLM` + ` · ` + English + `LRM` + `PDI`, and join the
  first ~30 characters of the English with no-break spaces.
  - The Arabic is read first and keeps its Latin words, brackets and full stops in place.
  - `RLM` keeps the `·` with the Arabic. Without it, a Latin word that ends the Arabic part (`على GitHub`) joins the
    English and moves to the wrong side (seen in the phone app).
  - The joined start of the English is too long to squeeze in beside the Arabic, so the Arabic gets a line of its own
    and the English starts on the next line (measured at 272–420 px and 16–18 px text: the website's and a phone's).
  - `LRM` keeps the English full stop at the end of the English.
  - In one-line lists (your repositories page) the Arabic sits to the right of the English, where an Arabic reader
    starts.
- Keep the Arabic short enough for one line (about 35 letters). A second Arabic line starts on the left.
- Without any marks, keep the Arabic part free of Latin words and full stops.
- Refused or useless: a new line (API error), U+2028 (shows nothing), flag emoji (letters on Windows).

```powershell
python code/arabic_text.py about --ar "دليل كتابة العربية على GitHub" --en "Guide to writing Arabic on GitHub." --out about.txt
gh api -X PATCH repos/OWNER/REPO -F description=@about.txt
```

### Titles: issues, PRs, releases, labels

Shown left to right. An Arabic title with a Latin word, number or bracket gets scrambled
(in `README: الجدول لا يظهر من اليمين في الإصدار 2` the `README:` lands at the far left, where an Arabic
reader finishes). Wrap the title in RLI…PDI. Wrap a bilingual `Arabic · English` title whole, like the About text
(RLI + Arabic + RLM + ` · ` + English + LRM + PDI): issue and commit lists then show the Arabic on the right, read
first. With only the Arabic part wrapped, the Arabic lands on the left. ([T46](../../tests/lab.md#t46))

```powershell
python code/arabic_text.py title "README: الجدول لا يظهر من اليمين في الإصدار 2" --out title.txt
gh api repos/OWNER/REPO/issues -F title=@title.txt -F body=@body.md
```

Labels and milestones take Arabic.

### Commit messages

GitHub shows commit titles and bodies left to right, left-aligned, as plain text (the body in a code font): no
Markdown, no automatic direction, and `&rlm;` or an RLM at the start of a line does nothing. An Arabic-only line reads
right. A line with a Latin word, a number or a full stop gets scrambled: wrap each such line in RLI…PDI, and a
bilingual title whole, as above, so the commit list shows the Arabic on the right.
([T37](../../tests/lab.md#t37))

```powershell
python code/arabic_text.py commit message.txt --out commit.txt
git commit -F commit.txt
```

Pull request bodies and comments are Markdown, like files; the diff view shows Arabic left to right in the code
font. ([T38](../../tests/lab.md#t38))

### Discussions, polls and Gists

Discussion bodies, comments, answers and Gist Markdown files work like issue bodies. Discussion titles, category
names, poll questions and options, and Gist descriptions are left-to-right fields: wrap Arabic with a Latin word,
number or bracket in RLI…PDI, and a bilingual line whole, as for titles ([T46](../../tests/lab.md#t46)). A Gist is named after its first file alphabetically, and Arabic names
sort last. ([T41](../../tests/lab.md#t41), [T42](../../tests/lab.md#t42))

### Search

Search finds Arabic words in code, issues and pull requests, but matches letters exactly: a word written with
tatweel (المـــفتاح) or vowel marks (المِصْباح) is not found by its plain spelling, nor the other way round. Keep
both out of titles and words people will search for. ([T40](../../tests/lab.md#t40))

### Release notes

Release notes get no automatic direction: without a div the Arabic list sits on the left with its full stops on the
wrong side. Put the Arabic part in the RTL div:

```markdown
<div dir="rtl">

## ما الجديد

- &rlm;AGENTS.md فيه القواعد لأدوات الذكاء الاصطناعي.

</div>

---

## What's new

- AGENTS.md has the rules for AI tools.
```

## 8. Names: repo, topics, branches, tags, files

| Name | Arabic? | What happens |
|---|---|---|
| Repo name | ✘ | Arabic letters become `-` (`مختبر-عربي-lab` became `----lab`) |
| Topics | ✘ | Refused |
| Labels, milestones | ✔ | Fine |
| Branches | works | Small code font, `%D8%...` in links, hard to type in a terminal |
| File and folder names | works | `%D8%...` links; `.md` sits on the wrong side in lists |
| Tags | works, with care | See below |

Tags, tested with a release each:

| Tag | On the Tags page | "Source code (zip)" file | Version tools (semver) |
|---|---|---|---|
| `v1.2.0` | fine | `repo-1.2.0.zip` | ✔ |
| `إصدار-1.2.0` | Arabic on the right, number on the left | `repo--1.2.0.zip` | ✘ (a loose search finds 1.2.0) |
| `v1.2.0-إصدار` | number left, Arabic right | `repo-1.2.0-.zip` | ✘ |
| `إصدار-١.٢.٠` | fine | `repo--.-.-.zip` (version lost) | ✘ |

- If you want Arabic tags: Arabic word + Western digits, `إصدار-1.2.0`. Never Arabic-Indic digits.
- If something reads the tag as a version (an app updater, a version script, semver sorting): keep `vX.Y.Z` and put
  the Arabic in the release title.

## 9. The GitHub phone app

The Android app draws less than the website (checked on this repo, November 2026):

| Thing | In the app |
|---|---|
| Math | Not drawn: raw `$...$` code shows |
| Mermaid | Not drawn: the code shows |
| Task lists in Arabic | The checkbox sits on top of the words |
| Arabic outside `<div dir="rtl">` | Left to right; `&rlm;` does not help ([T33](../../tests/lab.md#t33)) |
| `<picture>` and `#gh-dark-mode-only` pictures | Not loaded: broken icon plus the alt text. Only a plain `<img>` loads, so a dark/light pair is impossible: use one picture that reads on both ([T32](../../tests/lab.md#t32)) |
| `align="right"` | Text moves right but stays left to right, so its order is scrambled. Use `dir="rtl"` ([T33](../../tests/lab.md#t33)) |
| `<p dir="rtl">` | Works, for one paragraph ([T33](../../tests/lab.md#t33)) |
| Arabic in a GitHub alert | Left to right unless wrapped in `<p dir="rtl">` ([T29](../../tests/lab.md#t29), [T35](../../tests/lab.md#t35)) |
| A centered line mixing Arabic and English | Order scrambled: give the element `dir="rtl"`, e.g. `<h4 dir="rtl">` |
| GitHub's footnote list, loose lists | Footnotes left to right (avoid them); loose lists are fine in the app |
| Arabic inside the RTL div, lists, release titles | Fine |

So: wrap all Arabic in the RTL div (or `<p dir="rtl">`), use one plain `<img>` per picture that reads on dark and
light, always put the full text in a picture's alt text, give important diagrams a picture
too, and keep math and task lists out of Arabic text that must read well on a phone. The app also keeps an old copy
of a page for a while: pull down to refresh before judging a change.

## 10. Checking your page

1. Run the checker on your Markdown files:

   ```powershell
   python code/check_arabic_md.py README.md docs
   ```

2. Render with GitHub's API before pushing (catches alerts that did not render):
   `gh api -X POST markdown -f mode=gfm -F text=@README.md`.
3. After pushing, open the page on github.com, paste [`code/page_audit.js`](../../code/page_audit.js) into the browser
   console (F12) and run `auditArabic("web")`, then `auditArabic("phone")`. It lists every Arabic block that runs left
   to right, every list with its bullets on the left, and every picture, math, diagram or alert that won't show; the
   phone mode copies the GitHub Android app (it matched real phone screenshots).
4. Look at it in the GitHub phone app once by eye (pull down to refresh first).
