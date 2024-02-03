from cmu_graphics import *
from ball import Ball
from peg import Peg


def redrawAll(app):
    for peg in app.pegs:
        peg.draw()

    for ball in app.balls:
        ball.draw()


def onMousePress(app, mouseX, mouseY):
    app.balls.append(Ball([app.width / 2, 25], 10))


def onStep(app):
    for ball in app.balls:
        ball.vel[1] += 1
        ball.updatePos()
        for peg in app.pegs:
            if dist(*peg.pos, *ball.pos) <= 10:
                ball.collidePeg()


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = "green"

    app.pegs = []
    rows = 20
    pegWidth = 30
    pegHeight = 30
    firstY = 50
    for row in range(rows):
        thisY = firstY + row * pegHeight
        firstX = app.width / 2 - pegWidth * (row - 1) / 2
        nPegs = row
        for col in range(nPegs):
            thisX = firstX + pegWidth * col
            app.pegs.append(Peg((thisX, thisY)))

    app.balls = []
    app.stepsPerSecond = 60


if __name__ == '__main__':
    runApp()
