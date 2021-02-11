SHELL := /bin/bash

help:
	@echo 'Makefile for django-cache-url'
	@echo ''
	@echo 'Usage:'
	@echo '   make release      Make a puush a new release to PyPI'
	@echo '   make test         Run the test suite'
	@echo '   make lint         Run linting on the code'
	@echo ''

release:
	@./scripts/create_release.py

test:
	@pytest

lint:
	@flake8
