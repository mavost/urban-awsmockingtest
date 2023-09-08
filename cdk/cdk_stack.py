from aws_cdk import (
    Stack,
    CfnOutput
)
#import aws_cdk.aws_secretsmanager as secretsmanager
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, stage: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # attach the name, region of the underlying account(s) to the stack
        
        CfnOutput(self, f"{self.stack_name}-Name-{stage}",
            value=self.stack_name,
            description='Name of CF Stack',
            export_name=f"{self.stack_name}-Name-{stage}"
        )
        CfnOutput(self, f"{self.stack_name}-Account-{stage}", 
            value=self.account,
            description='Account ID of account',
            export_name=f"{self.stack_name}-Account-{stage}"
        )
        CfnOutput(self, f"{self.stack_name}-Region-{stage}",
            value=self.region,
            description='Region of account',
            export_name=f"{self.stack_name}-Region-{stage}"
        )

        # get latest version of plain string attribute from system manager during deployment
        #latest_string_token = ssm.StringParameter.value_for_string_parameter(
        #    self, "my-plain-parameter-name"
        #)

        # get access to the secret object
        # dbPasswordSecret = secretsmanager.Secret.fromSecretNameV2(
        #     self,
        #     'some_secret_id',
        #     'secret_name_in_store',
        # )

    

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
