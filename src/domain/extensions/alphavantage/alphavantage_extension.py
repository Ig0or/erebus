# Local
from src.domain.models.alphavantage.symbol_model import SymbolModel


class AlphavantageExtension:
    @staticmethod
    def __to_symbol_search_model(symbol_response: dict) -> SymbolModel:
        symbol_model: SymbolModel = {
            "symbol": symbol_response.get("1. symbol", ""),
            "name": symbol_response.get("2. name", ""),
            "type": symbol_response.get("3. type", ""),
            "region": symbol_response.get("4. region", ""),
            "market_open": symbol_response.get("5. marketOpen", ""),
            "market_close": symbol_response.get("6. marketClose", ""),
            "timezone": symbol_response.get("7. timezone", ""),
            "currency": symbol_response.get("8. currency", ""),
            "match_score": symbol_response.get("9. matchScore", ""),
        }

        return symbol_model

    @classmethod
    def to_array_symbol_search_model(cls, response: dict) -> list[SymbolModel]:
        symbols_response = response.get("bestMatches", list())

        symbols_model = list()

        for symbol in symbols_response:
            symbol_model = cls.__to_symbol_search_model(symbol_response=symbol)
            symbols_model.append(symbol_model)

        return symbols_model

    @classmethod
    def to_symbol_price_model(cls, response: dict):
        pass
