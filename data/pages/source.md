---
title: "Computation"
source: html/source.html
---

The programs below are listed in the order in which they appear in the text.

# Computation

## [stutter](pages/stutter.md)

interprets simple lisp and only understands car, cdr, cons, if, set, equal, quote, and lambda, but is still Turing-complete. Uses stop-and-copy garbage collection and has an adjustable heap size. Examples that implement integer and floating-point arithmetic are provided. There is even an example **stutter** function to compute the square root of a floating-point argument with nothing but the primitives listed above.

# Fractals

## [diffuse](pages/diffuse.md)

Generates diffusion limited aggregate growth that looks like coral.

## [lsys](pages/lsys.md)

Builds L-system fractals. Accepts multiple rules so that complicated fractals (such as a Penrose tiling) can be expressed. Great for generating plantlike fractals.

## [mrcm](pages/mrcm.md)

Uses the Multiple Reduction Copy Machine algorithm to generate affine fractals. Accepts an arbitrary number of transformations. Good for making snowflakes and mosaic patterns.

## [ifs](pages/ifs.md)

Similar to **mrcm** but uses Iterated Functional Systems for finer granularity.

## [mandel](pages/mandel.md)

Plots the famous Mandelbrot set. There are options for the displayed coordinates, zoom level, coloring schemes, etc.

## [julia](pages/julia.md)

Generates Julia sets, which are related to the Mandelbrot set. Has options similar to **mandel**.

# Chaos

## [gen1d](pages/gen1d.md)

Generates a time series from a one-dimensional map. Nothing fancy; it just shows how chaos can be seen in simple systems.

## [bifur1d](pages/bifur1d.md)

Plots a bifurcation diagram for a one-dimensional map to illustrate how a change in a single parameter can move a system from fixed-point behavior, to periodic, and finally to chaos. Different regions can be zoomed in on.

## [phase1d](pages/phase1d.md)

Plots the phase space and trajectories of a one-dimensional map. Showing trajectories in the phase space more clearly illustrates why fixed-points and limit cycles occur. This can also be used to show the exponential divergence of nearby trajectories.

## [henon](pages/henon.md)

Plots the phase space of the Hénon map, a two-dimensional system with a fractal shape. Different regions can be zoomed in on.

## [henbif](pages/henbif.md)

Plots a bifurcation diagram for the Hénon system. This is similar to **bifur1d** but shows that bifurcations apply to multidimensional systems as well.

## [henwarp](pages/henwarp.md)

Takes a square of a specified area and “warps” it a fixed number of times by the Hénon system. This illustrates the stretching and folding motion of chaotic systems as well as shows how points within an attractor's basin of attraction are eventually forced into a strange attractor.

## [lorenz](pages/lorenz.md)

Plots the phase space of the Lorenz system, a three-dimensional system described by differential equations with a fractal shape. Both plain phase-space plots and delayed state-space plots are possible.

## [rossler](pages/rossler.md)

Similar to **lorenz**, but uses the Rossler system.

## [mg](pages/mg.md)

Plots a two-dimensional embedding of the phase space of the Mackey-Glass system, a delay-differential system, with arbitrary parameters.

## [gsw](pages/gsw.md)

Simulates an individual-based three-species predator-prey ecosystem according to the specified parameters. The three species consist of plants, herbivores, and carnivores (grass, sheep, and wolves; hence the name, **gsw**). Updates are done synchronously, and each species has several parameters which can control their life cycles, from the ability to give birth, to the likelihood of starvation. Population statistics of the three species can be calculated over a subset of the entire grid.

## [predprey](pages/predprey.md)

Plots the phase space of a three-species predator-prey system (described by differential equations) which may be fractal in shape. Both plain phase-space plots and delayed state-space plots are possible.

## [lotka](pages/lotka.md)

Simulates the two-species Lotka-Volterra predator-prey system with a second-order Euler's method. This program serves as a simple introduction to differential equations.

## [hencon](pages/hencon.md)

Controls the Hénon system with the OGY control law for arbitrary choices of the system parameters. The control law is analytically calculated based on the system parameters. The user can select times in which control is turned on and off so that time-to-control and transients can be observed. Gaussian noise can be injected into the system.

# Complex Systems

## [ca](pages/ca.md)

Simulates arbitrary one-dimensional cellular automata with an arbitrary choice of simulation parameters. Random rules can be generated and used with a desired lambda value.

## [life](pages/life.md)

Simulates Conway's Game of Life with an arbitrary set of initial conditions. Input files need to be in the PBM file format.

## [hp](pages/hp.md)

Simulates and plots the time evolution of the hodgepodge machine according to specified parameters. With a proper choice of parameters, this system resembles the Belousov-Zhabotinsky reaction which forms self-perpetuating spirals in a lattice.

## [termites](pages/termites.md)

Simulates a population of termites which do a random walk while possibly carrying a wood chip. Under normal circumstances, the termites will self-organize and move the wood chips into piles without a global leader. The termites' behavior is dictated by the following set of rules: If a termite is not carrying anything and it bumps into a chip, then it picks it up, reverses direction, and continues with the random walk. If it is carrying a chip and bumps into another, it drops the chip, turns around, and starts walking again. Otherwise, it just does a random walk whether it is carrying a chip or not.

## [vants](pages/vants.md)

Simulates and plots a population of generalized virtual ants (vants). The behavior of the vants is determined by a bit string with length equal to the number of states that each cell in the vants' grid world can take. If a vant walks on a cell in state *s*, then the vant turns right if the *s*'th bit of the rule string is 1 and left if it is 0. As it leaves the cell the vant changes the state of the old cell to *(s + 1)* modulo the number of states.

## [boids](pages/boids.md)

Simulates a flock of boids according to rules that determine their individual behaviors as well as the “physics” of their universe. A boid greedily attempts to apply four rules with respect to its neighbors: It wants to fly in the same direction, be in the center of the local cluster of boids, avoid collisions with boids too close, and maintain a clear view ahead by skirting around others that block its view. Changing these rules can make the boids behave like birds, gnats, bees, fish, or magnetic particles.

## [sipd](pages/sipd.md)

Simulates and plots the spatial iterated Prisoner's Dilemma over time according to the specified parameters. Each cell in a grid plays a specific strategy against its eight neighbors for several rounds. At the end of the last round, each cell copies the strategy of its most successful neighbor, which is then used for the next time step. Possible strategies include “Always-Cooperate,” “Always-Defect”, “Random,” “Pavlov,” and “Tit-for-Tat.”

## [eipd](pages/eipd.md)

Simulates the ecological iterated Prisoner's Dilemma over time according to the specified parameters. At every time step the population of each strategy is calculated as a function of the expected scores earned against all strategies weighted by the populations of the opponents. Possible strategies include “Always-Cooperate,” “Always-Defect,” “Random,” “Pavlov,” and “Tit-for-Tat.”

# Adaptation

## [assoc](pages/assoc.md)

Attempts to reconstruct a corrupted image with a McCulloch-Pitts feedback neural network that acts as an associative memory. The weights of the network are determined via Hebb's rule after reading in multiple patterns. Weights can be pruned either by size, by locality, or randomly.

## [hopfield](pages/hopfield.md)

Solves a task assignment problem via a Hopfield neural network while plotting the activations of the neurons over time. The program uses the *k*-out-of-*n* rule for setting the external inputs and synapse strength of the neurons.

## [gastring](pages/gastring.md)

Uses a genetic algorithm to breed strings that match a user-specified target string. This program illustrates how GAs can perform a type of stochastic search in a space of discrete objects. Reproduction of strings entails crossover and mutation with strings being selected based on fitness.

## [gabump](pages/gabump.md)

Uses a genetic algorithm to find the maximum of a single-humped function that is centered at a user-specified location. This program serves as an example of how GAs can be used to optimize functions which take a floating-point argument.

## [gasurf](pages/gasurf.md)

Uses a genetic algorithm to find the maximum of a multi-humped function. This program serves as an example of how GAs can be used to optimize functions which take multiple floating-point arguments.

## [gatask](pages/gatask.md)

Uses a genetic algorithm to solve a task assignment problem with user-specified costs. This program illustrates how GAs can perform combinatorial optimization. Reproduction of strings entails special crossover and mutation operations which preserve constraints on the form of feasible solutions.

## [gaipd](pages/gaipd.md)

Uses a genetic algorithm to evolve iterated Prisoner's Dilemma (IPD) strategies according to user-specified constraints. This program illustrates how GAs can demonstrate coevolution since IPD strategies can only be successful within the context of their likely opponents.

## [zcs](pages/zcs.md)

Adapts a zeroth level classifier system (ZCS) with the implicit bucket brigade algorithm and a genetic algorithm so that the ZCS can traverse a two-dimensional terrain, avoid obstacles, and find food. At the beginning of each step the ZCS is placed at a random location of its world. It interacts with its environment until it finds food, which yields a reward. The simulation then restarts with the ZCS placed at a new random location. The progress of the ZCS is continuously plotted, while the statistics on the time to find food are calculated and displayed. At the end of the simulation the classifiers that make up the final ZCS are saved to a log file.

## [zcscup](pages/zcscup.md)

Trains a zeroth level classifier system (ZCS) to solve the cups problem with the implicit bucket brigade algorithm and a genetic algorithm. Solving this problem requires the ZCS to learn to remember important features from previous states, which makes this problem very challenging. The ZCS always starts in the same initial position. It interacts with its environment until it finds both cups, which (only at that point) yields a reward. The simulation then restarts with the ZCS placed at the original location. The progress of the ZCS is continuously plotted, while the statistics on the time to find both cups are calculated and displayed. At the end of the simulation the classifiers that make up the final ZCS are saved to a log file.

## [mlp](pages/mlp.md)

Trains a multilayer perceptron with a single hidden layer of neurons on a set of data contained in a file using the backpropagation learning algorithm with momentum. Output units can be linear or sigmoidal, allowing you to model both discrete and continuous output target values.
