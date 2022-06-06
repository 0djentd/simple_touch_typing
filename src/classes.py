import time
import dataclasses
import logging
import curses

logger = logging.getLogger(__name__)


@dataclasses.dataclass
class Session():
    charset: list[str]


class App():
    sessions: list[Session]

    def __init__(self) -> None:
        logger.info("Started")
