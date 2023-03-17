# Local
from src.domain.enums.exceptions.exceptions_message_enum import (
    ErebusExceptionMessageEnum,
)
from src.domain.exceptions.base.base_exception import BaseErebusException


class InfrastructureKafkaNoBrokersException(BaseErebusException):
    def __init__(self, operation: str, exception: Exception):
        self.__operation = operation
        self.__exception = exception
        self.__message = ErebusExceptionMessageEnum.infrastructure.NO_BROKERS_AVAILABLE

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )


class InfrastructureUnexpectedException(BaseErebusException):
    def __init__(self, operation: str, exception: Exception):
        self.__operation = operation
        self.__exception = exception
        self.__message = ErebusExceptionMessageEnum.general.UNEXPECT_EXCEPTION

        super().__init__(
            operation=self.__operation,
            exception=self.__exception,
            message=self.__message,
        )
