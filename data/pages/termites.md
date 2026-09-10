---
title: "TERMITES Documentation"
source: html/termites.html
---

## Name

termite - simulate a population of termites

## Synopsis

```
termite -help
  or
termite
       [-width  integer]  [-height integer] [-num integer]
       [-dense double] [-steps  integer]  [-seed  integer]
       [-inv] [-mag integer] [-term string]
```

## Description

Simulate a population of termites which do a random walk while possibly carrying a wood chip. Under normal circumstances, the termites will self-organize and move the wood chips into piles without a global leader. The termites' behavior is dictated by the following set of rules: If a termite is not carrying anything and she bumps into a chip, then she picks it up, reverses direction, and continues with the random walk. If she is carrying a chip and bumps into another, she drops her chip, turns around, and starts walking again. Otherwise, she just does a random walk whether she is carrying a chip or not.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-num` *integer* — Number of termites in population.
- `-dense` *double* — Density of chips at start.
- `-steps` *integer* — Number of simulated steps.
- `-seed` *integer* — Random seed for initial state.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

The walking pattern of the termites is not actually a strict random walk. Instead, at each time step they

randomly turn -45, 0, or 45 degrees with equal probability.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
