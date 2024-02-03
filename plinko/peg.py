from cmu_graphics import *
from


class Peg:

    def __init__(self, pos: tuple[float, float], radius: int = 5, color: str = 'black'):
        self.pos = pos
        self.radius = radius
        self.color = color

    def draw(self):
        drawCircle(*self.pos, self.radius, fill=self.color)
