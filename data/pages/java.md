---
title: "Java Applets"
source: html/java.html
---

Mike Miller graciously coded up a set of Java classes to simplify porting the source code from the book. Using this framework, Mike has ported about half of the programs from the original C source into Java. His framework is in keeping with the philosophy behind the design of the original C source in that all of the details for the GUI are more or less extracted away from the main source. This means that the heart of the code, i.e., the interesting stuff, is pretty easy to understand from looking at the class definitions.

Of course, the java source code is freely available, [with](legacy/cbn-java+class.zip) and [without](legacy/cbn-java.jar) the class files precompiled. If you don't have a Java compiler or you are not sure, get the package with the class files included.

Since the Java applets closely resemble the [C programs](pages/download.md), you may wish to consult the [online documentation](pages/source.md) of the original programs.

While using the applets, note that you can often interact with the main viewer. For example, some applets will allow you to zoom in and/or rotate an image, depending on what is appropriate; so try your mouse on the viewer and see what happens.

Depending on the size of your screen and the amount of processing power that you have, you should choose one links below to run the applets.

- [small screen:](pages/javasmall.md) 420x520 panel, 100x100 graphics
- [medium screen:](pages/javamed.md) 520x520 panel, 200x200 graphics
- [large screen:](pages/javalarge.md) 620x520 panel, 300x300 graphics

NB: Netscape under Linux and Solaris has a strange update policy for the screen that I can't quite figure out. If the graphics take a long time to update, try moving your mouse around or clicking the menu. Anyone know what's the deal here?


_The original page embedded the `CBNapplet` Java applet (legacy/classes/); the javasmall/javamed/javalarge pages were applet-only and are not converted._
