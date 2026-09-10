---
title: "HENWARP Documentation"
source: html/henwarp.html
---

## Name

henwarp - warps a square into the phase space of the Henon system

## Synopsis

```
henwarp -help
  or
henwarp
       [-width  integer]  [-height  integer] [-swap] [-len
       integer] [-count integer] [-A double]  [-B  double]
       [-ulx  double]  [-uly  double] [-lly double] [-inv]
       [-mag integer] [-term string]
```

## Description

A square (initially centered about the origin) is transformed by the Henon system, which is described by the equation x(t+1) = A - x(t)^2 + B * x(t - 1), a fixed number of times according to the specified parameters.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-swap` — Swap the x and y axis.
- `-len` *integer* — Length of edge of square.
- `-count` *integer* — Number of transformations.
- `-A` *double* — Value of the A parameter.
- `-B` *double* — Value of the B parameter.
- `-ulx` *double* — Upper-left corner x-coordinate.
- `-uly` *double* — Upper-left corner y-coordinate.
- `-lly` *double* — Lower-left corner y-coordinate.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

You may wish to try this with a small length for the size of square and watch how the resulting plot changes as you slowly increase the value passed to the -count option starting at zero. The square will slowly spread out and converge to the attractor of the system.

The method for choosing the viewable region may seem counter-intuitive at first, but it has some nice properties. In particular, selecting the exact (x, y) coordinates for the upper-left corner and only selecting the lower right y coordinate forces both the x and y scales to be identical since all scales are uniquely determined by these values along with the plot width and height. If you then change the width or height of the plot, the relative scales will still match up. The options for making a box work similarly.

## Bugs

The length of the square is in pixels and works best if it is an odd value. With even numbered values it can produce a gap in the plot for small values supplied with the -count option.

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
