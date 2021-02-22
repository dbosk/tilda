.PHONY: all
all: hamming.pdf

LATEXFLAGS+=	-shell-escape

hamming.pdf: hamming.tex preamble.tex hamming.bib hamming.py

hamming.tex: hamming.nw

hamming.pytxmcr ltxobj/hamming.pytxmcr::
	cd ltxobj && pythontex hamming

.PHONY:
all: hamming

hamming.py: hamming.nw
hamming: hamming.py
	cp $^ $@
	chmod +x $@


.PHONY: clean
clean:
	${RM} hamming hamming.py hamming.pdf hamming.tex
	${RM} -R __pycache__


INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
include ${INCLUDE_MAKEFILES}/noweb.mk
