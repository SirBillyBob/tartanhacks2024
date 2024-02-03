from cmu_graphics import *
from ball import Ball
from peg import Peg
import random as rd
from vector2 import *


def redrawAll(app):
    for peg in app.pegs:
        peg.draw()

    for ball in app.balls:
        ball.draw()

    drawLine(app.width / 2 - 35, 0, app.width / 2 - 35, 100)
    drawLine(app.width / 2 + 35, 0, app.width / 2 + 35, 100)
    drawLine(app.width / 2 - 35, 100, app.width / 2 - 335, 700)
    drawLine(app.width / 2 + 35, 100, app.width / 2 + 335, 700)
    drawLine(app.width / 2 - 335, 700, app.width / 2 - 335, app.height)
    drawLine(app.width / 2 + 335, 700, app.width / 2 + 335, app.height)

    for x in range(int(app.width / 2 - 285), int(app.width / 2 + 286), 30):
        drawLine(x, 700, x, app.height)

    for i in range(21):
        x = 100 + i * 30
        if i == 0:
            x -= 10
        elif i == 20:
            x += 10
        drawLabel(f"x{app.slotValues[i]}", x, 750, size=16)


def onMousePress(app, mouseX, mouseY):
    shift = Vector2(rd.uniform(-20, 20), rd.uniform(-20, 20))
    app.balls.append(Ball(Vector2(app.width / 2, 50) + shift, 10))


def onStep(app):
    for ball in app.balls:
        ball.vel[1] += 1
        ball.updatePos()
        for peg in app.pegs:
            if dist(peg.pos, ball.pos) <= 10:
                ball.collidePeg(peg)
                break

        else:
            if ball.pos.y > app.height + 5:
                if ball.pos.x <= app.width / 2 - 285:
                    app.slotFrequencies[0] += 1
                elif ball.pos.x >= app.width / 2 + 285:
                    app.slotFrequencies[-1] += 1
                else:
                    slot = (int(ball.pos.x - (app.width / 2 - 285)) // 30) + 1
                    app.slotFrequencies[slot] += 1
                app.balls.remove(ball)
            else:
                ball.collideWalls(app.width)

    app.count += 1
    if app.count % 3 == 0:
        onMousePress(app, 0, 0)
        if app.count == 300:
            app.count = 0
            print(app.slotFrequencies)



def onKeyPress(app, key):
    if key == "enter":
        print(app.slotFrequencies)
    else:
        onMousePress(app, 0, 0)


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = "green"

    app.pegs = []
    rows = 21
    pegWidth = 30
    pegHeight = 30
    firstY = 100
    for row in range(3, rows):
        thisY = firstY + row * pegHeight
        firstX = app.width / 2 - pegWidth * (row - 1) / 2
        nPegs = row
        for col in range(nPegs):
            thisX = firstX + pegWidth * col
            app.pegs.append(Peg(Vector2(thisX, thisY)))

    app.balls = []
    app.slotValues = [
        0,10,5,2,1,0.5,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.2,0.5,1,2,5,10,0  # 88% return (based on data)
    ]
    app.stepsPerSecond = 25
    app.count = 0

    app.slotFrequencies = [0 for _ in range(21)]


if __name__ == '__main__':
    runApp()
