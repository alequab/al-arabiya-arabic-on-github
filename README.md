<div align="center">

<img src="docs/assets/opening-kufic.svg" width="560" alt="بسم الله الرحمن الرحيم، والصلاة والسلام على رسول الله">

<h4 dir="rtl">العربية على GitHub&rlm; · Arabic on GitHub</h4>

<div dir="rtl">

[قبل وبعد](#قبل-القاعدة-وبعدها) · [الخلاصة](#الخلاصة) · [الدليل الكامل](docs/ar/guide.md) · [الأنماط](docs/ar/styles.md) · [الطراز التراثي](docs/ar/heritage.md) · [الأدوات](#الأدوات) · [للذكاء الاصطناعي](#للذكاء-الاصطناعي) · [صفحة الاختبارات](tests/lab.md) · [مسرد المصطلحات](docs/glossary.md) · [المساهمة](CONTRIBUTING.md) · [الترخيص](#الترخيص)

</div>

[Before and after](#before-and-after) · [Summary](#summary) · [Full guide](docs/en/guide.md) · [Styles](docs/en/styles.md) · [Heritage style](docs/en/heritage.md) · [Tools](#tools) · [For AI tools](#for-ai-tools) · [Test page](tests/lab.md) · [Glossary](docs/glossary.md#glossary) · [Contributing](CONTRIBUTING.md) · [License](#license)

</div>

<div dir="rtl">

دليل مجرَّب لكتابة العربية (من اليمين إلى اليسار) على GitHub: الملفات التمهيدية والتوثيق والبلاغات وطلبات الدمج وملاحظات الإصدار ووصف المستودع والعناوين والأسماء. كل قاعدة فيه جُرّبت على الموقع، ولأكثرها اختبار حي في [صفحة الاختبارات](tests/lab.md). ونتائج تطبيق الهاتف (Android) من لقطات حقيقية حيث ذُكر ذلك، وإلا فمن أداة تحاكيه.

### قبل القاعدة وبعدها

أمثلة حية: انظر كيف يعرضها GitHub على هذه الصفحة الآن.

**1. سطر يبدأ بكلمة لاتينية** ([T2](tests/lab.md#t2))

✘ بلا علامة، فيقف السطر على اليسار وتنتقل نقطته:

<!-- check-arabic: off -->

GitHub هو الموقع الذي تُعرض عليه هذه الصفحة.

<!-- check-arabic: on -->

✔ مع &lrm;`&rlm;`&lrm; في أوله، وهو داخل وسم الاتجاه فيعرضه تطبيق الهاتف صحيحًا أيضًا:

&rlm;GitHub هو الموقع الذي تُعرض عليه هذه الصفحة.

**2. جدول عربي** ([T6](tests/lab.md#t6))

✘ خارج وسم الاتجاه، فتبدأ أعمدته من اليسار:

</div>

<!-- check-arabic: off -->

| الأداة | عملها |
|---|---|
| الفحص | يجد المشكلات في ملفاتك |
| العلامات | يضعها في العناوين |

<!-- check-arabic: on -->

<div dir="rtl">

✔ داخل &lrm;`<div dir="rtl">`&lrm;:

| الأداة | عملها |
|---|---|
| الفحص | يجد المشكلات في ملفاتك |
| العلامات | يضعها في العناوين |

**3. عنوان بلغتين** في قائمة الإيداعات أو البلاغات ([T37](tests/lab.md#t37)، [T46](tests/lab.md#t46))، وهذه الكتلة تعرضه كما تعرضه تلك القوائم:

⚠ بلا علامات، فالترتيب صحيح لكن الجزء العربي يقع على اليسار ويُقرأ آخرًا:

</div>

```
إضافة دليل التثبيت · Add the install guide
```

<div dir="rtl">

✔ العنوان كله بين علامتي RLI وPDI، فيقع العربي على اليمين ويُقرأ أولًا (الأداة &lrm;`code/arabic_text.py`&lrm; تضعهما):

</div>

```
⁧إضافة دليل التثبيت‏ · Add the install guide‎⁩
```

<div dir="rtl">

### الخلاصة

1. السطر العربي يقف على اليمين وحده، لأن GitHub يأخذ اتجاه كل فقرة من أول حرف فيها.
2. إن بدأ السطر العربي بكلمة لاتينية فابدأه بالعلامة &lrm;`&rlm;`&lrm;.
3. ضع القسم العربي داخل &lrm;`<div dir="rtl">`&lrm;، فتطبيق الهاتف والجداول وملاحظات الإصدار تحتاجه، واترك سطرًا فارغًا بعد فتحه وقبل إغلاقه.
4. أغلق هذا العنصر قبل كتل الشيفرة وقبل تنبيهات GitHub، ثم افتحه بعدها.
5. تجنّب في العربية: الاقتباس &lrm;`>`&lrm;، والحواشي الأصلية &lrm;`[^1]`&lrm;، والمائل، وقوائم المهام.
6. وصف المستودع والعناوين حقول من اليسار إلى اليمين، فضعها بين علامتي RLI وPDI، والعنوان ذو اللغتين يوضع كله بينهما كالوصف، فيظهر العربي على اليمين (الأداة &lrm;`code/arabic_text.py`&lrm; تفعل ذلك).
7. أسماء المستودعات والمواضيع بالإنجليزية، ووسم الإصدار (tag) العربي كلمة عربية مع أرقام غربية.
8. اكتب النص كاملًا في الوصف البديل لكل صورة، وانظر إلى صفحتك في تطبيق الهاتف أيضًا.

التفاصيل والأمثلة في [الدليل الكامل](docs/ar/guide.md)، وأشهر أنماط تزيين الملف التمهيدي مجرَّبةً بالعربية في [صفحة الأنماط](docs/ar/styles.md): اللافتات والنص الذي يُكتب أمامك والشارات والبطاقات. وفي [الطراز التراثي](docs/ar/heritage.md) طراز مأخوذ من الكتاب العربي القديم: الفواتح والفواصل والأبواب والفوائد والعدّ بأبجد والشعر والحواشي والخطوط.

### الأدوات

- أداة فحص ملفات Markdown، تُخرج لكل مشكلة سطرها وسببها. وما بين &lrm;`<!-- check-arabic: off -->`&lrm; و&lrm;`<!-- check-arabic: on -->`&lrm; لا تُبلّغ عنه، للأمثلة الخاطئة عمدًا:

</div>

```powershell
python code/check_arabic_md.py README.md docs
```

<div dir="rtl">

- أداة تصنع وصف المستودع، وبالأمر &lrm;`title`&lrm; عناوين البلاغات وطلبات الدمج والإصدارات، وبالأمر &lrm;`commit`&lrm; رسائل الإيداعات، بالعلامات الخفية الصحيحة:

</div>

```powershell
python code/arabic_text.py about --ar "دليل كتابة العربية" --en "Guide to writing Arabic." --out about.txt
gh api -X PATCH repos/OWNER/REPO -F description=@about.txt
```

<div dir="rtl">

- أداة تفحص صفحة على github.com كما يعرضها الموقع وكما يعرضها تطبيق الهاتف: [`code/page_audit.js`](code/page_audit.js)، تُلصق في وحدة التحكم في المتصفح، ثم يُشغَّل &lrm;`auditArabic("web")`&lrm; ثم &lrm;`auditArabic("phone")`&lrm;.
- أداة ترسم نصًا عربيًا بخطوط Windows على هيئة صور تُقرأ في الوضعين الداكن والفاتح (تختار أنت النص والخطوط واللون): [`code/make-font-samples.ps1`](code/make-font-samples.ps1).
- أدوات تصنع صورًا من اليمين إلى اليسار في مستودعك: نصًّا يُكتب أمامك بخط عربي، أو ثابتًا بالخيار &lrm;`--still`&lrm; ([`code/typing_svg.py`](code/typing_svg.py))، وشارة وبطاقة إحصاءات وبطاقة اقتباس ([`code/arabic_cards.py`](code/arabic_cards.py))، وزخارف المخطوطات ([`code/ornaments.py`](code/ornaments.py)).
- قالب جاهز لملف تمهيدي بالعربية والإنجليزية: [`templates/README.ar-en.md`](templates/README.ar-en.md).
- اختبارات الأدوات: &lrm;`python code/test_tools.py`&lrm;.

الأدوات تحتاج Python 3.10 أو أحدث، ولا تحتاج مكتبات إضافية.

الإصدارات ووسومها والفروع والبلاغات والنقاشات في هذا المستودع مواد اختبار، تربط إليها صفحة الاختبارات شواهدَ.

### للذكاء الاصطناعي

الملف [`AGENTS.md`](AGENTS.md) فيه القواعد مرقمة مختصرة لأدوات الذكاء الاصطناعي، والملف [`llms.txt`](llms.txt) فهرس للمستودع. أعطِ أداتك رابط المستودع أو انسخ لها ملف القواعد.

### الترخيص

المستودع كله بترخيص [MIT](LICENSE): انسخه وعدّله واستعمله كما تشاء، مع إبقاء إشعار الترخيص.

</div>

---

A tested guide to writing Arabic (right-to-left) text on GitHub: README and docs, issues, pull requests, release
notes, the repo About text, titles and names. Every rule was checked on github.com, and most have a live test on the [test page](tests/lab.md). Phone-app
(Android) results come from real screenshots where marked, otherwise from a tool that copies the app.

### Before and after

Live examples: see how GitHub shows them on this page right now.

**1. An Arabic line that starts with a Latin word** ([T2](tests/lab.md#t2))

✘ No mark: the line sits on the left and its full stop moves.

<!-- check-arabic: off -->

GitHub هو الموقع الذي تُعرض عليه هذه الصفحة.

<!-- check-arabic: on -->

✔ With `&rlm;` at the start (inside the RTL div, so the phone app shows it right too):

<div dir="rtl">

&rlm;GitHub هو الموقع الذي تُعرض عليه هذه الصفحة.

</div>

**2. An Arabic table** ([T6](tests/lab.md#t6))

✘ Outside the RTL div: the columns start from the left.

<!-- check-arabic: off -->

| الأداة | عملها |
|---|---|
| الفحص | يجد المشكلات في ملفاتك |
| العلامات | يضعها في العناوين |

<!-- check-arabic: on -->

✔ Inside `<div dir="rtl">`:

<div dir="rtl">

| الأداة | عملها |
|---|---|
| الفحص | يجد المشكلات في ملفاتك |
| العلامات | يضعها في العناوين |

</div>

**3. A bilingual title** in a commit or issue list ([T37](tests/lab.md#t37), [T46](tests/lab.md#t46)); this block shows it the way those lists do.

⚠ No marks: the order is right, but the Arabic lands on the left, read last.

```
إضافة دليل التثبيت · Add the install guide
```

✔ The whole title in RLI…PDI: the Arabic on the right, read first (`code/arabic_text.py` adds the marks).

```
⁧إضافة دليل التثبيت‏ · Add the install guide‎⁩
```

### Summary

1. An Arabic line sits on the right by itself: GitHub takes each paragraph's direction from its first letter.
2. If an Arabic line starts with a Latin word, start it with `&rlm;`.
3. Put the Arabic section in `<div dir="rtl">` (the phone app, tables and release notes need it), with a blank line after the
   opening tag and before the closing one.
4. Close that div before code blocks and GitHub alerts, and reopen it after.
5. Avoid in Arabic: `>` quotes, `[^1]` footnotes, italic, task lists.
6. The About text and titles are left-to-right fields: wrap them in RLI…PDI (a bilingual title whole, like the About text, so the Arabic shows on the right) (`code/arabic_text.py` does it).
7. Repo names and topics in English; an Arabic tag is an Arabic word with Western digits.
8. Put the full text in every picture's alt text, and look at your page in the phone app too.

Details and examples: [full guide](docs/en/guide.md). Popular README styles (banners, typing text, badges, cards)
tested with Arabic: [styles](docs/en/styles.md). A style taken from the classical Arabic book (openings, dividers,
chapters, notes, abjad numbering, verse, margin notes, fonts): [heritage style](docs/en/heritage.md).

### Tools

- `python code/check_arabic_md.py README.md docs`: checks Markdown files and prints each problem with its line and reason.
  Lines between `<!-- check-arabic: off -->` and `<!-- check-arabic: on -->` are not reported (for deliberate mistakes).
- `python code/arabic_text.py about --ar "..." --en "..." --out about.txt`: builds the About text (and, with
  `title`, issue / PR / release titles, and with `commit`, commit messages) with the right invisible marks. Then
  `gh api -X PATCH repos/OWNER/REPO -F description=@about.txt` sets the About text.
- [`code/make-font-samples.ps1`](code/make-font-samples.ps1): draws Arabic text in Windows fonts as pictures that
  read on dark and light pages (text, fonts and colours are parameters).
- [`code/page_audit.js`](code/page_audit.js): paste into the browser console on a github.com page, run
  `auditArabic("web")` and `auditArabic("phone")`; lists what reads wrong on the website and in the phone app.
- Right-to-left pictures made in your repo: typing text in an Arabic font, or still text with `--still`
  ([`code/typing_svg.py`](code/typing_svg.py)), badge, stats card and quote card
  ([`code/arabic_cards.py`](code/arabic_cards.py)), manuscript ornaments ([`code/ornaments.py`](code/ornaments.py)).
- A ready README template in Arabic and English: [`templates/README.ar-en.md`](templates/README.ar-en.md).
- Tests: `python code/test_tools.py`. Python 3.10 or newer, no extra packages.

The releases, tags, branches, issues and discussions in this repo are test fixtures: the test page links to them as
evidence.

### For AI tools

[`AGENTS.md`](AGENTS.md) has the short, numbered rules for AI tools; [`llms.txt`](llms.txt) is an index of the repo.
Give your tool the repo link, or paste it the rules file.

### License

The whole repo is under the [MIT license](LICENSE): copy it, change it and use it as you like; keep the
license notice.
