from .enums import ErrorMessageCodes


class ApiException(Exception):
    def __init__(self, msg: str, error_code: ErrorMessageCodes, status_code: int):
        self.msg = msg
        self.error_code = error_code
        self.status_code = status_code


class TokenError(Exception):
    pass


class TokenBackendError(Exception):
    pass


class ServiceNotAvailable(ApiException):
    def __init__(self, msg: str):
        super().__init__(msg, error_code=ErrorMessageCodes.BAD_REQUEST, status_code=400)


class ValidateFileContent(ApiException):
    def __init__(self, msg: str):
        super().__init__(msg, error_code=ErrorMessageCodes.BAD_REQUEST, status_code=400)


class ParsingFileFailed(ApiException):
    def __init__(self, msg: str):
        super().__init__(msg, error_code=ErrorMessageCodes.BAD_REQUEST, status_code=400)


class NotFound(ApiException):
    def __init__(self, msg: str):
        super().__init__(msg, error_code=ErrorMessageCodes.NOT_FOUND, status_code=404)


class AlreadyExists(ApiException):
    def __init__(self, msg: str):
        super().__init__(msg, error_code=ErrorMessageCodes.ALREADY_EXISTS, status_code=400)
