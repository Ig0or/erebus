# Third Party
from decouple import config
from kafka import KafkaConsumer

# Local
from src.services.obfuscate_data.obfuscate_data_service import DeobfuscateDataService

#
# class KafkaInfrastructure:
#     __producer = None
#
#     @classmethod
#     def get_producer(cls) -> KafkaConsumer:
#         if cls.__producer is None:
#             producer_config = {
#                 "bootstrap_servers": config("KAFKA_URL"),
#                 "client_id": config("KAFKA_CLIENT_ID"),
#                 "key_serializer": ObfuscateDataService.obfuscate_value,
#                 "value_serializer": ObfuscateDataService.obfuscate_value,
#             }
#
#             cls.__producer = KafkaConsumer(**producer_config)
#
#         return cls.__producer
