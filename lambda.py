import logging
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("This is a test log for info")
    logger.error("This is a test log for error")
    logger.error("Testing CI/CD")

    logger.error("Testing if the lambda function works")


    return {
        'statusCode': 200,
        'body': 'Hello from Lambda v5!'
    }