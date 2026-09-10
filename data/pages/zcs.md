---
title: "ZCS Documentation"
source: html/zcs.html
---

## Name

zcs - run a zeroth level classifier system on a terrain

## Synopsis

```
zcs -help
  or
zcs    [-specs  string]  [-steps  integer] [-seed integer]
       [-size integer]  [-sinit  double]  [-lrate  double]
       [-drate  double]  [-trate  double]  [-crate double]
       [-mrate double]  [-grate  double]  [-cover  double]
       [-wild double] [-avelen integer] [-inv] [-mag inte-
       ger] [-term string]
```

## Description

Train a zeroth level classifier system (ZCS) to traverse a two-dimensional terrain, avoid obstacles, and find food with the implicit bucket brigade algorithm and a genetic algorithm. At the beginning of each step the ZCS is placed at a random location of it's world. It interacts with its environment until it finds food, which yields a reward. The simulation then restarts with the ZCS placed at a new random location. The progress of the ZCS is continuously plotted, while the statistics on the time to find food are calculated and displayed. At the end of the simulation the classifiers that make up the final ZCS are saved to a log file.

## Options

- `-specs` *string* — World specification file.
- `-steps` *integer* — Number of simulated trials.
- `-seed` *integer* — Random seed for initial state.
- `-size` *integer* — Population size.
- `-sinit` *double* — Initial classifier strength.
- `-lrate` *double* — BB learning rate.
- `-drate` *double* — BB discount rate.
- `-trate` *double* — Tax rate for strength reduce.
- `-crate` *double* — GA crossover rate.
- `-mrate` *double* — GA mutation rate.
- `-grate` *double* — GA invocation rate.
- `-cover` *double* — Covering factor.
- `-wild` *double* — Probability of # in cover.
- `-avelen` *integer* — Length of windowed average.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

The file format for the specifications files must contain the width and height of the world followed by the details of the world in ASCII format, where '.' is an empty cell, 'O' is a rock, and 'F' represent food. See any of the examples in the 'data' subdirectory of this distribution for more details.

The log file, 'zcs.log', contains one line per classifier with the condition string, the action string, and the strength of the classifier. The classifiers are sorted so the the strongest classifiers are printed first.

The ASCII output of the program shows the most recent, windowed average and the total average for the number of steps needed to find food.

## Hints

See the author's book, "The Computational Beauty of Nature," for more details.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is

given or implied.
