from peg import *
from ball import *
from vector2 import *
from cmu_graphics import *  # only necessary to run this file directly


class Plinko:

    def __init__(self, balance: int):
        """
        Plinko game class.

        Set app.background and app.stepsPerSecond before running.
        """

        self.width = 800
        self.height = 800
        self.background = "black"

        self.balance = balance

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
        self.stepsPerSecond = 30
    
    def onKeyPress(self, key):
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
        elif self == '5' and self.balance >= 50:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 50))
            self.balance -= 50
            self.balance = pythonRound(self.balance, 2)
        elif key == '6' and self.balance >= 100:
            self.balls.append(Ball(Vector2(self.width / 2, 50), 100))
            self.balance -= 100
            self.balance = pythonRound(self.balance, 2)
    
    def onStep(self):
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
    
    def redrawAll(self):
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

        drawLabel(f"Balance: {self.balance} tokens", 600, 50, size=20, bold=True, fill="lightSlateGray")

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
        app.plinko = Plinko(500)
        app.background = app.plinko.background
        app.stepsPerSecond = app.plinko.stepsPerSecond
    
    def onStep(app):
        app.plinko.onStep()
    
    def redrawAll(app):
        app.plinko.redrawAll()
    
    def onKeyPress(app, key):
        app.plinko.onKeyPress(key)
    
    runApp(800, 800)
