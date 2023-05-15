from tkinter import *

from classes.engine import Engine2D
from constants.colors import Color
from constants.tkinter_config import HEIGHT, WIDTH, WINDOW_CLOSE_TIMER

import pytest as pytest


def pytest_configure(config):
    config.addinivalue_line("markers", "engine: engine test")
    config.addinivalue_line("markers", "canvas: canvas test")


@pytest.fixture(scope="function")
def get_engine():
    """
    This fixture returns example of Engine2D with auto-closing parameter.
    geometry - size of the window
    root.destroy() - finish work with the canvas widget
    all parameters may be changed in constants.tkinter_config.py
    """
    root = Tk()
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.title("Engine Canvas")
    root.resizable(width=False, height=False)
    root.after(WINDOW_CLOSE_TIMER, lambda: root.destroy())
    field = Canvas(root, bg=Color.WHITE.value, width=WIDTH, height=HEIGHT)
    field.pack()
    return Engine2D(root, field)
