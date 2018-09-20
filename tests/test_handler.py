import unittest
import index


class TestHandlerCase(unittest.TestCase):

    def test_response(self):
        event = {
            'pathParameters': {
                'species': 'Walleye',
                'length': '23.75'
            }
        }
        result = index.handler(event, None)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')
        self.assertIn('Walleye', result['body'])


if __name__ == '__main__':
    unittest.main()
