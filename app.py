#!/bin/python

import logging

from src.ui import AppUI
from tests.utils import get_random_charset

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start():
    logger.info("Started.")
    charset = get_random_charset(10)
    print(charset)
    app = AppUI()
    app.start()
    app.add_new_session(charset)
    app.exit()
    logger.info("Finished.")


if __name__ == "__main__":
    start()
