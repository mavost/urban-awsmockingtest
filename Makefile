SHELL := /bin/bash

VENV_NAME ?= mytestenv

PYTHON = $(VENV_NAME)/bin/python

testvar ?= somesetting

.PHONY: run_tests clean

run_tests: logs/test_results.log

# actual test cases
logs/test_results.log: tests/test_s3.py src/*.py tests/conftest.py pytest.ini
	source $(VENV_NAME)/bin/activate && pytest -q $<

# preparing python environment
$(VENV_NAME)/bin/activate: requirements.txt
	python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -r $<

clean:
	rm -rf $(VENV_NAME)
	rm -rf **/__pycache__
	rm -rf .pytest_cache
	rm -rf logs/*.log

# another experiment with command line
tests/test_cmd_var.py:
	source $(VENV_NAME)/bin/activate && pytest -q $@ --cmdopt=$(testvar)

