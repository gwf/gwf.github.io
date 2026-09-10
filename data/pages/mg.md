---
title: "MG Documentation"
source: html/mg.html
---

## Name

mg - plot the phase space of the Mackey-Glass system

## Synopsis

```
mg -help
  or
mg     [-width  integer] [-height integer] [-skip integer]
       [-points integer] [-delta integer]  [-tau  integer]
       [-A  double]  [-B double] [-dt double] [-x0 double]
       [-factor  double]  [-data]  [-inv]  [-mag  integer]
       [-term string]
```

## Description

The phase space of the Mackey-Glass system, which is described by the delay differential equation

dx(t)/dt = A * x(t-Tau) / (1 + x(t-Tau)^10) - B * x(t),

is plotted according to the specified parameters. The xcoordinate of the plot is determined by x(t) while the ycoordinate is determined by x(t-delta).

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-skip` *integer* — Number of initial points to skip.
- `-points` *integer* — Number of points to plot.
- `-delta` *integer* — Time steps to delay for.
- `-tau` *integer* — Value of the Tau parameter.
- `-A` *double* — Value of the A parameter.
- `-B` *double* — Value of the B parameter.
- `-dt` *double* — Time step size.
- `-x0` *double* — Initial X value.
- `-factor` *double* — Auto-scale expansion factor.
- `-data` — Don't plot, but print points.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

The plot region is determined by the points that are initially skipped. If this number is too small (i.e., it is not very representative of the range of the plotted values), then you may need to increase the number specified by the -skip option. Alternatively, you can adjust the value given to -factor, which simply fractionally increases the border of the plot.

The program uses a second-order Euler's method to perform the numerical integration, which is sufficient for simple tasks such as this.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
