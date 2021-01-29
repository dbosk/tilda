.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

CODE+=		bst.py
CODE+=		fib_efficient.py
CODE+=		fib_print.py
CODE+=		fib.py
CODE+=		gcd.py

SRC+=		$(addprefix src/,${CODE})

notes.pdf: notes.tex
notes.pdf: ${SRC}

slides.pdf: slides.tex
slides.pdf: ${SRC}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
