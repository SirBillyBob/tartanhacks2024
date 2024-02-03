from cmu_graphics import *
from PIL import Image as img
import random

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = rgb(0, 0, 0)
    app.slotMachineLever = (CMUImage(img.open("redcircle.png")), 1)
    app.leverX = 730
    app.leverY = 327
    app.slotMachineLeverOn = False
    app.infoButtonGrayBackground = False
    app.infoBackButtonGrayBackground = False
    app.spinButtonGrayBackground = False
    app.isInfo = False
    app.isSpin = False
    app.imageList = [(CMUImage(img.open('balsamiq_logo.png')), 500/1000), (CMUImage(img.open('codedex_logo.png')), 150/939),
                     (CMUImage(img.open('gsa_logo.png')), 400/400), (CMUImage(img.open('olympus_logo.png')), 380/1123),
                     (CMUImage(img.open('pls_logo.png')), 405/1200), (CMUImage(img.open('ripple_logo.png')), 735/2560),
                     (CMUImage(img.open('theroboticsclub_logo.png')), 280/280),(CMUImage(img.open('wolfram_logo.png')), 349/1200)]
    app.imagesSlot1 = [4,5,6]
    app.imagesSlot2 = [4,5,6]
    app.imagesSlot3 = [4,5,6]
    app.imagesY = [225,375,525]
    app.imagesYStop = [225,375,525]
    app.spinStart = 0
    app.spinCounter = 0

def redrawAll(app):
    if (not app.isInfo):
        #levers
        drawPolygon(690, 375, 730, app.leverY-2, 730, app.leverY+3, 690, 380, fill='white')
        drawImage(
            app.slotMachineLever[0], app.leverX, app.leverY, align = 'center', width = 25, height = 25 * app.slotMachineLever[1])
        
        #slot1Button
        drawRect(200, 375, 200, 300, fill='white', border='Gray', borderWidth=5, align='center')
        #slot2Button
        drawRect(395, 375, 200, 300, fill='white', border='Gray', borderWidth=5, align='center')
        #slot3Button
        drawRect(590, 375, 200, 300, fill='white', border='Gray', borderWidth=5, align='center')
        
        for i in range(3):
            for j in range(3):
                if (i == 0): imagesSlot = app.imagesSlot1
                if (i == 1): imagesSlot = app.imagesSlot2
                if (i == 2): imagesSlot = app.imagesSlot3
                imagesY = app.imagesY
                if (app.spinStart > i): imagesY = app.imagesYStop
                drawImage(app.imageList[imagesSlot[j]][0], 200+i*195, imagesY[j], align = 'center',
                    width = 140, height = 140 * app.imageList[imagesSlot[j]][1])
        
        #cover top and bottom gray
        drawRect(395, 227.5, 590, 5, fill='gray', align='center')
        drawRect(395, 522.5, 590, 5, fill='gray', align='center')
        #cover top and bottom black
        drawRect(395, 125, 590, 200, fill='black', align='center')
        drawRect(395, 625, 590, 200, fill='black', align='center')

        
        #title
        drawLabel("SPIN TO WIN", 400, 100, size=70, font='monospace', fill='gold', bold=True)

        #wins
        if (not app.isSpin):
            strWinnings = winnings([app.imagesSlot1[1], app.imagesSlot2[1], app.imagesSlot3[1]])
            if (strWinnings == "nothing"): strWinnings = "Nothing..."
            elif (strWinnings == "two"): strWinnings = "You won with two of a kind! (+2 XRP)"
            elif (strWinnings == "twoRipple"): strWinnings = "You won with two Ripple! (+4 XRP)"
            elif (strWinnings == "three"): strWinnings = "You won with three of a kind! (+10 XRP)"
            else: strWinnings = "YOU WON THE JACKPOT!!! (+15 XRP)"
            
            if (strWinnings == "Nothing..."): drawLabel(strWinnings, 400, 195, size=20, font='arial', fill='white', bold=True)
            else: drawLabel(strWinnings, 400, 195, size=30, font='arial', fill='green', bold=True)

        #infoButtonGrayBackground
        if (app.infoButtonGrayBackground): drawRect(202.5, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
        #infoButton
        drawRect(202.5, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')
        drawLabel(
            "Info", 202.5, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
        
        #spinButtonGrayBackground
        if (app.spinButtonGrayBackground): drawRect(592.5, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
        #spinButton
        drawRect(592.5, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')
        drawLabel(
            "Spin", 592.5, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
    elif (app.isInfo):
        #subtitle
        drawLabel("Information", 400, 100, size=40, font='monospace', fill='white', bold=True)

        #info
        drawLabel("To spin the slots, you may either:", 400, 150, size=20, font='monospace', fill='white')
        drawLabel("click the 'Spin' button", 400, 170, size=20, font='monospace', fill='white')
        drawLabel("or", 400, 190, size=20, font='monospace', fill='white')
        drawLabel("press the lever (red) and pull it down", 400, 207, size=20, font='monospace', fill='white')
        
        drawLabel("Winning:", 400, 300, size=20, font='monospace', fill='white', bold=True)
        drawLabel("2 of a kind = 2 XRP", 400, 320, size=20, font='monospace', fill='white')
        drawLabel("2 of a kind (Ripple) = 4 XRP", 400, 340, size=20, font='monospace', fill='white')
        drawLabel("3 of a kind = 10 XRP", 400, 360, size=20, font='monospace', fill='white')
        drawLabel("3 of a kind (Ripple) = 15 XRP", 400, 380, size=20, font='monospace', fill='white')

        #infoBackButtonGrayBackground
        if (app.infoBackButtonGrayBackground): drawRect(400, 650, 115, 65, fill='Gray', border=None, borderWidth=2, align='center')
        #infoBackButton
        drawRect(400, 650, 100, 50, fill='white', border=None, borderWidth=2, align='center')
        drawLabel(
            "Back", 400, 650, size=20, font='arial', bold=True, italic=False, fill='black', border=None, borderWidth=2, align='center')
    
def onStep(app):
    if (app.isSpin):
        app.imagesY[0] += 50
        app.imagesY[1] += 50
        app.imagesY[2] += 50

        if ((app.imagesY[0]+app.imagesY[1])/2 >= 375):
            for i in range(app.spinStart, 3):
                if (i == 0): imagesSlot = app.imagesSlot1
                if (i == 1): imagesSlot = app.imagesSlot2
                if (i == 2): imagesSlot = app.imagesSlot3
                imagesSlot[2] = imagesSlot[1]
                imagesSlot[1] = imagesSlot[0]
                if (app.spinCounter == 23):
                    newList = imagesSlot+[app.imagesSlot1[1], app.imagesSlot1[1]]
                    rand = int(random.randrange(0,9))%8
                    while (rand == imagesSlot[1] or rand == imagesSlot[2]):
                        rand = int(random.randrange(0,9))%8
                elif (app.spinCounter == 33):
                    newList = imagesSlot+[app.imagesSlot1[1], app.imagesSlot1[1], app.imagesSlot2[1], app.imagesSlot2[1]]
                    rand = int(random.randrange(0,10))%8
                    while (rand == imagesSlot[1] or rand == imagesSlot[2]):
                        rand = int(random.randrange(0,10))%8
                else:
                    rand = int(random.randrange(0,8))
                    while (rand == imagesSlot[1] or rand == imagesSlot[2]):
                        rand = int(random.randrange(0,8))
                imagesSlot[0] = rand
            
            app.imagesY[2] = app.imagesY[1]
            app.imagesY[1] = app.imagesY[0]
            app.imagesY[0] = app.imagesY[1]-150
            app.spinCounter += 1
            if (app.spinCounter >= 15): app.spinStart = 1
            if (app.spinCounter >= 25): app.spinStart = 2
            if (app.spinCounter >= 35):
                app.imagesY = [225,375,525]
                app.spinStart = 0
                app.spinCounter = 0
                app.isSpin = False

def onMouseDrag(app, x, y):
    if (not app.isInfo and not app.isSpin):
        if (app.slotMachineLeverOn or ((x-app.leverX)**2+(y-app.leverY)**2)**(1/2) < 25):
            #slotmachinelever
            app.slotMachineLeverOn = True
            if (y >= 410 or y <= 327):
                if (y <= 327):
                    app.leverY = 327
                if (y >= 410):
                    app.leverY = 410
            
            if (app.slotMachineLeverOn or ((x-app.leverX)**2+(y-app.leverY)**2)**(1/2) < 25):
                if (y <= 327):
                    app.leverY = 327
                elif (y >= 410):
                    app.leverY = 410
                else:
                    app.leverY = y

def onMouseRelease(app, x, y):
    app.slotMachineLeverOn = False

    if (app.leverY == 410):
        app.isSpin = True
        app.leverY = 327
    else:
        app.leverY = 327

def onMouseMove(app, x, y):
    if (not app.isInfo and not app.isSpin):
        #infoButton
        if (x >= 152.5 and x <= 252.5 and y >= 625 and y <= 675): app.infoButtonGrayBackground = True
        else: app.infoButtonGrayBackground = False

        #spinButton
        if (x >= 542.5 and x <= 642.5 and y >= 625 and y <= 675): app.spinButtonGrayBackground = True
        else: app.spinButtonGrayBackground = False
    
    if (app.isInfo):
        #infoBackButton
        if (x >= 350 and x <= 450 and y >= 625 and y <= 675): app.infoBackButtonGrayBackground = True
        else: app.infoBackButtonGrayBackground = False

def onMousePress(app, x, y):
    if (not app.isInfo and not app.isSpin):
        #infoButton
        if (x >= 152.5 and x <= 252.5 and y >= 625 and y <= 675):
            app.isInfo = True
            app.infoButtonGrayBackground = False

        #spinButton
        if (x >= 542.5 and x <= 642.5 and y >= 625 and y <= 675):
            app.isSpin = True
            app.spinButtonGrayBackground = False
    
    if (app.isInfo):
        if (x >= 350 and x <= 450 and y >= 625 and y <= 675):
            app.isInfo = False
            app.infoBackButtonGrayBackground = False

def winnings(list):
    sortedList = sorted(list)
    if (sortedList[0] == sortedList[2]):
        if (sortedList[0] == 5): return "jackpot"
        else: return "three"
    elif (sortedList[0] == sortedList[1] or sortedList[1] == sortedList[2]):
        if (sortedList[1] == 5): return "twoRipple"
        else: return "two"
    else:
        return "nothing"

runApp()