# Local
from src.domain.exceptions.base.base_exception import BaseErebusException
from src.domain.exceptions.service.service_exceptions import ServiceUnexpectedException
from src.domain.models.alphavantage.price_model import SymbolPriceModel
from src.domain.models.alphavantage.symbol_model import SymbolModel
from src.domain.extensions.alphavantage.alphavantage_extension import (
    AlphavantageExtension,
)
from src.transport.alphavantage.alphavantage_transport import AlphavantageTransport


class AlphavantageService:
    @staticmethod
    async def symbol_search(symbol: str) -> list[SymbolModel]:
        try:
            response = await AlphavantageTransport.process_request(
                callback=AlphavantageTransport.symbol_search, symbol=symbol
            )
            symbols_model = AlphavantageExtension.to_array_symbol_search_model(
                response=response
            )

            return symbols_model

        except BaseErebusException as exception:
            raise ServiceUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="AlphavantageService::symbol_search",
                exception=exception,
            )

    @staticmethod
    async def symbol_price(symbol: str) -> SymbolPriceModel:
        try:
            response = await AlphavantageTransport.process_request(
                callback=AlphavantageTransport.symbol_price, symbol=symbol
            )
            price_model = AlphavantageExtension.to_symbol_price_model(response=response)

            return price_model

        except BaseErebusException as exception:
            raise ServiceUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise ServiceUnexpectedException(
                operation="AlphavantageService::symbol_price",
                exception=exception,
            )
