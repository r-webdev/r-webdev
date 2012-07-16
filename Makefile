all:
	@./build/build.sh
init:
	@./build/init.sh

clean:
	@rm *.html

.PHONY: clean all
