# Local
from src.domain.models.alphavantage.price_model import SymbolPriceModel
from src.domain.models.alphavantage.symbol_model import SymbolModel
from src.domain.extensions.alphavantage.alphavantage_extension import (
    AlphavantageExtension,
)
from src.transport.alphavantage.alphavantage_transport import AlphavantageTransport


class AlphavantageService:
    @staticmethod
    async def symbol_search(symbol: str) -> list[SymbolModel]:
        response = await AlphavantageTransport.symbol_search(symbol=symbol)
        symbols_model = AlphavantageExtension.to_array_symbol_search_model(
            response=response
        )

        return symbols_model

    @staticmethod
    async def symbol_price(symbol: str) -> SymbolPriceModel:
        response = await AlphavantageTransport.symbol_price(symbol=symbol)
        price_model = AlphavantageExtension.to_symbol_price_model(response=response)

        return price_model
