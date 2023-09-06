SHELL := /bin/bash

VENV_NAME ?= mytestenv

PYTHON = $(VENV_NAME)/bin/python

testvar ?= somesetting

.PHONY: run_tests clean

run_tests: tests/test_s3.py

tests/test_cmd_var.py: $(VENV_NAME)/bin/activate
	source $(VENV_NAME)/bin/activate && pytest -q $@ --cmdopt=$(testvar)

tests/test_s3.py: $(VENV_NAME)/bin/activate
	source $(VENV_NAME)/bin/activate && pytest -q $@

$(VENV_NAME)/bin/activate: requirements.txt
	python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -r $?

clean:
	rm -rf $(VENV_NAME)

