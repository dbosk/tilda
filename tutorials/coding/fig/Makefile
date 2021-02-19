.PHONY: all
all: rovar-tree-codewords.pdf
all: rovar-tree.pdf
all: overwatch-tree.pdf

.PHONY: clean
clean:
	${RM} rovar-tree-codewords.pdf
	${RM} rovar-tree.pdf
	${RM} overwatch-tree.pdf
	${RM} rovar-tree-codewords.pdf_tex
	${RM} rovar-tree.pdf_tex
	${RM} overwatch-tree.pdf_tex

.PHONY: distclean
distclean:
	true

INCLUDE_MAKEFILES=../../../makefiles
include ${INCLUDE_MAKEFILES}/doc.mk
