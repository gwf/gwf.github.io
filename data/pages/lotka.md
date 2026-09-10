---
title: "LOTKA Documentation"
source: html/lotka.html
---

## Name

predprey - integrate the Lotka-Volterra system

## Synopsis

```
predprey -help
  or
predprey
       [-seed integer] [-points integer] [-f0 double] [-s0
       double] [-a double] [-b  double]  [-c  double]  [-d
       double] [-dt double]
```

## Description

Integrates the two-species Lotka-Volterra predator-prey system,

dF/dt = F(a - bS), dS/dt = S(cF - d),

according to the specified parameters.

## Options

- `-seed` *integer* — Seed for random parameters.
- `-points` *integer* — Number of points to produce.
- `-f0` *double* — Initial fish population.
- `-s0` *double* — Initial shark population.
- `-a` *double* — Fish growth rate.
- `-b` *double* — Shark consumption rate.
- `-c` *double* — Fish nutritional value.
- `-d` *double* — Shark death rate.
- `-dt` *double* — Time step increment.

## Miscellany

The program uses a second-order Euler's method to perform the numerical integration, which is sufficient for simple tasks such as this.

## Bugs

No sanity checks are performed to make sure that any of

the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
