---
title: "HENBIF Documentation"
source: html/henbif.html
---

## Name

henbif - plot a bifurcation diagram for the Henon system

## Synopsis

```
henbif -help
  or
henbif [-width  integer] [-height integer] [-skip integer]
       [-abmin double] [-abmax double] [-ab]  [-A  double]
       [-B  double] [-factor double] [-ymin double] [-ymax
       double] [-box integer] [-brmin double] [-brmax dou-
       ble]  [-bymin  double] [-bymax double] [-inv] [-mag
       integer] [-term string]
```

## Description

A bifurcation diagram of the Henon system, which is described by the equation x(t+1) = A - x(t)^2 + B * x(t - 1), is plotted according to the specified parameters. Either of the parameters (A or B) can be varied in the plot.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-skip` *integer* — Number of initial points to skip.
- `-abmin` *double* — Smallest value for A (or B).
- `-abmax` *double* — Largest value for A (or B).
- `-ab` — If TRUE, plot for A; B otherwise.
- `-A` *double* — Value of the A parameter.
- `-B` *double* — Value of the B parameter.
- `-factor` *double* — Multiplicative factor for iterates.
- `-ymin` *double* — Smallest value for y range.
- `-ymax` *double* — Largest value for y range.
- `-box` *integer* — Line width for a box.
- `-brmin` *double* — Smallest r-value for the box.
- `-brmax` *double* — Largest r-value for the box.
- `-bymin` *double* — Smallest value for box y range.
- `-bymax` *double* — Largest value for box y range.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
