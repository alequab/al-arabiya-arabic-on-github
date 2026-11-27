// Audit a rendered Markdown page on github.com for Arabic problems: as the website draws it, and as the GitHub
// Android app draws it.
//
// How to run: open the page on github.com (a file, an issue, a pull request, a discussion), open the browser
// console (F12), paste this whole file, then
//   auditArabic("web")     the page as github.com draws it
//   auditArabic("phone")   the page as the GitHub Android app draws it (changes the page; reload to undo)
// Run "web" first. Browser automation tools can paste it the same way.
//
// The phone mode copies what the app was seen doing (2026-11-27, tests T29-T35 of arabic-readme-lab, matched against
// real phone screenshots of T29-T34): no dir="auto" on paragraphs (only dir="rtl" set by you counts), no <picture>, no
// #gh-dark-mode-only / #gh-light-mode-only pictures, no math, no Mermaid.
//
// A block counts as Arabic when its own text (not inline code) has more Arabic than Latin letters. Findings:
// Arabic running left to right, Arabic lists with bullets on the left, code running right to left, pictures that
// failed or that the app won't show, math / Mermaid the app won't draw, alerts left as raw [!NOTE] text, and links to
// headings that don't exist. Phone mode only: centered or right-aligned lines mixing Arabic and Latin with no
// direction, and Arabic task lists.
function auditArabic(mode) {
  if (mode !== "web" && mode !== "phone") return { error: 'mode must be "web" or "phone"' };
  // Every rendered Markdown block: a file, or the bodies and comments of an issue, PR, release or discussion.
  const roots = [...document.querySelectorAll(".markdown-body")].filter((r) => !r.parentElement.closest(".markdown-body"));
  if (!roots.length) return { error: "no rendered Markdown on this page" };
  if (mode === "web" && document.body.dataset.auditPhone) return { error: "phone mode changed this page: reload, then run web" };
  const AR = /[ء-يٱ-ۓ]/g;
  const LA = /[A-Za-z]/g;
  const isArabic = (t) => (t.match(AR) || []).length > (t.match(LA) || []).length;
  const short = (t) => t.replace(/\s+/g, " ").trim().slice(0, 60);
  const ownText = (e) => {
    const c = e.cloneNode(true);
    c.querySelectorAll("code, ul, ol, p, div, table, [data-audit]").forEach((x) => x.remove());
    return c.textContent;
  };
  const hide = (el, what) => {
    const s = document.createElement("span");
    s.dataset.audit = what;
    s.textContent = "[" + what + " not shown] " + (el.alt || el.querySelector?.("img")?.alt || "");
    el.replaceWith(s);
  };
  const findings = [];
  let pending = 0;

  roots.forEach((art, k) => {
    if (mode === "phone") {
      document.body.dataset.auditPhone = "1";
      art.querySelectorAll('[dir="auto"]').forEach((e) => e.removeAttribute("dir"));
      art.querySelectorAll("picture").forEach((p) => hide(p, "picture"));
      art.querySelectorAll("img").forEach((i) => {
        const src = i.getAttribute("data-canonical-src") || i.getAttribute("src") || "";
        if (/#gh-(dark|light)-mode-only/.test(src)) hide(i, "picture");
      });
      art.querySelectorAll("math-renderer").forEach((m) => (m.dataset.audit = "math"));
      art.querySelectorAll('[data-type="mermaid"]').forEach((m) => (m.dataset.audit = "mermaid"));
    }

    const where = (e) => {
      if (e.matches("h1,h2,h3,h4,h5,h6")) return short(e.textContent);
      for (let h = e; h && h !== art; h = h.parentElement) {
        for (let p = h.previousElementSibling; p; p = p.previousElementSibling) {
          const hh = p.matches(".markdown-heading") ? p.querySelector("h1,h2,h3,h4,h5,h6") : null;
          if (hh) return short(hh.textContent);
        }
      }
      return "(top)";
    };
    const block = roots.length > 1 ? "block " + (k + 1) + ": " : "";   // which body or comment on the page
    const add = (problem, e, text) => findings.push({ problem, section: block + where(e), text: short(text || "") });

    art.querySelectorAll("p, li, h1, h2, h3, h4, h5, h6, td, th, summary").forEach((e) => {
      if (e.closest("pre, code, .markdown-alert-title")) return;
      const own = ownText(e);
      const s = getComputedStyle(e);
      if (own.trim() && isArabic(own) && s.direction === "ltr") add("Arabic runs left to right", e, own);
      else if (mode === "phone" && s.direction === "ltr" && /[ء-ي]/.test(own) && /[A-Za-z]/.test(own) &&
               /center|right/.test(s.textAlign))   // align="center" computes as -webkit-center
        add("centered line mixing Arabic and Latin, no direction in the phone app", e, own);
    });
    art.querySelectorAll("ul, ol").forEach((l) => {
      const items = [...l.children].filter((x) => x.matches("li"));
      if (items.length && items.every((x) => isArabic(x.textContent)) && getComputedStyle(l).direction === "ltr")
        add("Arabic list with its bullets on the left", l, items[0].textContent);
      if (mode === "phone" && items.some((x) => x.querySelector('input[type="checkbox"]') && isArabic(x.textContent)))
        add("task-list checkboxes cover Arabic words in the phone app", l, items[0].textContent);
    });
    art.querySelectorAll("pre").forEach((p) => {
      if (getComputedStyle(p).direction === "rtl") add("code block runs right to left", p, p.textContent);
    });
    art.querySelectorAll("img").forEach((i) => {
      if (!i.complete) pending++;
      else if (i.naturalWidth === 0) add("picture did not load", i, i.alt);
    });
    art.querySelectorAll("[data-audit]").forEach((s) => add(s.dataset.audit + " not shown in the phone app", s, s.textContent));
    art.querySelectorAll("p").forEach((p) => {
      if (/^\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/.test(p.textContent)) add("alert not drawn (raw [!...] text)", p, p.textContent);
    });
    art.querySelectorAll('a[href^="#"]').forEach((a) => {
      let id = a.getAttribute("href").slice(1);
      try {
        id = decodeURIComponent(id);
      } catch (e) {
        /* keep the raw id */
      }
      const found = (x) => document.getElementById(x) || document.getElementsByName(x).length;
      if (id && !found("user-content-" + id) && !found(id)) add("link to a missing heading", a, "#" + id);
    });
  });
  const result = { mode, page: location.pathname, count: findings.length, findings };
  if (pending) result.note = pending + " picture(s) still loading: wait and run again to check them";
  return result;
}
