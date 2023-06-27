import logging

import yfinance as yf

logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_price(symbol: str, date: str) -> float:
    logger.info(f"Calling get_price with {symbol=} and {date=}")
    history = yf.download(symbol, start=date, period="1d", interval="1d", progress=False)
    return history["Close"].iloc[0].item()
