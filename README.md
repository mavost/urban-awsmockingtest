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

## How to start out with AWS CDK based on Python

The `cdk.json` file tells the CDK Toolkit how to execute your app.

To activate the virtualenv on MacOS and Linux:

```bash
source mytestenv/bin/activate
```

At this point you can now synthesize the CloudFormation template for this code,
most likely by referring to a aws access profile.

``` bash
cdk synth --profile <PROFILE_NAME>
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

* `cdk ls`          list all stacks in the app
* `cdk synth`       emits the synthesized CloudFormation template
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk docs`        open CDK documentation
