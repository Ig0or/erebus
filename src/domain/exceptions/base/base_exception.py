class BaseErebusException(Exception):
    def __init__(self, operation: str, exception: Exception, message: str):
        self.__operation = operation
        self.__exception = exception
        self.__message = message

    @property
    def operation(self) -> str:
        return self.__operation

    @property
    def exception(self) -> Exception:
        return self.__exception

    @property
    def message(self) -> str:
        return self.__message
