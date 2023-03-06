# Third Party
from decouple import config
import requests


class AlphavantageTransport:
    __alphavantage_url = config("ALPHAVANTAGE_URL")
    __alphavantage_api_key = config("ALPHAVANTAGE_API_KEY")

    @classmethod
    async def symbol_search(cls, symbol: str) -> dict:
        params = {
            "function": "SYMBOL_SEARCH",
            "keywords": symbol,
            "apikey": cls.__alphavantage_api_key,
        }

        api_response = requests.get(url=cls.__alphavantage_url, params=params)
        dict_response = api_response.json()

        return dict_response
