.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex
SRC+=		bibliography.bib
SRC+=		rk.py

contents.tex: contents.nw

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}

%.pytxmcr: ltxobj/%.pytxmcr
ltxobj/%.pytxmcr::
	cd $(dir $@) && pythontex $(notdir $@)


.PHONY:
all: rk.py

rk.py: contents.nw
	${NOTANGLE}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf
	${RM} contents.tex
	${RM} rk.py


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
