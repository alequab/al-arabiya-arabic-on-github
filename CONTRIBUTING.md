<div dir="rtl">

# المساهمة

شكرًا لاهتمامك. هذا الدليل يقوم على الاختبار، فكل قاعدة فيه جُرّبت على موقع GitHub، ونتائج تطبيق الهاتف من لقطات حقيقية أو من أداة تحاكيه.

- **وجدت عرضًا خاطئًا؟** افتح بلاغًا بالنموذج «عرض خاطئ»، واذكر الصفحة والمكان (الموقع أو التطبيق)، وأرفق صورة إن استطعت.
- **عندك طريقة أفضل؟** اكتب الحالة اختبارًا جديدًا في آخر &lrm;`tests/lab.md`&lrm; برقم جديد (مثل T47)، فيه الطريقة المعتادة والحل، ثم اربط القاعدة به في الدليلين.
- **عندك كلمة عربية أصح لمصطلح؟** انظر [مسرد المصطلحات](docs/glossary.md)، ثم افتح بلاغًا بالنموذج «مصطلح» واذكر الكلمة ومصدرها.
- **غيّرت قاعدة؟** غيّرها في الدليل العربي والإنجليزي معًا، وفي &lrm;`AGENTS.md`&lrm;، حتى لا تختلف النسخ.
- **قبل الإرسال:** شغّل الفحص والاختبارات، ثم افتح صفحتك على GitHub وشغّل &lrm;`page_audit.js`&lrm; كما في القسم 10 من الدليل.
- **مثال خاطئ عمدًا؟** ضعه بين &lrm;`<!-- check-arabic: off -->`&lrm; و&lrm;`<!-- check-arabic: on -->`&lrm;، فلا تُبلّغ عنه أداة الفحص. أما &lrm;`page_audit.js`&lrm; فتُبلّغ عنه دائمًا، لأن GitHub يحذف التعليقات من الصفحة.

</div>

```powershell
python code/check_arabic_md.py README.md docs
python code/test_tools.py
```

<div dir="rtl">

اكتب «GitHub» بحروفه اللاتينية، واستعمل علامات الترقيم العربية (، ؛ ؟)، والعربية الفصحى.

بمساهمتك توافق على أن يكون عملك بترخيص [MIT](LICENSE).

</div>

---

# Contributing

Thank you for your interest. This guide is built on tests: every rule was checked on github.com, and phone-app results
come from real screenshots or from a tool that copies the app.

- **Found something that renders wrong?** Open an issue with the "Wrong rendering" form: the page, where you saw it
  (website or app), and a screenshot if you can.
- **Know a better way?** Add it as a new test at the end of `tests/lab.md` with the next number (T47, ...), showing the
  usual way and the fix, then link the rule to it in both guides.
- **Know a better Arabic word for a term?** See the [glossary](docs/glossary.md#glossary), then open an issue with
  the "Term" form: the word and its source.
- **Changed a rule?** Change it in the Arabic and English guides and in `AGENTS.md` together, so they never disagree.
- **Before you send:** run the checker and the tests, then open your page on GitHub and run `page_audit.js` as in
  section 10 of the guide.
- **A deliberate mistake?** Put it between `<!-- check-arabic: off -->` and `<!-- check-arabic: on -->` and the checker
  won't report it. `page_audit.js` still will, because GitHub removes comments from the page.

```powershell
python code/check_arabic_md.py README.md docs
python code/test_tools.py
```

In Arabic text write "GitHub" in Latin letters, and use Arabic punctuation (، ؛ ؟) and Modern Standard Arabic.

By contributing you agree that your work is licensed under the [MIT License](LICENSE).
