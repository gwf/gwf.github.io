---
title: "MLP Documentation"
source: html/mlp.html
---

## Name

mlp - train a multilayer perceptron with backprop

## Synopsis

```
mlp -help
  or
mlp    [-dfile  string]  [-steps  integer] [-seed integer]
       [-freq integer] [-numin integer] [-numhid  integer]
       [-numout  integer]  [-lrate double] [-mrate double]
       [-winit double] [-linout] [-pdump] [-gdump]
```

## Description

Train a multilayer perceptron with a single hidden layer of neurons on a set of data contained in a file using the backpropagation learning algorithm with momentum. Output units can be linear or sigmoidal, allowing you to model both discrete and continuous output target values.

## Options

- `-dfile` *string* — Training data file.
- `-steps` *integer* — Number of simulated steps.
- `-seed` *integer* — Random seed for initial state.
- `-freq` *integer* — Status print frequency.
- `-numin` *integer* — Number of inputs.
- `-numhid` *integer* — Number of hidden nodes.
- `-numout` *integer* — Number of outputs.
- `-lrate` *double* — Learning rate.
- `-mrate` *double* — Momentum rate.
- `-winit` *double* — Weight init factor
- `-linout` — Use linear outputs?
- `-pdump` — Dump patterns at end of run?
- `-gdump` — Dump gnuplot commands at end?

## Miscellany

The number of inputs and outputs must agree with the format of your training data file. The program expects to find training patterns listed one after another with each training pattern consisting of the inputs followed by the target outputs.

If the -pdump switch is used, then the patterns will printed to stdout. Hence,redirect this to a file if you want to save it.

You should always use linear outputs if your target values are continuous.

The error value displayed via stderr is the root mean squared error taken over the entire data step. Calculating this error measure is typically far more expensive than a single training step, so you may wish to use the -freq option to make it happen less frequently.

If you network doesn't converge to anything useful, try increasing the number of hidden nodes. Moreover, you may need to tweak the learning rate and momentum term. This is just one of the curses of backprop.

## Bugs

The -gplot switch isn't very useful as it only works on the first output neuron.

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
