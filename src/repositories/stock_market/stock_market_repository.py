# Third Party
from decouple import config
from kafka import KafkaConsumer
from typing import NoReturn

# Local
from src.domain.models.stock_market.order_model import OrderModel
from src.infrastructure.kafka.kafka_infrastructure import KafkaInfrastructure
from src.infrastructure.mongodb.mongodb_infrastructure import MongoDBInfrastructure


class StockMarketRepository:
    @staticmethod
    def subscribe_to_orders_topic() -> KafkaConsumer:
        topic_name = config("KAFKA_TOPIC_NAME")
        consumer = KafkaInfrastructure.get_consumer()

        consumer.subscribe(topics=topic_name)

        return consumer

    @staticmethod
    async def update_order_on_database(order_model: OrderModel) -> NoReturn:
        connection = MongoDBInfrastructure.get_connection()

        query_filter = {"order_id": order_model["order_id"]}
        updated_object = {"$set": order_model}

        connection.update_one(filter=query_filter, update=updated_object)

        return

