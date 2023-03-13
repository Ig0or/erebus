# Standard
from typing import TypedDict


class SymbolPriceModel(TypedDict):
    open: float
    high: float
    low: float
    close: float
    adjusted_close: float
    volume: int
    dividend_amount: float
    split_coefficient: float
