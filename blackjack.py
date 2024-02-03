from cmu_graphics import *
from PIL import Image as img
import random


def blackjackOAS(app):
    app.width = 800
    app.height = 800
    app.background = rgb(0, 0, 0)

    app.cards = []
    app.card = img.open('blackjack_assets/playingcards.png')
    dx = 2906/13
    dy = 1563/5
    for i in range(5):
        for j in range(13):
            temp = app.card.crop( (j*dx, i*dy, (j+1)*dx, (i+1)*dy))
            app.cards.append(CMUImage(temp))

    app.startButton = True
    app.startButtonY = 600
    app.isStart = False
    app.startButtonGrayBackground = False
    app.hitButtonGrayBackground = False
    app.standButtonGrayBackground = False
    app.nextButtonGrayBackground = False
    app.replayButtonGrayBackground = False
    app.usedCardIndices = []
    app.houseCards = []
    app.playerCards = []
    start4Cards(app)
    app.isPlayerTurn = True
    app.playerBust = False
    app.houseBust = False
    app.playerDirectWin = False
    app.gameOver = False
    app.balance -= 10
    

def blackjackOKP(app, key):
    if key == "escape":
        app.reset(app)

def blackjackRA(app):
    drawLabel(f"Balance: {app.balance} XRP", app.width//2, 144, size = 20, fill = 'white')
    if (not app.isStart):
        #title
        drawLabel("Blackjack", 400, 100, size=70, font='monospace', fill='white', bold=True)
        
        #logo
        drawImage(app.cards[26], 390, 360, align='center', rotateAngle=-5)
        drawImage(app.cards[51], 420, 370, align='center', rotateAngle=5)

        #startButtonGrayBackground
        if (app.startButtonGrayBackground): drawRect(400, app.startButtonY, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
        #startButton
        drawRect(400, app.startButtonY, 100, 50, fill='white', border=None, borderWidth=2, align='center')
        drawLabel("Start", 400, app.startButtonY, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
    else:
        if (app.isPlayerTurn):
            #hitButtonGrayBackground
            if (app.hitButtonGrayBackground): drawRect(202.5, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
            #hitButton
            drawRect(202.5, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')
            drawLabel(
                "Hit", 202.5, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
            
            #standButtonGrayBackground
            if (app.standButtonGrayBackground): drawRect(592.5, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
            #standButton
            drawRect(592.5, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')
            drawLabel(
                "Stand", 592.5, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
        else:
            if (not app.gameOver):
                #nextButtonGrayBackground
                app.nextButtonGrayBackground
                if (app.nextButtonGrayBackground): drawRect(592.5, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
                #nextButton
                drawRect(592.5, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')
                drawLabel(
                    "Next", 592.5, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
            else:
                #replayButtonGrayBackground
                app.replayButtonGrayBackground
                if (app.replayButtonGrayBackground): drawRect(400, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
                #replayButton
                drawRect(400, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')

                if (not app.playerBust):
                    if (app.playerDirectWin or app.houseBust or (sum(app.playerCards) > sum(app.houseCards))):
                        drawLabel(
                            "YOU WON!!!", 150, 450, size=40, font='arial', bold=True, italic=False, fill='Green', border=None, borderWidth=2, align='center')
                    elif (sum(app.playerCards) == sum(app.houseCards)):
                        drawLabel(
                            "Tie", 150, 450, size=30, font='arial', bold=True, italic=False, fill='Cyan', border=None, borderWidth=2, align='center')
                    else:
                        drawLabel(
                            "You lost", 150, 450, size=20, font='arial', bold=True, italic=False, fill='red', border=None, borderWidth=2, align='center')
                drawLabel(
                        "Replay", 400, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')

        #title
        drawLabel("Blackjack", 400, 70, size=50, font='monospace', fill='white', bold=True)
        #house and player score
        if (not app.isPlayerTurn): houseStr = str(sum(app.houseCards))
        else: houseStr = ""
        drawLabel("House score: " + houseStr, 150, 200, size=20, font='monospace', fill='white', bold=True)
        drawLabel("Player score: " + str(sum(app.playerCards)), 150, 400, size=20, font='monospace', fill='white', bold=True)

        if (app.houseBust):
            drawPolygon(50, 180, 250, 230, 250, 220, 50, 170, fill='red')
            drawPolygon(50, 220, 250, 170, 250, 180, 50, 230, fill='red')
            drawLabel("BUST", 150, 250, size=40, font='arial', fill='red', bold=True)
        
        if (app.playerBust):
            drawPolygon(50, 380, 250, 430, 250, 420, 50, 370, fill='red')
            drawPolygon(50, 420, 250, 370, 250, 380, 50, 430, fill='red')
            drawLabel("BUST", 150, 450, size=40, font='arial', fill='red', bold=True)
            

        #house cards
        index = 0
        if (app.isPlayerTurn):
            drawImage(app.cards[app.houseCards[0]], 410, 250, align='center', width = 120, height = 120*((1563/5)/(2906/13)))
            drawImage(app.cards[52], 450, 250, align='center', width = 120, height = 120*((1563/5)/(2906/13)))
        else:
            for i in app.houseCards:
                drawImage(app.cards[i], 410+index*40, 250, align='center', width = 120, height = 120*((1563/5)/(2906/13)))
                index += 1
        #player cards
        index = 0
        for i in app.playerCards:
            drawImage(app.cards[i], 410+index*40, 450, align='center', width = 120, height = 120*((1563/5)/(2906/13)))
            index += 1


#def onStep(app):

def blackjackOMM(app, x, y):
    if (app.isStart):
        if (app.isPlayerTurn):
            #hitButton
            if (x >= 152.5 and x <= 252.5 and y >= 650-25 and y <= 650+25): app.hitButtonGrayBackground = True
            else: app.hitButtonGrayBackground = False
            #standButton
            if (x >= 542.5 and x <= 642.5 and y >= 650-25 and y <= 650+25): app.standButtonGrayBackground = True
            else: app.standButtonGrayBackground = False
        else:
            if (not app.gameOver):
                #nextButton
                if (x >= 542.5 and x <= 642.5 and y >= 650-25 and y <= 650+25): app.nextButtonGrayBackground = True
                else: app.nextButtonGrayBackground = False
            else:
                #replayButton
                if (x >= 350 and x <= 450 and y >= 650-25 and y <= 650+25): app.replayButtonGrayBackground = True
                else: app.replayButtonGrayBackground = False
    else:
        #startButton
        if (x >= 350 and x <= 450 and y >= app.startButtonY-25 and y <= app.startButtonY+25): app.startButtonGrayBackground = True
        else: app.startButtonGrayBackground = False

def blackjackOMP(app, x, y):
    if (app.isStart):
        if (app.isPlayerTurn):
            #hitButton
            if (x >= 152.5 and x <= 252.5 and y >= 650-25 and y <= 650+25):
                hit(app, app.playerCards, True)
                app.hitButtonGrayBackground = False
            #standButton
            if (x >= 542.5 and x <= 642.5 and y >= 650-25 and y <= 650+25):
                app.standButtonGrayBackground = False
                app.isPlayerTurn = False
        elif (not app.gameOver):
            #nextButton
            if (x >= 542.5 and x <= 642.5 and y >= 650-25 and y <= 650+25):
                hit(app, app.houseCards, False)
                app.nextButtonGrayBackground = True
            else: app.nextButtonGrayBackground = False
        else:
            #replayButton
            if (x >= 350 and x <= 450 and y >= 650-25 and y <= 650+25):
                app.replayButtonGrayBackground = True
                blackjackOAS(app)
            else: app.replayButtonGrayBackground = False
    else:
        if (x >= 350 and x <= 450 and y >= app.startButtonY-25 and y <= app.startButtonY+25):
            app.isStart = True
            app.startButtonGrayBackground = False
        
def start4Cards(app):
    startCards = []
    randI = int(random.randrange(0, 52))
    startCards.append(randI)
    app.usedCardIndices.append(randI)
    for i in range(3):
        randI = int(random.randrange(0, 52))
        for j in app.usedCardIndices:
            if (randI == j): randI = int(random.randrange(0,52))
        startCards.append(randI)
        app.usedCardIndices.append(randI)
    app.houseCards.append(startCards[0])
    app.houseCards.append(startCards[1])
    app.playerCards.append(startCards[2])
    app.playerCards.append(startCards[3])

def sum(list):
    sum = 0
    numAce = 0
    sortedList = []
    for i in list:
        sortedList.append(i%13)
    sortedList = sorted(sortedList)
    for i in sortedList:
        if (i == 0): numAce += 1
        else: break
        
    for i in range(numAce, len(sortedList)):
        sum += min(sortedList[i]%13 + 1, 10)
    
    for i in range(0, numAce):
        if (sum + 11 <= 21): sum += 11
        else: sum += 1
    return sum

def hit(app, list, isPlayer):
    if (isPlayer):
        if (sum(list) == 21): 
            app.balance+= 20
            app.isPlayerTurn = False
    if (not isPlayer):
        if (sum(list) >= 17):
            app.gameOver = True
            return
    rand = int(random.randrange(0, 52))
    for i in app.usedCardIndices:
        if (rand == i): rand = int(random.randrange(0,52))
    list.append(rand)
    app.usedCardIndices.append(rand)
    
    if (sum(list) > 21):
        if isPlayer:
            app.playerBust = True
            app.isPlayerTurn = False
        else:
            app.houseBust = True
            app.playerDirectWin = True
            app.balance += 20
        app.gameOver = True
    elif (isPlayer and len(list) == 5):
        app.playerDirectWin = True
        app.balance += 20
        app.gameOver = True
