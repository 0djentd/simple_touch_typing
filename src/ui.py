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
