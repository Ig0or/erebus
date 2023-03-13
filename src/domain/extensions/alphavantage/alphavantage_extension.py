# Local
from src.domain.models.alphavantage.price_model import SymbolPriceModel
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
    def to_symbol_price_model(cls, response: dict) -> SymbolPriceModel:
        days_price = iter(response.get("Time Series (Daily)", dict()).values())
        price_information = next(days_price, dict())

        price_model: SymbolPriceModel = {
            "open": float(price_information.get("1. open", 0)),
            "high": float(price_information.get("2. high", 0)),
            "low": float(price_information.get("3. low", 0)),
            "close": float(price_information.get("4. close", 0)),
            "adjusted_close": float(price_information.get("5. adjusted close", 0)),
            "volume": int(price_information.get("6. volume", 0)),
            "dividend_amount": float(price_information.get("7. dividend amount", 0)),
            "split_coefficient": float(price_information.get("1. open", 0)),
        }

        return price_model
