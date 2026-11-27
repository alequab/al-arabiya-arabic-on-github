"""Tests for the tools in code/ (the picture tools offline, without fonts):  python code/test_tools.py"""
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import arabic_cards  # noqa: E402
import arabic_text  # noqa: E402
import ornaments  # noqa: E402
import typing_svg  # noqa: E402
from check_arabic_md import check_text, first_strong  # noqa: E402


def rules(md: str, outside: bool = False):
    """Rule hits; the outside-rtl-div warning only when asked, so the other tests can stay short."""
    return [(n, rule) for _, n, _, rule, _ in check_text("t.md", md.split("\n"))
            if outside or rule != "outside-rtl-div"]


class FirstStrong(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(first_strong("هذا سطر"), "ar")
        self.assertEqual(first_strong("GitHub هو الموقع"), "latin")
        self.assertEqual(first_strong("2026 هو العام"), "ar")          # digits don't count
        self.assertEqual(first_strong("✔ تم الحفظ"), "ar")              # emoji don't count
        self.assertEqual(first_strong("`gh` هي الأداة"), "latin")      # code text counts
        self.assertEqual(first_strong("[GitHub](https://x) هو"), "latin")
        self.assertEqual(first_strong("[النظام](https://x.com) هو"), "ar")  # the URL doesn't count
        self.assertEqual(first_strong("$V=IR$ هي المعادلة"), "math")
        self.assertEqual(first_strong("- README في أول البند"), "latin")
        self.assertEqual(first_strong("## البدء السريع"), "ar")


class Checker(unittest.TestCase):
    def test_starts_ltr(self):
        self.assertIn((1, "starts-ltr"), rules("GitHub هو الموقع."))
        self.assertEqual(rules("&rlm;GitHub هو الموقع."), [])
        self.assertEqual(rules("2026 هو العام."), [])
        self.assertEqual(rules("English only line."), [])

    def test_math(self):
        self.assertIn((1, "rlm-math"), rules("&rlm;$V$ هي المعادلة."))
        self.assertNotIn((1, "starts-ltr"), rules("&rlm; $V$ هي المعادلة."))
        self.assertIn((1, "starts-ltr"), rules("$V$ هي المعادلة."))

    def test_div_and_blocks(self):
        md = '<div dir="rtl">\n\nنص\n\n```\ncode\n```\n\n> [!NOTE]\n> ملاحظة\n\n</div>'
        r = rules(md)
        self.assertIn((5, "code-in-rtl-div"), r)
        # A block with a language takes its direction from its first letter; the div does not matter.
        self.assertNotIn((3, "code-in-rtl-div"), rules('<div dir="rtl">\n\n```powershell\ngh repo view\n```\n\n</div>'))
        # ... but the phone app has no dir="auto", so the block takes the div's direction there.
        self.assertIn((3, "code-in-rtl-div-phone"), rules('<div dir="rtl">\n\n```powershell\ngh repo view\n```\n\n</div>'))
        self.assertIn((1, "code-starts-arabic"), rules("```markdown\nجملة\n```"))
        self.assertEqual(rules("```markdown\n<!-- note -->\nجملة\n```"), [])
        self.assertEqual(rules("```text\nجملة\n```"), [])
        self.assertIn((9, "alert-in-rtl-div"), r)
        self.assertIn((1, "div-blank-line"), rules('<div dir="rtl">\nنص\n</div>'))
        self.assertNotIn((9, "alert-in-rtl-div"), rules('<div dir="rtl">\n\nنص\n\n</div>\n\n\n\n> [!NOTE]\n> ملاحظة'))

    def test_outside_rtl_div(self):
        self.assertIn((1, "outside-rtl-div"), rules("نص عربي", outside=True))
        self.assertEqual(rules('<div dir="rtl">\n\nنص عربي\n\n</div>', outside=True), [])
        self.assertEqual(rules('<div align="center">\n\nنص عربي\n\n</div>', outside=True), [])
        self.assertEqual(rules('<p dir="rtl">نص عربي</p>', outside=True), [])
        self.assertEqual(rules("English with one word عربي here", outside=True), [])

    def test_phone_rules(self):
        self.assertIn((2, "alert-arabic-phone"), rules("> [!NOTE]\n> ملاحظة عربية"))
        self.assertEqual(rules('> [!NOTE]\n> <p dir="rtl">ملاحظة عربية</p>'), [])
        self.assertEqual(rules('> [!TIP]\n> <div dir="rtl">\n>\n> نصيحة عربية\n>\n> </div>'), [])
        self.assertIn((1, "phone-picture"), rules('<picture><img src="a.png" alt="x"></picture>'))
        self.assertIn((1, "phone-picture"), rules('<img src="a.png#gh-dark-mode-only" alt="x">'))
        self.assertEqual(rules("mention `<picture>` in code"), [])
        self.assertIn((1, "align-right"), rules('<p align="right">نص عربي</p>'))

    def test_code_edges(self):
        div = '<div dir="rtl">\n\n{}\n\n</div>'
        self.assertIn((3, "code-edge-rtl"), rules(div.format("ابدأ بالعلامة `&rlm;` هنا")))
        self.assertIn((3, "code-edge-rtl"), rules(div.format("ضع <code>&lt;div&gt;</code> هنا")))
        self.assertEqual(rules(div.format("ابدأ بالعلامة &lrm;`&rlm;`&lrm; هنا")), [])
        self.assertEqual(rules(div.format("شغّل `README.md` هنا")), [])      # letters at both ends
        self.assertEqual(rules("An English line with `&rlm;` and عربي"), [])  # not in a right-to-left part
        mixed = "اللون &lrm;`$x\\text{نص}$`&lrm; هنا"                       # Arabic and Latin inside the code
        self.assertIn((3, "code-edge-rtl"), rules(div.format(mixed)))
        self.assertNotIn((3, "code-edge-rtl"),
                         rules(div.format(mixed.replace("&lrm;`", "&#x2066;`").replace("`&lrm;", "`&#x2069;"))))

    def test_review_fixes(self):
        div = '<div dir="rtl">\n\n{}\n\n</div>'
        # &rlm; after an emoji or inside bold is a strong right-to-left letter
        self.assertEqual(rules(div.format("✔ &rlm;GitHub هو الموقع.")), [])
        # $ with no closing $ is not math
        self.assertNotIn((3, "starts-ltr"), rules(div.format("$20 هو السعر.")))
        # an inline tag at the start does not hide a Latin first letter
        self.assertIn((3, "starts-ltr"), rules(div.format("<b>GitHub</b> هو الموقع.")))
        # tag attributes are not counted as Latin letters
        self.assertIn((1, "outside-rtl-div"), rules('<p align="center">مرحبًا بكم</p>', outside=True))
        # align="right" on English or on a floated picture is fine
        self.assertEqual(rules('<p align="right">English text</p>\n\nMore'), [])
        self.assertEqual(rules('<img src="a.png" align="right" alt="x">\n\nنص'), [])
        # mixed Arabic/Latin code is reported even when both ends are letters
        self.assertIn((3, "code-edge-rtl"), rules(div.format("الوسم &lrm;`v1.2.0-إصدار`&lrm; هنا")))
        # <small> is removed by GitHub
        self.assertIn((1, "stripped-tag"), rules("<small>نص</small>"))
        # a multi-line <td dir="rtl"> and <table dir="rtl"> count as right to left
        self.assertEqual(rules('<table dir="rtl">\n<tr>\n<td>\n\nنص عربي\n\n</td>\n</tr>\n</table>', outside=True), [])
        # <div dir="ltr"> inside an RTL div is left to right
        self.assertNotIn((5, "code-edge-rtl"), rules('<div dir="rtl">\n\n<div dir="ltr">\n\nكلمة `&rlm;` هنا\n\n</div>\n\n</div>'))
        # fences under a list item and inside a quote are code
        self.assertEqual(rules("1. step\n\n    ```text\n    GitHub هو\n    ```"), [])
        self.assertEqual(rules("> ```text\n> GitHub هو\n> ```"), [])
        # the first letter is searched in the whole block, not only its first line
        self.assertIn((1, "code-starts-arabic"), rules('```json\n{\n  "الاسم": 1\n}\n```'))
        # italic is checked in list items too
        self.assertIn((1, "italic"), rules("- هذا *مائل* هنا"))
        # a table row is not a separator case
        self.assertNotIn((3, "latin-across-separator"), rules(div.format("| اسم GitHub | English |")))
        # HTML comments are not shown
        self.assertEqual(rules("<!--\nنص عربي في تعليق\n-->", outside=True), [])
        # a wrapped paragraph: the second line does not decide the direction
        self.assertNotIn((4, "starts-ltr"), rules(div.format("هذا سطر عربي طويل\nGitHub يكمله.")))
        # centered mixed line with no dir
        self.assertIn((3, "center-mixed-phone"), rules('<div align="center">\n\nالعربية على GitHub\n\n</div>'))
        # math in a mostly-English or display line is still noted
        self.assertIn((1, "math-phone"), rules("$$\\text{السرعة} = \\frac{d}{t}$$"))

    def test_review2_fixes(self):
        div = '<div dir="rtl">\n\n{}\n\n</div>'
        # text after a fence inside a quote is still checked
        self.assertIn((5, "starts-ltr"), rules('> ```text\n> x\n> ```\n\nGitHub هو الموقع.'))
        # a deeper fence inside a fenced block does not close it
        md = "```markdown\n1. step\n\n    ```text\n    x\n    ```\n```\n\nGitHub هو الموقع."
        self.assertIn((9, "starts-ltr"), rules(md))
        # a comment opener inside a code block does not hide the rest
        self.assertIn((5, "starts-ltr"), rules("```html\n<!-- x\n```\n\nGitHub هو الموقع."))
        # text after --> on the same line is checked
        self.assertIn((1, "outside-rtl-div"), rules("<!-- note --> نص عربي هنا", outside=True))
        # align="center" on the element itself
        self.assertIn((1, "center-mixed-phone"), rules('<h1 align="center">مشروعي على GitHub · My project</h1>'))
        # an unclosed <td dir="rtl"> ends with its </table>
        md = '<table>\n<tr>\n<td dir="rtl">\n\nنص\n\n</tr>\n</table>\n\nنص عربي بعده'
        self.assertIn((10, "outside-rtl-div"), rules(md, outside=True))
        # a multi-line <p dir="rtl"> and a one-line <td dir="rtl"> after another tag
        self.assertEqual(rules('<p dir="rtl">\nنص عربي\n</p>', outside=True), [])
        self.assertEqual(rules('<tr><td dir="rtl">نص عربي</td></tr>', outside=True), [])
        # every line of an alert is checked, not only the first
        md = '> [!NOTE]\n> <p dir="rtl">نص أول</p>\n> نص ثان بلا وسم'
        self.assertIn((3, "alert-arabic-phone"), rules(md))
        # a heading right under a text line still decides its own direction
        self.assertIn((4, "starts-ltr"), rules(div.format("نص عربي\n## GitHub عنوان القسم الطويل")))
        # emoji shortcodes and isolated text do not count
        self.assertEqual(rules(div.format(":rocket: ابدأ الآن")), [])
        self.assertEqual(rules(div.format("&#x2066;README.md&#x2069; هو الملف.")), [])
        # &rlm; before a price is not math
        self.assertNotIn((3, "rlm-math"), rules(div.format("&rlm;$20 هو السعر")))
        # math quoted in code is not math
        self.assertNotIn((3, "math-phone"), rules(div.format("اكتب &lrm;`$x$`&lrm; للمعادلة")))
        # a date and time are one group
        found = [m for _, _, _, r, m in check_text("t", div.format("الموعد 2026-11-27 10:30 هنا").split("\n"))
                 if r == "digit-groups-rtl"]
        self.assertIn("2026-11-27 10:30", found[0])

    def test_review3_fixes(self):
        # inline code made of three backticks at the start of a line is not a code fence
        self.assertIn((3, "starts-ltr"), rules("```x``` مثال عربي هنا\n\nGitHub هو الموقع."))
        # a closing tag also closes what was left open inside it (<p> needs no closing tag)
        md = '<div dir="rtl">\n\n<p align="center">\nنص\n\n</div>\n\nنص عربي بعده'
        self.assertIn((8, "outside-rtl-div"), rules(md, outside=True))
        # bold and italic together is still italic
        self.assertIn((1, "italic"), rules("هذا ***نص مهم*** هنا"))
        self.assertNotIn((1, "italic"), rules("هذا **نص مهم** هنا"))

    def test_digit_groups(self):
        div = '<div dir="rtl">\n\n{}\n\n</div>'
        self.assertIn((3, "digit-groups-rtl"), rules(div.format("اتصل على 050 123 4567 الآن.")))
        self.assertIn((3, "digit-groups-rtl"), rules(div.format("الدوام من 10:30 - 11:00 صباحًا.")))
        self.assertEqual(rules(div.format("اتصل على &#x2066;050 123 4567&#x2069; الآن.")), [])
        self.assertEqual(rules(div.format("الإصدار 1.2.0 في عام 2026.")), [])   # single numbers are fine
        self.assertEqual(rules(div.format("التاريخ 2026-11-27 والهاتف 050-123-4567.")), [])  # hyphens keep it whole
        found = [m for _, _, _, r, m in check_text("t", div.format("الرقم 050 123 4567 هنا").split("\n"))
                 if r == "digit-groups-rtl"]
        self.assertIn("050 123 4567", found[0])                                    # the whole number

    def test_latin_across_separator(self):
        self.assertIn((1, "latin-across-separator"), rules('<h4 dir="rtl">العربية على GitHub · Arabic on GitHub</h4>'))
        self.assertEqual(rules('<h4 dir="rtl">العربية على GitHub&rlm; · Arabic on GitHub</h4>'), [])

    def test_loose_list(self):
        self.assertIn((3, "loose-list"), rules("- بند\n\n- بند"))
        self.assertEqual(rules("- بند\n- بند"), [])

    def test_elements(self):
        self.assertIn((1, "quote"), rules("> اقتباس عربي"))
        self.assertIn((1, "task-list"), rules("- [ ] مهمة"))
        self.assertIn((1, "footnote"), rules("جملة.[^1]"))
        self.assertIn((1, "table-outside-rtl-div"), rules("| الاسم | الوصف |"))
        self.assertNotIn((3, "table-outside-rtl-div"), rules('<div dir="rtl">\n\n| الاسم | الوصف |\n\n</div>'))
        self.assertIn((1, "italic"), rules("هذا *نص مائل* هنا"))
        self.assertIn((1, "italic"), rules("هذا <i>مائل</i>"))
        self.assertNotIn((1, "italic"), rules("هذا **عريض** هنا"))
        self.assertIn((1, "stripped-tag"), rules("<u>نص</u>"))
        self.assertEqual(rules("```\nGitHub هو\n```"), [])        # code is skipped


class TextTool(unittest.TestCase):
    def test_about(self):
        text, notes = arabic_text.about("دليل العربية", "Arabic guide.")
        self.assertEqual(text, "\u2067دليل العربية\u200f \u00b7 Arabic\u00a0guide.\u200e\u2069")
        self.assertEqual(notes, [])
        text, _ = arabic_text.about("دليل", "A tested guide to writing Arabic on GitHub, with tools.")
        joined = arabic_text.NBSP.join("A tested guide to writing Arabic".split(" "))
        self.assertIn(joined + " on GitHub, with tools.", text)
        _, notes = arabic_text.about("دليل " * 10, "x")
        self.assertTrue(notes)
        with self.assertRaises(ValueError):
            arabic_text.about("سطر\nثان", "x")

    def test_commit(self):
        msg = "README: تحديث القسم العربي.\n\nEnglish line.\nسطر فيه GitHub في وسطه.\n"
        self.assertEqual(arabic_text.commit(msg),
                         "\u2067README: تحديث القسم العربي.\u2069\n\nEnglish line.\n\u2067سطر فيه GitHub في وسطه.\u2069\n")
        self.assertEqual(arabic_text.commit("إضافة الاختبار على GitHub · Add test\n"),
                         "\u2067إضافة الاختبار على GitHub\u200f · Add test\u200e\u2069\n")

    def test_text_review_fixes(self):
        self.assertEqual(arabic_text.title("Fix README."), "Fix README.")            # English titles left alone
        self.assertEqual(arabic_text.title("الإصدار 1.2.0 · Release 1.2.0"),
                         "\u2067الإصدار 1.2.0\u200f · Release 1.2.0\u200e\u2069")
        msg = "تحديث الدليل.\n\n  سطر مزاح فيه GitHub.\n\nSigned-off-by: عبد الله <a@b.c>\n"
        out = arabic_text.commit(msg).split("\n")
        self.assertTrue(out[2].startswith("  \u2067"))                                # indentation kept
        self.assertEqual(out[4], "Signed-off-by: عبد الله <a@b.c>")                  # trailer untouched
        with self.assertRaises(ValueError):
            arabic_text.about("", "English")
        with self.assertRaises(ValueError):
            arabic_text.about("سطر\u2028ثان", "x")
        _, notes = arabic_text.about("دليل", "x " * 200)
        self.assertTrue(any("350" in n for n in notes))
        text, _ = arabic_text.about("دليل", "Two  spaces here")
        self.assertNotIn(arabic_text.NBSP + arabic_text.NBSP, text)

    def test_text_review2_fixes(self):
        self.assertTrue(arabic_text.title("Follow-up: الجدول لا يظهر").startswith("\u2067"))
        self.assertTrue(arabic_text.commit("Re-do: إعادة الجدول.\n").startswith("\u2067"))      # subject, not a trailer
        msg = "عنوان.\n\nنص.\nSigned-off-by: عبد الله <a@b.c>\n"
        self.assertIn("\nSigned-off-by: عبد الله <a@b.c>\n", arabic_text.commit(msg))
        import os, tempfile, contextlib, io
        base = pathlib.Path(__file__).parent.parent / ".tmp"                      # scratch stays in the project
        base.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=base) as d:
            src, out = os.path.join(d, "m.txt"), os.path.join(d, "o.txt")
            with open(src, "w", encoding="utf-8-sig") as f:                    # a BOM, as PowerShell 5.1 writes
                f.write("عنوان الالتزام.\n")
            self.assertEqual(arabic_text.main(["commit", src, "--out", out]), 0)
            with open(out, encoding="utf-8") as f:
                self.assertEqual(f.read(), "\u2067عنوان الالتزام.\u2069\n")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(arabic_text.main(["commit", os.path.join(d, "missing.txt")]), 2)
        _, notes = arabic_text.about("guide", "دليل")
        self.assertEqual(len(notes), 2)                                              # both parts swapped

    def test_text_review3_fixes(self):
        # blank lines at the end of the message do not hide the trailers
        msg = "عنوان.\n\nنص.\n\nSigned-off-by: عبد الله <a@b.c>\n\n"
        self.assertEqual(arabic_text.commit(msg).split("\n")[4], "Signed-off-by: عبد الله <a@b.c>")
        # an Arabic part with its own separator: the whole title is wrapped, the separator stays in the Arabic part
        self.assertEqual(arabic_text.title("الإصدار 1.2 · إصلاحات · Release 1.2 · Fixes"),
                         "\u2067الإصدار 1.2 · إصلاحات\u200f · Release 1.2 · Fixes\u200e\u2069")

    def test_title_no_double_marks(self):
        t = arabic_text.title("\u2067README: الجدول\u2069")
        self.assertEqual(t, "\u2067README: الجدول\u2069")


class LatinSlash(unittest.TestCase):
    def test_slash_without_spaces_is_one_run(self):
        self.assertEqual([r for _, r in rules("نمط IEC/ISO في الرسم.")], [])
        self.assertEqual([r for _, r in rules("مشاهد Factory I/O هنا.")], [])
        self.assertIn("latin-across-separator", [r for _, r in rules('<h4 dir="rtl">دليل GitHub / Guide</h4>')])


class Muted(unittest.TestCase):
    def test_off_on(self):
        md = "\n".join(["GitHub هو الموقع.", "<!-- check-arabic: off -->", "GitHub هو الموقع.",
                         "<!-- check-arabic: on -->", "GitHub هو الموقع."])
        self.assertEqual([n for n, r in rules(md) if r == "starts-ltr"], [1, 5])

    def test_structure_still_read(self):
        # a div opened inside the muted part still counts after it
        md = "\n".join(["<!-- check-arabic: off -->", '<div dir="rtl">', "", "<!-- check-arabic: on -->",
                         "سطر عربي.", "", "</div>"])
        self.assertEqual(rules(md, outside=True), [])


class Pictures(unittest.TestCase):
    def num(self, svg, pattern):
        return [float(x) for x in re.findall(pattern, svg)]

    def test_typing_from_the_right(self):
        svg = typing_svg.build(["مرحبًا بك", "سطر <ثانٍ>"], width=600)
        self.assertIn("direction='rtl'", svg)
        self.assertIn("&lt;ثانٍ&gt;", svg)                                  # text is escaped
        first_x = self.num(svg, r"attributeName='x' values='([0-9.]+);")
        self.assertTrue(all(x > 300 for x in first_x))                      # the uncovering starts on the right
        once = typing_svg.build(["سطر", "آخر"], once=True)
        self.assertIn("fill='freeze'", once)
        self.assertEqual(once.count("<text"), 1)                            # --once keeps only the first line
        with self.assertRaises(ValueError):
            typing_svg.build(["سطر", " "])

    def test_still(self):
        svg = typing_svg.build(["سطر أول", "سطر ثان"], width=500, height=60, still=True)
        self.assertNotIn("<animate", svg)
        self.assertIn("height='120'", svg)                                  # two lines, one under the other
        self.assertEqual(svg.count("<text"), 2)

    def test_controls_not_counted(self):
        self.assertEqual(typing_svg.CONTROLS.sub("", "\u2067نص\u2069"), "نص")

    def test_badge_label_on_the_right(self):
        svg = arabic_cards.badge("الترخيص", "MIT")
        xs = self.num(svg, r"<text x='([0-9.]+)'")
        self.assertGreater(xs[0], xs[1])                                    # label right of the value

    def test_quote_and_stats(self):
        q = arabic_cards.quote("من جدّ وجد", "مثل عربي")
        self.assertIn("«من جدّ وجد»", q)
        self.assertIn("— مثل عربي", q)
        s = arabic_cards.stats({"stars": 84000, "commits": 38}, "إحصاءات")
        self.assertIn(">84k<", s)
        self.assertIn("مجموع النجوم", s)
        self.assertNotIn("البلاغات", s)                                     # only the numbers given
        self.assertEqual(arabic_cards.fmt_num(1234), "1.2k")
        self.assertEqual(arabic_cards.fmt_num(999), "999")

    def test_ornaments(self):
        for svg in (ornaments.shamsa("#C9A24D", "#2B6A8F"), ornaments.interlace("#C9A24D", "#2B6A8F"),
                    ornaments.arabesque("#C9A24D", "#2B6A8F"), ornaments.arcade("#C9A24D", "#2B6A8F")):
            self.assertTrue(svg.startswith("<svg xmlns='http://www.w3.org/2000/svg' viewBox="))
            self.assertIn("<title>", svg)
        self.assertIn("scale(-1 1)", ornaments.arabesque("#C9A24D", "#2B6A8F"))   # mirrored halves


if __name__ == "__main__":
    unittest.main(verbosity=1)
