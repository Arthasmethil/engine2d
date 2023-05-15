import math

from classes.figures.shape import Shape
from classes.figures.common.point import Point


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        if p1 is None or p2 is None or p3 is None:
            raise ValueError("One of the point is None")
        length_ab = math.sqrt((pow(self.p2.x - self.p1.x, 2) + pow(self.p2.y - self.p1.y, 2)))
        length_bc = math.sqrt((pow(self.p3.x - self.p2.x, 2) + pow(self.p3.y - self.p2.y, 2)))
        length_ac = math.sqrt((pow(self.p3.x - self.p1.x, 2) + pow(self.p3.y - self.p1.y, 2)))
        if length_ab + length_bc <= length_ac \
                or length_ac + length_ab <= length_bc \
                or length_ac + length_bc <= length_ab:
            raise ValueError("The Triangle isn't exist")
        elif self.p1.x == self.p2.x and self.p1.x == self.p3.x or self.p1.y == self.p2.y and self.p1.y == self.p3.y:
            raise ValueError("The Triangle isn't exist")
        elif self.p1.x == self.p1.y and self.p2.x == self.p2.y and self.p3.x == self.p3.y:
            raise ValueError("The Triangle isn't exist")

    def draw(self):
        print(f"\nDrawing {self.color} {self.__class__.__name__} "
              f"{self.p1.x, self.p1.y}, {self.p2.x, self.p2.y}, {self.p3.x, self.p3.y}")
