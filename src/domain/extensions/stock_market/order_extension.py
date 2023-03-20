# Local
from src.domain.enums.stock_market.stock_market_enums import (
    OrderStatusEnum,
)
from src.domain.exceptions.domain.domain_exceptions import DomainUnexpectedException
from src.domain.models.stock_market.order_model import OrderModel


class StockMarketExtension:
    @staticmethod
    def to_order_model(order: dict) -> OrderModel:
        try:
            order_model: OrderModel = {
                "symbol": order.get("symbol", ""),
                "quantity": order.get("quantity", 0),
                "order_status": order.get("order_type", OrderStatusEnum.PENDING),
                "order_id": order.get("order_id", ""),
            }

            return order_model

        except Exception as exception:
            raise DomainUnexpectedException(
                operation="StockMarketExtension::to_order_model",
                exception=exception,
            )
