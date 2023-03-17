# Standard
from enum import Enum


class GeneralExceptionMessageEnum(str, Enum):
    UNEXPECT_EXCEPTION = "An unexpect error occurred."


class InfrastructureExceptionsMessageEnum(str, Enum):
    NO_BROKERS_AVAILABLE = "Error while connecting to the kafka broker."


class ServiceExceptionsMessageEnum(str, Enum):
    INVALID_FERNET_KEY = "Error decrypting topic value because the value signature isn't the same as your FERNET KEY in .env file"


class ErebusExceptionMessageEnum:
    general = GeneralExceptionMessageEnum
    infrastructure = InfrastructureExceptionsMessageEnum
    service = ServiceExceptionsMessageEnum