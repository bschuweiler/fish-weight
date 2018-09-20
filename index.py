import json
import datetime
from fishweight import fishweight


def handler(event, context):
    if (not event or
            not event['pathParameters'] or
            not (len(event['pathParameters']) is 2) or
            not event['pathParameters']['species'] or
            not event['pathParameters']['length']):
        raise ValueError(
            "Missing one or both required parameters ('species' and 'length')")

    species = event['pathParameters']['species']
    length = event['pathParameters']['length']

    response = fishweight.lengthToWeight(species, length)

    return {
        'statusCode': 200,
        'body': response,
        'headers': {'Content-Type': 'application/json'}
    }
