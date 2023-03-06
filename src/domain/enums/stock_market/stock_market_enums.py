# Local
from enum import Enum


class OrderStatusEnum(str, Enum):
    PENDING = "PENDING"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"


class OrderMessageEnum(str, Enum):
    INVALID_SYMBOL = "This symbol doesn't exist"
