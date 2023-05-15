import pytest

from classes.engine import Engine2D
from classes.figures.circle import Circle
from classes.figures.common.point import Point
from classes.figures.rectangle import Rectangle
from classes.figures.triangle import Triangle
from constants.colors import Color


@pytest.mark.engine
@pytest.mark.parametrize("figures", [[
    Circle(Point(600, 600), 100),
    Rectangle(Point(100, 100), Point(200, 200)),
    Circle(Point(300, 300), 100)
]])
def test_draw_figures_engine(get_engine, figures):
    engine = get_engine
    for figure in figures:
        engine.add_figure_in_canvas(figure)
    engine.draw()
    assert len(engine.canvas) == 0


@pytest.mark.engine
@pytest.mark.parametrize("figures", [[
    Circle(Point(600, 600), 100),
    Rectangle(Point(100, 100), Point(200, 200)),
    Rectangle(Point(300, 300), Point(400, 400)),
    Circle(Point(250, 500), 100)
]])
def test_change_color_for_figures(get_engine, figures):
    new_color = Color.PINK.value
    engine = get_engine
    engine.add_figure_in_canvas(figures[0])
    engine.add_figure_in_canvas(figures[1])
    engine.change_color(new_color)
    engine.add_figure_in_canvas(figures[2])
    engine.add_figure_in_canvas(figures[3])

    for i in range(len(engine.canvas)):
        if i < 2:
            assert engine.canvas[i].color != new_color
        else:
            assert engine.canvas[i].color == new_color
    engine.draw()


@pytest.mark.engine
@pytest.mark.parametrize("figures, colors", [([
    Circle(Point(500, 500), 100),
    Rectangle(Point(100, 100), Point(200, 200)),
    Rectangle(Point(600, 600), Point(700, 700)),
    Circle(Point(250, 500), 100)
], [
    Color.PINK.value,
    Color.RED.value,
    Color.GREEN.value,
    Color.BLUE.value
]), ([
    Circle(Point(100, 100), 30),
    Rectangle(Point(200, 200), Point(222, 222)),
    Triangle(Point(100, 350), Point(500, 650), Point(400, 300)),
    Circle(Point(777, 555), 70)
], [
    Color.RED.value,
    Color.PINK.value,
    Color.BLACK.value,
    Color.GREEN.value
])])
def test_multiple_change_color_for_figures(get_engine, figures, colors):
    engine = get_engine
    for i in range(len(figures)):
        engine.change_color(colors[i])
        engine.add_figure_in_canvas(figures[i])
    for i in range(len(engine.canvas)):
        assert engine.canvas[i].color == colors[i]
    engine.draw()


@pytest.mark.engine
@pytest.mark.parametrize("figures", [[
    Circle(Point(700, 500), 50),
    Triangle(Point(100, 150), Point(200, 250), Point(500, 300)),
    Rectangle(Point(300, 300), Point(400, 400)),
]])
def test_draw_each_type_figure(get_engine, figures):
    engine = get_engine
    for figure in figures:
        engine.add_figure_in_canvas(figure)
    engine.draw()
    assert len(engine.canvas) == 0


@pytest.mark.engine
def test_engine_existence(get_engine):
    engine = get_engine
    assert isinstance(engine, Engine2D)
