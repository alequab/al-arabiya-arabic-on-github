# Heritage style for an Arabic README

[العربية](../ar/heritage.md) · [Styles](styles.md) · [Guide](guide.md)

A README style taken from the classical Arabic book: opening and closing formulas, chapters (أبواب) and sections
(فصول), "benefit" and "caution" notes, abjad numbering, margin notes and verse laid out in two halves. Everything is
text except the parts that are pictures (the heritage fonts, the geometric band and the manuscript ornaments),
which you can leave out.
**See it live on the [Arabic page](../ar/heritage.md)**; this page explains the same parts with copy-paste code. Tested on the website and
with `page_audit.js` in phone mode (November 2026).

Marks: ✔ works · ⚠ works with a flaw · ✘ doesn't work

| Part | Verdict | How |
|---|---|---|
| Opening (فاتحة) | ✔ | Bismillah and the blessing on the Prophet as centered `<h3 dir="rtl">` lines, then «أما بعد». In a chosen font (Kufic, as in this repo's README): one `<img>` made by `code/typing_svg.py --still`, the text in alt |
| Dividers | ✔ | A line of ornaments in `<div align="center">`: `ـــــ ۞ ـــــ`, `❁ ❁ ❁`, `✿ ✿ ✿`, `◆ ◇ ◆` (not `۝`: it is made to hold a verse number and draws as an empty circle). More, tested on the website (S15): old `۞ ۩ ٭ ❦ ❧ ⁂ ※ ⸙`; common today `❀ ✿ ❁ ✾ ❖ ◈ ✦ ✧`; the pairs `༺ ༻` and `⊱ ⊰` are mirrored for you, so type them in reading order. ⚠ `ღ ꕥ ꧁ ꧂ ࿐` are letters of other scripts (Georgian, Vai, Javanese, Tibetan): a line that starts with one turns left to right, so start it with `&rlm;`, and type `꧂` before `꧁` (they are not mirrored). Not tried in the phone app |
| Chapter headings | ✔ ⚠ | المقدمة, الباب الأول, فصل, الخاتمة. A symbol at the start of a heading is dropped from its link and leaves a hyphen: `#-الفاتحة` |
| Benefit / caution notes | ✔ | Native alerts with the Arabic name in bold inside `<p dir="rtl">`. The English alert title stays |
| Abjad numbering | ✔ | Markdown lists always number 1. 2. 3. Write أ. ب. ج. by hand, one line each, joined with `<br>` |
| Quran verses | ✔ ⚠ | Ornate brackets around the verse, as in «﴿ وَقُل رَّبِّ زِدْنِي عِلْمًا ﴾» (their look depends on the reader's font; Windows draws them close to plain brackets): type U+FD3F first, then the verse, then U+FD3E. Check the text against a mushaf |
| Verse (poetry) | ✔ ⚠ | Both halves on one centered `<p dir="rtl">` line with `&emsp;` between; on narrow screens the second half wraps under the first |
| Margin notes | ✔ | Not `[^1]` (that adds an English "Footnotes" section on the left): `<sup>(١)</sup>` after the word and a «الحواشي» section at the end |
| Heritage fonts | ⚠ text, ✔ picture | Text uses the reader's font. `code/typing_svg.py` builds the Google font into the picture and writes from the right: Amiri, Scheherazade New (Naskh), Reem Kufi, Kufam (Kufic), Aref Ruqaa (Ruqʿa), Noto Nastaliq Urdu (Nastaʿlīq), Rakkas. readme-typing-svg types Arabic from the left |
| Geometric band | ✔ picture | `docs/assets/heritage-band.svg`: eight-pointed stars, transparent background, no outside service |
| Manuscript ornaments | ✔ picture | `code/ornaments.py`: shamsa (sun rosette), title cartouche (ʿunwān), interlace border, arabesque vine divider, arcade of pointed arches; transparent, gold and lapis blue (test S14) |
| Justified lines | ✔ ⚠ | `<div dir="rtl" align="justify">`, like Word's Justify: both edges straight. ⚠ The browser widens spaces, it doesn't stretch letters. The whole Arabic page uses it (T36). Phone app not verified |
| Closing (خاتمة) | ✔ | The closing praise («وآخر دعوانا…») as a centered `<h4 dir="rtl">`, then the completion line and the Hijri date |

Don't stretch words with tatweel (بســـم): GitHub search does not find them by their plain spelling (vowel marks
do the same, test T40). Tatweel on its own, in a divider, is
fine.

## Copy-paste parts

Opening:

```html
<div align="center">

<h3 dir="rtl">بسم الله الرحمن الرحيم</h3>
<h3 dir="rtl">والصلاة والسلام على رسول الله</h3>

</div>
```

Or as one Kufic picture:

```sh
python code/typing_svg.py --still --line "بسم الله الرحمن الرحيم" --line "والصلاة والسلام على رسول الله" --font "Reem Kufi" --size 40 --color "#C9A24D" --width 560 --height 66 --out docs/assets/opening.svg
```

```html
<div align="center">

<img src="docs/assets/opening.svg" width="560" alt="بسم الله الرحمن الرحيم، والصلاة والسلام على رسول الله">

</div>
```

Divider:

```html
<div align="center">

ـــــــــ ۞ ـــــــــ

</div>
```

Benefit note (outside the RTL div; alerts are not drawn inside it):

```markdown
> [!NOTE]
> <p dir="rtl"><b>فائدة:</b> النص هنا.</p>
```

Names: Note → فائدة · Tip → لطيفة · Important → قاعدة · Warning → تنبيه · Caution → تحذير

Abjad numbering:

```markdown
<!-- abjad numbering, one line each -->
**أ.** البند الأول.<br>
**ب.** البند الثاني.<br>
**ج.** البند الثالث.
```

Quran verse:

```html
<h4 dir="rtl">﴿ وَقُل رَّبِّ زِدْنِي عِلْمًا ﴾ [طه: ١١٤]</h4>
```

Verse in two halves:

```html
<div align="center">

<p dir="rtl">الصدر&emsp;&emsp;&emsp;العجز</p>

</div>
```

Margin note:

```markdown
<!-- hand-made footnote -->
بعد الكلمة<sup>(١)</sup>

## الحواشي

<sup>(١)</sup> نص الحاشية.
```

Heritage font title (picture made by `code/typing_svg.py`; `--once` types it once and keeps it):

```sh
python code/typing_svg.py --line "دليل" --font "Aref Ruqaa" --size 44 --color "#C9A24D" --width 520 --height 90 --once --out docs/assets/title.svg
```

```html
<img src="docs/assets/title.svg" alt="دليل">
```

Geometric band (picture, from your own repo):

```html
<div align="center">

<img src="docs/assets/heritage-band.svg" width="840" alt="">

</div>
```

Manuscript ornaments (pictures made in your repo; `--gold` and `--blue` change the colours):

```sh
python code/ornaments.py --out-dir docs/assets/ornaments --title "دليل الكتابة العربية"
```

```html
<div align="center">

<img src="docs/assets/ornaments/cartouche.svg" alt="دليل الكتابة العربية">

<img src="docs/assets/ornaments/interlace.svg" alt="">

</div>
```

Closing:

```html
<div align="center">

<h4 dir="rtl">وآخر دعوانا أن الحمد لله رب العالمين</h4>

<p dir="rtl">تمّ بحمد الله · جمادى الآخرة ١٤٤٨هـ</p>

</div>
```

All Arabic body text still goes inside `<div dir="rtl">` with blank lines, as the [guide](guide.md) says.
