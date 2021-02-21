from http import HTTPStatus

from cvr.errors import (UnauthorizedError, NotFoundError, InternalServerError,
                        PaymentRequiredError, UnhandledStatusCode)


def handle_response_status_code(response):
    if response.status_code == HTTPStatus.OK:
        return

    if response.status_code == HTTPStatus.UNAUTHORIZED:
        raise UnauthorizedError('Invalid API key')
    if response.status_code == HTTPStatus.NOT_FOUND:
        raise NotFoundError('Entity not found')
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        raise InternalServerError('Something went wrong. Try again later')
    if response.status_code == HTTPStatus.PAYMENT_REQUIRED:
        raise PaymentRequiredError(
            'You have insufficient credits to perform the requested action'
        )

    raise UnhandledStatusCode(
        "Got HTTP status code {s}, but it's not handled".format(s=response.status_code)
    )
