import boto3
import json
from contextlib import closing
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logging.info(f"Event request:         {json.dumps(event)}")
    logging.info(f"Lambda function ARN:   {context.invoked_function_arn}")

    # get info on lambda tags
    with closing(boto3.client('lambda')) as lmb_client:
        tagResponse = lmb_client.list_tags(Resource=context.invoked_function_arn)
        logging.info(f"Lambda Tag response:   {tagResponse}")
    
        stackName = tagResponse['Tags']['aws:cloudformation:stack-name']
        logging.info(f"Lambda Stack name:     {stackName}")

    # get info on parent stack via tag info
    with closing(boto3.client('cloudformation')) as cfm_client:
        stackResponse = cfm_client.describe_stacks(StackName=stackName)
        logging.info(f"CF response:           {stackResponse}")

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit my lambda function!'
    }