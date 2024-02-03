from cmu_graphics import *
from vector2 import *


class Peg:

    def __init__(self, pos: Vector2, radius: int = 5, bounce: float = 0.5, color: str = 'lightSlateGray'):
        self.pos = pos
        self.radius = radius
        self.bounce = bounce
        self.color = color
        self.highlight = False

    def draw(self):
        if self.highlight:
            drawCircle(*self.pos, self.radius, fill='orangered')
            self.highlight = False
        else:
            drawCircle(*self.pos, self.radius, fill=self.color)
