#! /bin/sh

rm -f deployments/*.zip
create_aws_lambda.py -i "main.py, AlexaDatadogHandler.py"
