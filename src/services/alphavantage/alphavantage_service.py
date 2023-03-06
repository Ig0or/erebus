# Local
from src.domain.models.alphavantage.symbol_model import SymbolModel
from src.extensions.alphavantage.alphavantage_extension import AlphavantageExtension
from src.transport.alphavantage.alphavantage_transport import AlphavantageTransport


class AlphavantageService:
    @staticmethod
    async def symbol_search(symbol: str) -> list[SymbolModel]:
        response = await AlphavantageTransport.symbol_search(symbol=symbol)
        symbols_model = AlphavantageExtension.symbol_search_to_array_model(
            response=response
        )

        return symbols_model
