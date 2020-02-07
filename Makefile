SHELL := /bin/bash

help:
	@echo 'Makefile for django-cache-url'
	@echo ''
	@echo 'Usage:'
	@echo '   make release      push to the PyPI'
	@echo '   make test         run the test suite'
	@echo ''

release:
	rm -rf build dist
	python setup.py sdist bdist_wheel
	twine upload dist/*

test:
	tox
