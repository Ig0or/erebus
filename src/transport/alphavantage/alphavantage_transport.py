import requests


class AlphavantageTransport:
    @staticmethod
    async def ticker_search(symbol: str ):
        api_response = requests.get(url="https://www.alphavantage.co/query", params={
            "function": "SYMBOL_SEARCH",
            "keywords": "tesla",
            "apikey": "",
        })

        print(api_response)

import asyncio
from requests import Response

a = asyncio.get_event_loop()
a.run_until_complete(AlphavantageTransport.ticker_search("petr4"))