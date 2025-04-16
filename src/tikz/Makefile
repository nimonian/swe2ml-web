OUTPUT_DIR := ../images
TEX_FILES := $(wildcard ./*.tex)
SVG_FILES := $(TEX_FILES:./%.tex=$(OUTPUT_DIR)/%.svg)

.PHONY: all clean

all: $(SVG_FILES)

$(OUTPUT_DIR)/%.svg: %.tex
	@mkdir -p $(OUTPUT_DIR)
	@echo "Processing $<..."
	@latex -shell-escape -interaction=nonstopmode -output-directory=. $<
	@dvisvgm $*.dvi --output=$@ --no-fonts
	@rm -f $*.aux $*.log $*.dvi
	@echo "Saved $@"

clean:
	rm -f $(OUTPUT_DIR)/*.svg ./*.aux ./*.log ./*.dvi
