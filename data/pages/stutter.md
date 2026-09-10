---
title: "STUTTER Documentation"
source: html/stutter.html
---

## Name

stutter - a simple lisp interpreter

## Synopsis

```
stutter -help
  or
stutter
       [-heap integer]
```

## Description

This is a simple lisp interpreter that only understands car, cdr, cons, if, set, equal, quote, and lambda, but is still Turing-complete. It uses stop-and-copy garbage collection and has an adjustable heap size. Besides the primitive functions listed above, STUTTER only knows about two cells, t and nil. See the examples for how integer arithmetic and more complicated programming constructs can be formed with the primitives.

## Options

- `-heap` *integer* — Number of cells in the heap.

## Bugs

If STUTTER can free no cell after a call to the garbage collector, it will exit.

## See Also

In the data directory are the STUTTER examples demo.slp, sample.slp and float.slp, which may be helpful.

## Author

Copyright (c) 1997, Gary William Flake.

Permission granted for any use according to the standard GNU ``copyleft'' agreement provided that the author's comments are neither modified nor removed. No warranty is given or implied.
