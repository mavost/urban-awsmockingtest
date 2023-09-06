# Testing of AWS components using pytest and mocking using the moto module

Purpose: running a few mocked tests of AWS S3 (boto3) functions using the moto module.

Assumes a Python installation > 3.9 and uses pytest > 7.0 in a virtual environment
for simplified path discovery.

Invoke the automatic build or a local python env and trigger of `pytest` into a `.log` file` using

```bash
make run_tests
```

or trigger a rebuild forcefully by

```bash
rm -f logs/test_results.log && make run_tests
```

in case there have been no changes to the code base on neither `src` nor `tests` side.
