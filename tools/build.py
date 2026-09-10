#!/usr/bin/env python3
"""Build the CBofN book site into site/ from data/ (stdlib only).

Inputs (produced by tools/convert.py and by hand):
  data/demos.json      per-demo manifests (hand written)
  data/toc.json        parts -> chapters -> sections, with pdf page starts
  data/figures.json    figures with numbers, captions, files
  data/glossary.json   glossary entries
  data/programs.json   per-program documentation (from the man pages)
  data/quotes.json, data/reviews.json
  data/pages/*.md      migrated prose pages
Outputs: site/*.html plus site/programs/*.html
"""
import json, os, re, html, sys, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
OUT = os.path.join(ROOT, "site")

def load(name, default=None):
    p = os.path.join(DATA, name)
    if not os.path.exists(p):
        return default
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def read_md(name):
    p = os.path.join(DATA, "pages", name + ".md")
    if not os.path.exists(p):
        return None
    with open(p, encoding="utf-8") as f:
        t = f.read()
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)          # front matter
    return fixlinks(t)

PROGRAM_IDS = set()
def fixlinks(t):
    """Rewrite links from the converted legacy pages to the new site."""
    def page_link(m):
        name = m.group(1)
        if name in PROGRAM_IDS: return "](programs/%s.html%s)" % (name, m.group(2) or "")
        return "](%s.html%s)" % (PAGE_ALIAS.get(name, name), m.group(2) or "")
    t = re.sub(r"\]\(pages/([\w-]+)\.md(#[^)]*)?\)", page_link, t)
    t = re.sub(r"\]\(([\w-]+)\.html(#[^)]*)?\)", page_link, t)
    t = re.sub(r"\]\(legacy/cbn-[^)]+\)", "](https://github.com/gwf/CBofN)", t)   # the old tarballs: now GitHub
    t = t.replace("](legacy/", "](../legacy/").replace("](figures/", "](../figures/")
    t = re.sub(r"\((legacy|figures)/", r"(../\1/", t)
    return t

PAGE_ALIAS = {"java": "programs", "javasmall": "programs", "javamed": "programs", "javalarge": "programs", "download": "programs", "source": "programs", "ordering": "about", "cover": "about", "news": "news", "excerpts0": "excerpts", "excerpts1": "excerpts", "excerpts2": "excerpts", "excerpts3": "excerpts", "excerpts4": "excerpts",
              "theme1": "themes", "theme2": "themes", "theme3": "themes", "oldnews": "news", "glossary-intro": "glossary", "fig": "figures", "toc": "index", "home": "index", "back": "index"}

# ---------------------------------------------------------------- markdown
def md(text):
    """A small Markdown-to-HTML converter: headings, paragraphs, lists,
    emphasis, links, images, code, blockquotes, horizontal rules."""
    if text is None:
        return ""
    out, para, lst = [], [], None
    def flush_para():
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>")
            para.clear()
    def close_list():
        nonlocal lst
        if lst:
            out.append("</%s>" % lst)
            lst = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para(); close_list(); continue
        m = re.match(r"^(#{1,6})\s+(.*)", line)
        if m:
            flush_para(); close_list()
            n = min(len(m.group(1)) + 1, 6)
            out.append("<h%d>%s</h%d>" % (n, inline(m.group(2)), n)); continue
        if re.match(r"^\s*([-*+]|\d+\.)\s+", line):
            flush_para()
            kind = "ol" if re.match(r"^\s*\d+\.", line) else "ul"
            if lst != kind:
                close_list(); out.append("<%s>" % kind); lst = kind
            out.append("<li>" + inline(re.sub(r"^\s*([-*+]|\d+\.)\s+", "", line)) + "</li>"); continue
        if line.startswith(">"):
            flush_para(); close_list()
            out.append("<blockquote>" + inline(line.lstrip("> ")) + "</blockquote>"); continue
        if re.match(r"^\s*(---|\*\*\*)\s*$", line):
            flush_para(); close_list(); out.append("<hr>"); continue
        if line.startswith("    ") or line.startswith("\t"):
            flush_para(); close_list()
            out.append("<pre>" + html.escape(line.strip()) + "</pre>"); continue
        para.append(line.strip())
    flush_para(); close_list()
    return "\n".join(out)

def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img alt="\1" src="\2">', s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*]+)\*(?!\w)", r"<em>\1</em>", s)
    s = re.sub(r"(?<![\w_])_([^_]+)_(?!\w)", r"<em>\1</em>", s)
    return s

# ---------------------------------------------------------------- layout
CSS = """
* { box-sizing: border-box; }
html { color-scheme: dark; }
body { margin: 0; background: #0b0c0f; color: #cfd2d8; font: 16px/1.6 -apple-system, "Helvetica Neue", Helvetica, Arial, sans-serif; }
a { color: #9cc4ff; text-decoration: none; } a:hover { text-decoration: underline; }
header.top { border-bottom: 1px solid #1d1f25; padding: 14px 28px; display: flex; gap: 22px; align-items: baseline; flex-wrap: wrap; }
header.top .brand { font: 400 18px Georgia, "Times New Roman", serif; color: #f2f2f2; }
header.top nav a { color: #9aa0ab; margin-right: 16px; font-size: 14px; }
header.top nav a.cur { color: #fff; }
main { max-width: 980px; margin: 0 auto; padding: 36px 28px 80px; }
h1 { font: 400 34px/1.15 Georgia, "Times New Roman", serif; color: #f4f4f4; margin: 0 0 8px; }
h2 { font: 400 24px/1.2 Georgia, "Times New Roman", serif; color: #eee; margin: 38px 0 12px; }
h3 { font: 500 17px/1.3 -apple-system, Helvetica, Arial, sans-serif; color: #e6e6e6; margin: 26px 0 8px; }
.kicker { font-size: 12px; letter-spacing: 0.12em; text-transform: uppercase; color: #8a8f99; }
.lede { color: #aab; font-size: 17px; margin-bottom: 26px; }
p { margin: 0 0 14px; }
blockquote { border-left: 2px solid #333; margin: 14px 0; padding: 2px 16px; color: #b9bcc4; font-style: italic; }
pre, code { font: 13.5px Menlo, Consolas, monospace; } pre { background: #14161b; padding: 12px 14px; border-radius: 4px; overflow-x: auto; }
code { color: #dde; }
.grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 16px; }
.card { background: #101218; border: 1px solid #1d1f25; border-radius: 6px; overflow: hidden; }
.card img { display: block; width: 100%; aspect-ratio: 16/9; object-fit: cover; background: #000; }
.card .b { padding: 10px 12px 12px; } .card b { color: #eee; font-weight: 500; display: block; } .card small { color: #8a8f99; }
.card:hover { border-color: #444; }
.parts { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 22px; }
.part { border-top: 1px solid #23262d; padding-top: 12px; }
.part h2 { margin: 4px 0 8px; font-size: 21px; }
.part ol { margin: 0; padding-left: 22px; color: #aab; } .part li { margin: 3px 0; } .part li a { color: #cfd2d8; }
.part .demo { color: #9cc4ff; font-size: 13px; margin-left: 6px; }
ul.plain { list-style: none; columns: 2; column-gap: 30px; padding-left: 22px; color: #aab; margin: 0 0 8px; } ul.plain li { margin: 2px 0; } @media (max-width: 700px) { ul.plain { columns: 1; } }
.figs { display: grid; grid-template-columns: repeat(auto-fill, minmax(170px, 1fr)); gap: 14px; }
.figs a { display: block; background: #fff; border-radius: 4px; padding: 6px; }
.figs img { width: 100%; height: 120px; object-fit: contain; display: block; }
.figs span { display: block; font-size: 12px; color: #444; margin-top: 4px; }
dl.gloss dt { color: #eee; font-weight: 500; margin-top: 14px; } dl.gloss dd { margin: 2px 0 0; color: #b5b9c2; }
input.search { width: 100%; font: 16px inherit; padding: 10px 12px; background: #14161b; border: 1px solid #2a2d35; color: #eee; border-radius: 6px; margin: 14px 0 22px; }
.chapnav { display: flex; justify-content: space-between; margin: 40px 0 0; color: #9aa0ab; font-size: 14px; }
.opts td { vertical-align: top; padding: 4px 10px 4px 0; font-size: 14px; } .opts code { white-space: nowrap; }
.muted { color: #8a8f99; font-size: 14px; }
.hero { display: flex; gap: 28px; align-items: flex-start; flex-wrap: wrap; }
.hero .cover { width: 220px; border-radius: 4px; box-shadow: 0 6px 30px rgba(0,0,0,0.6); }
.two { columns: 2; column-gap: 34px; } @media (max-width: 700px) { .two { columns: 1; } }
footer { color: #6d727b; font-size: 13px; border-top: 1px solid #1d1f25; margin-top: 60px; padding: 18px 28px; }
.demo-embed { width: 100%; aspect-ratio: 16/9; border: 0; border-radius: 6px; background: #000; display: block; }
"""

NAV = [("index.html", "Programs"), ("figures.html", "Figures"), ("glossary.html", "Glossary"),
       ("quotes.html", "Quotations"), ("about.html", "About the book"), ("../index.html", "flake.org")]

def page(title, body, cur="", depth=0, kicker=None):
    pre = "../" * (depth - 1)
    nav = "".join('<a href="%s%s" class="%s">%s</a>' % (pre, h, "cur" if h == cur else "", t) for h, t in NAV)
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8">
<title>{html.escape(title)} - The Computational Beauty of Nature</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>{CSS}</style></head><body>
<header class="top"><span class="brand">The Computational Beauty of Nature</span><nav>{nav}</nav></header>
<main>{body}</main>
<script src="{pre}../excerpt.js"></script>
<footer>Gary William Flake, <em>The Computational Beauty of Nature: Computer Explorations of Fractals, Chaos, Complex Systems, and Adaptation</em>, MIT Press, 1998. Figures may be used freely for noncommercial purposes. Source code is GPL. Site text from the original companion site (1998-2002), rebuilt 2026.</footer>
</body></html>"""

def write(name, content):
    p = os.path.join(OUT, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

# ---------------------------------------------------------------- data
demos = (load("demos.json") or {}).get("demos", [])
toc = load("toc.json") or {"parts": []}
figures = load("figures.json") or []
if isinstance(figures, dict): figures = figures.get("figures", [])
glossary = load("glossary.json") or []
if isinstance(glossary, dict): glossary = glossary.get("entries", [])
programs = load("programs.json") or []
if isinstance(programs, dict): programs = programs.get("programs", [])
quotes = load("quotes.json") or []
if isinstance(quotes, dict): quotes = quotes.get("quotes", [])
_rv = load("reviews.json") or {}
reviews = _rv.get("reviews", []) if isinstance(_rv, dict) else _rv
awards = _rv.get("awards", []) + _rv.get("distinctions", []) if isinstance(_rv, dict) else []

demos_by_ch = {}
for d in demos:
    if d.get("rotate") is False or d["id"].endswith("-classic"):
        continue
    demos_by_ch.setdefault(int(d["chapter"]), []).append(d)
progs_by_id = {p.get("id") or p.get("name"): p for p in programs}
PROGRAM_IDS.update(progs_by_id.keys())

def fig_chapter(f):
    n = str(f.get("number") or "")
    return int(n.split(".")[0]) if n.split(".")[0].isdigit() else None

def chapters():
    """Flat list of chapters with part info."""
    out = []
    for part in toc.get("parts", []):
        for ch in part.get("chapters", []):
            out.append((part, ch))
    return out

def chapter_slug(ch):
    n = ch.get("number")
    return "chapter-%s" % n if n else re.sub(r"[^a-z0-9]+", "-", ch["title"].lower()).strip("-")

# ---------------------------------------------------------------- pages
def build_home():
    demo_cards = "".join(
        '<a class="card" href="../index.html#%s"><img src="../demos/thumbs/%s.png" alt=""><div class="b"><b>%s</b><small>Chapter %s &middot; %s</small></div></a>'
        % (d["id"], d["id"], html.escape(d["title"]), d["chapter"], html.escape(d.get("chapterTitle", "")))
        for d in demos if d.get("rotate") is not False and not d["id"].endswith("-classic"))
    body = f"""
<div class="hero"><img class="cover" src="../legacy/graphics/cover.gif" alt="" onerror="this.style.display='none'">
<div><div class="kicker">Gary William Flake &middot; MIT Press, 1998</div>
<h1>The Computational Beauty of Nature</h1>
<p class="lede">Computer Explorations of Fractals, Chaos, Complex Systems, and Adaptation.</p>
<p><a href="about.html">About the book</a> &middot; <a href="programs.html">The programs</a> &middot; <a href="figures.html">All {len(figures)} figures</a> &middot; <a href="glossary.html">Glossary</a> &middot; <a href="https://github.com/gwf/CBofN">Source on GitHub</a> &middot; <a href="https://mitpress.mit.edu/9780262561273/the-computational-beauty-of-nature/">MIT Press</a></p>
</div></div>
<h2>Live programs</h2>
<p class="muted">Every program from the book that draws something, rewritten to run in the browser. Each one is a single file; the algorithm is the one in the book. Click through for the chapter it comes from.</p>
<div class="grid">{demo_cards}</div>
"""
    write("index.html", page("Home", body, "index.html", 1))

def build_about():
    back = read_md("back") or ""
    author = read_md("author") or ""
    toc_html = ""
    for part in toc.get("parts", []):
        items = ""
        for ch in part.get("chapters", []):
            n = ch.get("number")
            ds = demos_by_ch.get(int(n) if n else -1, [])
            label = ("%s. " % n if n else "") + html.escape(ch["title"])
            if ds: label = '<a href="%s.html">%s</a>' % (chapter_slug(ch), label)
            items += "<li>%s</li>" % label
        toc_html += "<h3>%s%s</h3><ul class=\"plain\">%s</ul>" % (("Part %s: " % part["number"]) if part.get("number") else "", html.escape(part.get("title", "")), items)
    body = f"""<h1>About the book</h1>
<div class="two">{md(back)}</div>
<h2>Contents</h2><p class="muted">Chapters with a live program are linked.</p>{toc_html}
<h2>The author</h2>{md(author)}
<p><a href="reviews.html">Reviews and awards</a> &middot; <a href="themes.html">Three themes</a> &middot; <a href="parts.html">Part synopses</a> &middot; <a href="excerpts.html">Selected excerpts</a> &middot; <a href="errata.html">Errata</a> &middot; <a href="edu.html">For educators</a> &middot; <a href="bibliography.html">Bibliography</a> &middot; <a href="legacy-site.html">The 1998 site</a></p>"""
    write("about.html", page("About the book", body, "about.html", 1))

def build_chapters():
    chs = [(p, c) for p, c in chapters() if demos_by_ch.get(int(c["number"]) if c.get("number") else -1)]
    for i, (part, ch) in enumerate(chs):
        n = ch.get("number")
        secs = "".join("<li>%s</li>" % html.escape(s if isinstance(s, str) else s.get("title", "")) for s in ch.get("sections", []))
        ds = demos_by_ch.get(int(n) if n else -1, [])
        demo_html = ""
        for d in ds:
            demo_html += f"""<h3>{html.escape(d['title'])} <span class="muted">({html.escape(d.get('program',''))})</span></h3>
<iframe class="demo-embed" loading="lazy" src="../demos/{d['id']}.html" title="{html.escape(d['title'])}"></iframe>
<p>{html.escape(d.get('blurb',''))} <a href="../index.html#{d['id']}">Full screen &rarr;</a></p>"""
        figs = [f for f in figures if fig_chapter(f) == (int(n) if n else None)]
        fig_html = "".join('<a href="../figures/svg/%s.svg" title="%s"><img loading="lazy" src="../figures/thumb/%s.png" alt=""><span>Figure %s</span></a>' % (f["index"], html.escape(f.get("caption", "")), f["index"], f.get("number")) for f in figs)
        prev = '<a href="%s.html">&larr; %s</a>' % (chapter_slug(chs[i-1][1]), html.escape(chs[i-1][1]["title"])) if i > 0 else "<span></span>"
        nxt = '<a href="%s.html">%s &rarr;</a>' % (chapter_slug(chs[i+1][1]), html.escape(chs[i+1][1]["title"])) if i + 1 < len(chs) else "<span></span>"
        pdf = ch.get("pdf") or ch.get("pdf_page")
        read = f'<a href="#" onclick="CBNExcerpt.open(\'ch{n}\', \'../\'); return false;">Read the opening pages</a> &middot; printed page {pdf-20}' if pdf else ""
        body = f"""<div class="kicker">{html.escape(('Part %s: ' % part.get('number')) if part.get('number') else '')}{html.escape(part.get('title',''))}</div>
<h1>{('%s. ' % n) if n else ''}{html.escape(ch['title'])}</h1>
<p class="lede">{read}</p>
{demo_html}
<h2>Sections</h2><ol>{secs}</ol>
{('<h2>Figures</h2><div class="figs">' + fig_html + '</div>') if figs else ''}
<div class="chapnav">{prev}{nxt}</div>"""
        write(chapter_slug(ch) + ".html", page(ch["title"], body, "about.html", 1))

def build_programs():
    demo_by_prog = {}
    for d in demos:
        demo_by_prog.setdefault(d.get("program", "").split(".")[0].split(" ")[0], d)
    rows = ""
    for p in programs:
        pid = p.get("id") or p.get("name")
        d = demo_by_prog.get(pid)
        live = ' &middot; <a href="../index.html#%s">run it live</a>' % d["id"] if d else ""
        rows += '<p><a href="programs/%s.html"><code>%s</code></a> &mdash; %s%s</p>' % (pid, pid, html.escape(p.get("summary") or p.get("synopsis", "")), live)
        opts = ""
        if p.get("options"):
            opts = "<h2>Options</h2><table class=\"opts\">" + "".join(
                "<tr><td><code>%s</code></td><td>%s</td><td class=\"muted\">%s</td></tr>" % (html.escape(o.get("flag", "")), html.escape(o.get("help", "")), html.escape(str(o.get("default", ""))))
                for o in p["options"]) + "</table>"
        ex = ""
        if p.get("examples"):
            ex = "<h2>Examples</h2>" + "".join("<pre>%s</pre>" % html.escape(e if isinstance(e, str) else e.get("command", "")) for e in p["examples"])
        embed = f'<iframe class="demo-embed" loading="lazy" src="../../demos/{d["id"]}.html"></iframe><p><a href="../../index.html#{d["id"]}">Full screen &rarr;</a></p>' if d else ""
        body = f"""<div class="kicker">Source code</div><h1><code>{pid}</code></h1>
<p class="lede">{html.escape(p.get('summary') or p.get('synopsis',''))}</p>{embed}
{('<pre>' + html.escape(p['synopsis']) + '</pre>') if p.get('synopsis') else ''}
{md(p.get('blurb_md',''))}{md(p.get('description_md',''))}{opts}{ex}
<p class="muted"><a href="https://github.com/gwf/CBofN/blob/master/src/{pid}.c">{pid}.c on GitHub</a></p>"""
        write("programs/%s.html" % pid, page(pid, body, "programs.html", 2))
    src = read_md("source") or ""
    dl = read_md("download") or ""
    java = read_md("java") or ""
    body = f"""<h1>Programs</h1>
<p class="lede">Every example in the book is a small C program with a command-line interface and a plotting driver. The code is on <a href="https://github.com/gwf/CBofN">GitHub</a>; the programs that draw something also run in the browser here.</p>
{rows}
<h2>Overview</h2>{md(src)}
<h2>Downloads (historical)</h2>{md(dl)}
<h2>Java ports (historical)</h2><p class="muted">Mike Miller's Java applets from 1998 no longer run in any browser; the JavaScript versions above replace them.</p>{md(java)}"""
    write("programs.html", page("Programs", body, "programs.html", 1))

def build_figures():
    cur = None; body = "<h1>All figures</h1><p class=\"lede\">Every figure from the book, free for noncommercial use, as SVG (from the original PostScript).</p>"
    for f in figures:
        c = fig_chapter(f)
        if c != cur:
            if cur is not None: body += "</div>"
            cur = c
            title = ""
            for part, ch in chapters():
                if str(ch.get("number")) == str(c): title = ch["title"]
            body += '<h2>Chapter %s%s</h2><div class="figs">' % (c, (": " + html.escape(title)) if title else "")
        body += '<a href="../figures/svg/%s.svg" title="%s"><img loading="lazy" src="../figures/thumb/%s.png" alt=""><span>Figure %s</span></a>' % (f["index"], html.escape(f.get("caption", "")), f["index"], f.get("number"))
    if figures: body += "</div>"
    write("figures.html", page("Figures", body, "figures.html", 1))

def build_glossary():
    items = "".join('<dt id="%s">%s</dt><dd>%s</dd>' % (re.sub(r"[^a-z0-9]+", "-", g["term"].lower()), html.escape(g["term"]), md(g.get("definition_md") or g.get("definition", "")).replace("<p>", "").replace("</p>", " ")) for g in glossary)
    body = f"""<h1>Glossary</h1><p class="lede">{len(glossary)} terms, from the book.</p>
<input class="search" id="q" placeholder="filter terms and definitions" autofocus>
<dl class="gloss" id="g">{items}</dl>
<script>
var q=document.getElementById('q'),dts=[].slice.call(document.querySelectorAll('#g dt'));
q.oninput=function(){{var s=q.value.toLowerCase();dts.forEach(function(dt){{var dd=dt.nextElementSibling,hit=!s||(dt.textContent+' '+dd.textContent).toLowerCase().indexOf(s)>=0;dt.style.display=dd.style.display=hit?'':'none';}});}};
if(location.hash){{var e=document.getElementById(location.hash.slice(1));if(e)e.scrollIntoView();}}
</script>"""
    write("glossary.html", page("Glossary", body, "glossary.html", 1))

def build_quotes():
    if quotes:
        items = "".join('<blockquote>%s<br><span class="muted">&mdash; %s%s</span></blockquote>' % (html.escape(q.get("text") or q.get("quotation", "")), html.escape(q.get("attribution", "")), (" (%s)" % html.escape(str(q.get("part") or ("chapter %s" % q["chapter"])))) if q.get("chapter") is not None else "") for q in quotes)
    else:
        items = md(read_md("quotes"))
    write("quotes.html", page("Quotations", "<h1>Quotations</h1><p class=\"lede\">The epigraphs that open each chapter.</p>" + items, "quotes.html", 1))

def build_reviews():
    if reviews:
        items = "".join('<h2>%s</h2><p class="muted">%s%s</p>%s' % (html.escape(r.get("publication") or r.get("source", "")), html.escape(r.get("reviewer") or r.get("author", "")), (" &middot; " + html.escape(str(r["date"]))) if r.get("date") else "", md(r.get("excerpt_md") or r.get("excerpt") or r.get("text_md") or r.get("text", ""))) for r in reviews)
        if awards:
            items = "<h2>Awards and distinctions</h2><ul>" + "".join("<li>%s</li>" % inline(fixlinks(a if isinstance(a, str) else (a.get("text_md") or a.get("text") or a.get("title") or json.dumps(a)))) for a in awards) + "</ul>" + items
    else:
        items = md(read_md("reviews"))
    write("reviews.html", page("Reviews", "<h1>Reviews and awards</h1>" + items, "reviews.html", 1))

def build_plain(name, title, files, lede=""):
    parts = []
    for f in files:
        t = read_md(f)
        if t: parts.append(md(t))
    if not parts: return
    write(name + ".html", page(title, "<h1>%s</h1>%s%s" % (html.escape(title), ('<p class="lede">%s</p>' % lede) if lede else "", "".join(parts)), "index.html", 1))

def build_legacy_index():
    body = """<h1>The 1998 site</h1><p class="lede">The original companion site, as Gary built it between 1998 and 2002, preserved as it was.</p>
<p><a href="../legacy/home.html">Open the legacy site</a></p>"""
    write("legacy-site.html", page("The 1998 site", body, "index.html", 1))

def main():
    if os.path.isdir(OUT): shutil.rmtree(OUT)
    os.makedirs(OUT)
    build_home(); build_about(); build_chapters(); build_programs(); build_figures(); build_glossary()
    build_quotes(); build_reviews(); build_legacy_index()
    build_plain("themes", "Three themes", ["themes", "theme1", "theme2", "theme3"])
    build_plain("parts", "Part synopses", ["parts"])
    build_plain("excerpts", "Selected excerpts", ["excerpts0", "excerpts1", "excerpts2", "excerpts3", "excerpts4"])
    build_plain("author", "The author", ["author"])
    build_plain("errata", "Errata", ["errata"])
    build_plain("edu", "For educators", ["edu"], "Courses that used the book, and the author's offer to trade teaching material.")
    build_plain("bibliography", "Bibliography", ["bibliography"])
    build_plain("faq", "FAQ (historical)", ["faq"])
    build_plain("news", "News (historical)", ["news", "oldnews"])
    n = sum(len(fs) for _, _, fs in os.walk(OUT))
    print("built %d files into site/ (%d demos, %d chapters, %d figures, %d glossary terms, %d programs)" % (
        n, len(demos), len(chapters()), len(figures), len(glossary), len(programs)))

if __name__ == "__main__":
    main()
