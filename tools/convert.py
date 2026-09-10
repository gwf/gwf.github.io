#!/usr/bin/env python3
"""
Convert the legacy CBofN companion website (author's local copy, last
modified 30 Nov 2002) into structured data for the rebuild.

Re-runnable; python3 stdlib only.  External tools used (optional but
expected): pdftocairo (poppler) for SVG/PNG figure conversion and
pdftotext for locating the postscript-chapter page numbers.

Reads (read-only):   /Users/gary/Deprecated/cbn/{html,latex,code/src}
Writes:              /Users/gary/Git/cbn-site/{legacy,data,figures}

Never touches demos/, book/, data/demos.json or index.html.
"""

import html as htmlmod
import json
import os
import re
import shutil
import subprocess
import sys
from html.parser import HTMLParser

SRC = "/Users/gary/Deprecated/cbn"
HTML = os.path.join(SRC, "html")
LATEX = os.path.join(SRC, "latex")
CSRC = os.path.join(SRC, "code", "src")
OUT = "/Users/gary/Git/cbn-site"
LEGACY = os.path.join(OUT, "legacy")
DATA = os.path.join(OUT, "data")
PAGES = os.path.join(DATA, "pages")
FIGURES = os.path.join(OUT, "figures")
BOOK_PDF = os.path.join(OUT, "book", "cbn.pdf")
PDFTEXT_CACHE = os.path.join(OUT, "tools", "_cbn.txt")

SOURCE_NOTE = ("Author's local copy of the companion website for "
               "The Computational Beauty of Nature (MIT Press, 1998); "
               "site last modified 30 Nov 2002.")

PROGRAMS = ("assoc bifur1d boids ca diffuse eipd gabump gaipd gastring gasurf "
            "gatask gen1d gsw henbif hencon henon henwarp hopfield hp ifs julia "
            "life lorenz lotka lsys mandel mg mlp mrcm phase1d predprey rossler "
            "sipd stutter termites vants zcs zcscup").split()

ARCHIVE_EXT = {".tgz", ".zip", ".jar", ".hqx", ".sit", ".gz", ".tar"}

# pdf page starts supplied by the caller (1-based pdf page; printed = pdf - 20)
PDF_PAGES = {1: 21, 2: 31, 3: 43, 5: 81, 6: 97, 7: 115, 8: 131, 10: 159,
             11: 179, 12: 201, 13: 223, 15: 251, 16: 281, 17: 301, 18: 327,
             20: 359, 21: 381, 22: 403}
PDF_PAGES_NAMED = {"Epilogue": 445, "Source Code Notes": 455, "Glossary": 463}
PDF_OFFSET = 20

# LaTeX chapter files in book order -> chapter number (0 = preface)
TEX_CHAPTERS = [("preface", 0), ("introduction", 1), ("numbers", 2),
                ("compute", 3), ("post1", 4), ("selfsim", 5), ("lsystems", 6),
                ("ifscma", 7), ("julibrot", 8), ("post2", 9), ("chaos", 10),
                ("strange", 11), ("predprey", 12), ("control", 13),
                ("post3", 14), ("ca", 15), ("agents", 16), ("ipd", 17),
                ("analog", 18), ("post4", 19), ("ga", 20), ("class", 21),
                ("learn", 22), ("post5", 23), ("epilogue", 24),
                ("appendix", "Source Code Notes")]

report = {"warnings": []}


def warn(msg):
    report["warnings"].append(msg)
    print("WARN:", msg, file=sys.stderr)


def read(path):
    with open(path, "rb") as f:
        raw = f.read()
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("cp1252", errors="replace")


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def dump_json(path, obj):
    write(path, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def tex_quotes(s):
    """``x'' -> “x”, `x' -> ‘x’ (TeX-style quoting used all over the site)."""
    s = s.replace("``", "\u201c").replace("''", "\u201d")
    s = re.sub(r"(?<![A-Za-z])`", "\u2018", s)
    return s


def collapse(s):
    return re.sub(r"[ \t\r\n]+", " ", s).strip()


def content_section(doc):
    """Return the HTML between <div id="content"> and the copyright footer."""
    m = re.search(r'<div id="content">', doc)
    body = doc[m.end():] if m else doc
    # strip the copyright footer (and everything after it)
    body = re.split(r"<p>\s*<small>\s*Copyright", body, maxsplit=1)[0]
    # strip stray "Last update" lines
    body = re.sub(r"Last update:[^<]*", "", body)
    return body


def page_title(doc):
    m = re.search(r"<title>(.*?)</title>", doc, re.S)
    if not m:  # a few pages have no <title>; use the first content heading
        m = re.search(r'<div id="content">.*?<h[1-3]>(.*?)</h[1-3]>', doc, re.S)
        if not m:
            return ""
        return collapse(htmlmod.unescape(re.sub(r"<[^>]+>", "", m.group(1))))
    t = collapse(htmlmod.unescape(m.group(1)))
    return re.sub(r"^CBofN\s*-\s*", "", t)


# --------------------------------------------------------------------------
# HTML -> Markdown
# --------------------------------------------------------------------------

def rewrite_url(url):
    """Rewrite legacy relative URLs to repo-relative paths."""
    if not url:
        return url
    if re.match(r"^(https?|ftp|mailto|javascript):", url):
        return url
    if url.startswith("graphics/"):
        return "legacy/" + url
    m = re.match(r"^figs/(\d+)(?:-(\d+)dpi)?\.(gif|pdf|eps)$", url)
    if m:
        n, dpi, ext = m.groups()
        if ext == "pdf":
            return "figures/pdf/%s.pdf" % n
        if ext == "gif" and dpi == "100":
            return "figures/gif100/%s.gif" % n
        return "legacy/" + url  # eps / 24 / 300 dpi are not copied
    if re.match(r"^[A-Za-z0-9_.-]+\.(gif|jpg|jpeg|png|css|bib)$", url):
        return "legacy/" + url
    if re.match(r"^[A-Za-z0-9_-]+\.html(#.*)?$", url):
        base, _, frag = url.partition("#")
        return "pages/" + base[:-5] + ".md" + ("#" + frag if frag else "")
    if os.path.splitext(url)[1].lower() in ARCHIVE_EXT:
        return "legacy/" + url  # not copied; kept so the reference survives
    return url


class MD(HTMLParser):
    """Small, forgiving HTML -> Markdown converter tuned for this site."""

    BLOCK = {"p", "div", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
             "pre", "blockquote", "hr", "table", "tr", "center", "dl", "dt",
             "dd", "form", "applet"}
    SKIP = {"script", "style", "noscript", "form", "input", "applet", "ilayer",
            "head", "title"}

    def __init__(self, heading_shift=0):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.lists = []          # stack of ("ul"|"ol", counter)
        self.skip = 0
        self.pre = 0
        self.blockquote = 0
        self.href = None
        self.linktext = []
        self.table_colors = []   # stack of bgcolor per <table>
        self.box_title = None    # collecting a BLUE box title
        self.bold = 0
        self.ital = 0
        self.code = 0
        self.heading_shift = heading_shift
        self.in_heading = None
        self.strip_lead = False

    # -- helpers ------------------------------------------------------------
    def buf(self):
        if self.href is not None:
            return self.linktext
        if self.box_title is not None:
            return self.box_title
        return self.out

    def emit(self, s):
        self.buf().append(s)

    def open_mark(self, mark):
        self.emit(mark)
        self.strip_lead = True

    def close_mark(self, mark):
        """Append a closing emphasis marker, moving trailing spaces after it."""
        b = self.buf()
        text = "".join(b)
        stripped = text.rstrip(" ")
        if stripped.endswith(mark):  # empty emphasis: drop both markers
            b[:] = [stripped[:-len(mark)]]
            return
        b[:] = [stripped, mark, " " if len(stripped) != len(text) else ""]

    def newline(self, n=1):
        """Ensure the output ends with n newlines (in prose mode)."""
        if self.href is not None or self.box_title is not None:
            return
        text = "".join(self.out)
        stripped = text.rstrip(" \t")
        trailing = len(stripped) - len(stripped.rstrip("\n"))
        if not stripped:
            return
        self.out = [stripped + "\n" * max(0, n - trailing)]

    def indent(self):
        return "  " * (len(self.lists) - 1) if self.lists else ""

    # -- parser callbacks ---------------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in self.SKIP:
            self.skip += 1
            return
        if self.skip:
            return
        if tag == "table":
            self.table_colors.append((a.get("bgcolor") or "").upper())
            self.newline(2)
            return
        if tag == "td" and self.table_colors and self.table_colors[-1] == "BLUE":
            self.box_title = []
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.newline(2)
            lvl = min(6, int(tag[1]) + self.heading_shift)
            self.in_heading = lvl
            self.emit("#" * lvl + " ")
            return
        if tag == "p":
            self.newline(2)
            if self.blockquote:
                self.emit("> ")
            return
        if tag == "br":
            if self.pre:
                self.emit("\n")
            else:
                self.emit("  \n" + ("> " if self.blockquote else ""))
            return
        if tag == "hr":
            self.newline(2)
            self.emit("---")
            self.newline(2)
            return
        if tag in ("ul", "ol"):
            self.newline(1 if self.lists else 2)
            self.lists.append([tag, 0])
            return
        if tag == "li":
            self.newline(1)
            if not self.lists:
                self.lists.append(["ul", 0])
            kind, n = self.lists[-1]
            self.lists[-1][1] = n + 1
            self.emit(self.indent() + ("- " if kind == "ul" else "%d. " % (n + 1)))
            return
        if tag == "pre":
            if self.code:  # <tt><pre> pattern: drop the dangling inline marker
                b = self.buf()
                text = "".join(b).rstrip(" ")
                if text.endswith("`"):
                    b[:] = [text[:-1]]
                self.code = 0
            self.newline(2)
            self.emit("```\n")
            self.pre += 1
            return
        if tag == "blockquote":
            self.newline(2)
            self.blockquote += 1
            self.emit("> ")
            return
        if tag == "a":
            if self.href is not None:      # unclosed <a> (site has a few)
                self.handle_endtag("a")
            if a.get("href"):
                self.href = a.get("href")
                self.linktext = []
            return
        if tag == "img":
            src = rewrite_url(a.get("src", ""))
            alt = collapse(a.get("alt") or "")
            self.emit("![%s](%s)" % (alt, src))
            return
        if tag in ("b", "strong"):
            self.bold += 1
            self.open_mark("**")
            return
        if tag in ("i", "em"):
            self.ital += 1
            self.open_mark("*")
            return
        if tag in ("tt", "code"):
            if not self.pre:
                self.code += 1
                self.open_mark("`")
            return
        if tag in ("tr",):
            self.newline(1)
            return
        if tag in ("div", "center", "dl", "dd", "dt"):
            self.newline(2)
            return

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if self.skip:
            return
        if tag == "table":
            if self.table_colors:
                self.table_colors.pop()
            self.newline(2)
            return
        if tag == "td" and self.box_title is not None:
            title = collapse("".join(self.box_title).replace("**", "")).strip()
            self.box_title = None
            if title:
                self.newline(2)
                self.out.append("## " + title)
                self.newline(2)
            return
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.in_heading = None
            self.newline(2)
            return
        if tag == "p":
            self.newline(2)
            return
        if tag in ("ul", "ol"):
            if self.lists:
                self.lists.pop()
            self.newline(1 if self.lists else 2)
            return
        if tag == "li":
            self.newline(1)
            return
        if tag == "pre":
            self.pre = max(0, self.pre - 1)
            self.newline(1)
            self.emit("```")
            self.newline(2)
            return
        if tag == "blockquote":
            self.blockquote = max(0, self.blockquote - 1)
            self.newline(2)
            return
        if tag == "a":
            if self.href is None:
                return
            text = "".join(self.linktext)
            href = self.href
            self.href = None
            self.linktext = []
            text = text if self.pre else collapse(text)
            if not text:
                return
            self.emit("[%s](%s)" % (text, rewrite_url(href)))
            return
        if tag in ("b", "strong"):
            if self.bold:
                self.bold -= 1
                self.close_mark("**")
            return
        if tag in ("i", "em"):
            if self.ital:
                self.ital -= 1
                self.close_mark("*")
            return
        if tag in ("tt", "code"):
            if self.code:
                self.code -= 1
                self.close_mark("`")
            return
        if tag == "tr":
            self.newline(1)
            return
        if tag in ("div", "center", "dl", "dd", "dt"):
            self.newline(2)
            return

    def handle_data(self, data):
        if self.skip:
            return
        if self.pre:
            self.emit(data)
            return
        text = re.sub(r"[ \t\r\n]+", " ", data)
        if not text:
            return
        text = tex_quotes(text)
        cur = "".join(self.buf())
        if text == " " and (not cur or cur.endswith((" ", "\n"))):
            return
        if cur.endswith("\n") or not cur or self.strip_lead:
            text = text.lstrip()
        if not text:
            return
        self.strip_lead = False
        self.emit(text)

    def result(self):
        s = "".join(self.out)
        # tidy markdown: no trailing spaces before newline (except hard breaks)
        s = re.sub(r"(?<!  )[ \t]+\n", "\n", s)
        s = re.sub(r"\n{3,}", "\n\n", s)
        s = re.sub(r"(^|\n)> *\n", r"\1\n", s)
        s = re.sub(r"\n\s*---\s*\n\s*(?=#)", "\n\n", s)  # hr before heading
        return s.strip() + "\n"


def html_to_md(fragment, heading_shift=0):
    p = MD(heading_shift=heading_shift)
    p.feed(fragment)
    p.close()
    return p.result()


def inline_md(fragment):
    """Inline HTML -> single-line markdown (glossary definitions etc)."""
    return collapse(html_to_md(fragment).replace("\n", " "))


# --------------------------------------------------------------------------
# 1. legacy/ copy
# --------------------------------------------------------------------------

def copy_legacy():
    copied = 0
    size = 0
    for root, dirs, files in os.walk(HTML):
        rel = os.path.relpath(root, HTML)
        if rel == ".":
            rel = ""
        dirs[:] = [d for d in dirs if d != "figs"]
        for fn in files:
            if os.path.splitext(fn)[1].lower() in ARCHIVE_EXT:
                continue
            if fn == ".DS_Store":
                continue
            src = os.path.join(root, fn)
            dst = os.path.join(LEGACY, rel, fn)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if (not os.path.exists(dst) or
                    os.path.getmtime(dst) < os.path.getmtime(src) or
                    os.path.getsize(dst) != os.path.getsize(src)):
                shutil.copy2(src, dst)
            copied += 1
            size += os.path.getsize(src)
    return {"files": copied, "bytes": size}


# --------------------------------------------------------------------------
# 2. pages
# --------------------------------------------------------------------------

SKIP_PAGES = {"index"}  # splash page (image + amazon buy box) - nothing to keep
SKIP_PAGE_RE = re.compile(r"^(fig\d+|glossary(-[A-Z])?|java(small|med|large))$")


def convert_pages():
    names = []
    for fn in sorted(os.listdir(HTML)):
        if not fn.endswith(".html"):
            continue
        name = fn[:-5]
        if name in SKIP_PAGES or SKIP_PAGE_RE.match(name):
            continue
        doc = read(os.path.join(HTML, fn))
        title = page_title(doc)
        body = content_section(doc)
        md = html_to_md(body)
        if name in PROGRAMS:
            md = manpage_md(body)
        front = "---\ntitle: %s\nsource: html/%s\n---\n\n" % (
            json.dumps(title, ensure_ascii=False), fn)
        if name.startswith("java"):
            md += ("\n\n_The original page embedded the `CBNapplet` Java applet "
                   "(legacy/classes/); the javasmall/javamed/javalarge pages were "
                   "applet-only and are not converted._\n")
        write(os.path.join(PAGES, name + ".md"), front + md)
        names.append(name)
    return names


# --------------------------------------------------------------------------
# man pages / programs.json
# --------------------------------------------------------------------------

def man_sections(body):
    """Return ordered list of (SECTION, plain text) from a man2html page."""
    secs = []
    for m in re.finditer(r"<H4>([^<]+)</H4>\s*<PRE>(.*?)</PRE>", body, re.S):
        name = m.group(1).strip()
        txt = re.sub(r"<[^>]+>", "", m.group(2))
        txt = htmlmod.unescape(txt)
        secs.append((name, txt.strip("\n")))
    return secs


def dedent_block(txt):
    lines = txt.split("\n")
    ind = min((len(l) - len(l.lstrip()) for l in lines if l.strip()), default=0)
    return "\n".join(l[ind:] if len(l) >= ind else l for l in lines)


def unwrap(txt):
    """Join hard-wrapped man page paragraphs; keep blank-line paragraph breaks."""
    paras = re.split(r"\n\s*\n", dedent_block(txt).strip())
    out = []
    for p in paras:
        lines = [l.strip() for l in p.split("\n")]
        joined = ""
        for l in lines:
            if joined.endswith("-") and re.match(r"^[a-z]", l):
                joined = joined[:-1] + l  # re-join hyphenated word
            else:
                joined += (" " if joined else "") + l
        out.append(re.sub(r"  +", " ", joined))
    return "\n\n".join(out)


def parse_options(body):
    """Options from the raw OPTIONS section HTML: <B>-flag</B> [<I>type</I>] help."""
    m = re.search(r"<H4>OPTIONS</H4>\s*<PRE>(.*?)</PRE>", body, re.S)
    if not m:
        return []
    opts = []
    for e in re.finditer(r"<B>(-[^<]+)</B>(?:\s*<I>([^<]+)</I>)?(.*?)(?=<B>-|\Z)", m.group(1), re.S):
        flag, typ, rest = e.group(1).strip(), e.group(2), e.group(3)
        help_ = collapse(htmlmod.unescape(re.sub(r"<[^>]+>", "", rest)))
        help_ = re.sub(r"(\w)- (\w)", r"\1\2", help_)  # re-join man-page hyphenation
        opts.append({"flag": flag, "type": (typ.strip() if typ else "switch"),
                     "default": None, "help": help_})
    return opts


def parse_examples(txt):
    examples = []
    block = dedent_block(txt).strip()
    for chunk in re.split(r"\n\s*\n", block):
        lines = [l.rstrip() for l in chunk.split("\n") if l.strip()]
        if not lines:
            continue
        if lines[0].rstrip().endswith(":") and len(lines) > 1:
            label = lines[0].strip().rstrip(":")
            cmd = re.sub(r"\s+", " ", " ".join(l.strip() for l in lines[1:]))
            examples.append({"label": label, "command": cmd})
        elif lines[0].lstrip().startswith(("See ", "Note")):
            examples.append({"label": None, "note": re.sub(r"\s+", " ", " ".join(l.strip() for l in lines))})
        else:
            examples.append({"label": None, "command": re.sub(r"\s+", " ", " ".join(l.strip() for l in lines))})
    return examples


def c_source_info(prog):
    """Defaults from the C OPTION[] table and global initialisers."""
    path = os.path.join(CSRC, prog + ".c")
    if not os.path.exists(path):
        return {}
    src = read(path)
    # header comment (NAME/NOTES/... block)
    m = re.search(r"/\*\s*NAME(.*?)\*/", src, re.S)
    header = None
    if m:
        header = "\n".join(re.sub(r"^\s*\*\s?", "", l) for l in ("NAME" + m.group(1)).split("\n")).strip()
    head = src.split("OPTION options[]")[0]
    # global initialisers: type a = 1, b = 2; and char *s = "x";
    inits = {}
    for decl in re.finditer(r"^\s*(?:int|double|float|char|long|unsigned)\s*\*?\s*([^;]*);", head, re.M):
        for part in decl.group(1).split(","):
            mm = re.match(r"\s*\**\s*(\w+)(?:\[[^\]]*\])?\s*=\s*(.+?)\s*$", part)
            if mm:
                inits[mm.group(1)] = mm.group(2).strip()
            else:
                mm = re.match(r"\s*(\**)\s*(\w+)\s*$", part)
                if mm:  # uninitialised C global: zero / NULL
                    inits[mm.group(2)] = "NULL" if mm.group(1) else "0"
    defaults = {}
    types = {}
    tbl = re.search(r"OPTION options\[\]\s*=\s*\{(.*?)\n\};", src, re.S)
    if tbl:
        for e in re.finditer(r'\{\s*"(-[^"]+)"\s*,\s*(OPT_\w+)\s*,\s*([^,]+),', tbl.group(1)):
            flag, typ, var = e.group(1), e.group(2), e.group(3).strip()
            types[flag] = typ.replace("OPT_", "").lower()
            var = var.lstrip("&").strip()
            if var in inits:
                v = inits[var]
                if typ == "OPT_STRING":
                    v = None if v == "NULL" else v.strip('"')
                elif typ == "OPT_SWITCH":
                    v = v not in ("0",)
                else:
                    try:
                        v = int(v) if typ == "OPT_INT" else float(v)
                    except ValueError:
                        pass
                defaults[flag] = v
    return {"header": header, "defaults": defaults, "types": types}


def manpage_md(body):
    parts = []
    for name, txt in man_sections(body):
        parts.append("## " + name.title())
        if name in ("SYNOPSIS", "EXAMPLES"):
            parts.append("```\n" + dedent_block(txt).strip("\n") + "\n```")
        elif name == "OPTIONS":
            parts.append("\n".join(
                "- `%s`%s — %s" % (o["flag"], "" if o["type"] == "switch" else " *%s*" % o["type"], o["help"])
                for o in parse_options(body)))
        else:
            parts.append(unwrap(txt))
    return "\n\n".join(parts) + "\n"


def source_index():
    """Category + blurb for each program from source.html."""
    doc = content_section(read(os.path.join(HTML, "source.html")))
    info = {}
    cat = None
    order = 0
    for m in re.finditer(r"<h1>(.*?)</h1>|<h2><a\s+href=\"(\w+)\.html\">\w+</a></h2><p>(.*?)(?=<h[12]>|$)", doc, re.S):
        if m.group(1):
            cat = collapse(htmlmod.unescape(m.group(1)))
        else:
            order += 1
            info[m.group(2)] = {"category": cat, "blurb": inline_md(m.group(3)), "order": order}
    return info


def convert_programs():
    idx = source_index()
    progs = []
    for prog in PROGRAMS:
        path = os.path.join(HTML, prog + ".html")
        if not os.path.exists(path):
            warn("missing man page html for %s" % prog)
            continue
        body = content_section(read(path))
        secs = dict(man_sections(body))
        cinfo = c_source_info(prog)
        name_line = unwrap(secs.get("NAME", ""))
        m = re.match(r"(\w+)\s*-\s*(.*)", name_line, re.S)
        summary = m.group(2).strip() if m else name_line
        synopsis = dedent_block(secs.get("SYNOPSIS", "")).strip()
        opts = parse_options(body)
        ctype_names = {"int": "integer", "double": "double", "string": "string",
                       "switch": "switch", "other": "other"}
        for o in opts:
            o["default"] = cinfo.get("defaults", {}).get(o["flag"])
            ct = cinfo.get("types", {}).get(o["flag"])
            if ct:
                o["type"] = ctype_names.get(ct, ct)
        extra = []
        for k, v in secs.items():
            if k in ("NAME", "SYNOPSIS", "DESCRIPTION", "OPTIONS", "EXAMPLES", "AUTHOR"):
                continue
            extra.append("### " + k.title() + "\n\n" + unwrap(v))
        desc = unwrap(secs.get("DESCRIPTION", ""))
        if extra:
            desc += "\n\n" + "\n\n".join(extra)
        entry = {
            "id": prog,
            "name": prog,
            "summary": summary,
            "category": idx.get(prog, {}).get("category"),
            "book_order": idx.get(prog, {}).get("order"),
            "blurb_md": idx.get(prog, {}).get("blurb"),
            "synopsis": synopsis,
            "description_md": desc,
            "options": opts,
            "examples": parse_examples(secs.get("EXAMPLES", "")),
            "c_source": "code/src/%s.c" % prog if cinfo else None,
            "man_page": "pages/%s.md" % prog,
            "java_port": None,
        }
        progs.append(entry)
    # Java ports (Mike Miller): match <Name>Algorithm.java by lower-cased stem
    java = {}
    jdir = os.path.join(SRC, "java")
    if os.path.isdir(jdir):
        for fn in os.listdir(jdir):
            mm = re.match(r"(\w+)Algorithm\.java$", fn)
            if mm:
                java[mm.group(1).lower()] = fn
    alias = {"bifur1d": "bifurc", "henbif": "henonbifurc", "hencon": "henoncontrol",
             "mg": "mackeyglass"}
    for p in progs:
        key = alias.get(p["id"], p["id"])
        if key in java:
            p["java_port"] = "java/" + java[key]
    return progs


# --------------------------------------------------------------------------
# 3. glossary
# --------------------------------------------------------------------------

ENTRY_RE = re.compile(
    r'<p><b><a name="([^"]+)">(.*?)</a></b>\s*(?:&nbsp;\s*)*(.*?)(?=<p><b><a name=|\Z)', re.S)


def convert_glossary():
    entries = []
    anchor_to_term = {}
    raw = []
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        path = os.path.join(HTML, "glossary-%s.html" % letter)
        if not os.path.exists(path):
            continue
        body = content_section(read(path))
        for m in ENTRY_RE.finditer(body):
            anchor, term, defn = m.group(1), collapse(htmlmod.unescape(m.group(2))), m.group(3)
            defn = re.split(r"<br>\s*<br>|<hr", defn)[0]
            raw.append((letter, anchor, term, defn))
            anchor_to_term[anchor] = term
    for letter, anchor, term, defn in raw:
        links = re.findall(r'href="glossary-[A-Z]\.html#([^"]+)"', defn)
        refs = []
        for a in links:
            t = anchor_to_term.get(a)
            if t and t not in refs and t != term:
                refs.append(t)
        # rewrite cross-links to in-document anchors
        d = re.sub(r'href="glossary-[A-Z]\.html#([^"]+)"', r'href="#\1"', defn)
        dmd = inline_md(d)
        see_also = []
        for sent in re.split(r"(?<=[.!?])\s+", dmd):
            if re.match(r"^\(?See\b", sent):
                for t in re.findall(r"\[([^\]]+)\]\(#([^)]+)\)", sent):
                    tt = anchor_to_term.get(t[1], t[0])
                    if tt not in see_also:
                        see_also.append(tt)
        entries.append({"id": anchor, "term": term, "letter": letter,
                        "definition_md": dmd, "see_also": see_also,
                        "references": refs})
    dump_json(os.path.join(DATA, "glossary.json"), entries)
    lines = ["# Glossary", "",
             "_From The Computational Beauty of Nature (Gary William Flake, MIT Press 1998)._", ""]
    cur = None
    for e in entries:
        if e["letter"] != cur:
            cur = e["letter"]
            lines += ["## " + cur, ""]
        lines.append('**<a id="%s"></a>%s** \u2014 %s' % (e["id"], e["term"], e["definition_md"]))
        lines.append("")
    write(os.path.join(DATA, "glossary.md"), "\n".join(lines))
    return len(entries)


# --------------------------------------------------------------------------
# 4. table of contents
# --------------------------------------------------------------------------

def pdftext_pages():
    """Pages of book/cbn.pdf as a list of strings (index 0 == pdf page 1)."""
    if not os.path.exists(PDFTEXT_CACHE) and os.path.exists(BOOK_PDF):
        try:
            subprocess.run(["pdftotext", "-layout", BOOK_PDF, PDFTEXT_CACHE], check=True)
        except Exception as e:  # noqa
            warn("pdftotext failed: %s" % e)
    if not os.path.exists(PDFTEXT_CACHE):
        return []
    return read(PDFTEXT_CACHE).split("\f")


def find_chapter_page(pages, number, title):
    pat = re.compile(r"^\s*%d\s+%s\s*$" % (number, re.escape(title)))
    for i, pg in enumerate(pages):
        for line in pg.split("\n")[:12]:
            if pat.match(line):
                return i + 1
    return None


def convert_toc():
    doc = content_section(read(os.path.join(HTML, "toc.html")))
    doc = htmlmod.unescape(doc)
    # tokenise
    toks = re.findall(r"<h3>.*?</h3>|<ul>|</ul>|<li>[^<]*(?:<a[^>]*>[^<]*</a>)?[^<]*", doc, re.S)
    pages = pdftext_pages()
    parts = []
    cur_part = {"number": None, "title": "Front Matter", "chapters": []}
    parts.append(cur_part)
    depth = 0
    chapter = None
    chap_no = 0
    epilogue = False

    def li_info(tok):
        m = re.search(r'<a href="([^"]+)">', tok)
        text = collapse(re.sub(r"<[^>]+>", "", tok[4:]))
        return text, (m.group(1) if m else None)

    for tok in toks:
        if tok.startswith("<h3>"):
            text, href = li_info("<li>" + tok)
            text = collapse(re.sub(r"<[^>]+>", "", tok))
            m = re.match(r"Part (\w+)\s*-\s*(.*)", text)
            if m:
                cur_part = {"number": m.group(1), "title": m.group(2), "chapters": [],
                            "synopsis": rewrite_url(href)}
            else:
                cur_part = {"number": None, "title": text, "chapters": [],
                            "synopsis": rewrite_url(href)}
                epilogue = text == "Epilogue"
            parts.append(cur_part)
            depth = 0
        elif tok == "<ul>":
            depth += 1
        elif tok == "</ul>":
            depth -= 1
        elif tok.startswith("<li>"):
            text, href = li_info(tok)
            if depth == 1:
                entry = {"title": text, "sections": []}
                if href:
                    entry["excerpt"] = rewrite_url(href)
                if text == "Preface":
                    entry["number"] = None
                    entry["kind"] = "preface"
                elif epilogue and cur_part["chapters"]:
                    entry["number"] = None
                    entry["kind"] = "back_matter"
                else:
                    chap_no += 1
                    entry["number"] = chap_no
                    entry["kind"] = "postscript" if text.startswith("Postscript") else "chapter"
                    if epilogue:
                        entry["kind"] = "epilogue"
                cur_part["chapters"].append(entry)
                chapter = entry
            elif depth >= 2 and chapter is not None:
                sec = {"title": text}
                if href:
                    sec["excerpt"] = rewrite_url(href)
                chapter["sections"].append(sec)
    # page numbers
    ps_found = {}
    for part in parts:
        for ch in part["chapters"]:
            n = ch.get("number")
            pdf = None
            if n in PDF_PAGES:
                pdf = PDF_PAGES[n]
            elif ch["kind"] == "epilogue":
                pdf = PDF_PAGES_NAMED["Epilogue"]
            elif ch["title"] in PDF_PAGES_NAMED:
                pdf = PDF_PAGES_NAMED[ch["title"]]
            elif ch["kind"] == "postscript":
                pdf = find_chapter_page(pages, n, ch["title"])
                ps_found[n] = pdf
                if pdf is None:
                    warn("could not locate pdf page for chapter %s %s" % (n, ch["title"]))
            elif ch["kind"] == "back_matter":
                pat = re.compile(r"^\s*%s\s*$" % re.escape(ch["title"]))
                for i, pg in enumerate(pages):
                    if any(pat.match(l) for l in pg.split("\n")[:12]):
                        pdf = i + 1
                        break
            ch["pdf_page"] = pdf
            ch["printed_page"] = (pdf - PDF_OFFSET) if pdf else None
    toc = {"source": "html/toc.html", "pdf": "book/cbn.pdf",
           "page_offset_note": "printed page = pdf page - %d" % PDF_OFFSET,
           "parts": parts}
    dump_json(os.path.join(DATA, "toc.json"), toc)
    nchap = sum(1 for p in parts for c in p["chapters"] if c.get("number"))
    return {"chapters": nchap, "postscript_pages": ps_found}


# --------------------------------------------------------------------------
# 5. figures
# --------------------------------------------------------------------------

def detex(s):
    s = s.replace("\\ignorespaces", "")
    s = re.sub(r"\\(emph|textit|textbf|textsc|mbox|hbox)\{([^{}]*)\}", r"\2", s)
    s = re.sub(r"\{\\(em|it|bf|sc|tt)\s+([^{}]*)\}", r"\2", s)
    acc = {"'e": "é", "'a": "á", "'o": "ó", "'i": "í", '"o': "ö", '"u': "ü", '"a': "ä",
           "^e": "ê", "`e": "è", "ce": "çe"}
    s = re.sub(r"\\(['\"^`c])\{?([a-zA-Z])\}?(?:\{\})?",
               lambda m: acc.get(m.group(1) + m.group(2), m.group(2)), s)
    s = s.replace("---", "\u2014").replace("--", "\u2013").replace("~", " ")
    s = s.replace("\\,", " ").replace("\\&", "&").replace("\\%", "%")
    s = re.sub(r"\\[a-zA-Z]+\s*", "", s)
    s = s.replace("{", "").replace("}", "")
    return tex_quotes(collapse(s))


def parse_lof(path):
    out = []
    for line in read(path).split("\n"):
        m = re.match(r"\\contentsline \{figure\}\{\\numberline \{([\d.]+)\}\{(.*)\}\}\{(\d+)\}\s*$", line)
        if m:
            out.append({"number": m.group(1), "caption": detex(m.group(2)), "page": int(m.group(3))})
    return out


def run(cmd):
    try:
        r = subprocess.run(cmd, capture_output=True, text=True)
        return r.returncode == 0, (r.stderr or r.stdout).strip()
    except FileNotFoundError as e:
        return False, str(e)


def convert_figures():
    figsdir = os.path.join(HTML, "figs")
    indices = sorted(int(m.group(1)) for fn in os.listdir(figsdir)
                     for m in [re.match(r"^(\d+)\.pdf$", fn)] if m)
    master = parse_lof(os.path.join(LATEX, "master.lof"))
    allfigs = parse_lof(os.path.join(LATEX, "allfigs.lof"))
    if len(master) != len(indices):
        warn("master.lof has %d figures but html/figs has %d pdfs" % (len(master), len(indices)))
    if len(allfigs) != len(master):
        warn("allfigs.lof (%d) and master.lof (%d) differ in length" % (len(allfigs), len(master)))
    # Numbering.  html/figs/N follows allfigs.lof (the standalone allfigs.tex
    # build, numbered 25.N, full under-figure captions), which matches the
    # published book; master.lof has the real chapter numbering but is a
    # slightly older run (figures 74-77 in chapter 11 are in a different
    # order there).  So: take per-chapter figure counts from master.lof and
    # number the allfigs sequence positionally within each chapter, then
    # verify every "Figure c.n  <caption>" against the book PDF text.
    per_chapter = []
    for m in master:
        ch = int(m["number"].split(".")[0])
        if not per_chapter or per_chapter[-1][0] != ch:
            per_chapter.append([ch, 0])
        per_chapter[-1][1] += 1
    numbers = []
    for ch, k in per_chapter:
        numbers += ["%d.%d" % (ch, j + 1) for j in range(k)]
    lof_caption = {m["number"]: m for m in master}
    # Full under-figure captions (\caption[lof form]{full form}) from
    # allfigs-fff.tex, aligned to the lof sequence by matching text; a few
    # figures are not in that file, so alignment is best-effort.
    fff = []
    fpath = os.path.join(LATEX, "allfigs-fff.tex")
    if os.path.exists(fpath):
        src = "\n".join(l for l in read(fpath).split("\n") if not l.lstrip().startswith("%"))
        for m in re.finditer(r"\\caption\s*(\[)?", src):
            pos = m.end()
            short = None
            if m.group(1):
                depth, j = 1, pos
                while j < len(src) and depth:
                    depth += {"[": 1, "]": -1}.get(src[j], 0)
                    j += 1
                short = src[pos:j - 1]
                pos = j
                while pos < len(src) and src[pos] in " \n\t":
                    pos += 1
            if pos < len(src) and src[pos] == "{":
                full, _ = tex_arg(src, pos)
                fff.append((detex(short) if short else None, detex(full)))
    full_captions = [None] * len(allfigs)
    j = 0
    for i, a in enumerate(allfigs):
        if j < len(fff):
            short, full = fff[j]
            key = norm(a["caption"])[:20]
            if key and (norm(short or "")[:20] == key or norm(full)[:20] == key):
                full_captions[i] = full
                j += 1
    pages = pdftext_pages()
    pages_norm = [re.sub(r"\s+", " ", p.replace("ﬀ", "ff").replace("ﬁ", "fi")
                         .replace("ﬂ", "fl").replace("ﬃ", "ffi")) for p in pages]
    verified = 0
    toc_titles = chapter_titles()
    for d in ("pdf", "gif100", "svg", "thumb"):
        os.makedirs(os.path.join(FIGURES, d), exist_ok=True)
    figures = []
    failures = []
    for i in indices:
        number = numbers[i - 1] if i - 1 < len(numbers) else None
        meta = lof_caption.get(number, {"caption": None, "page": None})
        long_caption = allfigs[i - 1]["caption"] if i - 1 < len(allfigs) else None
        chapter = int(number.split(".")[0]) if number else None
        # verify against the book text and find the pdf page of the caption
        pdf_page = None
        verification = None
        full_caption = full_captions[i - 1] if i - 1 < len(full_captions) else None
        if number and pages_norm:
            # 1) "Figure c.n <first words of a caption form>" on some page
            for cap in (full_caption, long_caption, meta.get("caption")):
                if not cap or pdf_page:
                    continue
                words = re.findall(r"[A-Za-z]+", cap)[:3]
                pat = re.compile(r"Figure\s+%s\s+%s" % (re.escape(number),
                                 r"\W*".join(re.escape(w) for w in words)), re.I)
                for pi, pg in enumerate(pages_norm):
                    if pat.search(pg):
                        pdf_page, verification = pi + 1, "caption"
                        break
            # 2) fall back to the first page that mentions "Figure c.n" at all
            if pdf_page is None:
                pat = re.compile(r"Figure\s+%s(?![\d.])" % re.escape(number))
                for pi, pg in enumerate(pages_norm):
                    if pat.search(pg):
                        pdf_page, verification = pi + 1, "number-only"
                        break
            if verification == "caption":
                verified += 1
            else:
                warn("figure %d (%s): caption not matched in book pdf text (%s): %r"
                     % (i, number, verification or "number not found", long_caption))
        if pdf_page is None and meta.get("page"):
            pdf_page, verification = meta["page"] + PDF_OFFSET, "master.lof page"
        files = {}
        for key, fn in (("eps", "%d.eps"), ("pdf", "%d.pdf"), ("gif24", "%d-24dpi.gif"),
                        ("gif100", "%d-100dpi.gif"), ("gif300", "%d-300dpi.gif")):
            p = os.path.join(figsdir, fn % i)
            files[key] = ("legacy-source:html/figs/" + fn % i) if os.path.exists(p) else None
        srcpdf = os.path.join(figsdir, "%d.pdf" % i)
        dstpdf = os.path.join(FIGURES, "pdf", "%d.pdf" % i)
        if not os.path.exists(dstpdf):
            shutil.copy2(srcpdf, dstpdf)
        files["pdf"] = "figures/pdf/%d.pdf" % i
        g = os.path.join(figsdir, "%d-100dpi.gif" % i)
        if os.path.exists(g):
            dstg = os.path.join(FIGURES, "gif100", "%d.gif" % i)
            if not os.path.exists(dstg):
                shutil.copy2(g, dstg)
            files["gif100"] = "figures/gif100/%d.gif" % i
        svg = os.path.join(FIGURES, "svg", "%d.svg" % i)
        if not os.path.exists(svg):
            ok, err = run(["pdftocairo", "-svg", srcpdf, svg])
            if not ok:
                failures.append({"index": i, "kind": "svg", "error": err})
        files["svg"] = "figures/svg/%d.svg" % i if os.path.exists(svg) else None
        thumb = os.path.join(FIGURES, "thumb", "%d.png" % i)
        if not os.path.exists(thumb):
            prefix = os.path.join(FIGURES, "thumb", "_t%d" % i)
            ok, err = run(["pdftocairo", "-png", "-singlefile", "-scale-to", "320", srcpdf, prefix])
            if ok and os.path.exists(prefix + ".png"):
                os.replace(prefix + ".png", thumb)
            else:
                failures.append({"index": i, "kind": "thumb", "error": err})
        files["thumb"] = "figures/thumb/%d.png" % i if os.path.exists(thumb) else None
        figures.append({"index": i, "number": number,
                        "caption": long_caption or meta.get("caption"),
                        "caption_full": full_caption,
                        "caption_lof": meta.get("caption"),
                        "pdf_page_source": verification,
                        "chapter": chapter, "chapter_title": toc_titles.get(chapter),
                        "pdf_page": pdf_page,
                        "printed_page": (pdf_page - PDF_OFFSET) if pdf_page else None,
                        "gallery_page": "pages/fig%d.md" % ((i - 1) // 9 + 1),
                        "files": files})
    dump_json(os.path.join(DATA, "figures.json"), figures)
    return {"count": len(figures), "verified_in_pdf": verified, "failures": failures}


def chapter_titles():
    path = os.path.join(DATA, "toc.json")
    if not os.path.exists(path):
        return {}
    toc = json.load(open(path))
    return {c["number"]: c["title"] for p in toc["parts"] for c in p["chapters"] if c.get("number")}


# --------------------------------------------------------------------------
# 7. quotes & reviews
# --------------------------------------------------------------------------

def tex_arg(s, pos):
    """Parse a {...} group starting at s[pos]=='{'; return (content, end)."""
    assert s[pos] == "{"
    depth = 0
    for i in range(pos, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return s[pos + 1:i], i + 1
    return s[pos + 1:], len(s)


def book_quotes():
    """(chapter, text, author) for every \\xquote in the LaTeX, book order."""
    out = []
    for stem, num in TEX_CHAPTERS:
        path = os.path.join(LATEX, stem + ".tex")
        if not os.path.exists(path):
            continue
        src = "\n".join(l for l in read(path).split("\n") if not l.lstrip().startswith("%"))
        for m in re.finditer(r"\\xquote\s*\{", src):
            text, end = tex_arg(src, m.end() - 1)
            author = ""
            if end < len(src) and src[end] == "{":
                author, _ = tex_arg(src, end)
            out.append({"chapter": num, "text": detex(text.replace("\\\\", " ")), "author": detex(author)})
    return out


def norm(s):
    return re.sub(r"[^a-z0-9]", "", s.lower())


def convert_quotes():
    doc = content_section(read(os.path.join(HTML, "quotes.html")))
    m = re.search(r"<blockquote>(.*?)</blockquote>", doc, re.S)
    body = m.group(1) if m else doc
    chunks = [c for c in re.split(r"<p>\s*<br>", body) if c.strip()]
    book = book_quotes()
    used = set()
    quotes = []
    for c in chunks:
        parts = re.split(r"<br>\s*\n\s*---", c, maxsplit=1)
        if len(parts) != 2:
            warn("quote chunk without attribution: %r" % collapse(c)[:60])
            continue
        qtext = inline_md(parts[0]).strip()
        qtext = re.sub(r"^[\u201c\"]|[\u201d\"]$", "", qtext).strip()
        attr = inline_md(parts[1]).strip()
        attr_plain = attr.replace("**", "")
        chapter = None
        key = norm(qtext)[:40]
        for i, bq in enumerate(book):
            if i in used:
                continue
            bk = norm(bq["text"])[:40]
            if bk and (bk == key or bk[:25] == key[:25]):
                chapter = bq["chapter"]
                used.add(i)
                break
        if chapter is None:
            for i, bq in enumerate(book):
                if i in used:
                    continue
                if bq["author"] and norm(bq["author"]) in norm(attr_plain):
                    chapter = bq["chapter"]
                    used.add(i)
                    break
        quotes.append({"quotation": qtext, "attribution": attr_plain,
                       "attribution_md": attr,
                       "chapter": chapter, "part": chapter_part(chapter)})
    dump_json(os.path.join(DATA, "quotes.json"), quotes)
    return {"count": len(quotes), "book_xquotes": len(book),
            "unmatched": sum(1 for q in quotes if q["chapter"] is None)}


def chapter_part(ch):
    if ch is None:
        return None
    if isinstance(ch, str):
        return "Back Matter"
    if ch == 0:
        return "Preface"
    if ch == 1:
        return "Introduction"
    if ch == 24:
        return "Epilogue"
    for lo, hi, name in ((2, 4, "I - Computation"), (5, 9, "II - Fractals"),
                         (10, 14, "III - Chaos"), (15, 19, "IV - Complex Systems"),
                         (20, 23, "V - Adaptation")):
        if lo <= ch <= hi:
            return name
    return None


def box_sections(doc):
    """Split a page built from the blue 'box' tables into (title, inner_html)."""
    out = []
    pat = re.compile(r'bgcolor="BLUE"[^>]*>.*?<font[^>]*>(.*?)</font>.*?bgcolor="OFFWHITE"[^>]*>.*?<font[^>]*>(.*?)</font>\s*</td></tr></table></td></tr></table></td></tr></table>', re.S)
    for m in pat.finditer(doc):
        out.append((collapse(re.sub(r"<[^>]+>", "", htmlmod.unescape(m.group(1)))), m.group(2)))
    return out


def home_review_excerpts():
    """Reviewer -> quoted excerpt from the home page news items."""
    doc = content_section(read(os.path.join(HTML, "home.html")))
    out = {}
    for m in re.finditer(r"<h3>(.*?)</h3>\s*<p>(.*?)(?=<h3>|\Z)", doc, re.S):
        head, body = m.group(1), m.group(2)
        if "review" not in head.lower() and "on <i>CBofN</i>" not in head:
            continue
        rev = re.findall(r"--\s*<a[^>]*>([^<]+)</a>", body)
        if not rev:
            continue
        text = re.sub(r"<a href=\"reviews.html\">.*?</a>", "", body, flags=re.S)
        text = re.sub(r"The complete review can be found.*?(?=<|$)", "", text, flags=re.S)
        text = re.split(r"--\s*<a", text)[0]
        md = html_to_md(text).strip()
        md = re.sub(r"\n\s*\.\.\.\s*$", " ...", md)
        out[collapse(rev[-1])] = {"heading": collapse(re.sub(r"<[^>]+>", "", head)), "excerpt_md": md}
    return out


# The "Other Reviews" list on reviews.html is free prose; the structured
# fields are pinned here by URL (the prose itself is kept in note_md).
REVIEW_FIELDS = {
    "ece-www.colorado.edu/faculty/bradley": ("AI Magazine", "Summer 2000", "Elizabeth Bradley", "print"),
    "math.union.edu/people/faculty/framem": ("American Mathematical Monthly", None, "Michael Frame", "print"),
    "jasss.soc.surrey.ac.uk": ("Journal of Artificial Societies and Social Simulation", None, "Nigel Gilbert", "print/online"),
    "bcs.org.uk": ("The British Computer Society", None, "J. W. Bruce", "print/online"),
    "sbfonline.com": ("Science, Books & Films (AAAS)", "May 1999", None, "print"),
    "lowfield.co.uk": (None, None, "Chris Harrison", "online"),
    "ercb.com/ddj": ("Doctor Dobb's Journal", "August 1999", "Gregory V. Wilson", "print/online"),
    "slashdot.org": ("Slashdot", "October 29, 1998", None, "online"),
    "santafe.edu/~shalizi": ("Santa Fe Institute (personal page)", None, "Cosma Shalizi", "online"),
    "anatomy.usyd.edu.au/danny": (None, None, "Danny Yee", "online"),
    "cogs.susx.ac.uk": (None, "1999", "Michael Salsbury", "online"),
    "quebecmicro.com": ("Quebec Micro (in French)", None, None, "print/online"),
    "deja.com": ("USENET", None, "Arunprasad Marathe", "usenet"),
}


def li_items(inner):
    """Top-level <li> items of a <ul>, each with its nested <ul> kept inline."""
    items = []
    depth = 0
    cur = None
    for tok in re.split(r"(<ul>|</ul>|<li>)", inner):
        if tok == "<ul>":
            depth += 1
            if cur is not None and depth > 1:
                cur.append(" <ul>")
        elif tok == "</ul>":
            depth -= 1
            if cur is not None and depth >= 1:
                cur.append("</ul>")
        elif tok == "<li>":
            if depth <= 1:
                cur = []
                items.append(cur)
            elif cur is not None:
                cur.append("<li>")
        elif cur is not None:
            cur.append(tok)
    return ["".join(x) for x in items if collapse("".join(x))]


def award_md(li):
    """Award item as a single line; a nested list becomes a ';'-joined tail."""
    m = re.search(r"<ul>(.*?)</ul>", li, re.S)
    if not m:
        return inline_md(li)
    head = inline_md(li[:m.start()])
    subs = [inline_md(s) for s in re.split(r"<li>", m.group(1))[1:] if collapse(s)]
    return head + " " + "; ".join(subs)


def convert_reviews():
    doc = content_section(read(os.path.join(HTML, "reviews.html")))
    secs = box_sections(doc)
    excerpts = home_review_excerpts()
    reviews, awards, distinctions = [], [], []
    for title, inner in secs:
        if title == "Other Reviews":
            for li in li_items(inner):
                text = inline_md(li)
                urls = re.findall(r'href="(http[^"]+)"', li)
                mu = re.search(r'href="(http[^"]+)"[^>]*>\s*review', li, re.I | re.S)
                url = mu.group(1) if mu else (urls[0] if urls else None)
                pub = date = reviewer = medium = None
                for key, fields in REVIEW_FIELDS.items():
                    if any(key in u for u in urls):
                        pub, date, reviewer, medium = fields
                        break
                else:
                    warn("review item without field mapping: %s" % text[:60])
                r = {"publication": pub, "date": date, "reviewer": reviewer, "url": url,
                     "medium": medium, "note_md": text, "excerpt_md": None,
                     "full_text": False}
                ex = excerpts.get(reviewer or "")
                if ex:
                    r["excerpt_md"] = ex["excerpt_md"]
                reviews.append(r)
        elif title == "Awards":
            awards = [award_md(li) for li in li_items(inner)]
        elif title == "Distinctions":
            distinctions = [inline_md(li) for li in li_items(inner)]
        else:
            # full review reproduced on the page (The London Times / THES)
            m = re.search(r"^(.*?)<br>\s*<b>(?:<a[^>]*>)?([^<]+)(?:</a>)?</b><br>(.*)$", inner.strip(), re.S)
            head, reviewer, rest = (m.group(1), m.group(2), m.group(3)) if m else ("", None, inner)
            date = re.search(r"([A-Z][a-z]+ \d{1,2}, \d{4})", collapse(re.sub(r"<[^>]+>", "", head)))
            ht = re.search(r'<font size="\+4"><b>(.*?)</b></font>', rest, re.S)
            body = re.sub(r'<font size="\+4"><b>.*?</b></font>', "", rest, flags=re.S)
            body = re.split(r"<hr", body)[0]
            reviews.insert(0, {"publication": title, "date": date.group(1) if date else None,
                               "reviewer": collapse(reviewer) if reviewer else None,
                               "url": None, "medium": "print",
                               "headline": collapse(htmlmod.unescape(ht.group(1))) if ht else None,
                               "note_md": None, "excerpt_md": html_to_md(body).strip(),
                               "full_text": True})
    # AI Magazine / AMM / JASSS / BCS excerpts from the home page that aren't
    # tied to an "Other Reviews" entry get added standalone.
    have = {r.get("reviewer") for r in reviews}
    for rev, ex in excerpts.items():
        if rev not in have:
            reviews.append({"publication": ex["heading"], "date": None, "reviewer": rev,
                            "url": None, "medium": None, "note_md": None,
                            "excerpt_md": ex["excerpt_md"]})
    dump_json(os.path.join(DATA, "reviews.json"),
              {"reviews": reviews, "awards": awards, "distinctions": distinctions})
    return {"reviews": len(reviews), "awards": len(awards), "distinctions": len(distinctions)}


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def dir_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            total += os.path.getsize(os.path.join(root, f))
    return total


def main():
    os.makedirs(DATA, exist_ok=True)
    os.makedirs(PAGES, exist_ok=True)
    print("legacy copy ...")
    legacy = copy_legacy()
    print("pages ...")
    pages = convert_pages()
    print("programs ...")
    programs = convert_programs()
    dump_json(os.path.join(DATA, "programs.json"), programs)
    print("glossary ...")
    nglossary = convert_glossary()
    print("toc ...")
    toc = convert_toc()
    print("figures (pdftocairo may take a while) ...")
    figs = convert_figures()
    print("quotes ...")
    quotes = convert_quotes()
    print("reviews ...")
    reviews = convert_reviews()
    site = {
        "title": "The Computational Beauty of Nature",
        "subtitle": "Computer Explorations of Fractals, Chaos, Complex Systems, and Adaptation",
        "author": "Gary William Flake",
        "source": SOURCE_NOTE,
        "source_path": SRC,
        "source_last_modified": "2002-11-30",
        "generated_by": "tools/convert.py",
        "legacy": {"path": "legacy/", "files": legacy["files"], "bytes": legacy["bytes"],
                   "excluded": ["figs/ (see figures/)", "*.tgz *.zip *.jar *.hqx archives"]},
        "pages": {"path": "data/pages/", "count": len(pages), "names": pages,
                  "skipped": ["index (splash page)", "fig1..fig19 (thumbnail grids; see figures.json)",
                              "glossary, glossary-A..Z (see glossary.json)",
                              "javasmall/javamed/javalarge (applet-only)"]},
        "programs": {"path": "data/programs.json", "count": len(programs)},
        "glossary": {"path": "data/glossary.json", "markdown": "data/glossary.md", "count": nglossary},
        "toc": {"path": "data/toc.json", "chapters": toc["chapters"],
                "postscript_pdf_pages": toc["postscript_pages"]},
        "figures": {"path": "data/figures.json", "count": figs["count"],
                    "captions_verified_in_pdf": figs["verified_in_pdf"],
                    "numbering_note": ("html/figs order = allfigs.lof order = book order; "
                                       "chapter numbering derived from per-chapter counts in "
                                       "master.lof (which is stale for figs 74-77) and verified "
                                       "against book/cbn.pdf text"),
                    "dirs": {"pdf": "figures/pdf/", "gif100": "figures/gif100/",
                             "svg": "figures/svg/", "thumb": "figures/thumb/"},
                    "conversion_failures": figs["failures"]},
        "quotes": {"path": "data/quotes.json", **quotes},
        "reviews": {"path": "data/reviews.json", **reviews},
        "warnings": report["warnings"],
    }
    dump_json(os.path.join(DATA, "site.json"), site)
    print(json.dumps({k: v for k, v in site.items() if k not in ("pages",)}, indent=1)[:3000])
    print("pages:", len(pages), "legacy size: %.1f MB" % (dir_size(LEGACY) / 1e6))


if __name__ == "__main__":
    main()
