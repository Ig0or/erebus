# Third Party
from decouple import config
from kafka import KafkaConsumer

# Local
from src.infrastructure.kafka.kafka_infrastructure import KafkaInfrastructure


class StockMarketRepository:
    @staticmethod
    def subscribe_to_orders_topic() -> KafkaConsumer:
        topic_name = config("KAFKA_TOPIC_NAME")
        consumer = KafkaInfrastructure.get_consumer()

        consumer.subscribe(topics=topic_name)

        return consumer
