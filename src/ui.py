import logging
import curses

from . import core


logger = logging.getLogger(__name__)


class IterationUI():
    iteration: core.Iteration


class SessionUI():
    session: core.Session


class AppUI():
    app: core.App
    screen: curses._CursesWindow

    @property
    def session(self) -> core.Session | None:
        if self.app.sessions:
            return self.app.sessions[-1]
        else:
            return None

    def __init__(self):
        self.app = core.App()
        self.screen = curses.initscr()

    def start(self) -> None:
        curses.cbreak()

    def exit(self) -> None:
        curses.nocbreak()

    def add_new_session(self, charset) -> core.Session:
        session = core.Session(charset)
        self.app.sessions.append(session)
        return session
