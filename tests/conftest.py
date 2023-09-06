import boto3
import os
import pytest
import logging

from moto import mock_s3, mock_sqs

# this is for testing commands with parameters, see test_cmd_var.py
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


# print name of test case as bracket
@pytest.fixture(scope='function', autouse=True)
def test_log(request):
    logging.info(f"STARTED Test {request.node.originalname}")
    def fin():
        logging.info(f"COMPLETED Test {request.node.originalname}")
    request.addfinalizer(fin)


# start of aws global fixtures
@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        conn = boto3.client("s3", region_name="eu-central-1")
        yield conn


@pytest.fixture
def sqs_client(aws_credentials):
    with mock_sqs():
        conn = boto3.client("sqs", region_name="eu-central-1")
        yield conn
