import os
import unittest

from cvr.errors import UnauthorizedError

_ENV_API_KEY = "CVR_DEV_TEST_API_KEY"


def get_api_key():
    api_key = os.environ.get(_ENV_API_KEY, None)
    if not api_key:
        raise UnauthorizedError(
            "You must set '{key}' in order to run the live tests".format(
                key=_ENV_API_KEY)
        )
    return api_key


def skip_if_no_api_key(f):
    skip_tests = False
    try:
        get_api_key()
    except UnauthorizedError:
        return True

    return unittest.skipIf(skip_tests, "Env {} not set".format(_ENV_API_KEY))(f)
