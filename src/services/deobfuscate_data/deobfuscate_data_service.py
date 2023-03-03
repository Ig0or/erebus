# Third Party
from cryptography.fernet import Fernet
from decouple import config


class DeobfuscateDataService:
    __fernet_key = config("FERNET_KEY")
    __fernet_instance = Fernet(key=__fernet_key)

    @classmethod
    def __decode_value(cls, value: bytes) -> str:
        decoded_value = value.decode()

        return decoded_value

    @classmethod
    def deobfuscate_value(cls, value: bytes) -> str:
        deobfuscated_value = cls.__fernet_instance.decrypt(token=value)
        decoded_value = cls.__decode_value(value=deobfuscated_value)

        return decoded_value
