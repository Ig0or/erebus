# Standard
from typing import TypedDict


class SymbolModel(TypedDict):
    symbol: str
    name: str
    type: str
    region: str
    market_open: str
    market_close: str
    timezone: str
    currency: str
    match_score: str
