import os
import boto3
import json


def lambda_handler(event: dict, context) -> dict:
    env = os.environ.get("ENV", "stage")
    operation = event["queryStringParameters"].get("operation")

    if operation:
        lambda_client = boto3.client("lambda")
        lambda_client.invoke(
            FunctionName=f"{env}-{operation}",
            InvocationType="Event",
            LogType="None",
            Payload=json.dumps(event).encode()
        )

    # Async functionality
    # Return immediately to Nightbot
    return {
        "statusCode": 200,
        "body": " "
    }
