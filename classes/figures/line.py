from classes.figures.shape import Shape
from classes.figures.common.point import Point


class Line(Shape):
    def __init__(self, p1: Point, p2: Point):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
