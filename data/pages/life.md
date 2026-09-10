---
title: "LIFE Documentation"
source: html/life.html
---

## Name

life - play Conway's Game of Life

## Synopsis

```
life -help
  or
life   [-width integer] [-height integer] [-extra integer]
       [-wrap] [-infile string]  [-steps  integer]  [-inv]
       [-mag integer] [-term string]
```

## Description

Simulate Conway's Game of Life with an arbitrary set of initial conditions. Input files need to be in the PBM file format.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-extra` *integer* — Number of extra border pixels.
- `-wrap` — Wrap around world?
- `-infile` *string* — Initial configuration file
- `-steps` *integer* — Number of time steps to simulate.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

You will need to use the -extra option in conjuction with the -wrap option if you wish to simulate moving objects that tend to fly off in one direction. Periodic patterns may need the -extra option to give them a little bit of extra room to work in.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Credits

The data files for the initial states supplied with this

program were lifted and converted from the excellent and free program xlife.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
