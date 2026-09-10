---
title: "BOIDS Documentation"
source: html/boids.html
---

## Name

boids - simulate a flock of android birds from Brooklyn

## Synopsis

```
boids -help
  or
boids  [-width  integer]  [-height integer] [-num integer]
       [-steps integer] [-seed  integer]  [-angle  double]
       [-vangle  double]  [-rcopy  double] [-rcent double]
       [-rvoid double]  [-rviso  double]  [-wcopy  double]
       [-wcent  double]  [-wvoid  double]  [-wviso double]
       [-wrand double] [-dt double] [-ddt  double]  [-minv
       double] [-len integer] [-psdump] [-inv] [-mag inte-
       ger] [-term string]
```

## Description

Simulate a flock of boids according to rules that determine their individual behaviors as well as the ``physics'' of their universe. A boid greedily attempts to apply four rules with respect to its neighbors: it wants to fly in the same direction, be in the center of the local cluster of boids, avoid collisions with boids too close, and maintain a clear view ahead by skirting around others that block its view. Changing these rules can make the boids behave like birds, gnats, bees, fish, or magnetic particles. See the RULES section of the manual pages for more details.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-num` *integer* — Number of boids.
- `-steps` *integer* — Number of simulated steps.
- `-seed` *integer* — Random seed for initial state.
- `-angle` *double* — Number of viewing degrees.
- `-vangle` *double* — Visual avoidance angle.
- `-rcopy` *double* — Radius for copy vector.
- `-rcent` *double* — Radius for centroid vector.
- `-rvoid` *double* — Radius for avoidance vector.
- `-rviso` *double* — Radius for visual avoidance vector.
- `-wcopy` *double* — Weight for copy vector.
- `-wcent` *double* — Weight for centroid vector.
- `-wvoid` *double* — Weight for avoidance vector.
- `-wviso` *double* — Weight for visual avoidance vector.
- `-wrand` *double* — Weight for random vector.
- `-dt` *double* — Time-step increment.
- `-ddt` *double* — Momentum factor (0 < ddt < 1).
- `-minv` *double* — Minimum velocity.
- `-len` *integer* — Tail length.
- `-psdump` — Dump PS at the very end?
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Rules

All of the rules have a weight option and a radius option. The radius option specifies how close a boid need to be to another in order for the rule to be acted upon. The weight is used when combining all of the rules actions into a single new velocity vector.

The four rules can be simply described as follows:

Centering: move towards the center of any boids in my viewing area.

Copying: attempt to move in the average direction of that all boids that can be seen are moving in.

Avoidance: ``Please don't stand so close to me.'' Move away from any close flyers.

Visual: move in such a way that the bonehead obstructing your view no longer interferes.

The four rules are then normalized and added together to make the next velocity vector of the boid. All radii in the rules are in terms of pixels.

You may wish to try turning on and off different combinations of the rules to see how the boids' behaviors change. For example, if you turn off the avoidance rule, increase the centering radius and weight, and increase the viewing angle to nearly 360 degrees, then the boids will behave like a pack of wolves fighting over the center. Other changes can yield similar surprises.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
