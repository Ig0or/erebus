# Standard
from asyncio import AbstractEventLoop, new_event_loop, set_event_loop
from typing import NoReturn

# Third Party
from decouple import config
from pyfiglet import print_figlet

# Local
from src.services.stock_market.stock_market_service import StockMarketService


def get_event_loop() -> AbstractEventLoop:
    loop = new_event_loop()
    set_event_loop(loop=loop)

    return loop


def print_consumer_name() -> NoReturn:
    print_figlet(text="Erebus", colors="30;37;235")

    kafka_uri = config("KAFKA_URI")
    kafka_topic = config("KAFKA_TOPIC_NAME")

    print("**********************************************************************")
    print(f"Starting consuming from URI: {kafka_uri} - TOPIC: {kafka_topic}")
    print("**********************************************************************")

    return


if __name__ == "__main__":
    print_consumer_name()

    event_loop = get_event_loop()
    event_loop.run_until_complete(future=StockMarketService.start_consume())
