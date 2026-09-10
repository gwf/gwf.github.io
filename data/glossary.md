# Glossary

_From The Computational Beauty of Nature (Gary William Flake, MIT Press 1998)._

## A

**<a id="activation"></a>Activation** — The time-varying value that is the output of a [neuron](#neuron).

**<a id="activation_function"></a>Activation Function** — A [function](#function) that translates a [neuron](#neuron)'s [net input](#net_input) to an [activation](#activation) value.

**<a id="adaptive"></a>Adaptive** — Subject to [adaptation](#adaptation); can change over time to improve fitness or accuracy.

**<a id="adaptation"></a>Adaptation** — An internal change in a [system](#system) that mirrors an external event in the system's [environment](#environment).

**<a id="affine"></a>Affine** — An equation that can be written in terms of [matrix](#matrix)-[vector](#vector) multiplication and vector addition.

**<a id="agent"></a>Agent** — See [Autonomous Agent](#autonomous_agent).

**<a id="ai"></a>AI** — An abbreviation for [Artificial Intelligence](#artificial_intelligence).

**<a id="algorithm"></a>Algorithm** — A detailed and unambiguous sequence of instructions that describes how a [computation](#computation) is to proceed and can be implemented as a [program](#program).

**<a id="algorithmic_complexity"></a>Algorithmic Complexity** — The size of the smallest [program](#program) that can produce a particular sequence of numbers. Regular patterns have low algorithmic complexity and [random](#random/randomness) sequences have high algorithmic complexity.

**<a id="always_cooperate"></a>Always Cooperate** — A [Prisoner's Dilemma](#prisoners_dilemma) [strategy](#strategy) that cooperates with its opponent under all circumstances (the exact opposite of [always defect](#always_defect)).

**<a id="always_defect"></a>Always Defect** — A [Prisoner's Dilemma](#prisoners_dilemma) [strategy](#strategy) that never cooperates with its opponent under any circumstance (the exact opposite of [always cooperate](#always_cooperate)).

**<a id="analog"></a>Analog** — Having a [continuous](#continuous) value.

**<a id="analytical"></a>Analytical** — Can be symbolically represented in a closed form that does not require any of the complex aspects of a [program](#program) such as an [iterative](#iterate/iterative) sum.

**<a id="analytical_solution"></a>Analytical Solution** — An exact solution to a problem that can be calculated symbolically by manipulating equations (unlike a [numerical solution](#numerical_solution)).

**<a id="arms_race"></a>Arms Race** — Two or more species experience [adaptation](#adaptation) to one another in a [coevolutionary](#coevolution) manner. This often seen in [predator-prey systems](#predator-prey_system).

**<a id="artificial_intelligence"></a>Artificial Intelligence** — The science of making computers do interesting things that humans do effortlessly.

**<a id="artificial_life"></a>Artificial Life** — The study of life processes within the confines of a computer.

**<a id="associative_memory"></a>Associative Memory** — Memory that can be referenced by content, as opposed to location. [Hopfield networks](#hopfield_network) will act as associative memories when trained with the [Hebbian learning](#hebbian_learning) rule.

**<a id="asynchronous"></a>Asynchronous** — Describes events that occur independently of each other but on a similar time scale.

**<a id="attractor"></a>Attractor** — A characterization of the long-term behavior of a [dissipative](#dissipative_system) [dynamical system](#dynamical_system). Over long periods of time, the [state space](#state_space) of some [dynamical systems](#dynamical_system) will contract toward this region. Attractors may be [fixed points](#fixed_point), [periodic](#periodic), [quasiperiodic](#quasiperiodic), or [chaotic](#chaos/chaotic). They may also be [stable](#stable) or [unstable](#unstable).

**<a id="autonomous_agent"></a>Autonomous Agent** — An entity with limited perception of its [environment](#environment) that can process information to calculate an action so as to be goal-seeking on a local scale. A [boid](#boid) is an example of an autonomous agent.

**<a id="axiom"></a>Axiom** — A [statement](#statement) that is assumed to be true and can later be used along with [theorems](#theorem) to prove other theorems. Also, the starting configuration of an [L-System](#l-system).

## B

**<a id="backpropagation"></a>Backpropagation** — An [algorithm](#algorithm) for efficiently calculating the error [gradient](#gradient) of a [neural network](#neural_network_(nn)), which can then be used as the basis of [learning](#learning). Backpropagation is equivalent to the [delta rule](#delta_rule) for [perceptrons](#perceptron), but can also calculate appropriate [weight](#weight) changes for the [hidden layer](#hidden_layer) weights of a [multilayer perceptron](#multilayer_perceptron_(mlp)) by generalizing the notion of an error correction term. In the simplest case, backpropagation is a type of [steepest descent](#steepest_descent_(ascent)) in the [search space](#search_space) of the network weights, and it will usually [converge](#convergence) to a [local minimum](#local_minimum_(maximum)).

**<a id="basin_of_attraction"></a>Basin of Attraction** — A region of [state space](#state_space) in which all included states of a [dynamical system](#dynamical_system) ultimately lead into the [attractor](#attractor).

**<a id="bias"></a>Bias** — See [threshold](#threshold).

**<a id="bifurcation"></a>Bifurcation** — The splitting of a single mode of a [system](#system)'s behavior into two new modes. This usually occurs as a [function](#function) of a [continuously](#continuous) varying [control](#control) parameter. A cascade of bifurcations will usually precede the onset of [chaos](#chaos/chaotic).

**<a id="binary"></a>Binary** — Written in a form that uses only 0s and 1s. A [string](#string) of [bits](#bit).

**<a id="bit"></a>Bit** — The smallest unit of information; the answer to a yes/no question; the outcome of a coin toss; a 0 or a 1.

**<a id="boid"></a>Boid** — An [autonomous agent](#autonomous_agent) that behaves like a simplified bird but will display flocking patterns in the presence of other boids.

**<a id="boolean"></a>Boolean** — Taking only 0/1, true/false, yes/no values.

**<a id="bottom-up"></a>Bottom-Up** — A description that uses the lower-level details to explain higher-level patterns; related to [reductionism](#reductionism).

**<a id="brown_noise/brownian_motion"></a>Brown Noise/Brownian Motion** — A form of [randomness](#random/randomness) that is the result of cumulatively adding [white noise](#white_noise), to yield a [random walk](#random_walk) pattern.

**<a id="bucket_brigade_algorithm"></a>Bucket Brigade Algorithm** — A [learning](#learning) [algorithm](#algorithm) that is a method for adjusting the [strengths](#strength) of the [classifiers](#classifier) of a [classifier system](#classifier_system). “Winning” classifiers pay a portion of their earnings to other classifiers that assisted them in being activated, similar to an economic [system](#system).

**<a id="byte"></a>Byte** — Eight [bits](#bit). In programming, often used to store a single text character.

## C

**<a id="cantor_set"></a>Cantor Set** — A simple [fractal](#fractal) [set](#set) composed of an [uncountable infinity](#uncountable_infinity) of dust-like points, but that also has 0 measure (meaning that the sum width of all points is 0). The Cantor set is constructed by removing the middle third of a unit line segment, and then [recursively](#recursive) removing the middle third of any remaining line segments, for an infinite number of steps.

**<a id="cellular_automaton_(ca)"></a>Cellular Automaton (CA)** — A [discrete](#discrete) [dynamical system](#dynamical_system) that is composed of an array of cells, each of which behaves like a [finite-state automaton](#finite-state_automaton_(fsa)). All interactions are local, with the next state of a cell being a [function](#function) of the current state of itself and its neighbors. [Conway's Game of Life](#conways_game_of_life) is a CA.

**<a id="chaos/chaotic"></a>Chaos/Chaotic** — Irregular motion of a [dynamical system](#dynamical_system) that is [deterministic](#deterministic), [sensitive](#sensitivity) to initial conditions, and impossible to predict in the long term with anything less than an infinite and perfect representation of [analog](#analog) values.

**<a id="chomsky_hierarchy"></a>Chomsky Hierarchy** — Four classes of languages (or computing machines) that have increasing complexity: regular ([finite-state automata](#finite-state_automaton_(fsa))), context-free (push-down automata), context-sensitive (linear bounded automata), and [recursive](#recursive) ([Turing machines](#turing_machine)).

**<a id="classifier"></a>Classifier** — A rule that is part of a [classifier system](#classifier_system) and has a condition that must be matched before its [message](#message) (or action) can be posted (or effected). The [strength](#strength) of a classifier determines the likelihood that it can outbid other classifiers if more than one condition is matched.

**<a id="classifier_system"></a>Classifier System** — An [adaptive](#adaptive) [system](#system) similar to a [Post production system](#post_production_system) that contains many “if ... then” rules called [classifiers](#classifier). The state of the [environment](#environment) is encoded as a [message](#message) by a [detector](#detector) and placed on the [message list](#message_list) from which the condition portion of the classifiers can be matched. “Winning” classifiers can then post their own messages to the message list, ultimately forming a type of [computation](#computation) that may result in a message being translated into an action by an [effector](#effector). The [strengths](#strength) of the classifiers are modified by the [bucket brigade](#bucket_brigade_algorithm) [algorithm](#algorithm), and new rules can be introduced via a [genetic algorithm](#genetic_algorithm_(ga)).

**<a id="coevolution"></a>Coevolution** — Two or more entities experience [evolution](#evolution) in response to one another. Due to [feedback](#feedback) mechanisms, this often results in a biological [arms race](#arms_race).

**<a id="complement"></a>Complement** — A [set](#set) composed of all elements that are not members of another set.

**<a id="combinatorial_optimization"></a>Combinatorial Optimization** — A class of problems in which the number of candidate solutions is combinatorial in size. Each possible solution has an associated cost. The goal is to find the solution with the lowest cost. Because of the vast numbers involved, explicit [search](#search/search_method) an entire [search space](#search_space) is not always possible.

**<a id="complete"></a>Complete** — Describes a [formal system](#formal_system) in which all [statements](#statement) can be proved as being true or false. Most interesting formal systems are not complete, as proved in [Gödel's Incompleteness Theorem](#gödels_incompleteness_theorem).

**<a id="complex_number"></a>Complex Number** — A number that has a [real](#real_number) component and an [imaginary](#imaginary_number) component and is characterized as a point on a plane (instead of the [real number](#real_number) line).

**<a id="complex_system"></a>Complex System** — A collection of many simple [nonlinear](#nonlinear) units that operate in [parallel](#parallel/parallelism) and interact locally with each other so as to produce [emergent](#emergent) behavior.

**<a id="complexity"></a>Complexity** — An ill-defined term that means many things to many people. Complex things are neither [random](#random/randomness) nor regular, but hover somewhere in between. Intuitively, complexity is a measure of how interesting something is. Other types of complexity may be well defined; see the index for other references.

**<a id="compressible"></a>Compressible** — Having a description that is smaller than itself; not [random](#random/randomness); possessing regularity.

**<a id="computable"></a>Computable** — Expressible as a yes/no question that can be answered in any case by a computer in finite time.

**<a id="computation"></a>Computation** — The realization of a [program](#program) in a computer.

**<a id="connectivity"></a>Connectivity** — The amount of interaction in a [system](#system), the structure of the [weights](#weight) in a [neural network](#neural_network_(nn)), or the relative number of edges in a [graph](#graph).

**<a id="conservative_system"></a>Conservative System** — A [dynamical system](#dynamical_system) that preserves the volume of its [state space](#state_space) under motion and, therefore, does not display the types of behavior found in [dissipative systems](#dissipative_system).

**<a id="consistence"></a>Consistence** — In [formal systems](#formal_system), having the property that all [statements](#statement) are either true or false.

**<a id="continuous"></a>Continuous** — Taking a [real](#real_number) value, i.e., not [discrete](#discrete). [Dynamical systems](#dynamical_system) may operate in continuous time or space.

**<a id="control"></a>Control** — Exerting actions to manipulate a [system](#system) or [environment](#environment) in a goal-seeking manner.

**<a id="convergence"></a>Convergence** — For computers, halting with an answer; for [dynamical systems](#dynamical_system), falling into an [attractor](#attractor); for [searches](#search/search_method) (e.g., [backpropagation](#backpropagation) and [genetic algorithms](#genetic_algorithm_(ga))), finding a location that cannot be improved upon; for infinite summations, approaching a definite value.

**<a id="conways_game_of_life"></a>Conway's Game of Life** — A [cellular automaton](#cellular_automaton_(ca)) rule set that operates on a two-dimensional grid. Each cell changes its state according to the states of its eight nearest neighbors: dead cells come alive with exactly three live neighbors, and cells die if they have anything but two or three neighbors. The Game of Life can display complex patterns such as [gliders](#glider), [fish](#fish), and [glider guns](#glider_gun), and is also capable of [universal computation](#universal_computation).

**<a id="co-recursively_enumerable_(co-re)"></a>Co-Recursively Enumerable (CO-RE)** — The [complement](#complement) of a [set](#set) that can be [recursively enumerated](#recursively_enumerable_(re)).

**<a id="countable_infinity"></a>Countable Infinity** — Having the same number of objects as the [set](#set) of [natural numbers](#natural_number).

**<a id="crossover"></a>Crossover** — A genetic operator that splices information from two or more parents to form a composite offspring that has genetic material from all parents.

## D

**<a id="darwinism"></a>Darwinism** — The theory of [evolution](#evolution) as proposed by Charles Darwin, which combined [variation](#variation) of [inheritable](#inheritable) traits with [natural selection](#natural_selection). After the discovery of the physical mechanism of genetics, this was further refined into [neo-Darwinism](#neo-darwinism).

**<a id="delta_rule"></a>Delta Rule** — The [perceptron](#perceptron) [learning](#learning) rule that specifies that [weight](#weight) changes should be proportional to the product of a weight's input and the error (or delta) term for the perceptron.

**<a id="derivative"></a>Derivative** — An expression that characterizes how the output of a [function](#function) changes as the input is varied. Unlike [integrals](#integral), derivatives can be calculated in an [analytical](#analytical) manner very easily.

**<a id="decision_problem"></a>Decision Problem** — A problem in which all questions take the form “Is something a member of a particular [set](#set)?” and all answers are either “yes” or “no.”

**<a id="detector"></a>Detector** — A sensor that translates the state of a [classifier](#classifier)'s [environment](#environment) into a [message](#message) that is suitable for posting to the [message list](#message_list) of the [classifier system](#classifier_system).

**<a id="determinant"></a>Determinant** — A quantity of a [matrix](#matrix) that characterizes the amount of expansion or contraction that the matrix inflicts on a [vector](#vector) when that vector is multiplied by the matrix.

**<a id="deterministic"></a>Deterministic** — Occurring in a non-[random](#random/randomness) manner such that the next state of a [system](#system) depends only on prior states of the system or the [environment](#environment). Perfect knowledge of previous states implies perfect knowledge of the next state.

**<a id="diagonal_matrix"></a>Diagonal Matrix** — A [matrix](#matrix) that has 0 entries along all nondiagonal entries, i.e., only the main diagonal may have non-zero values.

**<a id="difference_equation"></a>Difference Equation** — An equation that describes how something changes in [discrete](#discrete) time steps. [Numerical solutions](#numerical_solution) to [integrals](#integral) are usually realized as difference equations.

**<a id="differential_equation"></a>Differential Equation** — A description of how something [continuously](#continuous) changes over time. Some differential equations can have an [analytical solution](#analytical_solution) such that all future states can be known without [simulation](#simulate/simulation) of the time evolution of the [system](#system). However, most can have a [numerical solution](#numerical_solution) with only limited accuracy.

**<a id="differentiation"></a>Differentiation** — The act of calculating a [derivative](#derivative); the inverse operation of calculating an [integral](#integral).

**<a id="diffusion_limited_aggregation"></a>Diffusion Limited Aggregation** — A type of [stochastic](#stochastic) [fractal](#fractal) formed by particles floating about in a [random](#random/randomness) manner until they stick to something solid.

**<a id="discrete"></a>Discrete** — Taking only non-[continuous](#continuous) values, e.g., [Boolean](#boolean) or [natural numbers](#natural_number).

**<a id="dissipative_system"></a>Dissipative System** — A [dynamical system](#dynamical_system) that contains internal friction that deforms the structure of its [attractor](#attractor), thus making motion such as [fixed points](#fixed_point), [limit cycles](#limit_cycle), [quasiperiodicity](#quasiperiodic), and [chaos](#chaos/chaotic) possible. Dissipative systems often have internal structure despite being far from [equilibrium](#equilibrium), like a whirlpool that preserves its basic form despite being in the midst of constant change.

**<a id="diverge"></a>Diverge** — For [algorithms](#algorithm) or computers, to run forever and never halt; for [iterative](#iterate/iterative) [systems](#system) (like the equations for the [Mandelbrot set](#mandelbrot_set)), reaching a state such that all future states explode in size.

**<a id="dot_product"></a>Dot Product** — The [inner product](#inner_product) of two [vectors](#vector).

**<a id="dynamical_system"></a>Dynamical System** — A [system](#system) that changes over time according to a set of fixed rules that determine how one state of the system moves to another state.

**<a id="dynamics/dynamical"></a>Dynamics/Dynamical** — Pertaining to the change in behavior of a [system](#system) over time.

## E

**<a id="ecology"></a>Ecology** — The study of the relationships and interactions between organisms and [environments](#environment).

**<a id="ecosystem"></a>Ecosystem** — A biological [system](#system) consisting of many organisms from different species.

**<a id="edge_of_chaos"></a>Edge of Chaos** — The hypothesis that many natural [systems](#system) tend toward [dynamical](#dynamics/dynamical) behavior that borders static patterns and the [chaotic](#chaos/chaotic) regime.

**<a id="effector"></a>Effector** — The part of a [classifier system](#classifier_system) that can translate [messages](#message) into actions that can manipulate a [system](#system) or an [environment](#environment).

**<a id="eigenvalue"></a>Eigenvalue** — The change in length that occurs when the corresponding [eigenvector](#eigenvector) is multiplied by its [matrix](#matrix).

**<a id="eigenvector"></a>Eigenvector** — A unit length [vector](#vector) that retains its direction when multiplied to the [matrix](#matrix) that it corresponds to. An (*n* * *n*) matrix can have as many as *n* unique eigenvectors, each of which will have its own [eigenvalue](#eigenvalue).

**<a id="embedding"></a>Embedding** — A method of taking a [scalar](#scalar) [time series](#time_series) and using delayed snapshots of the values at fixed time intervals in the past so that the [dynamics](#dynamics/dynamical) of the underlying [system](#system) can be observed as a [function](#function) of the previously observed states.

**<a id="emergent"></a>Emergent** — Refers to a property of a collection of simple subunits that comes about through the interactions of the subunits and is not a property of any single subunit. For example, the organization of an ant colony is said to “emerge” from the interactions of the lower-level behaviors of the ants, and not from any single ant. Usually, the emergent behavior is unanticipated and cannot be directly deduced from the lower-level behaviors. [Complex systems](#complex_system) are usually emergent.

**<a id="entropy"></a>Entropy** — A measure of a [system](#system)'s degree of [randomness](#random/randomness) or disorder.

**<a id="environment"></a>Environment** — If that which is under study is a [system](#system), then the rest of the world is the environment.

**<a id="equilibrium"></a>Equilibrium** — A state of a [system](#system) that, if not subjected to [perturbation](#perturbation), will remain unchanged.

**<a id="ergodic"></a>Ergodic** — The property of a [dynamical system](#dynamical_system) such that all regions of a [state space](#state_space) are visited with similar frequency and that all regions will be revisited (within a small proximity) if given enough time.

**<a id="euclidean"></a>Euclidean** — Pertaining to standard geometry, i.e., points, lines, planes, volumes, squares, cubes, triangles, etc.

**<a id="eulers_method"></a>Euler's Method** — The simplest method of obtaining a [numerical solution](#numerical_solution) of a [differential equation](#differential_equation). There are many other numerical techniques that are more accurate; however, an [analytical solution](#analytical_solution) (i.e., a closed form of an [integral](#integral)) is always preferred but not always possible.

**<a id="evolution"></a>Evolution** — A process operating on populations that involves [variation](#variation) among individuals, traits being [inheritable](#inheritable), and a level of [fitness](#fitness) for individuals that is a [function](#function) of the possessed traits. Over relatively long periods of time, the distribution of inheritable traits will tend to reflect the fitness that the traits convey to the individual; thus, evolution acts as a filter that selects fitness-yielding traits over other traits.

**<a id="evolutionary_stable_strategy_(ess)"></a>Evolutionary Stable Strategy (ESS)** — In [game theory](#game_theory) and biology, a [strategy](#strategy) that, when possessed by an entire population, results in an [equilibrium](#equilibrium) such that [mutation](#mutation) of the strategy can never result in an improvement for an individual. [Always Defect](#always_defect) is an ESS, while [Always Cooperate](#always_cooperate) is not.

**<a id="excitatory"></a>Excitatory** — Refers to a neural [synapse](#synapse) or [weight](#weight) that is positive such that activity in the source [neuron](#neuron) encourages activity in the connected neuron; the opposite of [inhibitory](#inhibitory).

**<a id="experimentation"></a>Experimentation** — One process by which scientists attempt to understand nature. A phenomenon is observed and/or manipulated so that changes in the phenomenon's state can be seen. The resulting data can be used to derive new [models](#model) of a process or to confirm an existing model. Experimentation is the complement of [theorization](#theorization). See also [simulation](#simulate/simulation).

**<a id="expert_system"></a>Expert System** — A special [program](#program) that resembles a collection of “if ... then” rules. The rules usually represent knowledge contained by a domain expert (such as a physician adept at diagnosis) and can be used to [simulate](#simulate/simulation) how a human expert would perform a task.

## F

**<a id="feedback"></a>Feedback** — A loop in information flow or in cause and effect.

**<a id="feedback_neural_network"></a>Feedback Neural Network** — A [neural network](#neural_network_(nn)) that has every [neuron](#neuron) potentially connected to every other neuron. The [activations](#activation) of all neurons are updated in [parallel](#parallel/parallelism) ([synchronous](#synchronous) or [asynchronous](#asynchronous) order), unlike a [feedforward](#feedforward_neural_network) or [recurrent neural network](#recurrent_neural_network).

**<a id="feedforward_neural_network"></a>Feedforward Neural Network** — A [neural network](#neural_network_(nn)) that is organized with separate layers of [neurons](#neuron). Connections in such a network are limited to one direction such that the [activations](#activation) of the input neurons are updated first, followed by any [hidden layers](#hidden_layer), and then finished with the outputs.

**<a id="feigenbaum_constant"></a>Feigenbaum Constant** — A constant number that characterizes when bump-like [maps](#map) such as the [logistic map](#logistic_map) will [bifurcate](#bifurcation).

**<a id="finite-state_automaton_(fsa)"></a>Finite-State Automaton (FSA)** — The simplest computing device. Although it is not nearly powerful enough to perform [universal computation](#universal_computation), it can recognize [regular expressions](#regular_expression). FSAs are defined by a state transition table that specifies how the FSA moves from one state to another when presented with a particular input. FSAs can be drawn as [graphs](#graph).

**<a id="fish"></a>Fish** — A simple object in [Conway's Game of Life](#conways_game_of_life) that swims vertically or horizontally.

**<a id="fitness"></a>Fitness** — A measure of an object's ability to reproduce viable offspring.

**<a id="fitness_landscape"></a>Fitness Landscape** — A representation of how [mutations](#mutation) can change the [fitness](#fitness) of one or more organisms. If high fitness corresponds to high locations in the landscape, and if changes in genetic material are mapped to movements in the landscape, then [evolution](#evolution) will tend to make populations move in an uphill direction on the fitness landscape.

**<a id="fixed_point"></a>Fixed Point** — A point in a [dynamical system](#dynamical_system)'s [state space](#state_space) that maps back to itself, i.e., the system will stay at the fixed point if it does not undergo a [perturbation](#perturbation).

**<a id="formal_system"></a>Formal System** — A mathematical formalism in which [statements](#statement) can be constructed and manipulated with logical rules. Some formal systems are built around a few basic [axioms](#axiom) (such as [Euclidean](#euclidean) geometry) and can be expanded with [theorems](#theorem) that can be deduced through [proofs](#proof).

**<a id="fractal"></a>Fractal** — An object with a [fractal dimension](#fractal_dimension). Fractals are [self-similar](#self-similar) and may be [deterministic](#deterministic) or [stochastic](#stochastic). See also [Cantor Set](#cantor_set), [Diffusion Limited Aggregation](#diffusion_limited_aggregation), [IFS](#ifs), [Julia Set](#julia_set), [L-Systems](#l-system), [MRCM](#mrcm), [Mandelbrot Set](#mandelbrot_set), and [Strange Attractor](#strange_attractor).

**<a id="fractal_dimension"></a>Fractal Dimension** — An extension of the notion of dimension found in [Euclidean](#euclidean) geometry. Fractal dimensions can be non-integer, meaning that objects can be “more than a line but less than a plane” and so on. There is more than one way of computing a fractal dimension, one common type being the Hausdorff-Besicovich dimension. Roughly speaking, a fractal dimension can be calculated as the quotient of the logarithm of the object's size and the logarithm of the measuring scale, in the limit as the scale approaches 0. Under this definition, standard Euclidean objects retain their original dimension.

**<a id="function"></a>Function** — A mapping from one space to another. This is usually understood to be a relationship between numbers. Functions that are [computable](#computable) can be calculated by a [universal computer](#universal_computer).

**<a id="function_approximation"></a>Function Approximation** — The task of finding an instance from a class of [functions](#function) that is minimally different from an unknown function. This is a common task for [neural networks](#neural_network_(nn)).

## G

**<a id="game_theory"></a>Game Theory** — A mathematical formalism used to study human games, economics, military conflicts, and biology. The goal of game theory is to find the optimal [strategy](#strategy) for one player to use when his opponent also plays optimally. A strategy may incorporate [randomness](#random/randomness), in which case it is referred to as a [mixed strategy](#mixed_strategy).

**<a id="gaussian"></a>Gaussian** — Normally distributed (with a bell-shaped curve) and having a [mean](#mean) at the center of the curve with tail widths proportional to the [standard deviation](#standard_deviation) of the data about the mean.

**<a id="generalized_delta_rule"></a>Generalized Delta Rule** — Another name for [backpropagation](#backpropagation).

**<a id="genetic_algorithm_(ga)"></a>Genetic Algorithm (GA)** — A method of [simulating](#simulate/simulation) the action of [evolution](#evolution) within a computer. A population of fixed-length [strings](#string) is evolved with a GA by employing [crossover](#crossover) and [mutation](#mutation) operators along with a [fitness](#fitness) [function](#function) that determines how likely individuals are to reproduce. GAs perform a type of [search](#search/search_method) in a [fitness landscape](#fitness_landscape).

**<a id="genetic_programming_(gp)"></a>Genetic Programming (GP)** — A method of applying simulated [evolution](#evolution) on [programs](#program) or program fragments. Modified forms of [mutation](#mutation) and [crossover](#crossover) are used along with a [fitness](#fitness) function.

**<a id="glider"></a>Glider** — A simple object in [Conway's Game of Life](#conways_game_of_life) that swims diagonally through the grid space.

**<a id="glider_gun"></a>Glider Gun** — An object in [Conway's Game of Life](#conways_game_of_life) that builds and emits [gliders](#glider), which can then be collided in purposeful ways to construct more complicated objects.

**<a id="global_minimum_(maximum)"></a>Global Minimum (Maximum)** — In a [search space](#search_space), the lowest (or highest) point of the surface, which usually represents the best possible solution in the space with respect to some problem.

**<a id="gödel_number"></a>Gödel Number** — A [natural number](#natural_number) computed via a [Gödelization](#gödelization) procedure that uniquely corresponds to a [string](#string).

**<a id="gödelization"></a>Gödelization** — A method for mapping arbitrary [strings](#string) to [natural numbers](#natural_number) such that the process is [one-to-one](#one-to-one) and [invertible](#invertible). The process usually exploits the properties of [prime numbers](#prime_number). Since Gödelization can be defined as a [computable](#computable) [function](#function), and since functions can be Gödelized, some functions (or [programs](#program)) can assert [statements](#statement) about other functions or programs, or themselves.

**<a id="gödels_incompleteness_theorem"></a>Gödel's Incompleteness Theorem** — Any sufficiently interesting [formal system](#formal_system) can express true [statements](#statement) for which there can be no [proof](#proof) in the original formal system.

**<a id="gödels_statement"></a>Gödel's Statement** — Given the formal [statement](#statement) “There does not exist any [proof](#proof) for the statement with [Gödel number](#gödel_number) *x* applied to *x*,” which has it own Gödel number, *g*, Gödel's statement paraphrased is “There does not exist a proof of the statement with Gödel number *g* applied to itself.” Gödel's statement is true, but cannot be proven true in the [formal system](#formal_system) in which it is constructed, which leads to [Gödel's Incompleteness Theorem](#gödels_incompleteness_theorem).

**<a id="gradient"></a>Gradient** — A [vector](#vector) of partial [derivatives](#derivative) of a [function](#function) that operates on vectors. Intuitively, the gradient represents the slope of a high-dimensional surface.

**<a id="graph"></a>Graph** — A construct that consists of many nodes connected with edges. The edges usually represent a relationship between the objects represented by the nodes. For example, if the nodes are cities, then the edges may have numerical values that correspond to the distances between the cities. A graph can be equivalently represented as a [matrix](#matrix).

## H

**<a id="halting_problem"></a>Halting Problem** — The problem of determining if a [program](#program) halts or doesn't halt on a particular input. This is an [incomputable](#incomputable) problem.

**<a id="halting_set"></a>Halting Set** — The [recursively enumerable](#recursively_enumerable_(re)) [set](#set) of [Gödel numbers](#gödel_number) that correspond to [programs](#program) that halt if given their own Gödel number as input.

**<a id="hebbian_learning"></a>Hebbian Learning** — A rule that specifies that the strength of a [synapse](#synapse) between two [neurons](#neuron) should be proportional to the product of the [activations](#activation) of the two neurons. cd

**<a id="hénon_map"></a>Hénon Map** — A [chaotic](#chaos/chaotic) [system](#system) (defined by the two equations *x(t+1) = a - x(t)^2 + b y(t)* and *y(t+1) = x(t)*) that has a [fractal](#fractal) [strange attractor](#strange_attractor) and operates in [discrete](#discrete) time.

**<a id="hidden_layer"></a>Hidden Layer** — In a [feedforward](#feedforward_neural_network) or [recurrent](#recursive) [neural network](#neural_network_(nn)), a layer of [neurons](#neuron) that is neither the input layer nor the output layer but is physically between the two.

**<a id="hill-climbing"></a>Hill-Climbing** — One of the simplest [search](#search/search_method) methods that attempts to find a [local maximum](#local_minimum_(maximum)) by moving in an uphill direction. It is related to [steepest ascent](#steepest_descent_(ascent)). Hill-climbing may use [gradient](#gradient) information, or [random](#random/randomness) sampling of nearby points, in order to estimate the uphill direction.

**<a id="holism"></a>Holism** — The idea that “the whole is greater than the sum of the parts.” Holism is credible on the basis of [emergence](#emergent) alone, since [reductionism](#reductionism) and [bottom-up](#bottom-up) descriptions of nature often fail to predict complex higher-level patterns. See also [top-down](#top-down).

**<a id="hopfield_network"></a>Hopfield Network** — A type of [feedback neural network](#feedback_neural_network) that is often used as an [associative memory](#associative_memory) or as a solution to a [combinatorial optimization](#combinatorial_optimization) problem.

## I

**<a id="ifs"></a>IFS** — An iterated functional system; it constructs a [fractal](#fractal) by [iterating](#iterate/iterative) a [vector](#vector) quantity through an [affine](#affine) equation that is [randomly](#random/randomness) selected on each iteration.

**<a id="imaginary_number"></a>Imaginary Number** — The square root of a negative number. The square root of -1 is often denoted as *i* for the purpose of writing out [complex numbers](#complex_number).

**<a id="implicit_parallelism"></a>Implicit Parallelism** — The idea that [genetic algorithms](#genetic_algorithm_(ga)) have an extra built-in form of [parallelism](#parallel/parallelism) that is expressed when a GA [searches](#search/search_method) through a [search space](#search_space). Implicit parallelism depends on the similarities and differences between individuals in the population. The theory posits that GAs process more [schemata](#schema/schemata) than there are [strings](#string) in a population, thus getting something of a free lunch. See also [no free lunch](#no_free_lunch_(nfl)).

**<a id="incomputable"></a>Incomputable** — Something that cannot be characterized by a [program](#program) that always halts. [Sets](#set) that are incomputable may be [recursively enumerable](#recursively_enumerable_(re)) (like the [halting set](#halting_set)), [co-recursively enumerable](#co-recursively_enumerable_(co-re)) (e.g., the halting set's [complement](#complement)), or [not recursively enumerable](#not_recursively_enumerable_(not-re)) (which, if also not CO-RE, is a [random](#random/randomness) set).

**<a id="incomputable_number"></a>Incomputable Number** — A [real number](#real_number) with an infinite decimal (or [binary](#binary)) expansion that cannot be enumerated by any [universal computer](#universal_computer).

**<a id="inheritable"></a>Inheritable** — Refers to a trait that can be genetically passed from parent to offspring.

**<a id="inhibitory"></a>Inhibitory** — Refers to a neural [synapse](#synapse) or [weight](#weight) that is negative such that activity in the source [neuron](#neuron) encourages inactivity in the connected neuron. The opposite of [excitatory](#excitatory).

**<a id="inner_product"></a>Inner Product** — For two [vectors](#vector) of the same dimensionality, the sum of the pairwise products of the two vector components.

**<a id="integral"></a>Integral** — The cumulative [continuous](#continuous) sum of a [function](#function). The integral of a [differential equation](#differential_equation) represents the future state of a [dynamical system](#dynamical_system); however, most integrals do not have an [analytical solution](#analytical_solution), which means that they may only have [numerical solutions](#numerical_solution), an admittedly inexact process.

**<a id="integration"></a>Integration** — The act of calculating an [integral](#integral), by either a [numerical](#numerical_solution) or an [analytical solution](#analytical_solution); the inverse operation of [differentiation](#differentiation).

**<a id="invertible"></a>Invertible** — A [function](#function) is invertible (with a unique inverse) if the output uniquely determines the input (i.e., it is [one-to-one](#one-to-one)) and the set of legal outputs is equal to the set of legal inputs. The function *x^2* is not strictly invertible, while *x^3* has an inverse. For operations the definition is slightly looser. While [integration](#integration) and [differentiation](#differentiation) are considered to be inverse operations, there are an infinite number of [integrals](#integral) that are valid results for integrating any function; thus, the process is not one-to-one.

**<a id="irrational_number"></a>Irrational Number** — A [real number](#real_number) that cannot be represented as a fraction.

**<a id="iterated_prisoners_dilemma"></a>Iterated Prisoner's Dilemma** — The [Prisoner's Dilemma](#prisoners_dilemma) game played in an [iterative](#iterate/iterative) manner for a number of rounds that is unknown to both players.

**<a id="iterate/iterative"></a>Iterate/Iterative** — Doing something repeatedly. Doing something repeatedly. Doing something repeatedly. Doing something repeatedly. Doing something repeatedly.

## J

**<a id="julia_set"></a>Julia Set** — A [set](#set) of [complex numbers](#complex_number) that do not [diverge](#diverge) if [iterated](#iterate/iterative) an infinite number of times via a simple equation. The points form an extremely complex [fractal](#fractal). There is an [uncountable infinity](#uncountable_infinity) of Julia sets, each of which corresponds to a particular complex number that appears as a constant in the iterative procedure. Julia sets are similar to [co-recursively enumerable](#co-recursively_enumerable_(co-re)) sets because only points that are not a members of the set can actually be identified as such. All of the Julia sets are related to the [Mandelbrot set](#mandelbrot_set).

## K

**<a id="koch_curve"></a>Koch Curve** — A [fractal](#fractal) curve that looks like the edge of a snowflake. It has no [derivative](#derivative) at any point.

## L

**<a id="lamarckism"></a>Lamarckism** — A method of heredity that does not apply to genetics but is applicable to social [adaptation](#adaptation). Lamarckism posits that acquired traits can be passed from parent to offspring.

**<a id="lambda_calculus"></a>Lambda Calculus** — A [model of computation](#model_of_computation) that is capable of [universal computation](#universal_computation). The [Lisp](#lisp) programming language was inspired by Lambda calculus.

**<a id="learning"></a>Learning** — A process of [adaptation](#adaptation) by which [synapses](#synapse), [weights](#weight) of [neural network](#neural_network_(nn))'s, [classifier](#classifier) [strengths](#strength), or some other set of adjustable parameters is automatically modified so that some objective is more readily achieved. The [backpropagation](#backpropagation) and [bucket brigade](#bucket_brigade_algorithm) [algorithms](#algorithm) are two types of learning procedures.

**<a id="life"></a>LIFE** — See [Conway's Game of Life](#conways_game_of_life).

**<a id="limit_cycle"></a>Limit Cycle** — A [periodic](#periodic) cycle in a [dynamical system](#dynamical_system) such that previous states are returned to repeatedly.

**<a id="linear"></a>Linear** — Having only a multiplicative factor. If *f(x)* is a linear [function](#function), then *f(a+b) = f(a) + f(b)* and *c f(x) = f(cx)* must both be true for all values of *a*, *b*, *c*, and *x*. Most things in nature are [nonlinear](#nonlinear).

**<a id="linearly_(in)separable"></a>Linearly (In)separable** — Two classes of points are linearly separable if a [linear](#linear) [function](#function) exists such that one class of points resides on one side of the hyperplane (defined by the linear function), and all points in the other class are on the other side. The [XOR](#xor) mapping defines two [sets](#set) of points that are linearly inseparable.

**<a id="lisp"></a>Lisp** — A programming language designed to manipulate lists that was inspired by [Lambda Calculus](#lambda_calculus) and was the inspiration for [Stutter](#stutter).

**<a id="local_minimum_(maximum)"></a>Local Minimum (Maximum)** — The bottom of a valley or the top of a peak; a point in a [search space](#search_space) such that all nearby points are either higher (for a minimum) or lower (for a maximum). In a [continuous](#continuous) search space, local minima and maxima have a 0 [gradient](#gradient) [vector](#vector). Note that this particular valley (or peak) may not necessarily be the lowest (or highest) location in the space, which is referred to as the [global minimum (maximum)](#global minimum (maximum)).

**<a id="logistic_map"></a>Logistic Map** — The simplest [chaotic](#chaos/chaotic) [system](#system) that works in [discrete](#discrete) time and is defined by the [map](#map) *x(t) = 4r x(t) (1-x(t))*. [Feigenbaum's constant](#feigenbaum_constant) was first identified for this map.

**<a id="lorenz_system"></a>Lorenz System** — A system of three [differential equations](#differential_equation) that was the first concrete example of [chaos](#chaos/chaotic) and a [strange attractor](#strange_attractor).

**<a id="lotka-volterra_system"></a>Lotka-Volterra System** — A two-species [predator-prey system](#predator-prey_system) that in its simplest form can display only [fixed points](#fixed_point) or [limit cycles](#limit_cycle). More complicated versions with three or more species can yield [chaos](#chaos/chaotic).

**<a id="l-system"></a>L-System** — A method of constructing a [fractal](#fractal) that is also a [model](#model) for plant growth. L-systems use an [axiom](#axiom) as a starting [string](#string) and [iteratively](#iterate/iterative) apply a set of [parallel](#parallel/parallelism) string substitution rules to yield one long string that can be used as instructions for drawing the fractal. One method of interpreting the resulting string is as an instruction to a [turtle graphics](#turtle_graphics) plotter. Many fractals, including the [Cantor set](#cantor_set), [Koch curve](#koch_curve), and [Peano curve](#peano_curve), can be expressed as an L-system.

## M

**<a id="mackey-glass_system"></a>Mackey-Glass System** — A delay [differential equation](#differential_equation) (dx/dt = (ax(t-tau))/(1 + x^10(t-tau)) - bx(t)) that can display a wide variety of behaviors via an adjustable delay term, tau. Even though this system generates a single [scalar](#scalar) [time series](#time_series), it can be extremely [chaotic](#chaos/chaotic) because its value at any time may depend on its entire previous history.

**<a id="mandelbrot_set"></a>Mandelbrot Set** — An extremely complex [fractal](#fractal) that is related to [Julia sets](#julia_set) in the way that it is constructed and by the fact that it acts as a sort of index to the Julia sets. Like the Julia sets, the Mandelbrot set is calculated via an [iterative](#iterate/iterative) procedure. Starting conditions that do not [diverge](#diverge) after an infinite number of iterations are considered to be inside the set. If, and only if, a [complex number](#complex_number) is in the Mandelbrot set, then the Julia set that uses that complex number as a constant will be connected; otherwise, the corresponding Julia set will be unconnected.

**<a id="map"></a>Map** — A [function](#function) that is usually understood to be [iterated](#iterate/iterative) in [discrete](#discrete) time steps.

**<a id="matrix"></a>Matrix** — A rectangular two-dimensional array of numbers that can be thought of as a [linear](#linear) operator on [vectors](#vector). Matrix-vector multiplication can be used to describe geometric transformations such as scaling, rotation, reflection, and translation. They can also describe the [affine](#affine) transformation used to construct [IFS](#ifs) and [MRCM](#mrcm) [fractals](#fractal).

**<a id="mean"></a>Mean** — The arithmetical average of a collection of numbers; the center of a [Gaussian](#gaussian) distribution.

**<a id="meme"></a>Meme** — A unit of cultural information that represents a basic idea that can be transferred from one individual to another, and subjected to [mutation](#mutation), [crossover](#crossover), and [adaptation](#adaptation).

**<a id="message"></a>Message** — The basic unit of information in a [classifier system](#classifier_system) that is stored in the [message list](#message_list). A message may correspond to an external state of an [environment](#environment) or an internal state of the classifier system.

**<a id="message_list"></a>Message List** — The portion of a [classifier system](#classifier_system) that retains information in the form of [messages](#message).

**<a id="mixed_strategy"></a>Mixed Strategy** — In [game theory](#game_theory), a [strategy](#strategy) that uses [randomness](#random/randomness) by employing different actions in identical circumstances with different [probabilities](#probability).

**<a id="model"></a>Model** — In the sciences, a model is an estimate of how something works. A model will usually have inputs and outputs that correspond to its real-world counterpart. An [adaptive](#adaptive) [system](#system) also contains an implicit model of its [environment](#environment) that allows it to change its behavior in anticipation of what will happen in the environment.

**<a id="model_of_computation"></a>Model of Computation** — An idealized version of a computing device that usually has some simplifications such as infinite memory. A [Turing machine](#turing_machine), the [lambda calculus](#lambda_calculus), and [Post production systems](#post_production_system) are all models of computation.

**<a id="monotonic"></a>Monotonic** — The property of a [function](#function) that is always strictly increasing or strictly decreasing, but never both. The [sigmoidal](#sigmoidal) [activation](#activation) function of a [multilayer perceptron](#multilayer_perceptron_(mlp)) is monotonically increasing.

**<a id="mrcm"></a>MRCM** — The Multiple Reduction Copy Machine [algorithm](#algorithm), which can be used to make [affine](#affine) [fractals](#fractal). MRCM fractals are related to [IFS](#ifs) fractals in that they both use the same types of affine transformations. The MRCM algorithm performs several affine transformations of a seed image in [parallel](#parallel/parallelism) to yield a secondary seed image. The output of the MRCM is [recursively](#recursive) passed back through to its input multiple times, to yield the fractal.

**<a id="multilayer_perceptron_(mlp)"></a>Multilayer Perceptron (MLP)** — A type of [feedforward neural network](#feedforward_neural_network) that is an extension of the [perceptron](#perceptron) in that it has at least one [hidden layer](#hidden_layer) of [neurons](#neuron). Layers are updated by starting at the inputs and ending with the outputs. Each neuron computes a weighted sum of the incoming signals, to yield a [net input](#net_input), and passes this value through its [sigmoidal](#sigmoidal) [activation function](#activation_function) to yield the neuron's [activation](#activation) value. Unlike the perceptron, an MLP can solve [linearly inseparable](#linearly_(in)separable) problems.

**<a id="mutation"></a>Mutation** — A [random](#random/randomness) change in any portion of genetic material. For a [genetic algorithm](#genetic_algorithm_(ga)), this means that a value in a [bit](#bit) [string](#string) is randomly set.

## N

**<a id="nash_equilibrium"></a>Nash Equilibrium** — In [game theory](#game_theory), a pair of [strategies](#strategy) for a game such that neither player can improve his outcome by changing his strategy. A Nash equilibrium sometimes takes the form of a [saddle](#saddle) structure. Under some cases, when a strategy is at a Nash equilibrium with itself, the strategy resembles an [evolutionary stable strategy](#evolutionary_stable_strategy_(ess)).

**<a id="natural_number"></a>Natural Number** — Any of the standard counting numbers; a positive integer.

**<a id="natural_selection"></a>Natural Selection** — The natural filtering process by which individuals with higher [fitness](#fitness) are more likely to reproduce than individuals with lower fitness.

**<a id="neo-darwinism"></a>Neo-Darwinism** — A synthesis of [Darwinism](#darwinism) with the mechanisms of genetics; the idea that [adaptation](#adaptation) equals a combination of [variation](#variation), heredity, and selection. See also [evolution](#evolution), [inheritable](#inheritable), and [natural selection](#natural_selection).

**<a id="net_input"></a>Net Input** — The weighted sum of incoming signals into a [neuron](#neuron) plus a neuron's [threshold](#threshold) value.

**<a id="neural_network_(nn)"></a>Neural Network (NN)** — A network of [neurons](#neuron) that are connected through [synapses](#synapse) or [weights](#weight). In this book, the term is used almost exclusively to denote an artificial neural network and not the real thing. Each neuron performs a simple calculation that is a [function](#function) of the [activations](#activation) of the neurons that are connected to it. Through [feedback](#feedback) mechanisms and/or the [nonlinear](#nonlinear) output response of neurons, the network as a whole is capable of performing extremely complicated tasks, including [universal computation](#universal_computation) and [universal approximation](#universal_approximation). Three different classes of neural networks are [feedforward](#feedforward_neural_network), [feedback](#feedback), and [recurrent neural networks](#recurrent_neural_network), which differ in the degree and type of [connectivity](#connectivity) that they possess.

**<a id="neuron"></a>Neuron** — A simple computational unit that performs a weighted sum on incoming signals, adds a [threshold](#threshold) or bias term to this value to yield a [net input](#net_input), and maps this last value through an [activation function](#activation_function) to compute its own [activation](#activation). Some neurons, such as those found in [feedback](#feedback) or [Hopfield networks](#Hopfield Network), will retain a portion of their previous activation.

**<a id="newtons_method"></a>Newton's Method** — An [iterative](#iterate/iterative) method for finding 0 values of a [function](#function).

**<a id="niche"></a>Niche** — A way for an animal to make a living in an [ecosystem](#ecosystem).

**<a id="no_free_lunch_(nfl)"></a>No Free Lunch (NFL)** — A [theorem](#theorem) that states that in the worst case, and averaged over an infinite number of [search spaces](#search_space), all [search methods](#search/search_method) perform equally well. More than being a condemnation of any search method, the NFL theorem actually hints that most naturally occurring search spaces are, in fact, not [random](#random/randomness).

**<a id="nonlinear"></a>Nonlinear** — A [function](#function) that is not [linear](#linear). Most things in nature are nonlinear. This means that in a very real way, the whole is at least different from the sum of the parts. See also [holism](#holism).

**<a id="not_recursively_enumerable_(not-re)"></a>Not Recursively Enumerable (not-RE)** — An infinite [set](#set) that cannot be [recursively enumerated](#recursively_enumerable_(re)). [Sets](#set) of this type that are also not [co-recursively enumerable](#co-recursively_enumerable_(co-re)) are effectively [random](#random/randomness).

**<a id="np"></a>NP** — Nondeterministic polynomial time problems; a class of computational problems that may or may not be solvable in [polynomial](#polynomial) time but are expressed in such a way that candidate solutions can be tested for correctness in polynomial time. See also [time complexity](#time_complexity) and [NP-Complete](#np-complete).

**<a id="np-complete"></a>NP-Complete** — A problem type in which any instance of any other [NP](#np) class problem can be translated to in [polynomial](#polynomial) time. This means that if a fast [algorithm](#algorithm) exists for an NP-complete problem, then any problem that is in NP can be solved with the same algorithm.

**<a id="numerical_solution"></a>Numerical Solution** — A solution to a problem that is calculated through a [simulation](#simulate/simulation). For example, solving the [Three Body Problem](#three_body_problem) is not possible in the worst case; however, with the [differential equations](#differential_equation) that describe the motions of three bodies in space, one could simulate their movements by simulating each time step. Nevertheless, numerical solutions are usually error-prone due to [sensitivity](#sensitivity) and, therefore, can be used to estimate the future for only relatively short time spans, in the worst case.

## O

**<a id="occams_razor"></a>Occam's Razor** — The principle that when faced with multiple but equivalent interpretations of some phenomenon, one should always choose the simplest explanation that correctly fits the data. Occam's Razor is useful for selecting competing [models](#model) for some phenomena.

**<a id="one-to-one"></a>One-to-One** — A [function](#function) or [map](#map) that for every possible output has only one input that yields that particular output; if *f(a) = f(b)*, then *a = b*.

**<a id="optimization"></a>Optimization** — The process of finding parameters that minimizes or maximizes a [function](#function).

**<a id="outer_product"></a>Outer Product** — An operation on two [vectors](#vector) that yields a [matrix](#matrix). Given two vectors with the same dimensionality, the outer product is a square symmetric matrix that contains the product of all pairs of elements from the two vectors, i.e., *A[i,j] = x[i] y[j]*.

## P

**<a id="parallel/parallelism"></a>Parallel/Parallelism** — Many things happening at once.

**<a id="pattern_classification"></a>Pattern Classification** — A task that [neural networks](#neural_network_(nn)) are often trained to do. Given some input pattern, the task is to make an accurate class assignment to the input. For example, classifying many images of letters to one of the twenty-six letters of the alphabet is a pattern classification task.

**<a id="payoff"></a>Payoff** — In [game theory](#game_theory), the amount that a player wins, given the player's and his opponent's actions.

**<a id="peano_curve"></a>Peano Curve** — A [fractal](#fractal) [space-filling](#space-filling) curve that can fill a plane even though it is a line of infinite length. Oddly enough, it has an integer [fractal dimension](#fractal_dimension) of 2.

**<a id="perceptron"></a>Perceptron** — The simplest type of [feedforward neural network](#feedforward_neural_network). It has only inputs and outputs, i.e., no [hidden layers](#hidden_layer).

**<a id="periodic"></a>Periodic** — Refers to motion that goes through a finite number of regions, returns to a previous state, and repeats the same fixed pattern forever.

**<a id="perturbation"></a>Perturbation** — A slight nudge.

**<a id="phase_space"></a>Phase Space** — In this book, another name for [state space](#state_space). In the scientific literature, “phase space” is used to denote the space of motion in a [dynamical system](#dynamical_system) that moves in [continuous](#continuous) time, while [state space](#state_space) is often used for [discrete](#discrete) time [systems](#system).

**<a id="phase_transition"></a>Phase Transition** — In physics, a change from one state of matter to another. In [dynamical systems](#dynamical_system) theory, a change from one mode of behavior to another.

**<a id="planning"></a>Planning** — In computer science, and particularly in [artificial intelligence](#artificial_intelligence), the task of determining a stepwise plan to accomplish a very specific task.

**<a id="polynomial"></a>Polynomial** — A [function](#function) in which the output is the sum of terms that are the products of constant values and the input raised to some integer power. The polynomial of a polynomial is another polynomial. From a [time complexity](#time_complexity) point of view, polynomials are well-behaved.

**<a id="post_production_system"></a>Post Production System** — A [model of computation](#model_of_computation) that resembles a collection of “if ... then” rules and is capable of [universal computation](#universal_computation).

**<a id="predator-prey_system"></a>Predator-Prey System** — An [ecosystem](#ecosystem) in which one portion of the population consumes another. With three or more species, simple predator-prey interactions can lead to [chaos](#chaos/chaotic) and biological [arms races](#arms_race). See also [Lotka-Volterra system](#lotka-volterra_system).

**<a id="prime_number"></a>Prime Number** — A [natural number](#natural_number) that can be evenly divided only by itself and 1.

**<a id="prisoners_dilemma"></a>Prisoner's Dilemma** — A non-[zero-sum game](#zero-sum_game) in which both players have incentive not to cooperate under any circumstances. Thus, the optimal [game theory](#game_theory) [strategy](#strategy) of [always defect](#always_defect) has the paradoxical property that both players would have a higher [payoff](#payoff) if they ignored the advice of game theory.

**<a id="probability"></a>Probability** — The likelihood that a [random](#random/randomness) event will occur.

**<a id="program"></a>Program** — An [algorithm](#algorithm) that is written in a programming language for execution on a physical computer.

**<a id="proof"></a>Proof** — A sequence of [statements](#statement) in which each subsequent statement is derivable from one of the previous statements or from an [axiom](#axiom) of a [formal system](#formal_system). The final statement of a proof is usually the [theorem](#theorem) that one has set out to prove.

## Q

**<a id="quasiperiodic"></a>Quasiperiodic** — Refers to a form of motion that is regular but never exactly repeating. Quasiperiodic motion is always composed of multiple but simpler [periodic](#periodic) motions. In the general case, for motion that is the sum of simpler periodic motions, if there exists a length of time that evenly divides the frequencies of the underlying motions, then the composite motion will also be periodic; however, if no such length of time exists, then the motion will be quasiperiodic.

## R

**<a id="random/randomness"></a>Random/Randomness** — Without cause; not [compressible](#compressible); obeying the statistics of a fair coin toss.

**<a id="random_walk"></a>Random Walk** — A walk in one or more dimensions that is dictated by the outcome of a coin toss. The direction of each step of the walk is specified by the coin toss. The resulting [random](#random/randomness) motion is often referred to as [Brownian motion](#brown_noise/brownian_motion).

**<a id="rational_number"></a>Rational Number** — A number that can be expressed as a fraction.

**<a id="real_number"></a>Real Number** — Any number that can be represented with a potentially infinite decimal expansion to the right of the decimal point. [Natural](#natural_number), [rational](#rational_number), [irrational](#irrational_number), and [incomputable](#incomputable) numbers are all real numbers.

**<a id="recurrent_neural_network"></a>Recurrent Neural Network** — A network similar to a [feedforward neural network](#feedforward_neural_network) except that there may be connections from an output or [hidden layer](#hidden_layer) to the inputs. Recurrent neural networks are capable of [universal computation](#universal_computation).

**<a id="recursive"></a>Recursive** — Strictly speaking, a [set](#set) or [function](#function) is recursive if it is [computable](#computable); however, in the usual sense of the word, a function is said to be recursive if its definition make reference to itself. For example, factorial can be defined as x! = x * (x - 1)! with the base case of 1! equal to 1. See also [self-referential](#self-referential).

**<a id="recursively_enumerable_(re)"></a>Recursively Enumerable (RE)** — A potentially infinite [set](#set) whose members can be enumerated by a [universal computer](#universal_computer); however, a universal computer may not be able to determine that something is not a member of a recursively enumerable set. The [halting set](#halting_set) is recursively enumerable but not [recursive](#recursive).

**<a id="reductionism"></a>Reductionism** — The idea that nature can be understood by dissection. In other words, knowing the lowest-level details of how things work (at, say, the level of subatomic physics) reveals how higher-level phenomena come about. This is a [bottom-up](#bottom-up) way of looking at the universe, and is the exact opposite of [holism](#holism).

**<a id="regular_expression"></a>Regular Expression** — A definition for a class of [strings](#string) that can be recognized by a [finite-state automaton](#finite-state_automaton_(fsa)). An example of a class of strings that is regular would be legal mathematical expressions using only “+” and digits. An example that is not regular is the same legal mathematical expressions as before, but with properly nested parentheses.

## S

**<a id="saddle"></a>Saddle** — A type of surface that is neither a peak nor a valley but still has a 0 [gradient](#gradient). Saddle points are situated such that moving in one direction takes one uphill, while moving in another direction would be downhill. Hence, saddles look like the things that cowboys ride on.

**<a id="scalar"></a>Scalar** — A single number, as opposed to a multidimensional [vector](#vector) or [matrix](#matrix).

**<a id="schema/schemata"></a>Schema/Schemata** — A similarity template used to analyze [genetic algorithms](#genetic_algorithm_(ga)). By using wild-card characters, a schema defines an entire class of [strings](#string) that may be found in a population.

**<a id="search/search_method"></a>Search/Search Method** — A method for finding a region of interest in a [search space](#search_space). Usually, the interesting regions correspond to solutions to a specific problem. [Hill-climbing](#hill-climbing), [steepest descent (ascent)](#steepest descent (ascent)), [simulated annealing](#simulated_annealing), and [genetic algorithms](#genetic_algorithm_(ga)) are all search methods.

**<a id="search_space"></a>Search Space** — A characterization of every possible solution to a problem instance. For a [neural network](#neural_network_(nn)) the search space is defined as all possible assignments to the network [weights](#weight); for a [genetic algorithm](#genetic_algorithm_(ga)), it is every conceivable value assignment to the [strings](#string) in the population.

**<a id="selection"></a>Selection** — See [natural selection](#natural_selection).

**<a id="self-organization"></a>Self-Organization** — A spontaneously formed higher-level pattern of structure or [function](#function) that is [emergent](#emergent) through the interactions of lower-level objects.

**<a id="self-organized_criticality_(soc)"></a>Self-Organized Criticality (SOC)** — A mathematical theory that describes how [systems](#system) composed of many interacting parts can tune themselves toward [dynamical](#dynamics/dynamical) behavior that is critical in the sense that it is neither [stable](#stable) nor [unstable](#unstable) but at a region near a [phase transition](#phase_transition). SOC systems display events in a power-law distribution and are never quite at [equilibrium](#equilibrium). See also [edge of chaos](#edge_of_chaos) and [self-organization](#self-organization).

**<a id="self-referential"></a>Self-Referential** — Referring directly back to oneself through information flow, influence, or cause and effect. See [Self-Referential](#self-referential).

**<a id="self-similar"></a>Self-Similar** — An object that is structurally [recursive](#recursive) in that a part will look like the whole. See also [fractal](#fractal).

**<a id="sensitivity"></a>Sensitivity** — The tendency of a [system](#system) (sometimes [chaotic](#chaos/chaotic)) to change dramatically with only small [perturbations](#perturbation).

**<a id="set"></a>Set** — A collection of things, usually numbers. Sets may be infinite in size.

**<a id="shadowing_lemma"></a>Shadowing Lemma** — Implies that a numerical [simulation](#simulate/simulation) of [chaos](#chaos/chaotic) may “shadow” a real trajectory of a real [chaotic](#chaos/chaotic) [system](#system).

**<a id="sigmoidal"></a>Sigmoidal** — An “S” shaped [function](#function) that is often used as an [activation function](#activation_function) in a [neural network](#neural_network_(nn)).

**<a id="simulate/simulation"></a>Simulate/Simulation** — [Experimentation](#experimentation) in the space of theories, or a combination of experimentation and [theorization](#theorization). Some numerical simulations are [programs](#program) that represent a [model](#model) for how nature works. Usually, the outcome of a simulation is as much a surprise as the outcome of a natural event, due to the richness and uncertainty of [computation](#computation).

**<a id="simulated_annealing"></a>Simulated Annealing** — A partially [random](#random/randomness) method of [search](#search/search_method) and [optimization](#optimization) usually used for [combinatorial optimization](#combinatorial_optimization) problems. The technique is modeled on how the molecular structure of metals is disordered at high temperatures but very ordered and crystalline at low temperatures. In simulated annealing, a problem instance is reformulated so that it loosely resembles disordered material. Gradually, the temperature is lowered such that the ordered states correspond to good solutions to a problem.

**<a id="space_complexity"></a>Space Complexity** — A [function](#function) that describes the amount of memory required for a [program](#program) to run on a computer to perform a particular task. The function is parameterized by the length of the program's input. See also [time complexity](#time_complexity).

**<a id="space-filling"></a>Space-Filling** — Refers to a curve that manages to twist and turn in such a way that it actually fills a space or volume. All space-filling curves are [fractal](#fractal).

**<a id="special_function"></a>Special Function** — In [Lisp](#lisp) or [Stutter](#stutter), a built-in [function](#function) that may or may not fully evaluate its arguments, such as the `if` primitive.

**<a id="stable"></a>Stable** — Having a [basin of attraction](#basin_of_attraction) that is non-zero in size; an [attractor](#attractor) that can withstand some form of [perturbation](#perturbation).

**<a id="standard_deviation"></a>Standard Deviation** — A measure of the spread of a [set](#set) of data. For a [Gaussian](#gaussian) distribution, the standard deviation hints at the width of the tails of the distribution [function](#function).

**<a id="statement"></a>Statement** — In a [formal system](#formal_system), a [string](#string) of characters that is formed according to well-defined rules such that it is legal for the language that is the formal system. For example, in the formal system of arithmetic, the expression “5 + 3 * (2 - 4)” is a valid and well-formed statement, but “5 + )3 * * (2 (- 4)” is not.

**<a id="state_space"></a>State Space** — In this book, another name for the [phase space](#phase_space) of a [dynamical system](#dynamical_system). Roughly speaking, if the [dynamics](#dynamics/dynamical) of a dynamical system can be described by *n* values, then the state space is the *n*-dimensional volume that the system moves through. [Systems](#system) that are [continuous](#continuous) in time will form a smooth trajectory through this volume, while [discrete](#discrete) systems may jump to different locations on subsequent time steps. In either case, if a system ever returns to a previously visited location in the state space, then the system is in either a [fixed point](#fixed_point) or a [limit cycle](#limit_cycle). For [chaotic](#chaos/chaotic) systems, or for [programs](#program) that never halt, the system will always be at a previously unvisited portion of the state space.

**<a id="steepest_descent_(ascent)"></a>Steepest Descent (Ascent)** — A [search method](#search/search_method) that uses the [gradient](#gradient) information of a [search space](#search_space) and moves in the opposite direction from the gradient until no further downhill (or uphill) progress can be made. See also [hill-climbing](#hill-climbing).

**<a id="stochastic"></a>Stochastic** — Something that is [random](#random/randomness).

**<a id="strange_attractor"></a>Strange Attractor** — An [attractor](#attractor) of a [dynamical system](#dynamical_system) that is usually [fractal](#fractal) in dimension and is indicative of [chaos](#chaos/chaotic).

**<a id="strategy"></a>Strategy** — In [game theory](#game_theory), a policy for playing a game. A strategy is a complete recipe for how a player should act in a game under all circumstances. Some policies may employ [randomness](#random/randomness), in which case they are referred to as [mixed strategies](#mixed_strategy).

**<a id="strength"></a>Strength** — For a [classifier system](#classifier_system), a [classifier](#classifier)'s relative ability to win a bidding match for the right to post its [message](#message) on the [message list](#message_list).

**<a id="string"></a>String** — Any sequence of letters, numbers, digits, [bits](#bit), or symbols.

**<a id="stutter"></a>Stutter** — A silly programming language used in this book that is based on [Lisp](#lisp) and is capable of [universal computation](#universal_computation).

**<a id="symmetric_matrix"></a>Symmetric Matrix** — A [matrix](#matrix) with the lower-left half equal to the mirror image of the upper-right half.

**<a id="synapse"></a>Synapse** — The junction between two [neurons](#neuron) in which neural activity is propagated from one neuron to another. See also [excitatory](#excitatory), [inhibitory](#inhibitory), and [weight](#weight).

**<a id="synchronous"></a>Synchronous** — Acting in a lockstep fashion, with each event occurring in a precise order, or in such a way as to eliminate the notion of order entirely.

**<a id="system"></a>System** — Something that can be studied as a whole. Systems may consist of subsystems that are interesting in their own right. Or they may exist in an [environment](#environment) that consists of other similar systems. Systems are generally understood to have an internal state, inputs from an environment, and methods for manipulating the environment or themselves. Since cause and effect can flow in both directions of a system and environment, interesting systems often posses [feedback](#feedback), which is [self-referential](#self-referential) in the strongest case.

## T

**<a id="theorem"></a>Theorem** — A [statement](#statement) in a [formal system](#formal_system) that has [proof](#proof).

**<a id="theorization"></a>Theorization** — A process by which scientists attempt to understand nature; it is the complement to [experimentation](#experimentation). Theorization is the process of building mathematical [models](#model) for how things work. Scientists always desire theories that are simpler than the data they explain. See also [Occam's Razor](#occams_razor) and [simulation](#simulate/simulation).

**<a id="three_body_problem"></a>Three Body Problem** — The problem of determining the future positions and velocities of three gravitational bodies. The problem was proved unsolvable in the general case by Henri Poincaré, which forshadowed the importance of [chaos](#chaos/chaotic). Although no [analytical solutions](#analytical_solution) are possible in the worst case, a [numerical solution](#numerical_solution) is sometimes sufficient for many tasks.

**<a id="threshold"></a>Threshold** — A quantity added to (or subtracted from) the weighted sum of inputs into a [neuron](#neuron), which forms the neuron's [net input](#net_input). Intuitively, the net input (or bias) is proportional to the amount that the incoming neural [activations](#activation) must exceed in order for a neuron to fire.

**<a id="time_complexity"></a>Time Complexity** — A [function](#function) that describes the amount of time required for a [program](#program) to run on a computer to perform a particular task. The function is parameterized by the length of the program's input. See also [space complexity](#space_complexity).

**<a id="time-reversible"></a>Time-Reversible** — A property of [dynamical systems](#dynamical_system) that can be run unambiguously both forward and backward in time. The [Hénon map](#hénon_map), [Lorenz system](#lorenz_system), and [vant](#vant) [cellular automata](#cellular_automaton_(ca)) are all time-reversible, while the [logistic map](#logistic_map), the [Mackey-Glass system](#mackey-glass_system), and most other [cellular automata](#cellular_automaton_(ca)) are not. Time-reversible systems are described by [functions](#function) that are [invertible](#invertible).

**<a id="time_series"></a>Time Series** — A sequence of values generated from a [dynamical system](#dynamical_system) over time. [Chaotic](#chaos/chaotic) [systems](#system) can be analyzed by examining the time series generated by a single portion of the [system](#system). See also [embedding](#embedding).

**<a id="tit-for-tat"></a>Tit-for-Tat** — An effective [strategy](#strategy) for playing the [Iterated Prisoner's Dilemma](#iterated_prisoners_dilemma). Tit-for-Tat starts by cooperating, and then does whatever its opponent did in the previous round of play.

**<a id="top-down"></a>Top-Down** — A method of examining things that first looks at higher-level phenomena and then tries to explain lower-level patterns in terms of the higher-level observations. This is the exact opposite of [bottom-up](#bottom-up). See also [holism](#holism) and [reductionism](#reductionism).

**<a id="transpose"></a>Transpose** — An operation that flips a [matrix](#matrix) about the main diagonal.

**<a id="turing_machine"></a>Turing Machine** — A [model of computation](#model_of_computation) that uses an underlying [finite-state automaton](#finite-state_automaton_(fsa)) but also has an infinite tape to use as memory. Turing machines are capable of [universal computation](#universal_computation).

**<a id="turtle_graphics"></a>Turtle Graphics** — A simple language for drawing graphics in which a “turtle” is used to make strokes on a plotting device. Typical commands include “move forward,” “draw forward,” and “turn left.”

## U

**<a id="uncountable_infinity"></a>Uncountable Infinity** — An order of infinity that is larger than the number of [natural numbers](#natural_number). The number of [real numbers](#real_number) is uncountably infinite.

**<a id="universal_approximation"></a>Universal Approximation** — Having the ability to approximate any [function](#function) to an arbitrary degree of accuracy. [Neural networks](#neural_network_(nn)) are universal approximators.

**<a id="universal_computation"></a>Universal Computation** — Capable of computing anything that can in principle be computed; being equivalent in computing power to a [Turing machine](#turing_machine), the [lambda calculus](#lambda_calculus), or a [Post production system](#post_production_system).

**<a id="universal_computer"></a>Universal Computer** — A computer that is capable of [universal computation](#universal_computation), which means that given a description of any other computer or [program](#program) and some data, it can perfectly emulate this second computer or program. Strictly speaking, home PCs are not universal computers because they have only a finite amount of memory. However, in practice, this is usually ignored.

**<a id="unstable"></a>Unstable** — Having a [basin of attraction](#basin_of_attraction) that is 0 in size; being such that the slightest [perturbation](#perturbation) will forever change the state of a [system](#system). A pencil balanced on its point is unstable.

## V

**<a id="value_function"></a>Value Function** — A built-in [function](#function) in [Lisp](#lisp) or [Stutter](#stutter) that evaluates all of its arguments prior to being executed, e.g., `car`, `cdr`, and `cons`.

**<a id="vant"></a>Vant** — A virtual ant; a type of [cellular automaton](#cellular_automaton_(ca)) that vaguely emulates the activity of one or more ants.

**<a id="variation"></a>Variation** — Genetic differences among individuals in a population.

**<a id="vector"></a>Vector** — A one-dimensional array of numbers that can be used to represent a point in a multidimensional space.

## W

**<a id="weight"></a>Weight** — In a [neural network](#neural_network_(nn)), the strength of a [synapse](#synapse) (or connection) between two [neurons](#neuron). Weights may be positive ([excitatory](#excitatory)) or negative ([inhibitory](#inhibitory)). The [thresholds](#threshold) of a neuron are also considered weights, since they undergo [adaptation](#adaptation) by a [learning](#learning) [algorithm](#algorithm).

**<a id="white_noise"></a>White Noise** — Noise that uniformly distributed in the frequency domain; [randomness](#random/randomness) that is uniformly distributed; thus, a white noise process with a range of 0 to 1 would yield a random number in this range with [probability](#probability) equal for all possible values. [Brown noise](#brown_noise/brownian_motion) is a result of cumulatively adding white noise.

## X

**<a id="xor"></a>XOR** — The exclusive-or [function](#function); given two [Boolean](#boolean) inputs, the output of XOR is 1 if and only if the two inputs are different; otherwise, the output is 0.

## Y

**<a id="yowza!"></a>Yowza!** — Yowza!

## Z

**<a id="zero-sum_game"></a>Zero-Sum Game** — In [game theory](#game_theory), a game in which a win for one player results in an equal but opposite loss for the other players.
