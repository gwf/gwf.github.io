---
title: "EIPD Documentation"
source: html/eipd.html
---

## Name

eipd - simulate the ecological iterated Prisoner's Dilemma

## Synopsis

```
eipd -help
  or
eipd   [-steps integer] [-rounds integer] [-seed  integer]
       [-CC double] [-CD double] [-DC double] [-DD double]
       [-Iallc  double]  [-Itft  double]  [-Irand  double]
       [-Ipav   double]   [-Ialld  double]  [-rcp  double]
       [-noise double]
```

## Description

The ecological iterated Prisoner's Dilemma is simulated over time according to the specified parameters. At every time step the population of each strategy is calculated as a function of the expected scores earned against all strategies weighted by the populations of the opponents. Possible strategies include 'Always Cooperate,' 'Always Defect,'

## Options

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

## Payoffs

The payoff matrix for the Prisoner's Dilemma game is usually expressed as: Player B's Move +-----------+-----------+ Player A's Move | cooperate | defect | +-----------+-----------+-----------+ | cooperate | CC, CC | CD, DC | +-----------+-----------+-----------+ | defect | DC, CD | DD, DD | +-----------+-----------+-----------+

where the table entries are (A's payoff, B's payoff) and CC, CD, DC, and DD are the reward, sucker, temptation, and punish payoffs, respectively. For each of these four outcomes you will probably want the payoffs to reflect the relationships:

(DC > CC > DD > CD) and ((CD + DC) / 2 < CC).

## Miscellany

random noise (via the -noise option) manifests itself as a cell making a randomly selected move in a single round. In this case, both the cell whose action was altered as well as that cell's opponents "remember" what the random move was on the next round.

During each time step, every strategy plays against every other strategy as well as against itself.

The initial population levels for all strategies will be normalized, so the scaling of the option values is irrelevant.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
