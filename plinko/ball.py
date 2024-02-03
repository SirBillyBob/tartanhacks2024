import random as rd
from peg import Peg
from cmu_graphics import *
from vector2 import *


class Ball:

    def __init__(self, pos: Vector2, value: float):
        self.pos = pos
        self.randomizePos(1)
        self.vel = Vector2(0, 0)
        self.value = value

    def randomizePos(self, scale: float = 0.1):
        randVec = Vector2(rd.uniform(-scale, scale), rd.uniform(-scale, scale))
        self.pos += randVec

    def randomizeVel(self, scale: float = 0.1):
        randVec = Vector2(rd.uniform(-scale, scale), rd.uniform(-scale, scale))
        self.vel += randVec

    def updatePos(self):
        self.pos += self.vel

    def collidePeg(self, peg: Peg):
        close = self.pos
        far = self.pos - self.vel
        mid = (close + far) / 2
        while dist(mid, peg.pos) <= 9.9 and dist(close, far) > 0.1:  # can do sum w iterations if heavy
            # print("mid", dist(mid, peg.pos))
            # print("close", dist(close, peg.pos))
            # print("far", dist(far, peg.pos))
            # print("dist", dist(close, far))
            mid = (close + far) / 2
            if dist(mid, peg.pos) >= 10:
                far = mid
            else:
                close = mid
        self.pos = mid

        relPegPos = peg.pos - self.pos
        remainingDist = relPegPos.mag - 10
        relPegPos.normalize()
        self.pos += relPegPos * remainingDist
        normalComponent = relPegPos * dot(relPegPos, self.vel)
        self.vel -= 2 * normalComponent
        self.randomizePos()
        self.randomizeVel()
        if self.vel.mag > 2:
            self.vel *= 0.5
        else:
            if rd.random() <= 0.5:
                peg.highlight = True
                self.vel = -relPegPos * 10

    def draw(self):
        drawCircle(*self.pos, 5, fill='midnightblue')
