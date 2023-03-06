# Third Party
from decouple import config
from kafka import KafkaConsumer

# Local
from src.services.deobfuscate_data.deobfuscate_data_service import (
    DeobfuscateDataService,
)


class KafkaInfrastructure:
    __consumer = None

    @classmethod
    def get_consumer(cls) -> KafkaConsumer:
        if cls.__consumer is None:
            consumer_config = {
                "bootstrap_servers": config("KAFKA_URL"),
                "client_id": config("KAFKA_CLIENT_ID"),
                "group_id": config("KAFKA_GROUP_ID"),
                "auto_offset_reset": "earliest",
                "key_deserializer": DeobfuscateDataService.deobfuscate_value,
                "value_deserializer": DeobfuscateDataService.deobfuscate_value,
            }

            cls.__consumer = KafkaConsumer(**consumer_config)

        return cls.__consumer
