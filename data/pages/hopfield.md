---
title: "HOPFIELD Documentation"
source: html/hopfield.html
---

## Name

hopfield - solve a task assignment problem via a Hopfield network

## Synopsis

```
hopfield -help
  or
hopfield
       [-specs  string]  [-dt double] [-tau double] [-gain
       double] [-scale  double]  [-seed  integer]  [-steps
       integer]  [-gray  integer]  [-inv]  [-mag  integer]
       [-term string]
```

## Description

Solve a task assignment problem via a Hopfield neural network while plotting the activations of the neurons over time. The program uses the K-out-of-N rule for setting the external inputs and synapse strength of the neurons.

## Options

- `-specs` *string* — Problem specification file.
- `-dt` *double* — Time step increment.
- `-tau` *double* — Decay term.
- `-gain` *double* — Sigmoidal gain.
- `-scale` *double* — Scaling for inputs.
- `-seed` *integer* — Random seed for initial state.
- `-steps` *integer* — Number of time steps.
- `-gray` *integer* — Number of gray levels.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Miscellany

As mentioned before, the weights and external inputs are

set according to the K-out-of-N rule which states that if we have N neurons in a mutually connected sub-network and that we wish this subset to converge with exactly K neurons activated, then each neuron should be connected to every other neuron with a weights of -2 and receive an external input of (2K - 1). Since we must produce solutions that look like permutation matrices, each neuron is in 2 K-out-of-N subsets, one for the column and one for the row. Thus, all neurons inhibit all other neurons in the same column or row with -2 and must (on average) receive a net input of 2 since they are all in two sets. The external inputs are slightly adjusted to favor neurons that represent more productive task performers. See the source code for more details.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

The final cost of the solution is printed at the end of the simulation; however, no check is done to insure that the system has actually converged. Hence, it may print out nonsense results.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
