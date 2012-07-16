all:
	@./build/build.sh
init:
	@git submodule update;cd build/marked;make;


clean:
	@rm *.html

.PHONY: clean all
