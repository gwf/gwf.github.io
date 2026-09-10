---
title: "HP Documentation"
source: html/hp.html
---

## Name

hp - simulate the hodgepodge machine

## Synopsis

```
hp -help
  or
hp     [-width  integer]  [-height integer] [-states inte-
       ger]  [-steps  integer]  [-seed  integer]   [-diag]
       [-wrap]  [-g  double]  [-k1  double]  [-k2  double]
       [-freq  integer]  [-inv]  [-mag   integer]   [-term
       string]
```

## Description

The time evolution of the hodgepodge machine is simulated and plotted according to the specified parameters. The neighborhood of a cell can optionally include or not include diagonal cells in a 3x3 area; Moreover, the neighborhood can also wrap around the edges so that the grid is topologically toroidal. With a proper choice of parameters, this system resembles the Belousov-Zhabotinsky reaction which forms self-perpetuating spirals in a lattice. See the RULES section of the manual pages or the source code for an explanation of how the cells change over time.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-states` *integer* — Number of cell states.
- `-steps` *integer* — Number of simulated steps.
- `-seed` *integer* — Random seed for initial state.
- `-diag` — Diagonal cells are neighbors?
- `-wrap` — Use a wrap-around space?
- `-g` *double* — Infection progression rate.
- `-k1` *double* — First weighting parameter.
- `-k2` *double* — Second weighting parameter.
- `-freq` *integer* — Plot frequency.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Rules

If each cell can be in one of N states (labelled 0 to n - 1), then cells in state 0 are ``healthy,'' cells in state n - 1 are ``ill,'' and all other cells are ``infected.''

Within a cell's neighborhood, let Nill, Ninf, and S, denote the number of ill cells, the number of infected cells, and the sum of the states of all neighbors plus this cell's state. The next state is determined by the three rules:

Healthy: floor( Ninf / k1 ) + floor( Nill / k2 )

Infected: floor( S / ( Ninf + 1 ) ) + g

Ill: magically becomes healthy, thus 0.

Where k1, k2, and g are the parameters specified by the command line options.

## Miscellany

If you move from (to) an 8 cell neighborhood to (from) a 4 cell neighborhood try dividing (multiplying) k1 and k2 by 2 to produce a similar time evolution that occurred with the previous neighborhood size.

For some reason, 4 cell neighborhoods seem to produce patterns with more spirals.

This simulation can be frustratingly slow at times, so you may wish to use the -freq option to cut down on the overhead of plotting the states.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is

given or implied.
