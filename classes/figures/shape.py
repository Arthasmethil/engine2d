from constants.colors import Color


class Shape:
    def __init__(self):
        self.color = Color.BLACK

    def draw(self):
        pass

    def change_color(self, color):
        self.color = color
