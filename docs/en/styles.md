# README styles with Arabic

[العربية](../ar/styles.md) · [Guide](guide.md) · [Heritage style](heritage.md) · [Test page](../../tests/styles.md)

The styles people use most in GitHub READMEs, tested with Arabic text (November 2026). The pictures come from free
services run by others: they can be slow or go away, so always put the full text in the alt text. The phone app
shows plain pictures; pictures from these services are not verified there yet.

In the code to copy, replace `YOUR-NAME` with your GitHub user name (the live pictures here use demo accounts).

✔ works · ⚠ works with a flaw · ✘ does not work

Most of these services draw left to right, so this guide has two tools that make the picture in your repo, right to left: `code/typing_svg.py` (typing text) and `code/arabic_cards.py` (badge, stats card, quote card). Copy the two files into your repo; they need Python 3.10 or newer and no extra packages.

**Arabic with a Latin word in a picture's text** (`العربية على GitHub`): the picture lays the text out left to
right, so the Latin word lands on the wrong side. Wrap the text in RLI…PDI (`%E2%81%A7` … `%E2%81%A9` in the URL), as
in the examples below (test S13).

| Style | Result | Test |
|---|---|---|
| Banner with an Arabic title | ✔ capsule-render. Arabic is joined and in order. The font is the reader's system font; `fontFamily` only works if the reader has that font. | S1 |
| Footer wave | ✔ capsule-render with no text: the same in every language. | S2 |
| Typing text | ✔ `code/typing_svg.py` makes the picture in your repo: it writes Arabic from the right and builds a Google font into it (`--still` for a fixed one). ⚠ readme-typing-svg types Arabic from the left, so the end of the sentence shows first. | S3 |
| Badges with Arabic text | ✔ `code/arabic_cards.py badge`: label on the right, value on the left. ✘ shields.io pulls Arabic letters apart and reverses them. ⚠ badgen.net and the komarev views counter draw the letters right but put the label on the left. | S4, S8 |
| Contribution streak card in Arabic | ✔ streak-stats with `locale=ar`: the whole card is Arabic and right to left. | S5 |
| Stats card in Arabic | ✔ `code/arabic_cards.py stats` reads your numbers from GitHub: title and labels on the right, numbers on the left. It is a still picture: make it again to refresh (by hand or on a GitHub Actions schedule). ⚠ GitHub Stats Extended with `locale=ar` is left to right, the colons are on the wrong side and a long label can run into its number. | S5 |
| Activity graph with an Arabic title | ⚠ `custom_title` takes Arabic; the axes stay in English and the days run left to right. | S6 |
| Arabic quote card | ✔ `code/arabic_cards.py quote`: right-aligned, in «», the author under it after a dash. ⚠ github-readme-quotes puts the text on the left and the dash on the author's left. | S7 |
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

```sh
python code/typing_svg.py --line "مرحبًا بك في دليل العربية" --line "اكتب العربية على GitHub بثقة" --font Amiri --size 32 --width 560 --out docs/typing.svg
```

```html
<img src="docs/typing.svg" alt="مرحبًا بك في دليل العربية. اكتب العربية على GitHub بثقة">
```

### Badges with Arabic text

```sh
python code/arabic_cards.py badge --label "الترخيص" --value MIT --out docs/badge-license.svg
```

```html
<img src="docs/badge-license.svg" alt="الترخيص: MIT"> <img src="https://komarev.com/ghpvc/?username=YOUR-NAME&label=%D8%B9%D8%AF%D8%AF%20%D8%A7%D9%84%D8%B2%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA&color=2ea44f" alt="عدد الزيارات">
```

### Contribution streak card in Arabic

```html
<img src="https://streak-stats.demolab.com/?user=YOUR-NAME&locale=ar" alt="سلسلة المساهمات">
```

### Stats card in Arabic

```sh
python code/arabic_cards.py stats --user YOUR-NAME --out docs/stats.svg
```

To refresh it every day:

```yaml
# .github/workflows/stats.yml
name: stats
on:
  schedule: [{cron: "0 3 * * *"}]
  workflow_dispatch:
permissions:
  contents: write
jobs:
  stats:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: python code/arabic_cards.py stats --user YOUR-NAME --out docs/stats.svg
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
      - run: |
          git config user.name github-actions
          git config user.email github-actions@users.noreply.github.com
          git add docs/stats.svg
          git diff --cached --quiet || git commit -m "$(printf '\u2067تحديث الإحصاءات\u2069') · Update stats"
          git push
```

### Activity graph with an Arabic title

```html
<img src="https://github-readme-activity-graph.ashutosh-dwivedi0710.workers.dev/graph?username=YOUR-NAME&custom_title=%E2%81%A7%D9%86%D8%B4%D8%A7%D8%B7%D9%8A%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&hide_border=true" alt="نشاطي على GitHub">
```

### Arabic quote card

```sh
python code/arabic_cards.py quote --text "من جدّ وجد، ومن زرع حصد" --author "مثل عربي" --out docs/quote.svg
```

```html
<img src="docs/quote.svg" alt="من جدّ وجد، ومن زرع حصد. مثل عربي">
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

## Does not work

- shields.io badges with Arabic text: the letters are pulled apart and reversed.
- github-profile-trophy: the public service is down (HTTP 402).
- Named fonts in capsule-render pictures: shown only if the reader has that font.
