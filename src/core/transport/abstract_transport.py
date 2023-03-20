# Standard
from typing import Callable

# Third Party
from requests import Response

# Local
from src.domain.exceptions.base.base_exception import BaseErebusException
from src.domain.exceptions.transport.transport_exceptions import (
    TransportResponseException,
    TransportUnexpectedException,
)


class AbstractTransport:
    @staticmethod
    async def __execute_callback(callback: Callable, **kwargs) -> Response:
        response = callback(**kwargs)

        return response

    @staticmethod
    def __handle_response_exception(
        callback: Callable, response: Response
    ) -> TransportResponseException:
        exception_message = Exception(
            f"status code: {response.status_code} - reason: {response.reason}"
        )
        operation_name = str(callback).split(" ")[2]

        exception = TransportResponseException(
            operation=operation_name, exception=exception_message
        )

        return exception

    @staticmethod
    async def process_request(callback: Callable, **kwargs) -> dict:
        try:
            response = await callback(**kwargs)

            if response.status_code != 200:
                exception = AbstractTransport.__handle_response_exception(
                    callback=callback, response=response
                )

                raise exception

            dict_response = response.json()

            return dict_response

        except BaseErebusException as exception:
            raise TransportUnexpectedException(
                operation=exception.operation,
                exception=exception.exception,
                message=exception.message,
            )

        except Exception as exception:
            raise TransportUnexpectedException(
                operation="AbstractTransport::process_request",
                exception=exception,
            )
