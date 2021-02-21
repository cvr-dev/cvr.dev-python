from cvr.http_helpers import handle_response_status_code
from cvr.errors import InvalidRequestError, NotFoundError
from cvr.dto import produktionsenhed, virksomhed


class CVRClient:
    """ cvr.dev cvr API Client.

    This client wraps the /cvr/ part of the cvr.dev API.
    This API returns cvr data verbatim as it was retrieved from Virk.dk's
    database. NOTE: _this data is returned as-is and has not been validated in
    any way_!
    """

    def __init__(self, session):
        self._session = session

    def produktionsenheder(self, adresse=None, p_numre=None):
        """ Retrieve produktionsenheder by either adresse or p_numre. adresse and p_numre
        are mutually exclusive; if both are set, InvalidRequestError will be returned.

        adresse must be a string.
        p_numre must be a list of ints (or string-encoded ints).
        """
        if adresse and p_numre:
            raise InvalidRequestError(
                "Only one of 'adresse' and 'p_numre' may be used at once"
            )

        params = {}
        if adresse:
            params["adresse"] = adresse

        if p_numre:
            if not is_iterable(p_numre):
                raise InvalidRequestError("'p_numre' must be an iterable")
            params["p_nummer"] = ','.join(str(p_nummer) for p_nummer in p_numre)

        resp = self._session.get('cvr/produktionsenhed', params=params)
        try:
            handle_response_status_code(resp)
        except NotFoundError:
            return []

        return produktionsenhed.map_to_objects(resp.json())

    def virksomheder(self, navn=None, cvr_numre=None):
        """ Retrieve virksomheder by either navn or cvr_numre. navm and cvr_numre
        are mutually exclusive; if both are set, InvalidRequestError will be returned.

        navn must be a string.
        cvr_numre must be a list of ints (or string-encoded ints).
        """
        if navn and cvr_numre:
            raise InvalidRequestError(
                "Only one of 'navn' and 'cvr_numre' may be used at once"
            )

        params = {}
        if navn:
            params["navn"] = navn

        if cvr_numre:
            if not is_iterable(cvr_numre):
                raise InvalidRequestError("'cvr_numre' must be an iterable")
            params["cvr_nummer"] = ','.join(str(cvr_nummer) for cvr_nummer in cvr_numre)

        resp = self._session.get('cvr/virksomhed', params=params)
        try:
            handle_response_status_code(resp)
        except NotFoundError:
            return []

        return virksomhed.map_to_objects(resp.json())


def is_iterable(v):
    try:
        iter(v)
        return True
    except TypeError:
        return False
