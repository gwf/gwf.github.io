---
title: "PHASE1D Documentation"
source: html/phase1d.html
---

## Name

phase1d - plot phase-space of a one-dimensional map

## Synopsis

```
phase1d -help
  or
phase1d
       [-width  integer]  [-height integer] [-points inte-
       ger] [-skip integer] [-r double] [-aux double] [-x0
       double]   [-dx  double]  [-func  string]  [-arrows]
       [-inv] [-mag integer] [-term string]
```

## Description

A phase-space diagram is plotted for a one-dimensional map according to the specified options. If the option for -dx is non-zero, then two trajectories are plotted: one staring at x0, and the other starting at (x0 + dx). See the MAPS section of the manual page for details of what maps are supported. User defined maps can be added to the file maps1d.c, but you must recompile the program.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-points` *integer* — Number of points to plot.
- `-skip` *integer* — Number of points to skip.
- `-r` *double* — Value for r.
- `-aux` *double* — Auxiliary map parameter.
- `-x0` *double* — Initial value for x.
- `-dx` *double* — Difference for second trajectory.
- `-func` *string* — Map function to use (one of 'log', 'tent', 'sin', or 'gauss').
- `-arrows` — Show arrows to indicate directions?
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Maps

The following four one-dimensional maps are allowed:

Logistic Map: x(t+1) = 4 * r * x(t) * (1.0 - x(t))

Tent Map: x(t+1) = (x(t) <= 0.5) ? 2 * r * x(t) : 2r * (1.0 x(t))

Sine Map: x(t+1) = sin(x(t) * PI * aux * 2 * r) / 2 + 0.5

Gaussian Map: x(t+1) = r * exp(-aux * (x(t) - 0.5) * (x(t) - 0.5))

See the file "maps1d.c" to see how to add user-defined maps.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
