SHELL := /bin/bash

VENV_NAME ?= mytestenv

PYTHON = $(VENV_NAME)/bin/python
PYTEST = $(VENV_NAME)/bin/pytest

testvar ?= somesetting

.PHONY: run_tests clean

run_tests: logs/test_results.log

# actual test cases
logs/test_results.log: tests/test_s3.py src/*.py tests/conftest.py pytest.ini $(PYTEST)
	$(PYTEST) $<
	mv $@ $(subst .py,.log,$(subst tests/,logs/,$<))


# after installation of venv and req. we should have a pytest executable
$(PYTEST): requirements.txt
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

# preparing python environment
#$(VENV_NAME)/bin/activate: requirements.txt
#	python3 -m venv $(VENV_NAME)
#	$(VENV_NAME)/bin/pip install -r $<

# run_via_source: tests/test_s3.py
#	source $(VENV_NAME)/bin/activate && pytest $<

# run_via_python: tests/test_s3.py
#	$(PYTHON) -m pytest $<
