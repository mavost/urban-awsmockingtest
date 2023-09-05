VENV_NAME?=mytestenv

PYTHON=${VENV_NAME}/bin/python

testvar?=somesetting

prepare_venv: $(VENV_NAME)/bin/activate

run_tests: tests/test_s3.py

tests/test_cmd_var.py: prepare_venv
	pytest -q $@ --cmdopt=$(testvar)

tests/test_s3.py: prepare_venv
	pytest -q $@

$(VENV_NAME)/bin/activate: requirements.txt
	python3 -m venv $(VENV_NAME)
	$(VENV_NAME)/bin/pip install -r $?
	touch $@

clean:
	rm -rf $(VENV_NAME)

