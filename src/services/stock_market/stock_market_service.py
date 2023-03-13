# Standard
from time import sleep
from typing import NoReturn

# Third Party
from kafka.consumer.fetcher import ConsumerRecord

# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderMessageEnum,
    OrderStatusEnum,
)
from src.domain.extensions.stock_market.order_extension import (
    StockMarketExtension,
)
from src.domain.models.stock_market.order_model import OrderModel
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

        if order_model.get("unit_price"):
            order_model["total_price"] = (
                order_model["quantity"] * order_model["unit_price"]
            )

        await StockMarketRepository.update_order_on_database(order_model=order_model)

        return

    @staticmethod
    async def __check_symbol_price(symbol: str) -> float:
        symbol_price_model = await AlphavantageService.symbol_price(symbol=symbol)

        return symbol_price_model["close"]

    @staticmethod
    async def __check_symbol_exists(symbol: str) -> str:
        symbols_model = await AlphavantageService.symbol_search(symbol=symbol)

        if symbols_model:
            market_symbol = symbols_model[0]["symbol"]

            return market_symbol

    @staticmethod
    async def __process_order(message: ConsumerRecord) -> NoReturn:
        order_model = StockMarketExtension.to_order_model(order=message.value)

        market_symbol = await StockMarketService.__check_symbol_exists(
            symbol=order_model["symbol"]
        )

        if not market_symbol:
            await StockMarketService.__update_order(
                order_model=order_model,
                status=OrderStatusEnum.CANCELLED,
                message=OrderMessageEnum.INVALID_SYMBOL,
            )

            return

        symbol_unit_price = await StockMarketService.__check_symbol_price(
            symbol=market_symbol
        )

        order_model["symbol"] = market_symbol
        order_model["unit_price"] = symbol_unit_price

        await StockMarketService.__update_order(
            order_model=order_model,
            status=OrderStatusEnum.FINISHED,
            message=OrderMessageEnum.ORDER_PROCESSED,
        )

        return

    @classmethod
    async def start_consume(cls):
        topic_consumer = StockMarketRepository.subscribe_to_orders_topic()

        for message in topic_consumer:
            if message:
                await cls.__process_order(message=message)

                continue

            sleep(cls.__time_to_sleep)
