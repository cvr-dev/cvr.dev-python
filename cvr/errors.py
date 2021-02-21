class CVRError(Exception):
    """ All CVR-errors wrap CVRError """


class UnauthorizedError(CVRError):
    """ Raised when the API key is invalid """


class NotFoundError(CVRError):
    """ Raised when a requested entity was not found """


class InvalidRequestError(CVRError):
    """ Raised when attempting to build a request that is invalid """


class InternalServerError(CVRError):
    """ Raised when an endpoint returns HTTP status code 500 """


class PaymentRequiredError(CVRError):
    """ Raised when your subscription does not have sufficient credits to perform the requested action """


class UnhandledStatusCode(CVRError):
    """ Raised when an endpoint returns an unhandled status code """
