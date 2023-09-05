# Testing of AWS components using pytest and mocking using the moto module

Assumes a Python installation > 3.9 and uses pytest > 7.0 in a virtual environment
for simplified path discovery.

Invoking
```bash
make run_tests
```
should set up the testing environment and run a few very basic tests against the AWS S3 client class defined in `./src`.
