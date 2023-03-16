# Standard
from asyncio import new_event_loop, set_event_loop

# Third Party
from decouple import config
from pyfiglet import print_figlet

# Local
from src.services.stock_market.stock_market_service import StockMarketService

if __name__ == "__main__":
    event_loop = new_event_loop()
    set_event_loop(loop=event_loop)

    print_figlet(text="Erebus", colors="30;37;235")

    kafka_url = config("KAFKA_URL")
    kafka_topic = config("KAFKA_TOPIC_NAME")
    text_color = "\033[0;34m"
    print(
        f"{text_color}Starting consuming from URL: {kafka_url} - TOPIC: {kafka_topic}"
    )

    event_loop.run_until_complete(future=StockMarketService.start_consume())
