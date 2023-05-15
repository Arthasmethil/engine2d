from classes.figures.shape import Shape
from classes.figures.common.point import Point


class Rectangle(Shape):
    def __init__(self, p1: Point, p2: Point):
        super().__init__()
        self.p1 = p1
        self.p2 = p2

    def draw(self):
        print(f"\nDrawing {self.color} {self.__class__.__name__} {self.p1.x, self.p1.y}, {self.p2.x, self.p2.y}")
