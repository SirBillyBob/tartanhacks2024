from cmu_graphics import *
from PIL import Image as img
from button import *
import random
from math import sin, cos, pi

def onAppStart(app):
    rouletteOAS(app)

def rouletteOAS(app):
    app.width = 800
    app.height = 800
    app.background = rgb(92*0.4, 64*0.4, 51*0.4)
    app.board = CMUImage(img.open("roulette_assets/roulette_board.png"))
    app.angles = [11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26,0,32,15,19,4,21,2,25,17,27,6,34,13,36]
    app.RA = -180
    app.spinSpeed = 0
    app.ballX = app.width//2 + 60
    app.ballY = app.height//2 - 160
    app.currOdds = "None"
    app.currOption = "None"
    app.redButton = Button("RED", app.width//6, app.height - app.height//11, 150, 50, 40, "red", "white", "white")
    app.blackButton = Button("BLACK", 50+ app.width//3, app.height - app.height//11, 150, 50, 40, "black", "white", "white")
    app.oddButton = Button("ODD", 100+app.width//2, app.height - app.height//11, 150, 50, 40, "lightslategrey", "white", "white")
    app.evenButton = Button("EVEN", 150+app.width//6 + app.width//2, app.height - app.height//11, 150, 50, 40, "darkslategrey", "white", "white")
    app.playAgain = Button("Spin Again", app.width//2, app.height//2+65,200,50,30, color = "lightgreen", border = "black", textColor = "black")
    app.spinning = False
    app.ballspinning = False
    app.goal = 0
    app.t = 0
    app.ballRS = -0.2
    app.nums = []
    app.clickedNums = []
    app.radius = 220
    app.roundOver = False
    app.victory = False
    for i in range(1,37):
        if i == 0:
            color = "lightgreen"
        elif 10<=i and i<=10 or 19<=i and i<=28:
            if i%2 == 0:
                color = 'black'
            else:
                color = 'red'
        else:
            if i%2 == 0:
                color = 'red'
            else:
                color = 'black'
        app.nums.append(Button(f"{i}",app.width//11 + 20*((i-1)%6), app.height//2+20*((i-1)//6) + 100, 20, 20, 10, color = color, textColor = 'white' if color == 'black' else 'white', border='grey'))
    app.backspaceButton = Button("Backspace", app.width//11+23, app.height//2 + 225, 70, 20, 10, color = "grey", textColor = "black", border = "black")

def redrawAll(app):
    drawImage(app.board, app.width//2 + 60, app.height//2+25, align = 'center', width = 450, height = 450, rotateAngle = app.RA)
    drawCircle(app.width//2 + 300, app.height//2+210 , 60, fill = "limegreen", border = "black")
    drawLabel("SPIN!",app.width//2 + 300, app.height//2+210, align = "center", fill = "white", bold = True, size = 35)
    drawLabel(f"Current Bet:", app.width//3 - 130, app.height//7 + 140, align = 'center', fill = "white", size = 25)
    drawLabel(f"{app.currOption}", app.width//3 - 130, app.height//7 + 172, align = 'center', fill = "white", size = 25)
    drawLabel(f"Payout:", app.width//3 - 130, app.height//7 + 240, align = 'center', fill = "white", size = 25)
    drawLabel(f"{app.currOdds}", app.width//3 - 130, app.height//7 + 272, align = 'center', fill = "white", size = 25)
    drawLabel("Choose up to 6 numbers: ", app.width//11 - 25, app.height//2 + 78, align = 'bottom-left', fill = "white", size = 15)
    drawLabel("Or choose from: ", app.width//11 - 25, app.height//2 + 275, align = 'bottom-left', fill = "white", size = 25)
    drawCircle(app.ballX, app.ballY, 7, fill = "white", border = "black")


    app.redButton.drawButton()
    app.blackButton.drawButton()
    app.oddButton.drawButton()
    app.evenButton.drawButton()
    app.backspaceButton.drawButton()
    for i in app.nums:
        i.drawButton()
    
    if app.roundOver:
        drawRect(app.width//2, app.height//2, 400, 200, fill = "grey", border = "black", align = "center")
        app.playAgain.drawButton()
        if app.victory:
            drawLabel("You guessed right!", app.width//2, app.height//2-25, align = "center",size = 25)
            drawLabel(f"The {app.currOdds} payout has been applied.",app.width//2, app.height//2+25, align = "center", size = 25)
        else:
            drawLabel("You were wrong :(", app.width//2, app.height//2-20, align = "center",size = 25)
        

    

def onStep(app):
    app.RA += app.spinSpeed
    if app.spinning and app.rotations == app.spinSpeed*10:
        app.spinSpeed -= 1
        if app.spinSpeed == 0:
            app.spinning = False
        app.rotations = 0
    elif app.spinning:
        app.rotations += 1
    
    if app.ballspinning:
        app.t+=app.ballRS
        app.ballRS += 0.0005
        app.radius -= 0.2
        if app.ballRS >= 0:
            app.ballspinning = False
            app.roundOver = True
            checkWin(app, app.goal, app.currOption)
        rotateBall(app,app.goal)

def checkWin(app, goal, state):
    win = False
    goal = app.angles[goal]
    if state == "RED":
        if goal in [3,12,7,18,9,14,1,16,5,23,30,36,34,27,25,21,19,32]:
            win = True
    elif state == "BLACK":
        if goal!= 0 and goal not in [3,12,7,18,9,14,1,16,5,23,30,36,34,27,25,21,19,32]:
            win = True
    elif state == "EVEN":
        if goal%2 == 0:
            win = True
    elif state == "ODD":
        if goal%2 == 1:
            win = True
    else:
        nums = state.split(' ')
        nums = [int(i) for i in nums]
        if goal in nums:
            win = True
    
    app.victory = win

def onMousePress(app, x, y):
    if not app.roundOver:
        app.redButton.buttonPressed(x,y,changeBet,(app,"RED"))
        app.blackButton.buttonPressed(x,y,changeBet,(app,"BLACK"))
        app.oddButton.buttonPressed(x,y,changeBet,(app,"ODD"))
        app.evenButton.buttonPressed(x,y,changeBet,(app,"EVEN"))
        for button in app.nums:
            button.buttonPressed(x, y, addNum, (app, button.text ))
        app.backspaceButton.buttonPressed(x,y,popNum, (app,))
        bx, by = (app.width//2 + 300, app.height//2+210)
        if (x-bx)**2 + (y-by)**2 <= 60**2 and not app.ballspinning:
            spin(app)
            temp = random.randrange(0, 37)
            for i,v in enumerate(app.angles):
                if v == temp:
                    app.goal = i
                    break
    else:
        app.playAgain.buttonPressed(x,y,rouletteOAS,(app,))


def spin(app):
    if app.currOption != "None" and not app.spinning:
        app.ballspinning = True
        app.spinning = True
        app.spinSpeed = 7
        app.rotations = 0

def rotateBall(app, goal):
    r = app.radius
    app.ballX = app.width//2 +60 + r*cos(app.t+pi/18*goal-(pi/(18*36))*goal if goal >= 18 else app.t+pi/18*goal)
    app.ballY = app.height//2+25 + r*sin(app.t+pi/18*goal-(pi/(18*36))*goal if goal >= 18 else app.t+pi/18*goal)


def popNum(app):
    if len(app.clickedNums) > 0:
        app.clickedNums.pop()
        changeBet(app, ' '.join(app.clickedNums))
    if len(app.clickedNums) == 0:
        changeBet(app, 'None')

def changeBet(app, bet):
    if not app.spinning:
        app.currOption = bet
        if bet == "BLACK" or bet == "RED" or bet == "ODD" or bet == "EVEN":
            app.clickedNums = []
            app.currOdds = "x2.0"
        else:
            l = len(app.clickedNums)
            match l:
                case 1:
                    app.currOdds = "x35.0"
                case 2:
                    app.currOdds = "x17.0"
                case 3:
                    app.currOdds = "x11.0"
                case 4:
                    app.currOdds = "x8.0"
                case 5:
                    app.currOdds = "x6.0"
                case 6:
                    app.currOdds = "x5.0"
                case _:
                    app.currOdds = None

def addNum(app, num):
    if len(app.clickedNums) < 6 and not app.spinning:
        if num not in app.clickedNums:
            app.clickedNums.append(num)
            changeBet(app, ' '.join(app.clickedNums))

if __name__ == "__main__":
    runApp()
