# Standard
from typing import NoReturn

# Third Party
from kafka.consumer.fetcher import ConsumerRecord
import loglifos

# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderMessageEnum,
    OrderStatusEnum,
)
from src.domain.exceptions.base.base_exception import BaseErebusException
from src.domain.exceptions.service.service_exceptions import ServiceUnexpectedException
from src.domain.extensions.stock_market.order_extension import (
    StockMarketExtension,
)
from src.domain.models.stock_market.order_model import OrderModel
from src.repositories.stock_market.stock_market_repository import StockMarketRepository
from src.services.alphavantage.alphavantage_service import AlphavantageService


class StockMarketService:
    @staticmethod
    async def __update_order(
        order_model: OrderModel, status: OrderStatusEnum, message: OrderMessageEnum
    ) -> NoReturn:
        try:
            order_model.update({"order_status": status, "order_message": message})

            if order_model.get("unit_price"):
                total_price = order_model["quantity"] * order_model["unit_price"]

                order_model.update({"total_price": total_price})

            await StockMarketRepository.update_order_on_database(
                order_model=order_model
            )

            return

        except BaseErebusException as exception:
            raise ServiceUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="StockMarketService::__update_order",
                exception=exception,
            )

    @staticmethod
    async def __check_symbol_price(symbol: str) -> float:
        try:
            symbol_price_model = await AlphavantageService.symbol_price(symbol=symbol)

            return symbol_price_model["close"]

        except BaseErebusException as exception:
            raise ServiceUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="StockMarketService::__check_symbol_price__check_symbol_price",
                exception=exception,
            )

    @staticmethod
    async def __check_symbol_exists(symbol: str) -> str:
        try:
            symbols_model = await AlphavantageService.symbol_search(symbol=symbol)

            if symbols_model:
                market_symbol = symbols_model[0]["symbol"]

                return market_symbol

        except BaseErebusException as exception:
            raise ServiceUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="StockMarketService::__check_symbol_exists",
                exception=exception,
            )

    @staticmethod
    async def __process_order(message: ConsumerRecord) -> NoReturn:
        try:
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

            order_model.update(
                {"symbol": market_symbol, "unit_price": symbol_unit_price}
            )

            await StockMarketService.__update_order(
                order_model=order_model,
                status=OrderStatusEnum.FINISHED,
                message=OrderMessageEnum.ORDER_PROCESSED,
            )

            return

        except BaseErebusException as exception:
            raise ServiceUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="StockMarketService::__process_order",
                exception=exception,
            )

    @staticmethod
    async def start_consume():
        try:
            topic_consumer = StockMarketRepository.subscribe_to_orders_topic()

            for message in topic_consumer:
                await StockMarketService.__process_order(message=message)

        except BaseErebusException as exception:
            loglifos.error(
                operation=exception.operation,
                msg=exception.message,
                exception=exception.exception,
            )

        except Exception as exception:
            loglifos.error(
                operation="StockMarketService::start_consume",
                msg="Unexpected error on consumer",
                exception=exception,
            )
