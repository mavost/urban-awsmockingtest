import boto3
import json

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    print("Lambda function ARN:   ", context.invoked_function_arn)

    # get info on lambda tags
    lmbClient = boto3.client('lambda')
    tagResponse = lmbClient.list_tags(Resource=context.invoked_function_arn)
    print("Lambda Tag response:   ", tagResponse)
    
    stackName = tagResponse['Tags']['aws:cloudformation:stack-name']
    print("Lambda Stack name:   ", stackName)

    # get info on parent stack via tag info
    cfClient = boto3.client('cloudformation')
    stackResponse = cfClient.describe_stacks(StackName=stackName)
    print("CF response:    ", stackResponse)

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit my lambda function!'
    }