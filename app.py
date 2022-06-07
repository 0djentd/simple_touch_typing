#!/bin/python

import logging

from src.core import App, Session
from tests.utils import get_random_charset

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start():
    logger.info("Started.")
    app = App()
    charset = get_random_charset(10)
    print(charset)
    logger.info("Finished.")


if __name__ == "__main__":
    start()
