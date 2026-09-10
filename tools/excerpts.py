#!/usr/bin/env python3
"""Render the short book excerpts listed in data/excerpts.json to PNG pages
under excerpts/<id>/<n>.png.  The PDF stays outside the repo (see
source_pdf); only these rendered pages are published."""
import json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cfg = json.load(open(os.path.join(ROOT, "data", "excerpts.json")))
pdf = sys.argv[1] if len(sys.argv) > 1 else cfg["source_pdf"]
if not os.path.exists(pdf):
    sys.exit("source PDF not found: %s (pass the path as an argument)" % pdf)
out_root = os.path.join(ROOT, "excerpts")
for ex in cfg["excerpts"]:
    d = os.path.join(out_root, ex["id"]); os.makedirs(d, exist_ok=True)
    for p in range(ex["pages"][0], ex["pages"][1] + 1):
        target = os.path.join(d, "%d.png" % p)
        if os.path.exists(target): continue
        # Crop the printer's marks: the page box is 612x684 pt, the type area
        # sits inside about 54 pt of trim on each side.
        subprocess.check_call(["pdftocairo", "-png", "-r", "110", "-f", str(p), "-l", str(p), "-singlefile",
                               "-x", "83", "-y", "8", "-W", "770", "-H", "1000", pdf, target[:-4]])
    print(ex["id"], ex["pages"])
