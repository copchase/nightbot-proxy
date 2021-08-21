import lambda_function


def test_lambda_handler(mocker):
    mocker.patch("boto3.client")
    event = {
        "queryStringParameters": {
            "operation": "d20"
        }
    }

    result = lambda_function.lambda_handler(event, None)

    assert result["statusCode"] == 200
    assert result["body"] == " "
