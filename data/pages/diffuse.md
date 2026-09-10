---
title: "DIFFUSE Documentation"
source: html/diffuse.html
---

## Name

diffuse - simulate diffusion limited aggregation

## Synopsis

```
diffuse -help
  or
diffuse
       [-width  integer]  [-height integer] [-levels inte-
       ger]  [-num  integer]  [-steps  integer]   [-invis]
       [-seed   integer]   [-inv]  [-mag  integer]  [-term
       string]
```

## Description

A special type of stochastic fractal is created by the random action of many particles. The fractal starts out as a single point seed that is fixed in position. Particles float about via a random walk. Whenever a floating particle moves adjacent to fixed particle the floating particles become frozen in place. In this way, the fractal gradually grows in size.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-levels` *integer* — Number of plot (gray) levels to use.
- `-num` *integer* — Number of floating particles.
- `-steps` *integer* — Number of simulated steps.
- `-invis` — Invisible particles?
- `-seed` *integer* — Random seed for initial state.
- `-inv` — Invert colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

Using invisible particle will make the simulation run much faster under interactive graphic terminals, especially X Windows.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
