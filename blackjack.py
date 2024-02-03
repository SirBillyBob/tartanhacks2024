from cmu_graphics import *
from PIL import Image as img


def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = rgb(0, 0, 0)

    app.cards = []
    app.card = img.open('playingcards.png')
    dx = 2906/13
    dy = 1563/5
    for i in range(4):
        for j in range(13):
            temp = app.card.crop( (j*dx, i*dy, (j+1)*dx, (i+1)*dy))
            app.cards.append(CMUImage(temp))

    app.startButton = True
    app.startButtonY = 600
    app.isStart = False
    app.startButtonGrayBackground = False

    app.houseCards = []
    app.playerCards = []



    


def redrawAll(app):
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
        #title
        drawLabel("Blackjack", 400, 70, size=50, font='monospace', fill='white', bold=True)
        #house vs player
        drawLabel("House", 150, 200, size=20, font='monospace', fill='white', bold=True)
        drawLabel("Player", 150, 400, size=20, font='monospace', fill='white', bold=True)


#def onStep(app):

def onMouseMove(app, x, y):
    if (app.isStart):
        a=1
    else:
        #startButton
        if (x >= 350 and x <= 450 and y >= app.startButtonY-25 and y <= app.startButtonY+25): app.startButtonGrayBackground = True
        else: app.startButtonGrayBackground = False

def onMousePress(app, x, y):
    if (app.isStart):
        a=1
    else:
        if (x >= 350 and x <= 450 and y >= app.startButtonY-25 and y <= app.startButtonY+25):
            app.isStart = True
            app.startButtonGrayBackground = False
        

runApp()