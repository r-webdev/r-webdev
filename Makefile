all:
	@./build/build.sh
init:
	@git submodule add https://github.com/chjj/marked.git build/marked;cd build/marked;make;


clean:
	@rm *.html

.PHONY: clean all
