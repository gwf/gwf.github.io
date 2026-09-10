---
title: "SIPD Documentation"
source: html/sipd.html
---

## Name

sipd - simulate the spatial iterated Prisoner's Dilemma

## Synopsis

```
sipd -help
  or
sipd   [-width integer] [-height integer] [-steps integer]
       [-rounds integer] [-seed integer] [-CC double] [-CD
       double]  [-DC  double] [-DD double] [-Iallc double]
       [-Itft  double]  [-Irand  double]  [-Ipav   double]
       [-Ialld   double]  [-rcp  double]  [-noise  double]
       [-mute  double]  [-stats]  [-inv]  [-mag   integer]
       [-term string]
```

## Description

The spatial iterated Prisoner's Dilemma is simulated and plotted over time according to the specified parameters. Each cell in a grid plays a specific strategy against its eight neighbors for several rounds. At the end of the last round, each cell copies the strategy of its most succesful neighbor, which is then used for the next time step. Possible strategies include 'Always Cooperate,' 'Always Defect,'

## Options

- `-width` *integer* — Width of world.
- `-height` *integer* — Height of world.
- `-steps` *integer* — Number of steps to simulate.
- `-rounds` *integer* — Number of rounds per step.
- `-seed` *integer* — Random seed for initial state.
- `-CC` *double* — Reward Payoff.
- `-CD` *double* — Sucker Payoff.
- `-DC` *double* — Temptation Payoff.
- `-DD` *double* — Punish Payoff.
- `-Iallc` *double* — Initial population of All-C.
- `-Itft` *double* — Initial population of TFT.
- `-Irand` *double* — Initial population of Random.
- `-Ipav` *double* — Initial population of Pavlov.
- `-Ialld` *double* — Initial population of All-D.
- `-rcp` *double* — Probability of C for Random strategy.
- `-noise` *double* — Probability of noise.
- `-mute` *double* — Probability of mutation.
- `-stats` — Print statistics?
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Payoffs

The payoff matrix for the Prisoner's Dilemma game is usually expressed as: Player B's Move +-----------+-----------+ Player A's Move | cooperate | defect | +-----------+-----------+-----------+ | cooperate | CC, CC | CD, DC | +-----------+-----------+-----------+ | defect | DC, CD | DD, DD | +-----------+-----------+-----------+

where the table entries are (A's payoff, B's payoff) and CC, CD, DC, and DD are the reward, sucker, temptation, and punish payoffs, respectively. For each of these four outcomes you will probably want the payoffs to reflect the relationships:

(DC > CC > DD > CD) and ((CD + DC) / 2 < CC).

## Miscellany

The option for the probability of mutation (-mute) corresponds to the act of a cell spontaneously changing to a

randomly selected strategy independent of the outcome of the most recent set of rounds.

random noise (via the -noise option) manifests itself as a cell making a randomly selected move in a single round. In this case, both the cell whose action was altered as well as that cell's opponents "remember" what the random move was on the next round.

The value supplied with the -term option may be "none," in which case no graphic output is performed. This is useful if you simply want the statistics to be calculated for each time step (via the -stats option).

The initial population levels for all strategies will be normalized, so the scaling of the option values is irrelevant.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
