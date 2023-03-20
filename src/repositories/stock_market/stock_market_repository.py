# Third Party
from decouple import config
from kafka import KafkaConsumer
from typing import NoReturn

# Local
from src.domain.exceptions.base.base_exception import BaseErebusException
from src.domain.exceptions.repository.repository_exceptions import (
    RepositoryUnexpectedException,
)
from src.domain.models.stock_market.order_model import OrderModel
from src.infrastructure.kafka.kafka_infrastructure import KafkaInfrastructure
from src.infrastructure.mongodb.mongodb_infrastructure import MongoDBInfrastructure


class StockMarketRepository:
    @staticmethod
    def subscribe_to_orders_topic() -> KafkaConsumer:
        try:
            topic_name = config("KAFKA_TOPIC_NAME")
            consumer = KafkaInfrastructure.get_consumer()

            consumer.subscribe(topics=topic_name)

            return consumer

        except BaseErebusException as exception:
            raise RepositoryUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise RepositoryUnexpectedException(
                operation="StockMarketRepository::subscribe_to_orders_topic",
                exception=exception,
            )

    @staticmethod
    async def update_order_on_database(order_model: OrderModel) -> NoReturn:
        try:
            connection = MongoDBInfrastructure.get_connection()

            query_filter = {"order_id": order_model["order_id"]}
            updated_object = {"$set": order_model}

            connection.update_one(filter=query_filter, update=updated_object)

            return

        except BaseErebusException as exception:
            raise RepositoryUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise RepositoryUnexpectedException(
                operation="StockMarketRepository::update_order_on_database",
                exception=exception,
            )
