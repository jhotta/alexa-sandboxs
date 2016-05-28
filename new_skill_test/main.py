import logging
from AlexaHandler import AlexaDeploymentTestHandler

#  Main entry point for the Lambda function.
#  In the AWS Lamba console, under the 'Configuration' tab there is an
#  input field called, 'Handler'.  That should be:  main.lambda_handler

#  Handler: main.lambda_handler
#  Role: lambda_basic_execution



logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info("Executing main lambda_handler for AlexaDeploymentTestHandler class")

    deployment_handler = AlexaDeploymentTestHandler()
    # handler_response = deployment_handler.process_request(event, context)
    handler_response = deployment_handler._test_response("")

    return handler_response
