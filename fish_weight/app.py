import json
import datetime
from .fishweight import lengthToWeight


def lambda_handler(event, context):
    """Fish Length to Weight Converter Lambda Function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    # TODO: Update these docs with specifics on input and returns

    try:
        if (not event or
                not event['pathParameters'] or
                not (len(event['pathParameters']) is 2) or
                not event['pathParameters']['species'] or
                not event['pathParameters']['length']):
            raise ValueError(
                "Missing one or both required parameters"
                "('species' and 'length')")

        species = event['pathParameters']['species']
        length = event['pathParameters']['length']

        response = lengthToWeight(species, length)

        return {
            'statusCode': 200,
            'body': response,
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        response = json.dumps({
            'Error': str(e)
        })
        return {
            'statusCode': 500,
            'body': response,
            'headers': {'Content-Type': 'application/json'}
        }
