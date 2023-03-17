class BaseErebusException(Exception):
    def __init__(self, operation: str, exception: Exception, message: str):
        self.__operation = operation
        self.__exception = exception
        self.__message = message
