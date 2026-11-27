<div dir="rtl" align="justify">

# الطراز التراثي للملف التمهيدي

&rlm;[English](../en/heritage.md) · [الأنماط](styles.md) · [الدليل](guide.md)

طراز للملف التمهيدي مأخوذ من تقاليد الكتاب العربي: الفواتح والخواتم، والأبواب والفصول، والفوائد والتنبيهات، والعدّ بحروف أبجد، والحواشي، وأبيات الشعر بصدرها وعجزها. كل ما في الصفحة نص، إلا قسمَي الخطوط التراثية والزخرفة الهندسية ففيهما صور، فاتركهما إن لم تُرد صورًا. جُرّبت الصفحة على الموقع وبوضع الهاتف في أداة page_audit.js (نوفمبر 2026).

العلامات: ✔ يعمل · ⚠ يعمل مع عيب · ✘ لا يعمل

الأمثلة في كتل الشيفرة تجري من اليسار إلى اليمين، فقد يبدو فيها ترتيب العربية مع الوسوم مضطربًا، لكنها تُنسخ صحيحة.

<div align="center">

ـــــــــ ۞ ـــــــــ

</div>

## ۞ الفاتحة

✔ يبدأ الكتاب بالبسملة، ثم الحمد والصلاة، ثم «أما بعد». اكتبها عناوين صغيرة في الوسط، كل سطر في &lrm;`<h3 dir="rtl">`&lrm;، فلا يرسم GitHub تحتها خطًّا، ويعرضها الهاتف من اليمين.

<div align="center">

<h3 dir="rtl">بسم الله الرحمن الرحيم</h3>
<h3 dir="rtl">والصلاة والسلام على نبينا محمد</h3>

</div>

أما بعد، فهذا دليل في كتابة العربية على GitHub.

</div>

```html
<div align="center">

<h3 dir="rtl">بسم الله الرحمن الرحيم</h3>
<h3 dir="rtl">والصلاة والسلام على نبينا محمد</h3>

</div>

أما بعد، فهذا ...
```

<div dir="rtl" align="justify">

## ۞ الفواصل

✔ زخارف من الحروف تفصل بين الأقسام بدل الخط الأفقي. ضعها وحدها في سطر داخل &lrm;`<div align="center">`&lrm;. وهي متناظرة، فلا يظهر فيها أثر الاتجاه.

<div align="center">

ـــــــــ ۞ ـــــــــ

❁ ❁ ❁

✿ ✿ ✿

◆ ◇ ◆

</div>

</div>

```html
<div align="center">

ـــــــــ ۞ ـــــــــ

</div>
```

<div dir="rtl" align="justify">

الخط الممدود هو حرف التطويل «ـ». ولا تضع التطويل داخل الكلمات (مثل «بســـم»)، لأن البحث في GitHub لا يجد الكلمة حينئذٍ برسمها المعتاد (الاختبار T40).

## ۞ الأبواب والفصول

✔ سمِّ الأقسام كما تُسمّى في الكتب: المقدمة، ثم الباب الأول، وفيه فصول، ثم الخاتمة. وضع الزخرفة في أول العنوان أو اتركها.

### الباب الأول: في التثبيت

#### فصل: المتطلبات

</div>

```markdown
<!-- headings like book chapters -->
## ۞ المقدمة
## ۞ الباب الأول: في التثبيت
### فصل: المتطلبات
## ۞ الخاتمة
```

<div dir="rtl" align="justify">

⚠ الزخرفة في أول العنوان تُحذف من رابطه، ويبقى مكانها شَرطة. فرابط «۞ الفاتحة» هو ‎`#-الفاتحة`‎، مثل هذا: [الفاتحة](#-الفاتحة).

## ۞ الفوائد والتنبيهات

✔ في كتب التراث «فائدة» و«تنبيه» و«قاعدة». اجعلها تنبيهات GitHub، واكتب الاسم العربي في أول النص، والنص في &lrm;`<p dir="rtl">`&lrm;. يبقى اسم التنبيه الإنجليزي فوقها (Note وغيره)، ولا سبيل إلى تغييره. والتنبيه لا يُرسم داخل &lrm;`<div dir="rtl" align="justify">`&lrm;، فأغلق القسم قبله وافتحه بعده.

</div>

> [!NOTE]
> <p dir="rtl"><b>فائدة:</b> الرموز والأرقام لا تحدد اتجاه السطر، وإنما يحدده أول حرف.</p>

> [!TIP]
> <p dir="rtl"><b>لطيفة:</b> ضع &lrm;<code>&amp;rlm;</code>&lrm; في أول السطر الذي يبدأ بكلمة إنجليزية.</p>

> [!IMPORTANT]
> <p dir="rtl"><b>قاعدة:</b> كل نص عربي داخل &lrm;<code>&lt;div dir="rtl"&gt;</code>&lrm;.</p>

> [!WARNING]
> <p dir="rtl"><b>تنبيه:</b> تطبيق الهاتف لا يعرض الصور داخل &lrm;<code>&lt;picture&gt;</code>&lrm;.</p>

> [!CAUTION]
> <p dir="rtl"><b>تحذير:</b> لا تستعمل الخاصية align بقيمة right للعربية، فإنها تخلط الكلمات في الهاتف.</p>

```markdown
> [!NOTE]
> <p dir="rtl"><b>فائدة:</b> النص هنا.</p>
```

<div dir="rtl" align="justify">

الأسماء المقترحة: Note ← فائدة · Tip ← لطيفة · Important ← قاعدة · Warning ← تنبيه · Caution ← تحذير

## ۞ العدّ بحروف أبجد

✔ القوائم المرقّمة في Markdown تظهر بالأرقام الغربية (1. 2. 3.) دائمًا. فإن أردت العدّ بحروف أبجد أو بالأرقام الهندية (١، ٢، ٣) فاكتبه بيدك، كل بند في سطر، وبين الأسطر &lrm;`<br>`&lrm;:

**أ.** اكتب النص العربي داخل &lrm;`<div dir="rtl" align="justify">`&lrm;.<br>
**ب.** اترك سطرًا فارغًا بعد الوسم وقبل إغلاقه.<br>
**ج.** افحص الملف بأداة check_arabic_md.py.<br>
**د.** افحص الصفحة بأداة page_audit.js.<br>
**هـ.** انظر في الصفحة على الهاتف.

</div>

```markdown
<!-- abjad numbering, one line each -->
**أ.** البند الأول.<br>
**ب.** البند الثاني.<br>
**ج.** البند الثالث.
```

<div dir="rtl" align="justify">

ترتيب أبجد: أ ب ج د هـ و ز ح ط ي، ثم ك (٢٠) ل (٣٠) م (٤٠) ن (٥٠).

## ۞ الآيات والأحاديث

✔ ضع الآية بين القوسين المزخرفين ﴿ ﴾ وبعدها اسم السورة ورقم الآية، والحديث والنقل بين «علامتي التنصيص». الحركات تظهر صحيحة على الموقع، لكن البحث لا يجد الكلمة المشكولة إلا بحركاتها (الاختبار T40).

<div align="center">

<h4 dir="rtl">﴿ وَقُل رَّبِّ زِدْنِي عِلْمًا ﴾ [طه: ١١٤]</h4>

</div>

</div>

```html
<h4 dir="rtl">﴿ وَقُل رَّبِّ زِدْنِي عِلْمًا ﴾ [طه: ١١٤]</h4>
```

<div dir="rtl" align="justify">

⚠ شكل القوسين من خط جهاز القارئ، وبعض الخطوط (كخط ويندوز) ترسمهما قريبين من القوسين العاديين. وللقوسين المزخرفين حرفان، فاكتب الذي على اليمين أولًا: ﴿ (U+FD3F) ثم الآية ثم ﴾ (U+FD3E). ولا تنسخ آية من مصدر لا تثق به، وراجعها في المصحف.

## ۞ الشعر

✔ يُكتب البيت شطرين متقابلين: الصدر على اليمين، والعجز على اليسار. اجعلهما في سطر واحد في الوسط، وبينهما فراغ واسع (&lrm;`&emsp;`&lrm;):

<div align="center">

<p dir="rtl">الخيلُ والليلُ والبيداءُ تعرفني&emsp;&emsp;&emsp;والسيفُ والرمحُ والقرطاسُ والقلمُ</p>

<p dir="rtl">— المتنبي</p>

</div>

</div>

```html
<div align="center">

<p dir="rtl">الصدر&emsp;&emsp;&emsp;العجز</p>

</div>
```

<div dir="rtl" align="justify">

⚠ إن ضاقت الشاشة (كالهاتف) نزل العجز تحت الصدر. وهذا مقبول، فكثير من الكتب تطبع الشعر هكذا.

## ۞ ضبط الأسطر

✔ في Word زرّ «ضبط» يجعل أطراف الأسطر متساوية من الجهتين. ومثله في GitHub الخاصية &lrm;`align="justify"`&lrm; مع &lrm;`dir="rtl"`&lrm;. وهذه الصفحة كلها مكتوبة بها، فانظر إلى الطرف الأيسر من الفقرات الطويلة. (الاختبار T36)

</div>

```html
<div dir="rtl" align="justify">

فقرة عربية طويلة ...

</div>
```

<div dir="rtl" align="justify">

⚠ المتصفح يضبط السطر بتوسيع المسافات بين الكلمات، لا بمدّ الحروف (الكشيدة) كما يفعل Word. وفي الشاشة الضيقة قد تتسع المسافات في بعض الأسطر، فاستعمله للفقرات الطويلة. ولم يُتحقق منه في تطبيق الهاتف بعد.

## ۞ الحواشي

✔ الحواشي في Markdown (&lrm;`[^1]`&lrm;) تُجمع في آخر الصفحة تحت عنوان إنجليزي «Footnotes» من اليسار. فاكتب الحاشية بيدك على طريقة الكتب: رقم صغير بين قوسين بعد الكلمة<sup>(١)</sup>، ثم قسم «الحواشي» في آخر الصفحة.

</div>

```markdown
<!-- hand-made footnote -->
بعد الكلمة<sup>(١)</sup>

## الحواشي

<sup>(١)</sup> نص الحاشية.
```

<div dir="rtl" align="justify">

## ۞ الخطوط التراثية (صور)

⚠ لا يمكن اختيار الخط في نص GitHub، فهو خط جهاز القارئ. فإن أردت عنوانًا بخط النسخ أو الكوفي أو الرقعة أو النستعليق، فاجعله صورة من خدمة readme-typing-svg، فهي تضمّن خطوط Google في الصورة. وعيبها أنها تكتب النص من اليسار حتى يتمّ، فاجعل `repeat=false` ليبقى النص بعد ذلك ثابتًا. واكتب النص كله في الوصف البديل (alt).

<div align="center">

<p dir="rtl"><b>النسخ</b> · Amiri</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Amiri&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

<p dir="rtl"><b>النسخ</b> · Scheherazade New</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Scheherazade+New&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

<p dir="rtl"><b>الكوفي</b> · Reem Kufi</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Reem+Kufi&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

<p dir="rtl"><b>الكوفي</b> · Kufam</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Kufam&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

<p dir="rtl"><b>الرقعة</b> · Aref Ruqaa</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Aref+Ruqaa&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

<p dir="rtl"><b>النستعليق</b> · Noto Nastaliq Urdu</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Noto+Nastaliq+Urdu&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

<p dir="rtl"><b>العناوين</b> · Rakkas</p>

<img src="https://readme-typing-svg.demolab.com/?lines=%D8%AF%D9%84%D9%8A%D9%84%20%D8%A7%D9%84%D9%83%D8%AA%D8%A7%D8%A8%D8%A9%20%D8%A7%D9%84%D8%B9%D8%B1%D8%A8%D9%8A%D8%A9&font=Rakkas&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="دليل الكتابة العربية">

</div>

</div>

```html
<img src="https://readme-typing-svg.demolab.com/?lines=نص-مرمّز&font=Amiri&center=true&width=520&height=90&size=44&repeat=false&color=C9A24D" alt="النص كاملًا">
```

<div dir="rtl" align="justify">

غيّر &lrm;`font=`&lrm; إلى اسم الخط في Google Fonts، والمسافة فيه &lrm;`+`&lrm;.

## ۞ زخرفة هندسية (صورة)

✔ شريط من النجوم الثمانية (الخاتم) في ملف SVG داخل المستودع، فلا يعتمد على خدمة خارجية. خلفيته شفافة، فيُرى في الوضع الفاتح والداكن. انسخ الملف `docs/assets/heritage-band.svg` إلى مستودعك.

<div align="center">

<img src="../assets/heritage-band.svg" width="840" alt="">

</div>

</div>

```html
<div align="center">

<img src="docs/assets/heritage-band.svg" width="840" alt="">

</div>
```

<div dir="rtl" align="justify">

## ۞ الخاتمة

✔ تُختم الكتب بالحمد، ثم ذكر تمام الكتاب وتاريخه بالهجري.

<div align="center">

ـــــــــ ۞ ـــــــــ

<h4 dir="rtl">وآخر دعوانا أن الحمد لله رب العالمين</h4>

<p dir="rtl">تمّ بحمد الله · جمادى الآخرة ١٤٤٨هـ</p>

</div>

</div>

```html
<div align="center">

<h4 dir="rtl">وآخر دعوانا أن الحمد لله رب العالمين</h4>

<p dir="rtl">تمّ بحمد الله · جمادى الآخرة ١٤٤٨هـ</p>

</div>
```

<div dir="rtl" align="justify">

## الحواشي

<sup>(١)</sup> هذه حاشية للمثال.

</div>
