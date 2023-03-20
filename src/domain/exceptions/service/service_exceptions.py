# Local
from src.domain.enums.exceptions.exceptions_message_enum import (
    ErebusExceptionMessageEnum,
)
from src.domain.exceptions.base.base_exception import BaseErebusException


class ServiceInvalidFernetKeyException(BaseErebusException):
    def __init__(
        self,
        operation: str,
        exception: Exception,
        message: str = ErebusExceptionMessageEnum.service.INVALID_FERNET_KEY,
    ):
        self.__operation = operation
        self.__exception = exception
        self.__message = message

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )


class ServiceUnexpectedException(BaseErebusException):
    def __init__(
        self,
        operation: str,
        exception: Exception,
        message: str = ErebusExceptionMessageEnum.general.UNEXPECTED_EXCEPTION,
    ):
        self.__operation = operation
        self.__exception = exception
        self.__message = message

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )
