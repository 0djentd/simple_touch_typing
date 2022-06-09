#!/bin/python

import logging
import time

from src.ui import AppUI
from tests.utils import get_random_charset

from curses import wrapper

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start(screen):
    charset = get_random_charset(10)
    app = AppUI(screen)
    app.start()
    app.add_new_session(charset)
    app.exit()
    time.sleep(1)


if __name__ == "__main__":
    wrapper(start)
