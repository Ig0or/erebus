# Local
from src.domain.enums.exceptions.exceptions_message_enum import (
    ErebusExceptionMessageEnum,
)
from src.domain.exceptions.base.base_exception import BaseErebusException


class TransportResponseException(BaseErebusException):
    def __init__(
        self,
        operation: str,
        exception: Exception,
        message: str = ErebusExceptionMessageEnum.transport.RESPONSE_EXCEPTION,
    ):
        self.__operation = operation
        self.__exception = exception
        self.__message = message

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )


class TransportUnexpectedException(BaseErebusException):
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
