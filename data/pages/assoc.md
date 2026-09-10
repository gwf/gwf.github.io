---
title: "ASSOC Documentation"
source: html/assoc.html
---

## Name

assoc - retrieve associative memories

## Synopsis

```
assoc -help
  or
assoc  [-pfile  ...]   [-tfile  string]  [-local  integer]
       [-cut  double]  [-pprob  double]  [-noise   double]
       [-seed integer] [-steps integer] [-inv] [-mag inte-
       ger] [-term string]
```

## Description

Attempt to reconstruct a potentially corrupted image from a McCulloch-Pitts feedback neural network that acts as an associative memory. The weights of the network are determined via Hebb's rule after reading in multiple patterns. Weights can be pruned either by size, locality, or randomly.

## Options

- `-pfile` *...* — File with pattern to store.
- `-tfile` *string* — File with test pattern.
- `-local` *integer* — locality of permitted weights
- `-cut` *double* — Cutoff size for weights.
- `-pprob` *double* — Probability of random pruning.
- `-noise` *double* — Amount of noise for test case.
- `-seed` *integer* — Random seed for initial state.
- `-steps` *integer* — Number of time steps.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

All pattern files must be in the PBM file format. You can

request that multiple patterns be stored into the weights by using the -pfile option multiple time.

The dimensions of the stored patterns and the test pattern must be identical.

For weight pruning, the program first checks to see if a weight is "non-local" which means that for a weight that connects two neurons either the row indices or column indices differ by the amount greater than the value specified by the -local option. (If a value for local -local is zero, then all weights are used.) Next, the program prunes weights that are too small in size as specified by the -cut option. If a weights has not been removed at this stage, then it will still be pruned with probability as specified by the -pprob option.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
