# Standard
import json

# Third Party
from cryptography.fernet import Fernet, InvalidToken
from decouple import config

# Local
from src.domain.exceptions.service.service_exceptions import (
    ServiceInvalidFernetKeyException,
    ServiceUnexpectedException,
)


class DeobfuscateDataService:
    __fernet_key = config("FERNET_KEY")
    __fernet_instance = Fernet(key=__fernet_key)

    @classmethod
    def __decode_value(cls, value: bytes) -> str:
        decoded_value = value.decode()

        return decoded_value

    @classmethod
    def deobfuscate_value(cls, value: bytes) -> str:
        try:
            deobfuscated_value = cls.__fernet_instance.decrypt(token=value)
            decoded_value = cls.__decode_value(value=deobfuscated_value)

            if "order_id" in decoded_value:
                decoded_value = json.loads(decoded_value)

            return decoded_value

        except InvalidToken as exception:
            raise ServiceInvalidFernetKeyException(
                operation="DeobfuscateDataService::deobfuscate_value",
                exception=exception,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="DeobfuscateDataService::deobfuscate_value",
                exception=exception,
            )
