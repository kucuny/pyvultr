import unittest
from pyvultr import util


class TestPyvultrUtil(unittest.TestCase):
    def test_get_error_description_is_valid(self):
        self.assertEqual('Function successfully executed',
                         util.get_error_description(200))
        self.assertEqual('Invalid API location. Check the URL that you are using',
                         util.get_error_description(400))
        self.assertEqual('Invalid or missing API key. Check that your API key is present and matches your assigned key',
                         util.get_error_description(403))
        self.assertEqual('Invalid HTTP method. Check that the method (POST|GET) matches what the documentation indicates',
                         util.get_error_description(405))
        self.assertEqual('Request failed. Check the response body for a more detailed description',
                         util.get_error_description(412))
        self.assertEqual('Internal server error. Try again at a later time',
                         util.get_error_description(500))
        self.assertEqual('Rate limit hit. API requests are limited to an average of 1/s. Try your request again later.',
                         util.get_error_description(503))
