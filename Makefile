.PHONY: serve build

serve:
	python3 -m http.server 8080

build:
	bash build.sh
