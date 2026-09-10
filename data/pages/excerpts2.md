---
title: "Selected Excerpts - Section 10.0"
source: html/excerpts2.html
---

[ [preface](pages/excerpts0.md) | [section 4.2](pages/excerpts1.md) | [section 10.0](pages/excerpts2.md) | [section 18.0](pages/excerpts3.md) | [section 22.0](pages/excerpts4.md) ]

## Section 10.0

# Nonlinear Dynamics in Simple Maps

> *Chaos is the score upon which reality is written.*

> --Henry Miller

> *... it may happen that small differences in the initial conditions produce very great ones in the final phenomena.*

> --Henri Poincaré

> *Prediction is difficult, especially of the future.*

> --Mark Twain (also attributed to Niels Bohr)

In the previous book part we saw how natural physical structures could be described in terms of fractal geometry. In this book part we will be concerned with the related topic of *chaos* in *nonlinear dynamical systems*. A dynamical system can be loosely defined as anything that has motion, such as swinging pendulums, bouncing balls, robot arms, reactions in a chemical process, water flowing in a stream, or an airplane in flight. For each of these examples there are two important aspects that must be considered. First, we need to determine what it is about a dynamical system that changes over time. In the case of the pendulum, both position and velocity vary over time, so we would be concerned with the “motion” of both of these states of the pendulum. A less obvious example is found in a chemical reaction, where the “motion” can be found in the ratio of reactants to reagents, or perhaps in some physical aspect of the chemicals, such as temperature or viscosity. The second aspect of a dynamical system that we must be concerned with is in the collection of rules that determine how a dynamical system changes over time. Usually, scientists have a mathematical model of how a real dynamical system works. The model will typically have equations that may be parameterized by time and the previous states of the system. Sometimes these equations can be used to get an estimate of what the future state of a dynamical system will be. In this spirit, let's agree that the “motion” of a dynamical system is dependent on how the state of the system changes over time. Moreover, there must exist a set of rules that governs how a dynamical system in some state evolves to another state. We may not know what the rules are, but if a dynamical system is deterministic, a set of rules for the time evolution of the system exists independently of our knowledge of it.

There are many different types of motion that can be exhibited by a dynamical system. The simplest is *fixed point* behavior, which can be seen in a pendulum when friction and gravity bring the system to a halt. Most fixed points can be likened to a ball placed on top of a hill, which rolls downward until at some point the ball sits on a flat spot and has no momentum to carry it further.

The next simplest type of motion is known as a *limit cycle* or *periodic* motion, which involves movement that repeats itself over and over. A lone planet orbiting a star in an elliptical orbit is an example of a limit cycle. Some limit cycles are more complicated than others. For example, a child on a swing drives the motion of the swing by periodically rocking in beat with the natural frequency of the swing, much like an idealized pendulum. Now, if the child rhythmically swings one leg at a higher frequency, the motion of that leg will cause the motion of his or her body to subtly wobble back and forth. If it is timed accurately, the child may be able to coerce the motion into behavior that is more complicated than that of the planet, with his or her body moving back and forth along the main axis of the swing, and perpendicularly left to right in step with the leg.

A slightly more complicated form of motion is found in *quasiperiodic* systems, which are similar to periodic systems except that they never quite repeat themselves. For example, the moon orbits Earth, which orbits the sun, which, in turn, orbits the galactic center, and so on. In order for the combined motion of the moon and Earth to be truly periodic, they must at some future point return to some previously occupied state. But in order for that to happen, all of the individual motions must resonate, which means that there must exist a length of time that will evenly divide all of the frequencies. Figure 10.1c shows quasiperiodic motion as consisting of two independent circular motions that fail to repeat due to a lack of resonance.

---

![fixed point](legacy/graphics/p1.gif) ![limit cycle](legacy/graphics/p2.gif) ![quasiperiodic](legacy/graphics/p3.gif)

(a) (b) (c)

**Figure 10.1:**    Different types of motion: (a) fixed point, (b) limit cycle (c)  quasiperiodic

---

Up until the last thirty years or so, almost every scientist believed that everything in the universe fell into either fixed point, periodic, or quasiperiodic behavior. The belief in a clockwork universe, as exemplified by the mathematician Pierre-Simon de Laplace [1], held that, in principle, if one had an accurate measure of the state of the universe and knew all of the laws that govern the motion of everything, then one would be able to predict the future with near perfect accuracy. We now know that this is not true, since science was mistaken in its assumption that everything is either a fixed point or a limit cycle. Chaotic systems are not just exceptions to the norm but are, in fact, more prevalent than anyone could imagine. Chaos is everywhere: in the turbulence of water and air, in the wobble of planets as they follow complicated orbits, in global weather patterns, in the human brain's electrochemical activity, and even in the motion of a child on a swing. In all of these cases the complicated motion produced by chaos prohibits predicting the future in the long term. On the other hand, phenomena that were once thought to be purely random are now known to be chaotic. The good news in this case is that chaotic systems admit prediction in the short term.

Chaos is related to the other topics of this book in many ways. The pathological nature of the incomputable functions from Part I is very similar to the unpredictability of chaotic systems. The motion of chaotic systems can be described by fractal geometry. There is also a hypothesis known as “computation on the edge of chaos” that will be relevant in the next book part when we study complex systems.

In this chapter we will be primarily concerned with getting an intuitive feel for how chaos works in a simple, discrete time, iterative system. The nice thing about the examples that we will be looking at is that the richness, diversity, and beauty of chaos are exhibited by a deceptively simple dynamical system.

---

[1]   Laplace claimed that “given for one instant an intelligence which could comprehend all the forces by which nature is animated and the respective positions of the beings which compose it ... nothing would be uncertain, and the future as the past would be present to its eyes.”

[ [preface](pages/excerpts0.md) | [section 4.2](pages/excerpts1.md) | [section 10.0](pages/excerpts2.md) | [section 18.0](pages/excerpts3.md) | [section 22.0](pages/excerpts4.md) ]
