
.SUFFIXES: .src .html

SOURCE=newsrc

vpath %.src $(SOURCE)
vpath %.inc $(SOURCE)

SRC    = $(wildcard $(SOURCE)/*.src)
INC    = $(wildcard $(SOURCE)/*.inc)
HTML   = $(SRC:$(SOURCE)/%.src=%.html)

.src.html:
	cd $(SOURCE); perl preproc.pl < ../$< > ../$@

default: $(HTML)


$(HTML): defaults.inc top.inc bottom.inc
slides.html: slide.inc

clean:
	rm -f *.html

dotar:	../html.tgz
	mcopy -o ../html.tgz a:

../html.tgz: tar

tar:	clean
	cd ..; tar cvvfz html.tgz html

figs: cbn-figs-all.tgz cbn-figs-gif.tgz cbn-figs-eps.tgz cbn-figs-pdf.tgz \
      cbn-figs-all.zip cbn-figs-gif.zip cbn-figs-eps.zip cbn-figs-pdf.zip

cbn-figs-all.tgz:
	cd ../..; tar cvvfhz cbn/html/cbn-figs-all.tgz cbn/figs

cbn-figs-all.zip:
	cd ../..; find cbn/figs/ -true -print | zip cbn/html/cbn-figs-all -@

cbn-figs-gif.tgz:
	cd ../..; tar cvvfz cbn/html/cbn-figs-gif.tgz cbn/figs/*.gif

cbn-figs-gif.zip:
	cd ../..; find cbn/figs/ -name "*.gif" -print | zip cbn/html/cbn-figs-gif -@

cbn-figs-eps.tgz:
	cd ../..; tar cvvfz cbn/html/cbn-figs-eps.tgz cbn/figs/*.eps

cbn-figs-eps.zip:
	cd ../..; find cbn/figs/ -name "*.eps" -print | zip cbn/html/cbn-figs-eps -@

cbn-figs-pdf.tgz:
	cd ../..; tar cvvfz cbn/html/cbn-figs-pdf.tgz cbn/figs/*.pdf

cbn-figs-pdf.zip:
	cd ../..; find cbn/figs/ -name "*.pdf" -print | zip cbn/html/cbn-figs-pdf -@

dist:
	rm -rf cbnhtml
	mkdir cbnhtml
	cp -r graphics figs classes *.bib *.zip *.jar *.hqx *.tgz *.html cbnhtml
	tar cvvfz ../cbnhtml.tgz cbnhtml
	rm -rf cbnhtml

