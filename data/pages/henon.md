---
title: "HENON Documentation"
source: html/henon.html
---

## Name

henon - plot the phase space of the Henon system

## Synopsis

```
henon -help
  or
henon  [-width  integer] [-height integer] [-skip integer]
       [-swap] [-points integer] [-delay integer] [-A dou-
       ble]  [-B double] [-ulx double] [-uly double] [-lly
       double] [-box integer] [-bulx double]  [-buly  dou-
       ble]  [-blly  double] [-data] [-inv] [-mag integer]
       [-term string]
```

## Description

The phase space of the Henon system, which is described by the equation x(t+1) = A - x(t)^2 + B * x(t - 1), is plotted according to the specified parameters.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-skip` *integer* — Number of initial points to skip.
- `-swap` — Swap the x and y axis?
- `-points` *integer* — Number of points to plot.
- `-delay` *integer* — Time steps to delay for.
- `-A` *double* — Value of the A parameter.
- `-B` *double* — Value of the B parameter.
- `-ulx` *double* — Upper-left corner x-coordinate.
- `-uly` *double* — Upper-left corner y-coordinate.
- `-lly` *double* — Lower-left corner y-coordinate.
- `-box` *integer* — Line width for a box.
- `-bulx` *double* — Box's upper-left x-coordinate.
- `-buly` *double* — Box's upper-left y-coordinate.
- `-blly` *double* — Box's lower-left y-coordinate.
- `-data` — Don't plot, but print points.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

The method for choosing the viewable region may seem counter-intuitive at first, but it has some nice properties. In particular, selecting the exact (x, y) coordinates for the upper-left corner and only selecting the lower right y coordinate forces both the x and y scales to be identical since all scales are uniquely determined by these values along with the plot width and height. If you then change the width or height of the plot, the relative scales will still match up. The options for making a box work similarly.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
