import pytest
import logging

from lambda_reporter.reporter import handler

# fixtures for test suite
# https://aws.amazon.com/blogs/devops/unit-testing-aws-lambda-with-python-and-mock-aws-services/

@pytest.fixture
def test_context():
    class Context:
        invoked_function_arn = 'my_aws_arn'
    return Context()

@pytest.fixture
def test_event():
    return {"testinput_1": "eu-central-1"}

@pytest.fixture
def lambda_setup(lambda_client):
    yield

@pytest.fixture
def test_response():
    return {"response": "123"}

# test cases
def test_input_output(lambda_client, lambda_setup, test_event, test_context, test_response):
    with lambda_client as client:
        client.list_tags(Resource='123')
    response = handler(event=test_event, context=test_context)
    assert response == test_response
