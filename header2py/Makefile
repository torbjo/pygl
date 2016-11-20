PYTHON=python3
DOWNLOAD=wget --quiet -O -

GL4URL=https://www.opengl.org/registry/api/GL/glcorearb.h
GL3URL=https://www.opengl.org/registry/oldspecs/glcorearb.h

DEPS=api.py.head api.py.tail

DATE=$(shell date --utc +%FT%TZ)

.PHONY: all mkheader clean dist-clean test

all: api4.py api3.py

api4.py: glcorearb4.h $(DEPS)
	$(MAKE) mkheader header=$^ outfile=$@ url=$(GL4URL)

api3.py: glcorearb3.h $(DEPS)
	$(MAKE) mkheader header=$^ outfile=$@ url=$(GL3URL)

mkheader:
	@echo "# This file was auto-generated on $(DATE) from:" > $(outfile)
	@echo "# $(url)" >> $(outfile)
	@echo >> $(outfile)
	cat api.py.head >> $(outfile)
	$(PYTHON) main.py < $(header) >> $(outfile)
	cat api.py.tail >> $(outfile)

glcorearb4.h:
	$(DOWNLOAD) $(GL4URL) > $@

glcorearb3.h:
	$(DOWNLOAD) $(GL3URL) > $@

clean:
	rm -f api3.py
	rm -f api4.py

dist-clean: clean
	rm -f glcorearb3.h
	rm -f glcorearb4.h

# Very simple test. Just check that the files loads without errors.
test: api3.py api4.py
	$(PYTHON) api3.py
	$(PYTHON) api4.py
