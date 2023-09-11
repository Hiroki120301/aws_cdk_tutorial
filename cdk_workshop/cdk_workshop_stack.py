from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
)


class CdkWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Defines 