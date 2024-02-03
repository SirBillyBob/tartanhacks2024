from cmu_graphics import *
from ball import Ball
from peg import Peg
from vector2 import *


def redrawAll(app):
    for peg in app.pegs:
        peg.draw()

    for ball in app.balls:
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

    drawLabel(f"Balance: ${app.balance}", 600, 50, size=20, bold=True, fill="lightSlateGray")

    drawLine(app.width / 2 - 35, 0, app.width / 2 - 35, 100, fill='lightSlateGray')
    drawLine(app.width / 2 + 35, 0, app.width / 2 + 35, 100, fill='lightSlateGray')
    drawLine(app.width / 2 - 35, 100, app.width / 2 - 335, 700, fill='lightSlateGray')
    drawLine(app.width / 2 + 35, 100, app.width / 2 + 335, 700, fill='lightSlateGray')
    drawLine(app.width / 2 - 335, 700, app.width / 2 - 335, app.height, fill='lightSlateGray')
    drawLine(app.width / 2 + 335, 700, app.width / 2 + 335, app.height, fill='lightSlateGray')

    for x in range(int(app.width / 2 - 285), int(app.width / 2 + 286), 30):
        drawLine(x, 700, x, app.height, fill='lightSlateGray')

    for i in range(21):
        x = 100 + i * 30
        if i == 0:
            x -= 10
        elif i == 20:
            x += 10
        drawLabel(f"{app.slotValues[i]}", x, 750, size=16, fill='lightSlateGray', bold=True)


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
                if app.width / 2 - 285 < ball.pos.x < app.width / 2 + 285:
                    slot = (int(ball.pos.x - (app.width / 2 - 285)) // 30) + 1
                    app.balance += app.slotValues[slot] * ball.value
                    app.balance = pythonRound(app.balance, 2)
                app.balls.remove(ball)
            else:
                ball.collideWalls(app.width)


def onMousePress(app, mouseX, mouseY):
    pass


def onKeyPress(app, key):
    if key == "enter":
        print(app.slotFrequencies)
    else:
        if key == '1' and app.balance >= 1:
            app.balls.append(Ball(Vector2(app.width / 2, 50), 1))
            app.balance -= 1
            app.balance = pythonRound(app.balance, 2)
        elif key == '2' and app.balance >= 5:
            app.balls.append(Ball(Vector2(app.width / 2, 50), 5))
            app.balance -= 5
            app.balance = pythonRound(app.balance, 2)
        elif key == '3' and app.balance >= 10:
            app.balls.append(Ball(Vector2(app.width / 2, 50), 10))
            app.balance -= 10
            app.balance = pythonRound(app.balance, 2)
        elif key == '4' and app.balance >= 20:
            app.balls.append(Ball(Vector2(app.width / 2, 50), 20))
            app.balance -= 20
            app.balance = pythonRound(app.balance, 2)
        elif key == '5' and app.balance >= 50:
            app.balls.append(Ball(Vector2(app.width / 2, 50), 50))
            app.balance -= 50
            app.balance = pythonRound(app.balance, 2)
        elif key == '6' and app.balance >= 100:
            app.balls.append(Ball(Vector2(app.width / 2, 50), 100))
            app.balance -= 100
            app.balance = pythonRound(app.balance, 2)

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = "black"

    app.balance = 200

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
    app.stepsPerSecond = 30


if __name__ == '__main__':
    runApp()
