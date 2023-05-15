from classes.figures.shape import Shape
from classes.figures.common.point import Point


class Circle(Shape):
    def __init__(self, center: Point, radius: float):
        super().__init__()
        self.center = center
        self.radius = radius

    def get_bottom_point(self):
        return Point(self.center.x - self.radius, self.center.y - self.radius)

    def get_top_point(self):
        return Point(self.center.x + self.radius, self.center.y + self.radius)

    def draw(self):
        print(f"\nDrawing {self.color} {self.__class__.__name__} {self.center.x, self.center.y} "
              f"with radius {self.radius}")
