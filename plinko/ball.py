import random as rd
from peg import Peg
from cmu_graphics import *
from vector2 import *


class Ball:

    def __init__(self, pos: Vector2, value: float, randomVel: bool = True):
        shift = Vector2(rd.uniform(-20, 20), rd.uniform(-20, 20))
        self.pos = pos + shift
        self.randomizePos(1)
        if randomVel:
            self.vel = Vector2(rd.uniform(-10, 10), rd.uniform(-5, 5))
        else:
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
        while dist(mid, peg.pos) <= (4.9 + peg.radius) and dist(close, far) > 0.1:
            mid = (close + far) / 2
            if dist(mid, peg.pos) >= (5 + peg.radius):
                far = mid
            else:
                close = mid
        self.pos = mid

        relPegPos = peg.pos - self.pos
        remainingDist = relPegPos.mag - (5 + peg.radius)
        unitRelPegPos = relPegPos.normalize()
        self.pos += unitRelPegPos * remainingDist
        normalComponent = unitRelPegPos * dot(unitRelPegPos, self.vel)
        self.vel -= 2 * normalComponent
        self.randomizePos()
        self.randomizeVel()
        if self.vel.mag > 2:
            self.vel *= peg.bounce
        else:
            if rd.random() <= 0.5:
                peg.highlight = True
                self.vel = -unitRelPegPos * 10

    def collideWalls(self, width: int):
        if self.pos.y <= 100:
            if abs(self.pos.x - width / 2) >= 30:
                self.vel.x = -self.vel.x
        elif self.pos.y >= 700:
            if self.pos.x <= width / 2 - 285:
                if self.pos.x <= width / 2 - 330:
                    self.vel.x = -self.vel.x
            elif width / 2 + 285 <= self.pos.x:
                if width / 2 + 330 <= self.pos.x:
                    self.vel.x = -self.vel.x
            elif width / 2 - 75 <= self.pos.x <= width / 2 + 75:
                if abs(self.pos.x - width / 2) >= 70:
                    self.vel.x = -self.vel.x
                elif 1 <= abs(self.pos.x - width / 2) <= 11 and self.pos.y > 750:
                    self.vel.x = -self.vel.x
            else:
                if 20 <= self.pos.x % 30 <= 30:
                    self.vel.x = -self.vel.x
        else:
            if 2 * self.pos.x + self.pos.y <= 40 + width:
                unitNormal = Vector2(-2, -1).normalize()
                normalComponent = unitNormal * dot(unitNormal, self.vel)
                self.vel -= 2 * normalComponent
            elif 2 * (-self.pos.x) + self.pos.y <= 40 - width:
                unitNormal = Vector2(2, -1).normalize()
                normalComponent = unitNormal * dot(unitNormal, self.vel)
                self.vel -= 2 * normalComponent

    def draw(self):
        if self.value <= 1:
            drawCircle(*self.pos, 5, fill='deepSkyBlue')
        if 1 < self.value <= 5:
            drawCircle(*self.pos, 5, fill='mediumSlateBlue')
        if 5 < self.value <= 10:
            drawCircle(*self.pos, 5, fill='limeGreen')
        if 10 < self.value <= 20:
            drawCircle(*self.pos, 5, fill='crimson')
        if 20 < self.value <= 50:
            drawCircle(*self.pos, 5, fill='gold')
        if 50 < self.value:
            drawCircle(*self.pos, 5, fill='white')
