---
title: "GASTRING Documentation"
source: html/gastring.html
---

## Name

gastring - breed strings with a genetic algorithm

## Synopsis

```
gastring -help
  or
gastring
       [-target  string]  [-size integer] [-steps integer]
       [-seed integer]  [-crate  double]  [-mrate  double]
       [-pbase double]
```

## Description

Use a genetic algorithm to breed strings that match a user-specified target string. This program illustrates how GAs can perform a type of stochastic search in a space of discrete objects. Reproduction of strings entails crossover and mutation with strings being selected based on fitness.

## Options

- `-target` *string* — Target string.
- `-size` *integer* — Population size.
- `-steps` *integer* — Number of generations.
- `-seed` *integer* — Random seed.
- `-crate` *double* — Crossover rate.
- `-mrate` *double* — Mutation rate.
- `-pbase` *double* — Power base for fitness.

## Miscellany

The fitness function works in three steps. First, the number of correct characters is tallied and denoted the raw fitness. The scaled fitness is then set to pow(PBASE, raw fitness - string len). The normalized fitness is then set to the scaled fitness divided by the sum of the scaled fitnesses. Thus the sum of the normalized fitnesses must be equal to one while a string with one letter more correct than another string is PBASE times as likely to reproduce, where PBASE is the value supplied with the -pbase option.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
