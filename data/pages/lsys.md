---
title: "LSYS Documentation"
source: html/lsys.html
---

## Name

lsys - builds an L-system fractal from multiple rules

## Synopsis

```
lsys -help
  or
lsys   [-width  integer]  [-height integer] [-border inte-
       ger] [-depth integer]  [-a0  double]  [-da  double]
       [-ds  double] [-unoise double] [-rule ... ] [-axiom
       string] [-inv] [-mag integer] [-term string]
```

## Description

An L-system is computed according to the specified axiom, rules, and step angle. The L-system axiom is recursively expanded for the specified depth, with 'F', 'G', and '|' actions resulting in movement of the virtual plotter, and '+' and '-' commands resulting in rotation of the virtual plotter. See the RULES section of the manual page for more information on the format for legal rules.

## Options

- `-width` *integer* — Width of the plot in pixels.
- `-height` *integer* — Height of the plot in pixels.
- `-border` *integer* — Approximate number of border pixels.
- `-depth` *integer* — Recursion depth to use.
- `-a0` *double* — Initial angle.
- `-da` *double* — Delta angle for '+' and '-' commands.
- `-ds` *double* — Delta step size. Only affects '|' commands and should be less than 1.
- `-unoise` *double* — Amount of uniform noise to add to step angle.
- `-rule` *...* — Specify a production rule. See RULES section of manual page.
- `-axiom` *string* — Starting axiom.
- `-inv` — Invert all colors?
- `-mag` *integer* — Magnification factor.
- `-term` *string* — How to plot points.

## Rules

The L-system rules should always take the form "x=..." where "x" is a letter and the remaining portion is a sequence of turtle graphics commands, which operate as described below.

'F' is the draw forward command, which moves the plotter forward by a fixed length, drawing a line from the old position to the new position.

'G' (Go Forward) is similar to 'F', but only moves the plotter and does not draw a line.

'+' and '-' turn the plotter to the right (or left) by a fixed angle determined by the -da switch. If an integer precedes the '+' or '-' symbol, then the plotter effectively makes that number of right-hand turns.

'[' saves the current position and angle of the plotter for later use, which is restored by the ']' command.

'|' move the turtle forward by a length computed from the execution depth, drawing a line from the old position to the new. Thus, this command is similar to 'F' but it is not recursively expanded. If DS is the value supplied by the -ds switch, then the step size will be proportional to DS^depth. This allows for certain types of figures to be drawn that would otherwise be difficult to express without this command.

## Examples

```
A weed:
       lsys -da 20 -rule "F=|[-F]|[+F][-F]F"

Kock curve:
       lsys -da 60 -rule F=F-F++F-F

Penrose Snowflake:
       lsys    -da    18    -axiom   F4-F4-F4-F4-F   -rule
       F=F4-F4-F10-F++F4-F

Sierpinski Arrowhead:
       lsys -da 60 -rule  "F=[-G+++F][-G+F][GG--F]"  -rule
       G=GG

See  the  author's  book,  "The  Computational  Beauty  of
Nature," for more examples.
```

## Miscellany

If you are using a UNIX command shell, be sure to quote any rules with brackets so that the shell passes them to the program correctly.

## Bugs

No sanity checks are performed to make sure that any of the options make sense.

The border size is only approximately calculated because the author felt a bit lazy at the time of writing this program. However, it's pretty close for most values.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
