# README styles with Arabic: test page

Each test puts Arabic into a style people use in READMEs (banners, typing text, badges, cards, layouts).
Results are in the styles guide ([English](../docs/en/styles.md) · [العربية](../docs/ar/styles.md)).
External pictures come from other people's free services; they can be slow or go away.

---
### S1

Banner (capsule-render) with an Arabic title. A: default font. B: `fontFamily=Amiri` (only works if the reader has the font).

<div align="center">

A ↓

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&fontSize=48&desc=%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D8%AC%D8%B1%D9%8E%D9%91%D8%A8%20%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&descAlignY=72" alt="العربية على GitHub">

B ↓

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&fontSize=48&fontFamily=Amiri" alt="العربية على GitHub">

</div>

---

### S2

Footer wave (capsule-render, no text). Works the same in any language.

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="">

---

### S3

Typing text in Arabic. A: readme-typing-svg, default font. B: readme-typing-svg `font=Amiri` (the service embeds the font in the picture). C: made in this repo by `code/typing_svg.py --font Amiri` (writes from the right).

<div align="center">

A ↓

<img src="https://readme-typing-svg.demolab.com/?lines=%D9%85%D8%B1%D8%AD%D8%A8%D9%8B%D8%A7%20%D8%A8%D9%83%20%D9%81%D9%8A%20%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9;%D8%A7%D9%83%D8%AA%D8%A8%20%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9%20%D8%A8%D8%AB%D9%82%D8%A9&center=true&width=500&size=28" alt="مرحبًا بك في دليل العربية">

B ↓

<img src="https://readme-typing-svg.demolab.com/?lines=%D9%85%D8%B1%D8%AD%D8%A8%D9%8B%D8%A7%20%D8%A8%D9%83%20%D9%81%D9%8A%20%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9;%D8%A7%D9%83%D8%AA%D8%A8%20%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9%20%D8%A8%D8%AB%D9%82%D8%A9&font=Amiri&center=true&width=500&size=32" alt="مرحبًا بك في دليل العربية">

C ↓

<img src="../docs/assets/styles/typing.svg" alt="مرحبًا بك في دليل العربية. اكتب العربية على GitHub بثقة">

</div>

---

### S4

Badges with Arabic text. A: shields.io. B: shields.io `for-the-badge`. C: badgen.net. D: `code/arabic_cards.py badge`.

A ↓ <img src="https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5-MIT-2ea44f" alt="الترخيص: MIT"> B ↓ <img src="https://img.shields.io/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5-MIT-2ea44f?style=for-the-badge" alt="الترخيص: MIT"> C ↓ <img src="https://badgen.net/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5/MIT/green" alt="الترخيص: MIT"> D ↓ <img src="../docs/assets/styles/badge.svg" alt="الترخيص: MIT">

---

### S5

Stats cards in Arabic (locale=ar). A: streak stats (has real right-to-left support). B: GitHub stats (Extended). C: `code/arabic_cards.py stats` (still picture of this repo owner's numbers, 2026-11-27).

A ↓

<img src="https://streak-stats.demolab.com/?user=denvercoder1&locale=ar" alt="سلسلة المساهمات">

B ↓

<img src="https://github-stats-extended.vercel.app/api?username=anuraghazra&locale=ar&show_icons=true&custom_title=%E2%81%A7%D8%A5%D8%AD%D8%B5%D8%A7%D8%A1%D8%A7%D8%AA%20GitHub%E2%81%A9" alt="إحصاءات GitHub">

C ↓

<img src="../docs/assets/styles/stats.svg" alt="إحصاءات GitHub">

---

### S6

Activity graph with an Arabic title. `custom_title`.

<img src="https://github-readme-activity-graph.ashutosh-dwivedi0710.workers.dev/graph?username=denvercoder1&custom_title=%E2%81%A7%D9%86%D8%B4%D8%A7%D8%B7%D9%8A%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&hide_border=true" alt="نشاطي على GitHub">

---

### S7

Quote card with an Arabic quote. A: github-readme-quotes `quote` and `author`. B: `code/arabic_cards.py quote`.

A ↓

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&quote=%D9%85%D9%86%20%D8%AC%D8%AF%D9%8E%D9%91%20%D9%88%D8%AC%D8%AF%D8%8C%20%D9%88%D9%85%D9%86%20%D8%B2%D8%B1%D8%B9%20%D8%AD%D8%B5%D8%AF&author=%D9%85%D8%AB%D9%84%20%D8%B9%D8%B1%D8%A8%D9%8A" alt="من جدَّ وجد، ومن زرع حصد">

B ↓

<img src="../docs/assets/styles/quote.svg" alt="من جدّ وجد، ومن زرع حصد. مثل عربي">

---

### S8

Views counter with an Arabic label. komarev `label`.

<img src="https://komarev.com/ghpvc/?username=al-arabiya-arabic-on-github&label=%D8%B9%D8%AF%D8%AF%20%D8%A7%D9%84%D8%B2%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA&color=2ea44f" alt="عدد الزيارات">

---

### S9

Skill icons (no text). Works the same in any language.

<img src="https://skillicons.dev/icons?i=python,js,html,css,git,github" alt="Python, JavaScript, HTML, CSS, Git, GitHub">

---

### S10

Picture and text side by side, right to left. A: image with `align="left"` beside Arabic text in the RTL div. B: a two-column table, Arabic on the right.

<div dir="rtl">

<img src="https://skillicons.dev/icons?i=github" align="left" width="80" alt="GitHub">

هذه فقرة عربية بجانبها صورة على اليسار. الصورة تطفو ويلتف النص حولها، فتبقى العربية على اليمين كما ينبغي.

<br clear="left">

</div>

<table>
<tr>
<td width="50%">

**English**

An English paragraph on the left.

</td>
<td width="50%" dir="rtl">

**العربية**

فقرة عربية في العمود الأيمن.

</td>
</tr>
</table>

---

### S11

Collapsible table of contents in Arabic. `<details>` with Arabic heading links.

<div dir="rtl">

<details>
<summary><b>المحتويات</b></summary>

- [الشعار](#s1)
- [النص المتحرك](#s3)
- [الشارات](#s4)

</details>

</div>

---

### S12

Centered nav bar with icons. Emoji before Arabic links, inside a centered block.

<div align="center" dir="rtl">

📘 [الدليل](../docs/ar/guide.md) · 🧪 [الاختبارات](lab.md) · 🤖 [للذكاء الاصطناعي](../AGENTS.md)

</div>

---
### S13

Arabic text with a Latin word inside a picture. A: as is. B: wrapped in RLI…PDI (U+2067…U+2069) in the URL. C: typing service, wrapped. D: `code/typing_svg.py`, not wrapped (the picture itself is right to left).

<div align="center">

A ↓

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=90&text=%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub&fontSize=40" alt="العربية على GitHub">

B ↓

<img src="https://capsule-render.vercel.app/api?type=rect&color=gradient&height=90&text=%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&fontSize=40" alt="العربية على GitHub">

C ↓ typing text, wrapped

<img src="https://readme-typing-svg.demolab.com/?lines=%E2%81%A7%D8%A7%D9%83%D8%AA%D8%A8%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%20%D8%A8%D8%AB%D9%82%D8%A9%E2%81%A9&font=Amiri&center=true&width=500&size=32&pause=5000" alt="اكتب العربية على GitHub بثقة">

D ↓ made in this repo, not wrapped

<img src="../docs/assets/styles/typing-mixed.svg" alt="اكتب العربية على GitHub بثقة">

</div>

---

---

### S14

Manuscript ornaments as pictures, made by `code/ornaments.py` (transparent; gold and blue): shamsa (sun rosette),
title cartouche, interlace border, arabesque vine divider, arcade of pointed arches.

<div align="center">

<img src="../docs/assets/ornaments/shamsa.svg" width="110" alt="شمسة">

<img src="../docs/assets/ornaments/cartouche.svg" alt="دليل الكتابة العربية">

<img src="../docs/assets/ornaments/interlace.svg" alt="ضفيرة">

<img src="../docs/assets/ornaments/arabesque.svg" alt="رقش">

<img src="../docs/assets/ornaments/arcade.svg" alt="قناطر">

</div>

---

### S15

Ornament characters typed as text, inside the RTL div. A: old (manuscripts and old print; ornate brackets typed
U+FD3F first). B: common today. B2: the same after `&rlm;`. C: pairs that face each other, typed in reading order
(opening one first). C2: `&rlm;` first and the Javanese pair typed the other way round.

<div dir="rtl">

A ↓

<p>۞ · ۩ · ٭ · ❦ · ❧ · ⁂ · ※ · ⸙ · ﴿ ﴾</p>

B ↓

<p>❀ · ✿ · ❁ · ✾ · ❖ · ◈ · ✦ · ✧ · ღ · ꕥ · ࿐</p>

B2 ↓ the same, starting with &amp;rlm;

<p>&rlm;❀ · ✿ · ❁ · ✾ · ❖ · ◈ · ✦ · ✧ · ღ · ꕥ · ࿐</p>

C ↓

<p>꧁ العربية ꧂</p>

C2 ↓ starting with &amp;rlm;, and ꧂ typed first

<p>&rlm;꧂ العربية ꧁</p>

<p>༺ العربية ༻</p>

<p>⊱ العربية ⊰</p>

<p>❦ العربية ❧</p>

<p>ﮩ٨ـﮩﮩ٨ـ ۞ ـ٨ﮩﮩـ٨ﮩ</p>

</div>
