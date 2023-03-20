# Standard
from enum import Enum


class GeneralExceptionMessageEnum(str, Enum):
    UNEXPECTED_EXCEPTION = "An unexpect error occurred."


class InfrastructureExceptionsMessageEnum(str, Enum):
    CONNECTION_ERROR = "Error while connecting to the data base."
    NO_BROKERS_AVAILABLE = "Error while connecting to the kafka broker."


class ServiceExceptionsMessageEnum(str, Enum):
    INVALID_FERNET_KEY = "Error decrypting topic value because the value signature isn't the same as your FERNET KEY in .env file"


class TransportExceptionsMessageEnum(str, Enum):
    RESPONSE_EXCEPTION = "There's a problem with the third party API called."


class ErebusExceptionMessageEnum:
    general = GeneralExceptionMessageEnum
    infrastructure = InfrastructureExceptionsMessageEnum
    service = ServiceExceptionsMessageEnum
    transport = TransportExceptionsMessageEnum
