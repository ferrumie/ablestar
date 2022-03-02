class ProductResourceException(BaseException):
    """Base Exception For Product Resources"""

    status_code = 500


class NotFoundException(ProductResourceException):
    """Resource Not Found."""

    status_code = 404


class UnAuthorizedException(ProductResourceException):
    """Not Authorized."""

    status_code = 401


class ForbiddenException(ProductResourceException):
    """Request Forbidden."""

    status_code = 403


class PaymentRequiredException(ProductResourceException):
    """Payment Required."""

    status_code = 402


class UnprocessableEntityException(ProductResourceException):
    """Unprocessable Entity."""

    status_code = 422


class ClientErrorException(ProductResourceException):
    """Client Error."""

    status_code = 400
