# Standard
from time import sleep
from typing import NoReturn

# Third Party
from kafka.consumer.fetcher import ConsumerRecord

from src.domain.enums.stock_market.stock_market_enums import (
    OrderStatusEnum,
    OrderMessageEnum,
)
from src.domain.extensions.stock_market.order_extension import (
    StockMarketExtension,
)
from src.domain.models.stock_market.order_model import OrderModel

# Local
from src.repositories.stock_market.stock_market_repository import StockMarketRepository
from src.services.alphavantage.alphavantage_service import AlphavantageService


class StockMarketService:
    __time_to_sleep = 120

    @staticmethod
    async def __update_order(
        order_model: OrderModel, status: OrderStatusEnum, message: OrderMessageEnum
    ) -> NoReturn:
        order_model["order_status"] = status
        order_model["order_message"] = message

        await StockMarketRepository.update_order_on_database(order_model=order_model)

        return

    @staticmethod
    async def __check_symbol_price(symbol: str) -> float:
        # symbol_price =
        pass

    @staticmethod
    async def __check_symbol_exist(symbol: str) -> str:
        symbols_model = await AlphavantageService.symbol_search(symbol=symbol)

        if symbols_model:
            market_symbol = symbols_model[0]["symbol"]

            return market_symbol

    @classmethod
    async def __process_order(cls, message: ConsumerRecord) -> NoReturn:
        order_model = StockMarketExtension.to_order_model(order=message.value)

        market_symbol = await cls.__check_symbol_exist(symbol=order_model["symbol"])

        if not market_symbol:
            await cls.__update_order(
                order_model=order_model,
                status=OrderStatusEnum.CANCELLED,
                message=OrderMessageEnum.INVALID_SYMBOL,
            )

            return

        order_model["symbol"] = market_symbol

    @classmethod
    async def start_consume(cls):
        topic_consumer = StockMarketRepository.subscribe_to_orders_topic()

        for message in topic_consumer:
            if message:
                await cls.__process_order(message=message)

                continue

            sleep(cls.__time_to_sleep)

        topic_consumer.commit()


import asyncio

a = asyncio.get_event_loop()
a.run_until_complete(StockMarketService.start_consume())
