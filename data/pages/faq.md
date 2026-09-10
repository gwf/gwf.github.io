---
title: "Frequently Asked Questions (FAQ) List"
source: html/faq.html
---

###  How do I compile the code under Windows?     New!

Thanks to Peter Ross for pointing out some difficulties. He writes:

*On digging, the problem seems to lie with the lines that say things like

```

        #if __dest_os == __mac_os
```

because, as near as I can tell, MS VC++ doesn't define either of these by default and so treats them as having value 0, so that the test succeeds! The simple fix is, in Project->Settings..->C++, under "Category: General", in "Preprocessor definitions:", add __dest_os (where WIN32 is already defined). Everything then compiles OK. You might like to include this somewhere in the FAQ for others who run into such problems?*

Done. Thanks Peter.

###  How do I compile the code under Linux?

You'll need to tweak one or two things to build it all from scratch. I wrote the code a few years back when `/usr/X11` was a fairly reasonable default for the base directory of X-windows. These days, `/usr/X11R6` is much more common. As a result, you'll need to edit the file `cbn/code/bin/Makefile` so that it references the correct base directory of your X11 installation.

###  How do I view the man pages under Linux (or Unix)?

Depending on your installation, one of the following will probably work:

1.  If your shell is `csh` or `tcsh`, try inserting the line:

```

        setenv MANPATH $HOME/cbn/code/man:.:
```

into your `.cshrc` file. If you use `sh`, `bash`, `ksh`, or some other Bourne shell-like variant, then insert the following into your `.profile` file:

```

        MANPATH=$HOME/cbn/code/man:.:
        export MANPATH
```

When done, using the command '`man mandel`' should find the man page to the Mandelbrot program. Of course, all of the above assumes that the *CBofN* source code is installed in `cbn/code` relative to your home directory, so you may need to change the specifics to fit your needs.

2.  If the fix above does not work, try using the command:

```

        nroff -man mandel.1 | less
```

while inside of the man page directory. You may use `more` instead of `less`, of course.

3.  Finally, if none of the above works, just use the HTML pages. Online versions can be found [here](pages/source.md).

###  How do I run the programs under Windows?

The software was originally developed under UNIX which uses what is know as a command-line interface. With a command-line interface, you give a program runtime options by specifying all of the options on the command-line.

To make a long story short, fire up the DOS shell, issue the command "cd DIRECTORY" where DIRECTORY is the location of the CBofN programs, and try running the programs by typing in the program name. With any luck, you'll get two windows showing the program output; one contains text, the other contains graphics. To change the runtime options, alter the command with "PROGRAM -SOMEOPTION -SOMEPARAM PARAMVALUE". All of the legal command-line options are described in the book. You can also see them by typing "PROGRAM -help".

Unfortunately, command-line interfaces are a hard thing for Windows users to understand. I am sorry about that. But this is the world that I live in. At some point in the future, I will attempt to create a more Windows-like interface to the programs.

###  LSYS doesn't work under Windows. How can I fix this?

This problem only occurs when you try to use the "|" characters in a rule. Unfortunately, the DOS shell under Windows not allow you to quote the pipe character (as far as I can tell). Thus, no matter how you form the command line argument, DOS (and Windows) will interpret the "|" character to be a functional pipe.

I know of three ways to work around this problem:

1.  Use the UNIX version of LSYS or use the [Java Applets](pages/java.md). UNIX doesn't have a problem quoting characters. Moreover, the LSYS [Java applet](pages/java.md) is much easier to use than the Windows version.

2.  Recompile the source, replacing the "|" character with something else, say "!". In the not so far future, I'll patch the source code myself, but I do not have access to a Windows compiler at this time.

3.  Install the Korn shell (ksh). Ksh handles quoting properly. Under ksh, I was able to run:

```

      lsys -rule 'f=|[-f][+f]' -ds 0.6 -axiom '[f]--f'
```

and everything worked fine. Ksh is part of the UWIN package, which can be downloaded from [ATT](http://www.research.att.com/sw/tools/uwin/). You can get it for free for research and educational use. You only need the base installation. Once it's in, run ksh with the icon, and use it instead of the DOS shell.

###  How Have the Programs Changed Since Publication of the Book

Duplicated from the the “[miscellany / errata](pages/errata.md)” section:

-  Source code program usage: The `-term` command-line option can now take four new (or modified) values:

  1. `-term X11`    color graphics under X11.
  2. `-term x11`    grayscale graphics under X11.
  3. `-term Win`    color graphics under Windows 95/98/NT.
  4. `-term win`    grayscale graphics under Windows
  5. `-term Mac`    color graphics under Mac OS.
  6. `-term mac`    grayscale graphics under Mac OS.

-  Source code program usage: All reference to the `-xmag` option should now be changed to `-mag` because this option now affects both Windows and X11.
