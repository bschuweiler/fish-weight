import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response_valid_input(self):
        event = {
            'pathParameters': {
                'species': 'walleye',
                'length': '23.75'
            }
        }
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('walleye', result['body'])

    def test_response_invalid_input(self):
        event = {
            'pathParameters': {
                'species': 'Walleye',
                'length': '23.75'
            }
        }
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 500)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Error', result['body'])


if __name__ == '__main__':
    unittest.main()
