import random as rd
from peg import Peg
from cmu_graphics import *


class Ball:

    def __init__(self, pos: list[float], value: float):
        self.pos = pos
        self.randomizePos(0.1)
        self.vel = [0, 0]
        self.value = value

    def randomizePos(self, scale: float):
        self.pos[0] += rd.uniform(-scale, scale)
        self.pos[1] += rd.uniform(-scale, scale)

    def updatePos(self):
        self.pos[0] += self.vel[0]
        self.pos[1] += self.vel[1]

    def collidePeg(self, peg: Peg):
        relPos = (self.pos[0] - peg.pos[0], self.pos[1] - peg.pos[1])
        unitRelPos = relPos

    def draw(self):
        drawCircle(*self.pos, 5, fill='midnightblue')
