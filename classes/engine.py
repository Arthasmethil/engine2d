from tkinter import *

from classes.figures.circle import Circle
from classes.figures.rectangle import Rectangle
from classes.figures.shape import Shape
from classes.figures.triangle import Triangle
from constants.colors import Color
from constants.tkinter_config import LINE_WIDTH


class Engine2D:

    def __init__(self, root: Tk, field: Canvas):
        self.canvas = []
        self.color = Color.BLACK.value
        self.root = root
        self.field = field

    def add_figure_in_canvas(self, shape: Shape):
        if isinstance(shape, (Triangle, Rectangle, Circle)):
            shape.change_color(self.color)
            self.canvas.append(shape)
        else:
            raise TypeError(f"Invalid type {shape.__class__}, valid types: Triangle, Rectangle, Circle")

    def get_width_of_window(self):
        print(self.field.winfo_width())

    def get_height_of_window(self):
        print(self.field.winfo_height())

    def clean_canvas(self):
        self.canvas.clear()

    def draw(self):
        for figure in self.canvas:
            if isinstance(figure, Triangle):
                draw_triangle(figure, self.field)
            elif isinstance(figure, Rectangle):
                draw_rectangle(figure, self.field)
            elif isinstance(figure, Circle):
                draw_circle(figure, self.field)
        self.clean_canvas()
        self.root.mainloop()

    def change_color(self, color):
        self.color = color


def draw_rectangle(rectangle: Rectangle, field: Canvas):
    rectangle.draw()
    field.create_rectangle(rectangle.p1.x, rectangle.p1.y,
                           rectangle.p2.x, rectangle.p2.y,
                           outline=rectangle.color,
                           fill=rectangle.color,
                           width=LINE_WIDTH)


def draw_circle(circle: Circle, field: Canvas):
    circle.draw()
    field.create_oval(
        circle.get_bottom_point().x, circle.get_bottom_point().y,
        circle.get_top_point().x, circle.get_top_point().y,
        outline=circle.color,
        fill=circle.color,
        width=LINE_WIDTH)


def draw_triangle(triangle: Triangle, field: Canvas):
    triangle.draw()
    field.create_polygon(triangle.p1.x, triangle.p1.y,
                         triangle.p2.x, triangle.p2.y,
                         triangle.p3.x, triangle.p3.y,
                         outline=triangle.color,
                         fill=triangle.color,
                         width=LINE_WIDTH)
