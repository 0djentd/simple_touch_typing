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


IterationResultTypes = typing.Literal[IterationResult.fail,
                                      IterationResult.ok,
                                      IterationResult.skip]


class Iteration():
    """Object to represent test iteration.

    How to use:
    >>> iteration = Iteration("a")
    >>> iteration.start()
    >>> iteration.answer = "a"
    >>> iteration.result
    <<< "OK"
    """

    char: str
    result: IterationResultTypes | None
    time_start: float | None
    time_end: float | None
    _answer: str | None

    def __init__(self, char):
        char = str(char)
        if len(char) != 1:
            raise ValueError
        self.char = char
        self.result = None
        self.time_start = None
        self.time_end = None
        self._answer = None

    @property
    def answer(self):
        if self._answer:
            return self._answer[:]

    @answer.setter
    def answer(self, val):
        if len(val) != 1:
            raise ValueError
        self._answer = str(val)
        self.time_end = time.time()
        self.result = self._check()

    def start(self):
        self.time_start = time.time()

    def skip(self):
        self.result = IterationResult.skip
        self.time_end = time.time()

    def _check(self):
        if self.answer == self.char:
            return IterationResult.ok
        else:
            return IterationResult.fail


class Session():
    charset: str
    iterations: list[Iteration] = []

    def start(self):
        for char in self.charset:
            while True:
                iteration = Iteration(char)
                self.iterations.append(iteration)
                iteration.time_start = time.time()
                q = char
                a = input(q)
                iteration.time_end = time.time()
                if q == a:
                    iteration.result = IterationResult.ok
                    break
                else:
                    iteration.result = IterationResult.fail

    def __init__(self, charset) -> None:
        self.charset = charset


class App():
    sessions: list[Session]

    def __init__(self) -> None:
        self.sessions = []
