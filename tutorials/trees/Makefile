.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

CODE+=		strykord.py
CODE+=		sjuor.py

FIG+=		graph.pdf

$(addprefix fig/,${FIG})::
	${MAKE} -C $(dir $@) $(notdir $@)

DEPENDS+=	$(addprefix src/,${CODE}) $(addprefix fig/,${FIG})

notes.pdf: notes.tex
notes.pdf: ${SRC} ${DEPENDS}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${DEPENDS}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf

.PHONY: distclean
distclean:
	${MAKE} -C fig clean distclean
	${MAKE} -C src clean distclean

INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
