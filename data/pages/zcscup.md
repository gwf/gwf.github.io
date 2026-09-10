---
title: "ZCSCUP Documentation"
source: html/zcscup.html
---

## Name

zcscup - run a zeroth level classifier system on the cups problem

## Synopsis

```
zcscup -help
  or
zcscup [-specs  string]  [-steps  integer] [-seed integer]
       [-size integer]  [-sinit  double]  [-lrate  double]
       [-drate  double]  [-trate  double]  [-crate double]
       [-mrate double]  [-grate  double]  [-cover  double]
       [-wild double] [-avelen integer] [-inv] [-mag inte-
       ger] [-term string]
```

## Description

Train a zeroth level classifier system (ZCS) to solve the cups problem with the implicit bucket brigade algorithm and a genetic algorithm. Solving this problem requires the ZCS to learn to remember important features from previous states, which makes this problem very challenging. The ZCS always starts in the same initial position. It interacts with its environment until it finds both cups, which (only at that point) yields a reward. The simulation then restarts with the ZCS placed at the original location. The progress of the ZCS is continuously plotted, while the statistics on the time to find both cups are calculated and displayed. At the end of the simulation the classifiers that make up the final ZCS are saved to a log file.

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

The file format for the specifications files must contain the width and height of the world followed by the details of the world in ASCII format, where '.' is an empty cell, 'O' is a wall, and 'F' represent a cup. See any of the examples in the 'data' subdirectory of this distribution for more details.

The log file, 'zcscup.log', contains one line per classifier with the condition string, the action string, and the strength of the classifier. The classifiers are sorted so the the strongest classifiers are printed first.

The ASCII output of the program shows the most recent, windowed average and the total average for the number of steps needed to find both cups.

## Hints

See the author's book, "The Computational Beauty of Nature," for more details.

## Bugs

The simulation always restarts with the ZCS location at position (0, 4), which really only makes sense for the data file to work around this or tweak the source code to try a different problem variation.

No sanity checks are performed to make sure that any of

the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
