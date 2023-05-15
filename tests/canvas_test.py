import sys

import pytest

from classes.figures.circle import Circle
from classes.figures.common.point import Point
from classes.figures.rectangle import Rectangle
from classes.figures.triangle import Triangle
from constants.colors import Color


@pytest.mark.canvas
@pytest.mark.parametrize("figures", [
    Circle(Point(600, 600), 100)
])
def test_clear_canvas_after_draw(get_engine, figures):
    engine = get_engine
    engine.add_figure_in_canvas(Circle(Point(600, 600), 100))
    engine.draw()
    assert len(engine.canvas) == 0


@pytest.mark.canvas
@pytest.mark.parametrize("width, height", [
    (1280, 720),
    (720, 1280)
])
def test_size_of_window_canvas(get_engine, width, height, capfd):
    saved_stdout = sys.stdout
    try:
        engine = get_engine
        engine.root.after(500, lambda: engine.get_width_of_window())
        engine.root.after(500, lambda: engine.get_height_of_window())
        engine.draw()
        captured = capfd.readouterr()
        assert captured.out.strip() == f"{width}\n{height}"
    finally:
        sys.stdout = saved_stdout


@pytest.mark.canvas
@pytest.mark.parametrize("width, height", [
    (1920, 1080),
    (1222, 7111),
    (23, 12)
])
def test_size_of_window_canvas_negative(get_engine, width, height, capfd):
    saved_stdout = sys.stdout
    try:
        engine = get_engine
        engine.root.after(500, lambda: engine.get_width_of_window())
        engine.root.after(500, lambda: engine.get_height_of_window())
        engine.draw()
        captured = capfd.readouterr()
        assert captured.out.strip() != f"{width}\n{height}"
    finally:
        sys.stdout = saved_stdout


@pytest.mark.canvas
@pytest.mark.parametrize("figures, colors, expected_values", [([
    Rectangle(Point(600, 600), Point(700, 700))
], [
    Color.PINK.value,
], "\nDrawing pink Rectangle (600, 600), (700, 700)\n"), ([
    Triangle(Point(100, 350), Point(500, 650), Point(400, 300))
], [
    Color.GREEN.value
], "\nDrawing green Triangle (100, 350), (500, 650), (400, 300)\n")])
def test_console_output(get_engine, figures, colors, expected_values, capfd):
    saved_stdout = sys.stdout
    try:
        engine = get_engine
        for i in range(len(figures)):
            engine.change_color(colors[i])
            engine.add_figure_in_canvas(figures[i])
        engine.draw()
        captured = capfd.readouterr()
        assert captured.out == expected_values
    finally:
        sys.stdout = saved_stdout


@pytest.mark.canvas
@pytest.mark.parametrize("figures", [[
    Circle(Point(600, 600), 100),
    Rectangle(Point(100, 100), Point(200, 200)),
    Circle(Point(300, 300), 100)
]])
def test_add_figures_to_canvas(get_engine, figures):
    engine = get_engine
    for figure in figures:
        engine.add_figure_in_canvas(figure)
    assert len(engine.canvas) == len(figures)
