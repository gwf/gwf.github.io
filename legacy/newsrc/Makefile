
.SUFFIXES: .1 .src

vpath %.1 ../../code/man

MAN  = $(wildcard ../../code/man/*.1)
SRC  = $(MAN:../../code/man/%.1=%.src)

.1.src:
	name=`basename $< .1 | tr '[a-z]' '[A-Z]'`; \
	echo '#define PROGRAM_NAME '$$name > $@
	echo '#include "code-top.inc"' >> $@
	nroff -man < $< \
	  | ../../misc/man2html -bare -compress -botm 6 -topm 5 -pgsize 66 \
	  | sed 's/H2/H4/g' >> $@
	echo '#include "bottom.inc"' >> $@
	echo '' >> $@

default: $(SRC)

clean:
	rm -f $(SRC)


