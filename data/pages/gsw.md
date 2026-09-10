---
title: "GSW Documentation"
source: html/gsw.html
---

## Name

gsw - simulate a three species individual-based ecosystem

## Synopsis

```
gsw -help
  or
gsw    [-width integer] [-height integer] [-steps integer]
       [-seed integer] [-plants integer] [-herbs  integer]
       [-carns  integer]  [-pmin  integer] [-pmax integer]
       [-Ep integer]  [-Eh  integer]  [-Ec  integer]  [-Ch
       integer]  [-Cc  integer] [-Pt integer] [-samp inte-
       ger]  [-stats]  [-pfreq  integer]  [-noext]  [-inv]
       [-mag integer] [-term string]
```

## Description

The time evolution of an individual-based three species predator-prey ecosystem is simulated according to the specified parameters. The three species consist of plants, herbivores, and carnivores (grass, sheep, and wolves; hence the name GSW). Updates are done synchronously, and each species has several parameters which can control the life cycle, from the ability to give birth, to the likelihood of starvation. Population statistics of the three species can be calculated over a subset of the entire grid.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-steps` *integer* — Number of simulated steps.
- `-seed` *integer* — Random seed for initial state.
- `-plants` *integer* — Initial number of plants.
- `-herbs` *integer* — Initial number of herbivores.
- `-carns` *integer* — Initial number of carnivores.
- `-pmin` *integer* — Minimum plants in vicinity to make new plant.
- `-pmax` *integer* — Maximum allowed plants in vicinity to make new plant.
- `-Ep` *integer* — Energy of plant.
- `-Eh` *integer* — Energy of herbivore.
- `-Ec` *integer* — Energy of carnivore.
- `-Ch` *integer* — Step energy cost for herbivores.
- `-Cc` *integer* — Step energy cost for carnivores.
- `-Pt` *integer* — Number of steps to grow plant.
- `-samp` *integer* — Size of subsample statistaics.
- `-stats` — Show statistics?
- `-pfreq` *integer* — Plot frequency.
- `-noext` — Prevent extinction?
- `-inv` — Invert colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

An interesting change to this code would involve making the the updates asynchronous, which would avoid some subtle deadlock conditions that can occur in how the critters move. Moreover, the motion of the overall system would probably be more "lifelike".

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
