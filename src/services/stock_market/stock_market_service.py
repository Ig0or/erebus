# Standard
from time import sleep

# Third Party
from kafka.consumer.fetcher import ConsumerRecord

# Local
from src.repositories.stock_market.stock_market_repository import StockMarketRepository


class StockMarketService:
    __time_to_sleep = 120

    @staticmethod
    async def __read_message(message: ConsumerRecord):
        pass

    @classmethod
    async def start_consume(cls):
        topic_consumer = StockMarketRepository.subscribe_to_orders_topic()

        for message in topic_consumer:
            if message:
                await cls.__read_message(message=message)

                continue

            sleep(cls.__time_to_sleep)
