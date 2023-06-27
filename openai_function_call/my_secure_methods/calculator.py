import logging
import operator

logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def calculate(a: float, b: float, op: str) -> float:
    logger.info(f" Calling calculate with {a=}, {b=} and {op=}")
    return getattr(operator, op)(a, b)
