import random as rd
from vector2 import *
from cmu_graphics import *  # only necessary to run this file directly


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


class Plinko:

    def __init__(self, app):
        """
        Plinko game class.

        Set app.width, app.height, app.background before running.
        """

        self.width = self.height = 800
        self.background = "black"

        self.balance = app.balance
        self.app = app

        self.pegs = []

        rows = 21
        pegWidth = 30
        pegHeight = 30
        firstY = 100
        for row in range(3, rows):
            thisY = firstY + row * pegHeight
            firstX = self.width / 2 - pegWidth * (row - 1) / 2
            nPegs = row
            for col in range(nPegs):
                thisX = firstX + pegWidth * col
                self.pegs.append(Peg(Vector2(thisX, thisY)))


        self.balls = []
        self.slotValues = [
            0,10,5,2,1,0.5,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.5,1,2,5,10,0
            # 88% return (based on data)
        ]

    @property
    def netProfit(self):
        self.balance - self.initBalance

    def onKeyPress(self, app, key):
        if key == '1' and self.balance >= 1:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 1))
            self.balance -= 1
        elif key == '2' and self.balance >= 5:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 5))
            self.balance -= 5
        elif key == '3' and self.balance >= 10:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 10))
            self.balance -= 10
            self.balance = pythonRound(self.balance, 2)
        elif key == '4' and self.balance >= 20:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 20))
            self.balance -= 20
            self.balance = pythonRound(self.balance, 2)
        elif key == '5' and self.balance >= 50:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 50))
            self.balance -= 50
            self.balance = pythonRound(self.balance, 2)
        elif key == '6' and self.balance >= 100:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 100))
            self.balance -= 100
            self.balance = pythonRound(self.balance, 2)
        elif key == 'escape':
            self.app.balance = self.balance
            self.app.reset(self.app)

    def onStep(self, app):
        for ball in self.balls:
            ball.vel[1] += 0.5
            ball.updatePos()
            for peg in self.pegs:
                if dist(peg.pos, ball.pos) <= 10:
                    ball.collidePeg(peg)
                    break


            else:
                if ball.pos.y > self.height + 5:
                    if self.width / 2 - 285 < ball.pos.x < self.width / 2 + 285:
                        slot = (int(ball.pos.x - (self.width / 2 - 285)) // 30) + 1
                        self.balance += self.slotValues[slot] * ball.value
                        self.balance = pythonRound(self.balance, 2)
                    self.balls.remove(ball)
                else:
                    ball.collideWalls(self.width)

    def onMousePress(self, app, x, y):
        pass

    def redrawAll(self, app):
        for peg in self.pegs:
            peg.draw()

        for ball in self.balls:
            ball.draw()

        drawCircle(50, 50, 5, fill='deepSkyBlue')
        drawLabel("$1", 50, 30, fill="lightSlateGray", size=16, bold=True)
        drawLabel("[1]", 50, 70, fill="lightSlateGray")
        drawCircle(100, 50, 5, fill='mediumSlateBlue')
        drawLabel("$5", 100, 30, fill="lightSlateGray", size=16, bold=True)
        drawLabel("[2]", 100, 70, fill="lightSlateGray")
        drawCircle(150, 50, 5, fill='limeGreen')
        drawLabel("$10", 150, 30, fill="lightSlateGray", size=16, bold=True)
        drawLabel("[3]", 150, 70, fill="lightSlateGray")
        drawCircle(200, 50, 5, fill='crimson')
        drawLabel("$20", 200, 30, fill="lightSlateGray", size=16, bold=True)
        drawLabel("[4]", 200, 70, fill="lightSlateGray")
        drawCircle(250, 50, 5, fill='gold')
        drawLabel("$50", 250, 30, fill="lightSlateGray", size=16, bold=True)
        drawLabel("[5]", 250, 70, fill="lightSlateGray")
        drawCircle(300, 50, 5, fill='white')
        drawLabel("$100", 300, 30, fill="lightSlateGray", size=16, bold=True)
        drawLabel("[6]", 300, 70, fill="lightSlateGray")

        drawLabel(f"Balance: {rounded(self.balance)} tokens", 600, 50, size=20, bold=True, fill="lightSlateGray")
        drawLabel(f"(Press [esc] to exit)", 600, 100, size=14, fill="lightSlateGray")

        drawLine(self.width / 2 - 35, 0, self.width / 2 - 35, 100, fill='lightSlateGray')
        drawLine(self.width / 2 + 35, 0, self.width / 2 + 35, 100, fill='lightSlateGray')
        drawLine(self.width / 2 - 35, 100, self.width / 2 - 335, 700, fill='lightSlateGray')
        drawLine(self.width / 2 + 35, 100, self.width / 2 + 335, 700, fill='lightSlateGray')
        drawLine(self.width / 2 - 335, 700, self.width / 2 - 335, self.height, fill='lightSlateGray')
        drawLine(self.width / 2 + 335, 700, self.width / 2 + 335, self.height, fill='lightSlateGray')

        for x in range(int(self.width / 2 - 285), int(self.width / 2 + 286), 30):
            drawLine(x, 700, x, self.height, fill='lightSlateGray')

        for i in range(21):
            x = 100 + i * 30
            if i == 0:
                x -= 10
            elif i == 20:
                x += 10
            drawLabel(f"{self.slotValues[i]}", x, 750, size=16, fill='lightSlateGray', bold=True)


if __name__ == "__main__":
    def onAppStart(app):
        app.balance = 1000
        app.plinko = Plinko(app)
        app.background = app.plinko.background

    def onStep(app):
        app.plinko.onStep(0)

    def redrawAll(app):
        app.plinko.redrawAll(0)

    def onKeyPress(app, key):
        app.plinko.onKeyPress(key, 0)

    runApp(800, 800)
