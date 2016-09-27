CONF := custodia.conf
PREFIX := /usr
PYTHON := python3
DOCS_DIR = docs

.NOTPARALLEL:
.PHONY: all clean clean_socket cscope docs lint pep8 test

all: clean_socket lint pep8 test docs
	echo "All tests passed"

clean_socket:
	rm -f server_socket

lint: clean_socket
	tox -e lint

pep8: clean_socket
	tox -e pep8py2
	tox -e pep8py3

clean: clean_socket
	rm -fr build dist *.egg-info .tox MANIFEST .coverage .cache
	rm -f custodia.audit.log secrets.db
	rm -rf docs/build
	find ./ -name '*.py[co]' -exec rm -f {} \;
	find ./ -depth -name __pycache__ -exec rm -rf {} \;
	rm -rf tests/tmp

cscope:
	git ls-files | xargs pycscope

test: clean_socket
	rm -f .coverage
	tox --skip-missing-interpreters -e py27
	tox --skip-missing-interpreters -e py34
	tox --skip-missing-interpreters -e py35

README: README.md
	echo -e '.. WARNING: AUTO-GENERATED FILE. DO NOT EDIT.\n' > $@
	pandoc --from=markdown --to=rst $< >> $@

.PHONY: install egg_info run release
install: clean_socket egg_info
	$(PYTHON) setup.py install --root "$(PREFIX)"

egg_info:
	$(PYTHON) setup.py egg_info

release: clean_socket egg_info README
	$(PYTHON) setup.py packages

run: egg_info
	$(PYTHON) -m custodia.server $(CONF)
