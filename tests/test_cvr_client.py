import unittest
from http import HTTPStatus
from unittest.mock import patch

from cvr import Client, UnauthorizedError, InternalServerError


class TestCVRProduktionsenheder(unittest.TestCase):
    def test_unauthorized(self):
        """ Verifies that UnauthorizedError is raised when the client receives
        HTTP status code 401.
        """
        client = Client(api_key='some-api-key')

        response = MockResponse(HTTPStatus.UNAUTHORIZED)
        with patch.object(client._session, 'get', return_value=response):
            with self.assertRaises(UnauthorizedError):
                client.cvr.produktionsenheder(adresse="adresse")

    def test_server_error(self):
        """ Verifies that InternalServerError is raised when the client receives
        HTTP status code 500.
        """
        client = Client(api_key='some-api-key')

        response = MockResponse(HTTPStatus.INTERNAL_SERVER_ERROR)
        with patch.object(client._session, 'get', return_value=response):
            with self.assertRaises(InternalServerError):
                client.cvr.produktionsenheder(adresse="adresse")

    def test_produktionsenhed_not_found(self):
        """ Verifies that the client returns an empty list when HTTP status code
        404 is received.
        """
        client = Client(api_key='some-api-key')

        response = MockResponse(HTTPStatus.NOT_FOUND)
        with patch.object(client._session, 'get', return_value=response):
            produktionsenheder = client.cvr.produktionsenheder(adresse="some adresse")
            self.assertEqual(0, len(produktionsenheder))

    def test_produktionsenhed_success(self):
        """ Verifies that the client returns a list of Produktionsenheder and
        deserializes them when HTTP status code 200 is returned.
        """
        client = Client(api_key='some-api-key')

        expected = [
            {"pNummer": 1234},
            {"pNummer": 2345},
            {"pNummer": 3456},
        ]

        response = MockResponse(
            status_code=HTTPStatus.OK,
            content=expected,
        )
        with patch.object(client._session, 'get', return_value=response):
            produktionsenheder = client.cvr.produktionsenheder(adresse="some adresse")
            self.assertEqual(len(expected), len(produktionsenheder))
            for i, penhed in enumerate(expected):
                self.assertEqual(penhed["pNummer"], produktionsenheder[i].p_nummer)


class MockResponse:
    def __init__(self, status_code, content=None):
        self.status_code = status_code
        self._content = content

    def json(self):
        return self._content
