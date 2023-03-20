# Third Party
from decouple import config
from requests import get, Response

# Local
from src.core.transport.abstract_transport import AbstractTransport


class AlphavantageTransport(AbstractTransport):
    __alphavantage_url = config("ALPHAVANTAGE_URL")
    __alphavantage_api_key = config("ALPHAVANTAGE_API_KEY")

    @classmethod
    async def symbol_search(cls, symbol: str) -> Response:
        params = {
            "function": "SYMBOL_SEARCH",
            "keywords": symbol,
            "apikey": cls.__alphavantage_api_key,
        }

        api_response = get(url=cls.__alphavantage_url, params=params)

        return api_response

    @classmethod
    async def symbol_price(cls, symbol: str) -> Response:
        params = {
            "function": "TIME_SERIES_DAILY_ADJUSTED",
            "symbol": symbol,
            "apikey": cls.__alphavantage_api_key,
        }

        api_response = get(url=cls.__alphavantage_url, params=params)

        return api_response
