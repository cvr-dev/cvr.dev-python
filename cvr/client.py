from requests_toolbelt.sessions import BaseUrlSession

from cvr.cvr_client import CVRClient
from cvr.http_helpers import handle_response_status_code


_BASE_URL = 'https://api.cvr.dev/api/'


class Client:
    """ cvr.dev API client.

    Contains a dedicated client for the /cvr/ part of the API.
    See https://docs.cvr.dev/#ra-cvr-data for more info.
    """

    def __init__(self, api_key):
        self._session = BaseUrlSession(_BASE_URL)
        self._session.headers.update({'Authorization': api_key})

        self.cvr = CVRClient(self._session)

    def test_api_key(self):
        resp = self._session.get('test/apikey')
        handle_response_status_code(resp)

    def close(self):
        self._session.close()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
