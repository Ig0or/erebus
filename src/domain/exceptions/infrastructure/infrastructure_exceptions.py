# Local
from src.domain.enums.exceptions.exceptions_message_enum import (
    ErebusExceptionMessageEnum,
)
from src.domain.exceptions.base.base_exception import BaseErebusException


class InfrastructureKafkaNoBrokersException(BaseErebusException):
    def __init__(
        self,
        operation: str,
        exception: Exception,
        message: str = ErebusExceptionMessageEnum.infrastructure.NO_BROKERS_AVAILABLE,
    ):
        self.__operation = operation
        self.__exception = exception
        self.__message = message

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )


class InfrastructureMongoConnectionErrorException(BaseErebusException):
    def __init__(
        self,
        operation: str,
        exception: Exception,
        message: str = ErebusExceptionMessageEnum.infrastructure.CONNECTION_ERROR,
    ):
        self.__operation = operation
        self.__exception = exception
        self.__message = message

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )


class InfrastructureUnexpectedException(BaseErebusException):
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
