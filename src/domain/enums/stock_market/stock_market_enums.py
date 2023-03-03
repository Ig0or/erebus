# Local
from enum import Enum


class OrdersTypeEnum(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class OrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"
