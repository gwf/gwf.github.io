---
title: "GATASK Documentation"
source: html/gatask.html
---

## Name

gatask - solve a task assignment problem via a genetic algorithm

## Synopsis

```
gatask -help
  or
gatask [-specs string]  [-size  integer]  [-gens  integer]
       [-seed  integer]  [-crate  double]  [-mrate double]
       [-pbase double]
```

## Description

Use a genetic algorithm to solve a task assignment problem with user-specified costs. This program illustrates how GAs can perform combinatorial optimization. Reproduction of strings entails special crossover and mutation operations which preserve constraints on the form of feasible solutions with strings being selected based on fitness.

## Options

- `-specs` *string* — Problem specification file.
- `-size` *integer* — Population size.
- `-gens` *integer* — Number of generations.
- `-seed` *integer* — Random seed.
- `-crate` *double* — Crossover rate.
- `-mrate` *double* — Mutation rate.
- `-pbase` *double* — Exponentiation base.

## Miscellany

Feasible solutions are represented as an array of LEN integers which must contain all integers between 0 and LEN - 1 to denote which person performs which task. As such, the mutation and crossover operators have to be subtly redefined so that candidate solutions are still feasible after they are crossed and mutated.

For mutation, we simply swap two locations in a solution array.

Crossing two solutions is a little more complicated. Consult the source code to see how it's done in a manner that

preserves the feasibility of the two children while blending portions of each parent solution.

The fitness function works in three steps. First, the score of a solution is calculated and denoted the raw fitness. The scaled fitness is then set to pow(PBASE, raw fitness - worst raw fitness). The normalized fitness is then set to the scaled fitness divided by the sum of the scaled fitnesses. Thus the sum of the normalized fitnesses must be equal to one while a string with a raw score of one better than another string is PBASE times as likely to reproduce, where PBASE is the value supplied with the -pbase option.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
