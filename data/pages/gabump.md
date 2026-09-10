---
title: "GABUMP Documentation"
source: html/gabump.html
---

## Name

gabump - find a bump's peak with a genetic algorithm

## Synopsis

```
gabump -help
  or
gabump [-target  double]  [-var  double]  [-size  integer]
       [-len  integer]  [-gens  integer]  [-seed  integer]
       [-crate double] [-mrate double]
```

## Description

Use a genetic algorithm to find the maximum of a singlehumped function that is centered at a user-specified location. This program serves as an example of how GAs can be used to optimize functions which take a floating point argument. Reproduction of strings entails crossover and mutation with strings being selected based on fitness.

## Options

- `-target` *double* — Target value for function.
- `-var` *double* — Variance of bump.
- `-size` *integer* — Population size.
- `-len` *integer* — DNA length.
- `-gens` *integer* — Number of generations.
- `-seed` *integer* — Random seed.
- `-crate` *double* — Crossover rate.
- `-mrate` *double* — Mutation rate.

## Miscellany

The bit strings are converted to floating point numbers with the formula (8 * int(string) / 2^len - 4) where int(string) is the integer value of a binary string. Thus, all numbers are forced to be between -4 and 4.

A more sophisticated GA encoding would use Gray codes to represent the floating point numbers which arguably are better behaved under mutation.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
