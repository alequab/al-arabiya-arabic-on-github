<div dir="rtl">

# مسرد المصطلحات

&rlm;[English](#glossary) · [الدليل](ar/guide.md) · [المساهمة](../CONTRIBUTING.md)

لكل مصطلح إنجليزي في هذا الدليل كلمة عربية واحدة. هذا الجدول يجمعها: المصطلح الإنجليزي، والكلمة المقترحة، ومعناها، والكلمات الأخرى التي رأيناها، ومصادرها، وحالها. فإن عرفت كلمة أصح أو مصدرًا أوثق، [فافتح مشكلة «مصطلح»](https://github.com/alequab/al-arabiya-arabic-on-github/issues/new?template=term.yml) واذكر المصطلح والكلمة التي تقترحها ومصدرها.

### الحال

- ✔ معتمد: مصدر واحد على الأقل يوافقه، وهو مستعمل في الدليل كله.
- ○ مستعمل: لم نجد له مصدرًا بعد، ولا خلاف عليه.
- ✎ اختير بدل كلمة أخرى: الكلمات الأخرى في صفه لا تُستعمل.
- ؟ يحتاج إلى اختيار: فيه أكثر من كلمة، ورأيك هنا يفيد.

### المصادر

- **و**: [ويكيبيديا العربية](https://ar.wikipedia.org)، عنوان المقالة المقابلة للمقالة الإنجليزية (2026-11-28).
- **ف**: [واجهة Forgejo العربية](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/options/locale/locale_ar.ini)، وهو برنامج منصة مثل GitHub، وواجهته مترجمة إلى العربية.
- **د**: [صفحة Git في ويكي Debian العربية](https://wiki.debian.org/ar/git).
- **ش**: كتب التراث في المكتبة الشاملة.
- **ح**: [دروس Git في أكاديمية حسوب](https://academy.hsoub.com/programming/workflow/git/)، أكبر موقع عربي لتعليم البرمجة.
- **ت**: [بحث مصطلحات Microsoft](https://learn.microsoft.com/globalization/reference/microsoft-terminology)، المسرد الرسمي لمنتجات Microsoft ومنها GitHub.
- **ر**: [مسرد ووردبريس العربي](https://translate.wordpress.org/locale/ar/default/glossary/)، وترجمة LibreOffice العربية.
- **م**: هذا المستودع، وعدد مرات الاستعمال فيه يوم كُتب المسرد (×).

## 1. مصطلحات GitHub وGit

| الإنجليزي | المقترح | المعنى | كلمات أخرى | المصدر | الحال |
|---|---|---|---|---|---|
| repository | المستودع | مجلد المشروع على GitHub بملفاته وتاريخه | | و، ف، د، ح، ت | ✔ |
| README | الملف التمهيدي | الملف الذي يُعرض أولًا في صفحة المستودع | اقرأني (و)، README بحروفه (ف)، ملف README (ح) | م ×9 | ✎ |
| commit | الإيداع | حفظ مجموعة تغييرات في تاريخ المستودع مع رسالة تصفها | الالتزام (م ×11)، التضمين (و)، الحفظ (د؛ وMicrosoft يقول «التثبيت» بمعنى قواعد البيانات) | ف، ح | ✎ |
| pull request | طلب السحب | طلب ضم تغييرات فرع إلى فرع آخر بعد مراجعتها | طلب الدمج (ف، م ×8) | ت، ح، ف | ✎ |
| merge | الدمج | ضم تغييرات فرع إلى فرع آخر | | ف، د، ح | ✔ |
| push | الدفع | إرسال الإيداعات من جهازك إلى المستودع على GitHub | | ح، ت، د | ✔ |
| fork | الاشتقاق | نسخة من مستودع غيرك في حسابك، تعمل عليها ثم تقترح تغييراتك | نسخة المستودع (ت)، التفرع، الشوكة | ف، ح | ✔ |
| clone | الاستنساخ | نسخ المستودع كله إلى جهازك | | ف، ح، د | ✔ |
| issue | المشكلة | صفحة يُبلَّغ فيها عن خطأ أو يُقترح فيها شيء. وما تجده أداة الفحص يُسمى «الأخطاء» حتى لا يُخلط بها | البلاغ (م ×15)، المسألة (ف)، القضية (ح) | ح | ✎ |
| release | الإصدار | نسخة منشورة من المشروع بملاحظاتها وملفاتها | | و، ف، د، ح، ر | ✔ |
| version | رقم الإصدار | الرقم الذي يميز كل إصدار، مثل 1.2.0 | رقم النسخة (م ×3؛ وووردبريس يقول «نسخة») | و، د، ف | ✎ |
| release notes | ملاحظات الإصدار | ما تغيّر في الإصدار، تحت عنوانه | | م | ○ |
| tag | وسم الإصدار | اسم ثابت يُعلَّق على إيداع بعينه، مثل v1.2.0. وتُذكر كلمة «الإصدار» معه دائمًا حتى لا يُخلط بوسم HTML | | ف، د، ر | ✔ |
| label | التصنيف | كلمة ملونة تُعلَّق على المشكلة أو طلب السحب | | ف | ✔ |
| topics | المواضيع | كلمات تصف المستودع وتظهر في صفحته | | ف | ✔ |
| branch | الفرع | خط عمل مستقل داخل المستودع | الإصدار الفرعي (ت) | ف، د، ح | ✔ |
| default branch | الفرع الافتراضي | الفرع الذي يُعرض أولًا ويُدمج فيه العمل | الفرع الأساسي (م ×1) | ف | ✎ |
| discussions | النقاشات | قسم للأسئلة والحوار خارج المشكلات | | م | ○ |
| poll | الاستطلاع | سؤال بخيارات يصوّت عليها الناس في النقاشات | | م | ○ |
| wiki | الويكي | صفحات توثيق يحررها أصحاب المستودع | الموسوعة (ف) | و، ح | ✔ |
| stars | النجوم | علامة إعجاب الناس بالمستودع | | ف | ✔ |
| contributions | المساهمات | ما قدّمه الشخص من إيداعات ومشكلات وغيرها | | ف | ✔ |
| About | وصف المستودع | النص القصير في أعلى صفحة المستودع | نبذة (قسم في الملف التمهيدي، م ×3) | ف | ✔ |
| license | الترخيص | شروط استعمال المشروع ونسخه | الرخصة (و، م ×1) | ف، م ×21 | ✎ |

## 2. التنسيق في Markdown

| الإنجليزي | المقترح | المعنى | كلمات أخرى | المصدر | الحال |
|---|---|---|---|---|---|
| Markdown | Markdown | لغة تنسيق النصوص التي يكتب بها GitHub، وتُكتب بحروفها اللاتينية كسائر أسماء المنتجات | ماركداون (و، م ×13) | | ✎ |
| code | الشيفرة | النص البرمجي | الكود (ف، م ×2)، التعليمات البرمجية | ح، م ×17 | ✎ |
| script | البرنامج النصي | برنامج قصير يُشغَّل بأمر | سكربت (م ×1، وحسوب يكتب «السكربتات») | | ✎ |
| code block | كتلة الشيفرة | شيفرة في سطور مستقلة بين ثلاث علامات &lrm;`` ` ``&lrm; | | م ×9 | ○ |
| HTML tag | الوسم | مثل &lrm;`<div>`&lrm; و&lrm;`<img>`&lrm; | | و، ح | ✔ |
| HTML attribute | الخاصية | ما يُكتب داخل الوسم، مثل &lrm;`dir="rtl"`&lrm; | الوسم (م ×2، خطأ)، الصفة | و، ح | ✎ |
| element | العنصر | الوسم مع ما بداخله | | و | ✔ |
| heading | العنوان | سطر يبدأ بعلامة &lrm;`#`&lrm; | | م | ○ |
| paragraph | الفقرة | | | و | ✔ |
| list / list item | القائمة / البند | | | م | ○ |
| footnote | الحاشية | تعليق في أسفل الصفحة تشير إليه علامة في النص | الحاشية السفلية (ر)، التعقيبة (و) | ش، ر | ✔ |
| alert | التنبيه | صندوق ملون مثل &lrm;`[!NOTE]`&lrm; | | م | ○ |
| quote | الاقتباس | سطر يبدأ بعلامة &lrm;`>`&lrm; | | م | ○ |
| table | الجدول | | | و | ✔ |
| link | الرابط | | الرابط التشعبي، الوصلة الترابطية (و) | و | ✔ |
| image | الصورة | | | و | ✔ |
| alt text | الوصف البديل | النص الذي يظهر مكان الصورة وتقرؤه قارئات الشاشة | النص البديل | م ×7 | ○ |
| emoji | الرموز التعبيرية | | إيموجي (و) | م | ○ |
| bold / italic | عريض / مائل | | | و (مائل) | ✔ |
| strikethrough / underline | الشطب / التسطير | خط على النص / خط تحته | الشخط (و) | م | ○ |
| superscript / subscript | النص المرتفع والمنخفض | نص صغير فوق السطر أو تحته | الرفع والخفض (م، ويُخلط برفع الملفات) | و | ✎ |
| math | المعادلة | | | م | ○ |
| diagram | المخطط | | | م | ○ |
| Mermaid | Mermaid | أداة ترسم المخططات من نص | ميرميد (م ×2) | | ✎ |

## 3. النص والاتجاه

| الإنجليزي | المقترح | المعنى | كلمات أخرى | المصدر | الحال |
|---|---|---|---|---|---|
| direction | الاتجاه | من اليمين إلى اليسار أو العكس | | و | ✔ |
| bidirectional text | النص ثنائي الاتجاه | نص يجمع العربية والإنجليزية | | و | ✔ |
| RLM / LRM | علامة اليمين / علامة اليسار | حرفان خفيان يحددان اتجاه ما حولهما | | | ○ |
| isolate (RLI … PDI) | العزل | حرفان خفيان يجعلان ما بينهما قطعة بلا أثر على ما حولها | | | ○ |
| no-break space | المسافة التي لا تنكسر | مسافة لا يقطع السطر عندها | الحيز غير المقطوع (و) | م | ؟ |
| diacritics | التشكيل | العلامات فوق الحروف وتحتها، ومنها الحركات | الحركات (و، للفتحة والضمة والكسرة وأخواتها) | و | ✔ |
| tatweel / kashida | التطويل / الكشيدة | التطويل: الحرف «ـ». الكشيدة: مد الحروف لضبط السطر. وهما شيء واحد في الأصل | | و | ✔ |
| Arabic-Indic digits | الأرقام الهندية | ٠١٢٣ | الأرقام العربية المشرقية (و) | م | ؟ |
| Western digits | الأرقام الغربية | 0123 | | م | ○ |
| punctuation | علامات الترقيم | ، ؛ ؟ | | و | ✔ |
| font | الخط | شكل الحروف، مثل Amiri | البنط، الطابع المحرفي (و) | م | ○ |
| Latin letters | الحروف اللاتينية | | | م | ○ |

## 4. الأماكن والأدوات

| الإنجليزي | المقترح | المعنى | كلمات أخرى | المصدر | الحال |
|---|---|---|---|---|---|
| phone app | تطبيق الهاتف | تطبيق GitHub على الهاتف | التطبيق المحمول (و) | م ×23 | ○ |
| website | الموقع | موقع github.com في المتصفح | | م | ○ |
| browser | المتصفح | | متصفح الويب (و) | و | ✔ |
| dark mode / light mode | الوضع الداكن / الوضع الفاتح | | | و | ✔ |
| checker / linter | أداة الفحص | أداة تجد الأخطاء في الملفات | لنت (و) | م | ○ |
| test | الاختبار | تجربة تثبت أن القاعدة تعمل | فحص البرمجيات (و) | م | ○ |
| upload / download | الرفع / التنزيل | | | و، ف، ر | ✔ |
| load (a picture) | التحميل | أن يجلب الموقع أو التطبيق الصورة ويعرضها | | م | ○ |
| file / folder | الملف / المجلد | | | و، ف | ✔ |
| table of contents | المحتويات | | جدول المحتويات (و) | و | ✔ |
| logo | الشعار | | | م | ○ |
| banner | اللافتة | صورة عريضة في أعلى الملف التمهيدي | الشعار (م، ويُخلط بشعار المشروع) | | ✎ |
| badge / card | الشارة / البطاقة | صورة صغيرة فيها اسم وقيمة / صورة فيها أرقام الحساب | | م | ○ |

## 5. الطراز التراثي

| الإنجليزي | المقترح | المعنى | كلمات أخرى | المصدر | الحال |
|---|---|---|---|---|---|
| Kufic / Naskh / Ruq'ah / Nastaliq | الخط الكوفي / خط النسخ / خط الرقعة / النستعليق | يُقال «خط النسخ» لا «النسخ» وحدها، حتى لا تُفهم بمعنى النُّسَخ | | و | ✔ |
| verse halves | الصدر والعجز | شطرا بيت الشعر | | ش | ✔ |
| abjad numbering | حروف أبجد | العد بالحروف: أ ب ج د | | ش | ✔ |
| NOTE / TIP (heritage names) | فائدة / لطيفة | | | ش | ✔ |
| IMPORTANT / WARNING / CAUTION (heritage names) | قاعدة / تنبيه / تحذير | «تنبيه» اسم تراثي لتنبيه WARNING، أما الميزة كلها فتُكتب «تنبيهات GitHub» فيُعرف المقصود من السياق | | ش (تنبيه) | ✔ |
| shamsa | الشمسة | زخرفة مستديرة كالشمس في أول المخطوط | | | ○ |
| cartouche | لوحة العنوان | إطار مزخرف فيه اسم الكتاب | العنوان (م، ويُخلط بعنوان الفقرة) | | ؟ |
| interlace | الضفيرة | شريطان متداخلان حول الصفحة | التشابك (و) | | ؟ |
| arabesque | الرقش | غصن ملتف بأوراقه | الزخرفة العربية (و) | | ؟ |
| arcade | القناطر | صف من العقود المدببة | | | ○ |

لم نتحقق بعد من دليل الأسلوب العربي من Microsoft، ولا من المعاجم الموحدة لمجامع اللغة العربية (لا نص لها على الشبكة). ولم نجد مصدرًا يذكر لماذا اختار كلمته. فإن كان لديك أحدها، فاذكر ما فيه في مشكلة.

</div>

---

# Glossary

[العربية](#مسرد-المصطلحات) · [Guide](en/guide.md) · [Contributing](../CONTRIBUTING.md)

Each English term in this guide gets one Arabic word. The table above lists them: the English term, the proposed
Arabic word, its meaning (in Arabic), other words we have seen, the sources, and a status. If you know a better word
or a stronger source, [open a "Term" issue](https://github.com/alequab/al-arabiya-arabic-on-github/issues/new?template=term.yml)
with the term, your word and where it comes from.

Status: ✔ agreed (at least one source, used throughout) · ○ in use, no source found yet · ✎ chosen over another word: the
other words in its row are not used · ؟ needs a choice: your opinion helps here.

Sources: و Arabic Wikipedia (the title of the article linked to the English one, 2026-11-28) · ف the
[Forgejo Arabic interface](https://codeberg.org/forgejo/forgejo/src/branch/forgejo/options/locale/locale_ar.ini) (a
GitHub-like forge) · د the [Arabic Debian wiki page on Git](https://wiki.debian.org/ar/git) · ش classical books in the
Shamela library · ح [Hsoub Academy's Git lessons](https://academy.hsoub.com/programming/workflow/git/) · ت
[Microsoft Terminology Search](https://learn.microsoft.com/globalization/reference/microsoft-terminology) (official,
covers GitHub) · ر the [WordPress Arabic glossary](https://translate.wordpress.org/locale/ar/default/glossary/) and
LibreOffice's Arabic translation · م this repo, with the number of uses when the glossary was written (×).

Not checked yet: Microsoft's Arabic style guide and the unified dictionaries of the Arabic language academies (no
text online). No source we found says why it chose its word. If you have one of them, say what it gives in an issue.
