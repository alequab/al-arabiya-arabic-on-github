<div dir="rtl">

# أنماط الملف التمهيدي بالعربية

&rlm;[English](../en/styles.md) · [الدليل](guide.md) · [الطراز التراثي](heritage.md) · [صفحة الاختبار](../../tests/styles.md)

أشهر ما يزيّن به الناس ملفاتهم التمهيدية على GitHub، مجرَّبًا بنص عربي (نوفمبر 2026). الصور من خدمات مجانية يديرها غيرنا، فقد تبطؤ أو تتوقف، فاكتب النص كاملًا في الوصف البديل لكل صورة. وتطبيق الهاتف يعرض الصور العادية، أما الصور من هذه الخدمات فلم يُتحقق منها فيه بعد.

في الشيفرة التي تنسخها ضع اسم حسابك على GitHub مكان &lrm;`YOUR-NAME`&lrm; (والصور الحية هنا لحسابات تجريبية).

العلامات: ✔ يعمل · ⚠ يعمل مع عيب · ✘ لا يعمل

إن كان في نص الصورة كلمة لاتينية بين العربية (مثل «العربية على GitHub») فالصورة ترتّب النص من اليسار إلى اليمين، فتقع الكلمة اللاتينية في غير مكانها. فضع النص كله بين علامتي RLI وPDI، وهما في الرابط ‎`%E2%81%A7`‎ في أوله و‎`%E2%81%A9`‎ في آخره، كما في الأمثلة هنا (الاختبار S13).

## صور من خدمات

### ✔ شعار علوي بعنوان عربي

خدمة capsule-render. العربية متصلة الحروف وصحيحة الترتيب. الخط خط جهاز القارئ، فالمعامل fontFamily لا ينفع إلا إن كان الخط عنده. (الاختبار S1)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&fontSize=48&desc=%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D8%AC%D8%B1%D9%8E%D9%91%D8%A8%20%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&descAlignY=72" alt="العربية على GitHub">

</div>

</div>

```html
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=180&section=header&text=%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&fontSize=48&desc=%D8%AF%D9%84%D9%8A%D9%84%20%D9%85%D8%AC%D8%B1%D9%8E%D9%91%D8%A8%20%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&descAlignY=72" alt="العربية على GitHub">
```

<div dir="rtl">

### ✔ موجة في آخر الصفحة

خدمة capsule-render بلا نص، فلا فرق فيها بين اللغات. (الاختبار S2)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="">

</div>

</div>

```html
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="">
```

<div dir="rtl">

### ⚠ نص يُكتب أمامك

خدمة readme-typing-svg. المعامل font=Amiri يضمّن خطًا عربيًا حقيقيًا في الصورة. لكن الكتابة تبدأ من اليسار، فتظهر آخر الجملة أولًا. فاجعل كل سطر قصيرًا. (الاختبار S3)

<div align="center">

<img src="https://readme-typing-svg.demolab.com/?lines=%D9%85%D8%B1%D8%AD%D8%A8%D9%8B%D8%A7%20%D8%A8%D9%83%20%D9%81%D9%8A%20%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9;%D8%A7%D9%83%D8%AA%D8%A8%20%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9%20%D8%A8%D8%AB%D9%82%D8%A9&font=Amiri&center=true&width=500&size=32" alt="مرحبًا بك في دليل العربية">

</div>

</div>

```html
<img src="https://readme-typing-svg.demolab.com/?lines=%D9%85%D8%B1%D8%AD%D8%A8%D9%8B%D8%A7%20%D8%A8%D9%83%20%D9%81%D9%8A%20%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9;%D8%A7%D9%83%D8%AA%D8%A8%20%E2%81%A7%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9%20%D8%A8%D8%AB%D9%82%D8%A9&font=Amiri&center=true&width=500&size=32" alt="مرحبًا بك في دليل العربية">
```

<div dir="rtl">

### ⚠ الشارات بنص عربي

شارات shields.io تفكك الحروف العربية وتعكس ترتيبها، فلا تستعملها للعربية. أما badgen.net فترسمها صحيحة، وكذلك عداد الزيارات komarev. (الاختباران S4 وS8)

<div align="center">

<img src="https://badgen.net/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5/MIT/green" alt="الترخيص: MIT"> <img src="https://komarev.com/ghpvc/?username=al-arabiya-arabic-on-github&label=%D8%B9%D8%AF%D8%AF%20%D8%A7%D9%84%D8%B2%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA&color=2ea44f" alt="عدد الزيارات">

</div>

</div>

```html
<img src="https://badgen.net/badge/%D8%A7%D9%84%D8%AA%D8%B1%D8%AE%D9%8A%D8%B5/MIT/green" alt="الترخيص: MIT"> <img src="https://komarev.com/ghpvc/?username=YOUR-NAME&label=%D8%B9%D8%AF%D8%AF%20%D8%A7%D9%84%D8%B2%D9%8A%D8%A7%D8%B1%D8%A7%D8%AA&color=2ea44f" alt="عدد الزيارات">
```

<div dir="rtl">

### ✔ بطاقة سلسلة المساهمات بالعربية

خدمة streak-stats مع locale=ar: البطاقة كلها عربية ومن اليمين إلى اليسار. (الاختبار S5)

<div align="center">

<img src="https://streak-stats.demolab.com/?user=denvercoder1&locale=ar" alt="سلسلة المساهمات">

</div>

</div>

```html
<img src="https://streak-stats.demolab.com/?user=YOUR-NAME&locale=ar" alt="سلسلة المساهمات">
```

<div dir="rtl">

### ⚠ بطاقة الإحصاءات بالعربية

خدمة GitHub Stats Extended (خليفة github-readme-stats الذي توقف تطويره) مع locale=ar: العناوين عربية، لكن النقطتين في الجهة الخطأ والبطاقة من اليسار. وعنوانها الذي تكتبه الخدمة فيه اسم GitHub بحروف عربية، فاكتب عنوانك بالمعامل custom_title، والنص بين RLI وPDI كما في المثال. (الاختبار S5)

<div align="center">

<img src="https://github-stats-extended.vercel.app/api?username=anuraghazra&locale=ar&show_icons=true&custom_title=%E2%81%A7%D8%A5%D8%AD%D8%B5%D8%A7%D8%A1%D8%A7%D8%AA%20GitHub%E2%81%A9" alt="إحصاءات GitHub">

</div>

</div>

```html
<img src="https://github-stats-extended.vercel.app/api?username=YOUR-NAME&locale=ar&show_icons=true&custom_title=%E2%81%A7%D8%A5%D8%AD%D8%B5%D8%A7%D8%A1%D8%A7%D8%AA%20GitHub%E2%81%A9" alt="إحصاءات GitHub">
```

<div dir="rtl">

### ✔ رسم النشاط بعنوان عربي

المعامل custom_title يقبل العربية، أما المحاور فإنجليزية. (الاختبار S6)

<div align="center">

<img src="https://github-readme-activity-graph.ashutosh-dwivedi0710.workers.dev/graph?username=denvercoder1&custom_title=%E2%81%A7%D9%86%D8%B4%D8%A7%D8%B7%D9%8A%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&hide_border=true" alt="نشاطي على GitHub">

</div>

</div>

```html
<img src="https://github-readme-activity-graph.ashutosh-dwivedi0710.workers.dev/graph?username=YOUR-NAME&custom_title=%E2%81%A7%D9%86%D8%B4%D8%A7%D8%B7%D9%8A%20%D8%B9%D9%84%D9%89%20GitHub%E2%81%A9&hide_border=true" alt="نشاطي على GitHub">
```

<div dir="rtl">

### ✔ بطاقة اقتباس عربي

خدمة github-readme-quotes: النص العربي متصل وصحيح، إلا أن الشَّرطة قبل اسم القائل تقع على يساره. (الاختبار S7)

<div align="center">

<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&quote=%D9%85%D9%86%20%D8%AC%D8%AF%D9%8E%D9%91%20%D9%88%D8%AC%D8%AF%D8%8C%20%D9%88%D9%85%D9%86%20%D8%B2%D8%B1%D8%B9%20%D8%AD%D8%B5%D8%AF&author=%D9%85%D8%AB%D9%84%20%D8%B9%D8%B1%D8%A8%D9%8A" alt="من جدَّ وجد، ومن زرع حصد">

</div>

</div>

```html
<img src="https://quotes-github-readme.vercel.app/api?type=horizontal&quote=%D9%85%D9%86%20%D8%AC%D8%AF%D9%8E%D9%91%20%D9%88%D8%AC%D8%AF%D8%8C%20%D9%88%D9%85%D9%86%20%D8%B2%D8%B1%D8%B9%20%D8%AD%D8%B5%D8%AF&author=%D9%85%D8%AB%D9%84%20%D8%B9%D8%B1%D8%A8%D9%8A" alt="من جدَّ وجد، ومن زرع حصد">
```

<div dir="rtl">

### ✔ أيقونات المهارات

خدمة skillicons بلا نص، فلا فرق فيها بين اللغات. (الاختبار S9)

<div align="center">

<img src="https://skillicons.dev/icons?i=python,js,html,css,git,github" alt="Python, JavaScript, HTML, CSS, Git, GitHub">

</div>

</div>

```html
<img src="https://skillicons.dev/icons?i=python,js,html,css,git,github" alt="Python, JavaScript, HTML, CSS, Git, GitHub">
```

<div dir="rtl">

## ترتيب الصفحة

### ✔ صورة بجانب النص

ضع الصورة بالمحاذاة &lrm;`align="left"`&lrm; داخل وسم الاتجاه، فيلتف النص العربي حولها من اليمين. (الاختبار S10)

</div>

```html
<div dir="rtl">

<img src="logo.png" align="left" width="80" alt="الشعار">

فقرة عربية بجانب الصورة.

<br clear="left">

</div>
```

<div dir="rtl">

### ✔ العربية والإنجليزية جنبًا إلى جنب

جدول بعمودين، والعمود العربي على اليمين بالوسم &lrm;`dir="rtl"`&lrm; على الخلية. (الاختبار S10)

### ✔ محتويات قابلة للطي

الوسم details داخل وسم الاتجاه، وفيه روابط العناوين العربية. (الاختبار S11)

</div>

```html
<div dir="rtl">

<details>
<summary><b>المحتويات</b></summary>

- [التثبيت](#التثبيت)
- [الاستعمال](#الاستعمال)

</details>

</div>
```

<div dir="rtl">

### ✔ شريط تنقل في الوسط

روابط عربية قبلها رموز تعبيرية، داخل وسم المحاذاة للوسط مع &lrm;`dir="rtl"`&lrm;، وبغيره يعرض تطبيق الهاتف الروابط من اليسار. (الاختبار S12)

## ما لا يعمل

- شارات shields.io بنص عربي: تتفكك الحروف وينعكس ترتيبها.
- كؤوس github-profile-trophy: الخدمة العامة متوقفة.
- الخطوط المسماة في صور capsule-render: لا تظهر إلا إن كان الخط عند القارئ.

</div>
