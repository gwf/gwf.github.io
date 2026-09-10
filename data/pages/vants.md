---
title: "VANTS Documentation"
source: html/vants.html
---

## Name

vants - simulate a population of generalized virtual ants

## Synopsis

```
vants -help
  or
vants  [-width  integer]  [-height integer] [-num integer]
       [-rule string]  [-dense  double]  [-steps  integer]
       [-seed   integer]   [-inv]  [-mag  integer]  [-term
       string]
```

## Description

Simulate and plot a population of virtual ants (vants). The behavior of the vants is determined by a bit string with length equal to the number of states that each cell in the vants' grid world can take. If a vant walks on a cell in state S, then the vant turns right if the S'th bit of the rule string is 1 and left if it's 0. As it leaves the cell the vant changes the state of the old cell to (S + 1) % NUMSTATES.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-num` *integer* — Number of ants.
- `-rule` *string* — Rule string.
- `-dense` *double* — Density of random crud.
- `-steps` *integer* — Number of simulated steps.
- `-seed` *integer* — Random seed for initial state.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

It is definitely worthwhile to simulate multiple vants as the possible composite behavior of multiple vants is far

different than a single vant. In fact, multiple vants can invert the work of other vants, which yields interesting deconstructive behavior.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
