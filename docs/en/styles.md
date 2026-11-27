# README styles with Arabic

[العربية](../ar/styles.md) · [Guide](guide.md) · [Heritage style](heritage.md) · [Test page](../../tests/styles.md)

The styles people use most in GitHub READMEs, tested with Arabic text (November 2026). The pictures come from free
services run by others: they can be slow or go away, so always put the full text in the alt text. The phone app
shows plain pictures; pictures from these services are not verified there yet.

In the code to copy, replace `YOUR-NAME` with your GitHub user name (the live pictures here use demo accounts).

✔ works · ⚠ works with a flaw · ✘ does not work

**Arabic with a Latin word in a picture's text** (`العربية على GitHub`): the picture lays the text out left to
right, so the Latin word lands on the wrong side. Wrap the text in RLI…PDI (`%E2%81%A7` … `%E2%81%A9` in the URL), as
in the examples below (test S13).

| Style | Result | Test |
|---|---|---|
| Banner with an Arabic title | ✔ capsule-render. Arabic is joined and in order. The font is the reader's system font; `fontFamily` only works if the reader has that font. | S1 |
| Footer wave | ✔ capsule-render with no text: the same in every language. | S2 |
| Typing text | ⚠ readme-typing-svg. `font=Amiri` embeds a real Arabic font in the picture. But it types from the left, so the end of the sentence shows first: keep each line short. | S3 |
| Badges with Arabic text | ⚠ shields.io pulls Arabic letters apart and reverses them: don't use it for Arabic. badgen.net draws Arabic correctly, and so does the komarev views counter. | S4, S8 |
| Contribution streak card in Arabic | ✔ streak-stats with `locale=ar`: the whole card is Arabic and right to left. | S5 |
| Stats card in Arabic | ⚠ GitHub Stats Extended (the successor of the unmaintained github-readme-stats) with `locale=ar`: Arabic labels, but the colons are on the wrong side and the card is left to right. Its own Arabic title spells GitHub in Arabic letters: set your own with `custom_title`, wrapped in RLI…PDI as in the example. | S5 |
| Activity graph with an Arabic title | ✔ `custom_title` takes Arabic; the axes stay in English. | S6 |
| Arabic quote card | ✔ github-readme-quotes: the Arabic is joined and in order; the dash before the author lands on its left. | S7 |
| Skill icons | ✔ skillicons: no text, the same in every language. | S9 |
| Picture beside the text | ✔ An image with `align="left"` inside the RTL div; the Arabic wraps around it from the right. | S10 |
| Arabic and English side by side | ✔ A two-column table, the Arabic cell with `dir="rtl"` on the right. | S10 |
| Collapsible contents | ✔ `<details>` inside the RTL div, with Arabic heading links. | S11 |
| Centered nav bar | ✔ Arabic links with emoji, in a centered block with `dir="rtl"` (without it the phone app puts the links left to right). | S12 |
| github-profile-trophy | ✘ the public service is down (HTTP 402) | — |

## Copy and paste

### Banner with an Arabic title

```html
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&fontSize=48&desc=%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D8%AC%D8%B1%D9%8E%D9%91%D8%A8%20%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&descAlignY=72" alt="العربية على GitHub">
```

### Footer wave

```html
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="">
```

### Typing text

```html
<img src="https://readme-typing-svg.demolab.com/?lines=%D9%85%D8%B1%D8%AD%D8%A8%D9%8B%D8%A7%20%D8%A8%D9%83%20%D9%81%D9%8A%20%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9;%D8%A7%D9%83%D8%AA%D8%A8%20%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9%20%D8%A8%D8%AB%D9%82%D8%A9&font=Amiri&center=true&width=500&size=32" alt="مرحبًا بك في دليل العربية">
```

### Badges with Arabic text

```html
<img src="https://badgen.net/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5/MIT/green" alt="الترخيص: MIT"> <img src="https://komarev.com/ghpvc/?username=YOUR-NAME&label=%D8%B9%D8%AF%D8%AF%20%D8%A7%D9%84%D8%B2%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA&color=2ea44f" alt="عدد الزيارات">
```

### Contribution streak card in Arabic

```html
<img src="https://streak-stats.demolab.com/?user=YOUR-NAME&locale=ar" alt="سلسلة المساهمات">
```

### Stats card in Arabic

```html
<img src="https://github-stats-extended.vercel.app/api?username=YOUR-NAME&locale=ar&show_icons=true&custom_title=%E2%81%A7%D8%A5%D8%AD%D8%B5%D8%A7%D8%A1%D8%A7%D8%AA%20GitHub%E2%81%A9" alt="إحصاءات GitHub">
```

### Activity graph with an Arabic title

```html
<img src="https://github-readme-activity-graph.ashutosh-dwivedi0710.workers.dev/graph?username=YOUR-NAME&custom_title=%E2%81%A7%D9%86%D8%B4%D8%A7%D8%B7%D9%8A%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&hide_border=true" alt="نشاطي على GitHub">
```

### Arabic quote card

```html
<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&quote=%D9%85%D9%86%20%D8%AC%D8%AF%D9%8E%D9%91%20%D9%88%D8%AC%D8%AF%D8%8C%20%D9%88%D9%85%D9%86%20%D8%B2%D8%B1%D8%B9%20%D8%AD%D8%B5%D8%AF&author=%D9%85%D8%AB%D9%84%20%D8%B9%D8%B1%D8%A8%D9%8A" alt="من جدَّ وجد، ومن زرع حصد">
```

### Skill icons

```html
<img src="https://skillicons.dev/icons?i=python,js,html,css,git,github" alt="Python, JavaScript, HTML, CSS, Git, GitHub">
```

### Picture beside Arabic text

```html
<div dir="rtl">

<img src="logo.png" align="left" width="80" alt="الشعار">

فقرة عربية بجانب الصورة.

<br clear="left">

</div>
```

### Collapsible Arabic contents

```html
<div dir="rtl">

<details>
<summary><b>المحتويات</b></summary>

- [التثبيت](#التثبيت)
- [الاستعمال](#الاستعمال)

</details>

</div>
```
