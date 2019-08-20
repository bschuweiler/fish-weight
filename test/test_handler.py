import json
import pytest
from fish_weight.app import lambda_handler


@pytest.fixture()
def walleye_event():
    return {
        'pathParameters': {
            'species': 'walleye',
            'length': '23.75'
        }
    }


@pytest.fixture()
def invalid_species_event():
    return {
        'pathParameters': {
            'species': 'something',
            'length': '23.75'
        }
    }


def test_response_valid_input(walleye_event):
    result = lambda_handler(walleye_event, None)
    data = json.loads(result['body'])

    assert result['statusCode'] == 200
    assert 'walleye' in result['body']
    assert result['headers']['Content-Type'] == 'application/json'


def test_response_invalid_input(invalid_species_event):
    result = lambda_handler(invalid_species_event, None)
    data = json.loads(result['body'])

    assert result['statusCode'] == 500
    assert result['headers']['Content-Type'] == 'application/json'
    assert 'Error'in result['body']
