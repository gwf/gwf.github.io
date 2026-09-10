---
title: "HENCON Documentation"
source: html/hencon.html
---

## Name

hencon - control the Henon system with the OGY control law

## Synopsis

```
hencon -help
  or
hencon [-points integer]  [-on1  integer]  [-off  integer]
       [-on2  integer]  [-skip  integer]  [-seed  integer]
       [-plimit double] [-A double]  [-B  double]  [-gauss
       double]
```

## Description

Control the Henon system, x(t+1) = A - x(t)^2 + B * x(t - 1), with the OGY control law for arbitrary choices of A and B. The control law is analytically calculated based on the system parameters. The user can select times in which control is turned on and off so that time-to-control and transients can be observed. Gaussian noise can also be injected into the system. The control timing options are constrained to obey (0 <= on1 <= off <= on2 <= points).

## Options

- `-points` *integer* — The length of the time series.
- `-on1` *integer* — Where to turn control on.
- `-off` *integer* — Where to turn control off.
- `-on2` *integer* — Where to turn control on again.
- `-skip` *integer* — Amount to skip initially.
- `-seed` *integer* — Random seed.
- `-plimit` *double* — Largest allowed size for p.
- `-A` *double* — Value of the A parameter.
- `-B` *double* — Value of the B parameter.
- `-gauss` *double* — Magnitude of Gaussian noise.

## Bugs

Few sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
