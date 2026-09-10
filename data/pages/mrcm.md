---
title: "MRCM Documentation"
source: html/mrcm.html
---

## Name

mrcm - generate fractals with the MRCM algorithm

## Synopsis

```
mrcm -help
  or
mrcm   [-infile string] [-width integer] [-height integer]
       [-depth integer]  [-border  integer]  [-bw  double]
       [-bh double] [-L] [-term string] [-inv] [-mag inte-
       ger]
```

## Description

An affine fractal is computed via the Multiple Reduction Copy Machine Algorithm. The rules must be supplied from a file with each line consisting of six values (A-F) such that the values of A-D describe a 2x2 matrix (A, B; C, D), while E and F describes a 2x1 column vector (E; F).

## Options

- `-infile` *string* — Data input file.
- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-depth` *integer* — Depth of recursive calls.
- `-border` *integer* — Number of pixels in border.
- `-bw` *double* — Width of the seed box.
- `-bh` *double* — Height of the seed box.
- `-L` — Draw an 'L' in each box?
- `-term` *string* — How to plot points.
- `-inv` — Invert colors?
- `-mag` *integer* — Magnification factor.

## Miscellany

There is a shell script called 'ifscma' supplied with the source code that has a simple interface that allows you to reference sets of predefined rules by name. You may also

wish to see the author's book, "The Computational Beauty of Nature," for some more examples.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

The maximum number of affine rules is determined by the constant MAXRULES, which you may need to adjust under exceptional circumstances.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
