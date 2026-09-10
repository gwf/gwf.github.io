---
title: "CA Documentation"
source: html/ca.html
---

## Name

ca - simulate arbitrary one-dimensional cellular automata

## Synopsis

```
ca -help
  or
ca     [-width  integer]  [-height integer] [-states inte-
       ger]  [-radius  integer]  [-seed  integer]  [-wrap]
       [-rules  string]  [-init  string]  [-lambda double]
       [-sq] [-bin] [-inv] [-mag integer] [-term string]
```

## Description

Computes a one-dimensional cellular automata. The evolution of the CA is determined by the number of states, the radius size, the initial state, and the supplied rule. A rule is specified by a (states - 1) * (radius * 2 + 1) length string. At each time step a sum of each cell plus all of its neighbors within the radius is computed. That sum is used as an index into the rules string which determines the next step For example, with radius = 1 and states = 2 the rule that sums of 0 and 3 map to the 0 state, and sums of 1 and 2 map to the 1 state. A negative init string randomly initializes the starting states. If the init string is of being non-zero.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-states` *integer* — Number of CA states.
- `-radius` *integer* — Radius of CA neighborhood.
- `-seed` *integer* — Random seed.
- `-wrap` — Use a wrap-around space?
- `-rules` *string* — CA rules to use.
- `-init` *string* — Starting state (< 0 is random).
- `-lambda` *double* — Lambda value for random rules.
- `-sq` — Enforce strong quiescence?
- `-bin` — Binary colors?
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

When supplying a lambda value for a random rule, it may not be possible to find a string with that lambda value because one may not exist. In this case, the program will do its best to find one as close as possible. In any event, the algorithm for finding random rules strings for a specified lambda value is non-deterministic and may not always find a perfect match even if one exists. However, it will work well with high probability, and even when it doesn't find a perfect match it almost always gets close.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
