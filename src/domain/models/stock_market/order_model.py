# Standard
from typing_extensions import NotRequired, TypedDict

# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderStatusEnum,
    OrdersTypeEnum,
)


class OrderModel(TypedDict):
    symbol: str
    quantity: int
    price: float
    order_type: OrdersTypeEnum
    order_status: OrderStatusEnum
    order_message: NotRequired[str]
    order_id: str
