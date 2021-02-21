import unittest
from http import HTTPStatus
from unittest.mock import patch

from cvr import Client, UnauthorizedError


class TestAPIKey(unittest.TestCase):
    def test_api_key_http_ok(self):
        """ Verifies that test_api_key does not raise an error when HTTP OK
        is returned from the server.
        """
        client = Client(api_key='some-api-key')

        response = MockResponse(HTTPStatus.OK)
        with patch.object(client._session, 'get', return_value=response):
            client.test_api_key()

    def test_api_key_http_unauthorized(self):
        """ Verifies that test_api_key raises UnauthorizedError when HTTP
        Unauthorized is returned from the server.
        """
        client = Client(api_key='some-api-key')

        response = MockResponse(HTTPStatus.UNAUTHORIZED)
        with patch.object(client._session, 'get', return_value=response):
            with self.assertRaises(UnauthorizedError):
                client.test_api_key()


class MockResponse:
    def __init__(self, status_code, content=None, text=None):
        self.status_code = status_code
        self._content = content
        self.text = text

    def json(self):
        return self._content
