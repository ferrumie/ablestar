class ProductResourceException(BaseException):
    """Base Exception For Product Resources"""

    status_code = 500


class NotFoundException(BaseException):
    """Resource Not Found."""

    status_code = 404


class UnAuthorizedException(BaseException):
    """Not Authorized."""

    status_code = 401


class ForbiddenException(BaseException):
    """Request Forbidden."""

    status_code = 403


class PaymentRequiredException(BaseException):
    """Payment Required."""

    status_code = 402


class UnprocessableEntityException(BaseException):
    """Unprocessable Entity."""

    status_code = 422


class ClientErrorException(BaseException):
    """Client Error."""

    status_code = 400
