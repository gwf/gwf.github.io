---
title: "IFS Documentation"
source: html/ifs.html
---

## Name

ifs - generate fractals with an IFS

## Synopsis

```
ifs -help
  or
ifs    [-infile string] [-width integer] [-height integer]
       [-border integer] [-its  integer]  [-skip  integer]
       [-term string] [-inv] [-mag integer]
```

## Description

An affine fractal is computed via an Iterated Functional System. The rules must be supplied from a file with each line consisting of six values (A-F) such that the values of A-D describe a 2x2 matrix (A, B; C, D), while E and F describes a 2x1 column vector (E; F).

## Options

- `-infile` *string* — Data input file.
- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-border` *integer* — Number of pixels in border.
- `-its` *integer* — Number of iterations.
- `-skip` *integer* — Number of iteration to skip.
- `-term` *string* — How to plot points.
- `-inv` — Invert colors?
- `-mag` *integer* — Magnification factor.

## Miscellany

There is a shell script called 'ifscma' supplied with the source code that has a simple interface that allows you to reference sets of predefined rules by name. You may also wish to see the author's book, "The Computational Beauty of Nature," for some more examples.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

The maximum number of affine rules is determined by the constant MAXRULES, which you may need to adjust under exceptional circumstances.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
