import logging
from AlexaNextBusHandler import AlexaNextBusHandler


#  Main entry point for the Lambda function.
#  In the AWS Lamba console, under the 'Configuration' tab there is an
#  input field called, 'Handler'.  That should be:  main.lambda_handler

#  Handler: main.lambda_handler
#  Role: lambda_basic_execution



logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logging.info("Executing main lambda_handler for YourDeploymentHandler class")

    deployment_handler = AlexaNextBusHandler()
    # handler_response = deployment_handler._test_response("next bus")
    handler_response = deployment_handler.process_request(event, context)

    return handler_response

