import time
import dataclasses
import logging
import curses
import enum
import typing

logger = logging.getLogger(__name__)


class IterationResult(enum.Enum):
    fail = 'FAIL'
    ok = 'OK'
    skip = 'SKIP'


typing.Literal[IterationResult.fail, IterationResult.ok, IterationResult.skip]


class Iteration():
    char: str
    result: str | None
    time_start: float | None
    time_end: float | None

    def __init__(self, char):
        char = str(char)
        if len(char) != 1:
            raise ValueError

        self.char = char
        self.result = None
        self.time_start = None
        self.time_end = None


@dataclasses.dataclass
class Session():
    charset: list[str]


class App():
    sessions: list[Session]

    def __init__(self) -> None:
        logger.info("Started")
