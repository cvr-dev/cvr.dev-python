import unittest

from cvr import Client, UnauthorizedError
from tests.utils import skip_if_no_api_key, get_api_key


@skip_if_no_api_key
class TestAPIKeyLive(unittest.TestCase):
    def test_api_key_valid_api_key(self):
        """ Verifies that test_api_key succeeds with a valid api key. """
        with Client(api_key=get_api_key()) as client:
            client.test_api_key()

    def test_api_key_invalid_api_key(self):
        """
        Verifies that test_api_key raises an error using an invalid api key.
        """
        with Client(api_key="invalid api key") as client:
            with self.assertRaises(UnauthorizedError):
                client.test_api_key()
