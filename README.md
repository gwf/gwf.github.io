# cbn-site

A rebuild of the companion site for *The Computational Beauty of Nature*
(Gary William Flake, MIT Press 1998), with the live browser versions of the
book's programs as the front door.

    index.html        flake.org home: one live program per visit, with a
                      "what is this?" panel (book chapter, figures, glossary)
    demos/            the single-file canvas/WebGL programs
    excerpts/         rendered pages of a few short excerpts (data/excerpts.json);
                      the book PDF itself is never published
    site/             the book site (generated; do not edit by hand)
    data/             structured content: demos.json (hand written),
                      toc/figures/glossary/programs/quotes/reviews (converted)
    figures/          all 164 figures as SVG, PDF, GIF, and thumbnails
    legacy/           the 1998-2002 site, preserved as-is
    tools/            convert.py (legacy -> data), build.py (data -> site),
                      shot.js (headless screenshots)

Build: `python3 tools/convert.py && python3 tools/excerpts.py <path-to-cbn.pdf> && python3 tools/build.py`. Serve any way you
like; everything is static.
