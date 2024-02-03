from cmu_graphics import *
import random
from PIL import Image as img

#slotmachine
#800x800

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = rgb(0, 83, 24)
    app.craps = CMUImage(img.open('craps/assets/cboard.PNG'))
    app.rolls = [0, 0]
    app.currMode = "C"
    app.bets = {}
    app.currBet = 10
    app.dbal = 500
    app.bal = 500
    app.point = 0


def redrawAll(app):
    drawImage(app.craps, 110, 250)
    drawLabel("Craps", 400, 80, size=100, font='arial', bold=False, fill='white')
    drawCircle(621, 415, 2, fill = rgb(222, 244, 53))
    drawCircle(611, 415, 2, fill = rgb(222, 244, 53))
    drawRect(150, 700, 150, 75, align = 'center', fill = 'white', border = "black")
    drawLabel("Roll", 150, 700, size=50, font='arial', bold=False, fill='black')
    drawLabel(app.rolls[0], 350, 700, size=50, font='arial', bold=False, fill='black')
    drawLabel(app.rolls[1], 450, 700, size=50, font='arial', bold=False, fill='black')
    drawRect(575, 700, 75, 75, align = 'center', fill = 'white', border = "black")
    drawRect(675, 700, 75, 75, align = 'center', fill = 'white', border = "black")
    drawRect(625, 700, 100, 75, align = 'center', fill = 'white', border = "black")
    drawLabel("Bet", 625, 640, size=50, font='arial', bold=False, fill='black')
    drawLabel(app.currBet, 625, 700, size=50, font='arial', bold=False, fill='black')
    drawLine(557, 679, 557, 718, arrowEnd = True)
    drawLine(691, 679, 691, 718, arrowStart = True)

def onMousePress(app, x, y):
    if (x > 175 and x < 195 and y > 310 and y < 545) or (x > 198 and x < 514 and y > 524 and y < 546):
        if("pass" in app.bets):
            app.bets["pass"] += app.currBet
            app.bal -= app.currBet
        else:
            app.bets["pass"] = app.currBet
            app.bal -= app.currBet
    elif (x > 255 and x < 513 and y > 491 and y < 514) or (x > 207 and x < 230 and y > 297 and y < 463):
        if("no pass" in app.bets):
            app.bets["no pass"] += app.currBet
            app.bal -= app.currBet
        else:
            app.bets["no pass"] = app.currBet
            app.bal -= app.currBet
    elif (x > 232 and x < 278 and y > 294 and y < 366):
        if("dont come" in app.bets):
            app.bets["dont come"] += app.currBet
            app.bal -= app.currBet
        else:
            app.bets["dont come"] = app.currBet
            app.bal -= app.currBet
    elif (x > 233 and x < 514 and y > 370 and y < 440):
        if("come" in app.bets):
            app.bets["come"] += app.currBet
            app.bal -= app.currBet
        else:
            app.bets["come"] = app.currBet
            app.bal -= app.currBet
    elif(x > 279 and x < 560 and y > 302 and y < 358):
        if(x < 326):
            if("4" in app.bets):
                app.bets["4"] += app.currBet
                app.bal -= app.currBet
            else:
                app.bets["4"] = app.currBet
                app.bal -= app.currBet
        elif(x < 373):
            if("5" in app.bets):
                app.bets["5"] += app.currBet
                app.bal -= app.currBet
            else:
                app.bets["5"] = app.currBet
                app.bal -= app.currBet
        elif(x < 420):
            if("six" in app.bets):
                app.bets["six"] += app.currBet
                app.bal -= app.currBet
            else:
                app.bets["six"] = app.currBet
                app.bal -= app.currBet
        elif(x < 468):
            if("8" in app.bets):
                app.bets["8"] += app.currBet
                app.bal -= app.currBet
            else:
                app.bets["8"] = app.currBet
                app.bal -= app.currBet
        elif(x < 515):
            if("nine" in app.bets):
                app.bets["nine"] += app.currBet
                app.bal -= app.currBet
            else:
                app.bets["nine"] = app.currBet
                app.bal -= app.currBet
        else:
            if("10" in app.bets):
                app.bets["10"] += app.currBet
                app.bal -= app.currBet
            else:
                app.bets["10"] = app.currBet
                app.bal -= app.currBet
    elif(x > 244 and x < 510 and y > 443 and y < 483):
        if("field" in app.bets):
            app.bets["field"] += 10
        else:
            app.bets["field"] = 10
    elif(x > 530 and x < 643 and y > 386 and y < 433):
        if(y < 408):
            if(x < 587):
                if("2 2" in app.bets):
                    app.bets["2 2"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["2 2"] = app.currBet
                    app.bal -= app.currBet
            else:
                if("5 5" in app.bets):
                    app.bets["5 5"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["5 5"] = app.currBet
                    app.bal -= app.currBet
        else:
            if(x < 587):
                if("3 3" in app.bets):
                    app.bets["3 3"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["3 3"] = app.currBet
                    app.bal -= app.currBet
            else:
                if("4 4" in app.bets):
                    app.bets["4 4"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["4 4"] = app.currBet
                    app.bal -= app.currBet
    elif(x > 530 and x < 643 and y > 452 and y < 480):
        if("seven" in app.bets):
            app.bets["seven"] += app.currBet
            app.bal -= app.currBet
        else:
            app.bets["seven"] = app.currBet
            app.bal -= app.currBet
    elif(x > 530 and x < 643 and y > 481 and y < 530):
        if(y < 505):
            if(x < 586):
                if("1 2" in app.bets):
                    app.bets["1 2"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["1 2"] = app.currBet
                    app.bal -= app.currBet
            else:
                if("5 6" in app.bets):
                    app.bets["5 6"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["5 6"] = app.currBet
                    app.bal -= app.currBet
        else:
            if(x < 586):
                if("3 3" in app.bets):
                    app.bets["3 3"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["3 3"] = app.currBet
                    app.bal -= app.currBet
            else:
                if("6 6" in app.bets):
                    app.bets["6 6"] += app.currBet
                    app.bal -= app.currBet
                else:
                    app.bets["6 6"] = app.currBet
                    app.bal -= app.currBet
    elif(x > 530 and x < 643 and y > 533 and y < 558):
        if("any craps" in app.bets):
            app.bets["any craps"] += app.currBet
            app.bal -= app.currBet
        else:
            app.bets["any craps"] = app.currBet
            app.bal -= app.currBet
    elif(x > 76 and x < 222 and y > 665 and y < 733):
        app.rolls[0] = random.randint(1,6)
        app.rolls[1] = random.randint(1,6)
        if(app.rolls[0] == 1 and app.rolls[1] == 1):
            if(app.currMode == "C"):
                if("pass" in app.bets):
                    app.dbal += app.bets["pass"]
                if("no pass" in app.bets):
                    app.bal += app.bets["no pass"] * 2
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 3
                if("any craps" in app.bets):
                    app.bal += app.bets["any craps"] * 7
            if(app.currMode == "P"):
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 3
                if("any craps" in app.bets):
                    app.bal += app.bets["any craps"] * 7
            for i in app.bets:
                if(i != "2 2" and i != "5 5" and i != "4 4" and i != "3 3"):
                    app.dbal += app.bets[i]
                    app.bets[i] = 0
        elif((app.rolls[0] == 1 and app.rolls[1] == 2) or (app.rolls[1] == 1 and app.rolls[0] == 2)):
            if(app.currMode == "C"):
                if("pass" in app.bets):
                    app.dbal += app.bets["pass"]
                if("no pass" in app.bets):
                    app.bal += app.bets["no pass"] * 2
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                if("any craps" in app.bets):
                    app.bal += app.bets["any craps"] * 7
                if("1 2" in app.bets):
                    app.bal += app.bets["1 2"] * 16
            if(app.currMode == "P"):
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                if("any craps" in app.bets):
                    app.bal += app.bets["any craps"] * 7
                if("1 2" in app.bets):
                    app.bal += app.bets["1 2"] * 16
            for i in app.bets:
                if(i != "2 2" and i != "5 5" and i != "4 4" and i != "3 3"):
                    app.dbal += app.bets[i]
                    app.bets[i] = 0
        elif((app.rolls[0] == 3 and app.rolls[1] == 1) or (app.rolls[1] == 3 and app.rolls[0] == 1)):
            if("4" in app.bets):
                app.bal += app.bets["4"] * (14/5)
            if(app.currMode == "C"):
                app.point = 4
                if("pass" in app.bets):
                    app.point = 4
                if("no pass" in app.bets):
                    app.point = 4
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
                app.currMode = "P"
            if(app.currMode == "P"):
                if(app.point == 4):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "3 3"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                    app.currMode = "C"
                if("field" in app.bets):
                    app.bal += app.bets["field"]
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 2 and app.rolls[1] == 2)):
            if("4" in app.bets):
                app.bal += app.bets["4"] * (14/5)
            if(app.currMode == "C"):
                app.point = 4
                if("pass" in app.bets):
                    app.point = 4
                if("no pass" in app.bets):
                    app.point = 4
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                if("2 2" in app.bets):
                    app.bal += app.bets["2 2"] * 8
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
                app.currMode = "P"
            if(app.currMode == "P"):
                if(app.point == 4):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    if("2 2" in app.bets):
                        app.bal += app.bets["2 2"] * 8
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "3 3"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                    app.currMode = "C"
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 3 and app.rolls[1] == 2) or (app.rolls[1] == 3 and app.rolls[0] == 2) or (app.rolls[1] == 1 and app.rolls[0] == 4) or (app.rolls[1] == 4 and app.rolls[0] == 1)):
            if("5" in app.bets):
                app.bal += app.bets["5"] * (12/5)
            if(app.currMode == "C"):
                app.point = 5
                if("pass" in app.bets):
                    app.point = 5
                if("no pass" in app.bets):
                    app.point = 5
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
                app.currMode = "P"
            if(app.currMode == "P"):
                if(app.point == 5):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "3 3"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                        app.currMode = "C"
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 1 and app.rolls[1] == 5) or (app.rolls[1] == 1 and app.rolls[0] == 5) or (app.rolls[1] == 2 and app.rolls[0] == 4) or (app.rolls[1] == 4 and app.rolls[0] == 2)):
            if("six" in app.bets):
                app.bal += app.bets["six"] * (13/6)
            if(app.currMode == "C"):
                app.point = 6
                if("pass" in app.bets):
                    app.point = 6
                if("no pass" in app.bets):
                    app.point = 6
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
                app.currMode = "P"
            if(app.currMode == "P"):
                if(app.point == 6):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                    app.currMode = "C"
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 3 and app.rolls[1] == 3)):
            if("six" in app.bets):
                app.bal += app.bets["six"] * (13/6)
            if("3 3" in app.bets):
                app.bal += app.bets["3 3"] * 10
            if(app.currMode == "C"):
                app.point = 6
                if("pass" in app.bets):
                    app.point = 6
                if("no pass" in app.bets):
                    app.point = 6
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if(app.point == 6):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 1 and app.rolls[1] == 6) or (app.rolls[1] == 1 and app.rolls[0] == 6) or (app.rolls[1] == 2 and app.rolls[0] == 5) or (app.rolls[1] == 5 and app.rolls[0] == 2) or (app.rolls[1] == 3 and app.rolls[0] == 4) or (app.rolls[1] == 4 and app.rolls[0] == 3)):
            if("seven" in app.bets):
                app.bal += app.bets["seven"] * 5
            if(app.currMode == "C"):
                if("pass" in app.bets):
                    app.bal += app.bets["pass"] * 2
                if("no pass" in app.bets):
                    app.dbal += app.bets["no pass"]
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i != "2 2"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if("no pass" in app.bets):
                    app.bal += app.bets["no pass"] * 2
                if("pass" in app.bets):
                    app.dbal += app.bets["pass"]
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 2 and app.rolls[1] == 6) or (app.rolls[1] == 2 and app.rolls[0] == 6) or (app.rolls[1] == 3 and app.rolls[0] == 5) or (app.rolls[1] == 5 and app.rolls[0] == 3)):
            if("8" in app.bets):
                app.bal += app.bets["8"] * (13/6)
            if(app.currMode == "C"):
                app.point = 8
                if("pass" in app.bets):
                    app.point = 8
                if("no pass" in app.bets):
                    app.point = 8
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i!= "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if(app.point == 8):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 4 and app.rolls[1] == 4)):
            if("8" in app.bets):
                app.bal += app.bets["8"] * (13/6)
            if("4 4" in app.bets):
                app.bal += app.bets["4 4"] * 10
            if(app.currMode == "C"):
                app.point = 8
                if("pass" in app.bets):
                    app.point = 8
                if("no pass" in app.bets):
                    app.point = 8
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 0
                for i in app.bets:
                    if(i != "5 5" and i != "3 3" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if(app.point == 8):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "3 3" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "3 3" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 3 and app.rolls[1] == 6) or (app.rolls[1] == 3 and app.rolls[0] == 6) or (app.rolls[1] == 4 and app.rolls[0] == 5) or (app.rolls[1] == 5 and app.rolls[0] == 4)):
            if("nine" in app.bets):
                app.bal += app.bets["nine"] * (12/5)
            if(app.currMode == "C"):
                app.point = 9
                if("pass" in app.bets):
                    app.point = 9
                if("no pass" in app.bets):
                    app.point = 9
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i!= "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if(app.point == 9):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "3 3" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 4 and app.rolls[1] == 6) or (app.rolls[1] == 4 and app.rolls[0] == 6)):
            if("10" in app.bets):
                app.bal += app.bets["10"] * (14/5)
            if(app.currMode == "C"):
                app.point = 10
                if("pass" in app.bets):
                    app.point = 10
                if("no pass" in app.bets):
                    app.point = 10
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i!= "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if(app.point == 10):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "5 5" and i != "4 4" and i != "3 3" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 5 and app.rolls[1] == 5)):
            if("10" in app.bets):
                app.bal += app.bets["10"] * (13/6)
            if("5 5" in app.bets):
                app.bal += app.bets["5 5"] * 10
            if(app.currMode == "C"):
                app.point = 10
                if("pass" in app.bets):
                    app.point = 10
                if("no pass" in app.bets):
                    app.point = 10
                if("field" in app.bets):
                    app.dbal += app.bets["field"]
                    app.bets["field"] = 10
                for i in app.bets:
                    if(i != "4 4" and i != "3 3" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if(app.point == 10):
                    if("pass" in app.bets):
                        app.bal += app.bets["pass"] * 2
                    if("no pass" in app.bets):
                        app.dbal += app.bets["no pass"]
                    for i in app.bets:
                        if(i != "4 4" and i != "3 3" and i != "2 2"):
                            app.dbal += app.bets[i]
                            app.bets[i] = 0
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "4 4" and i != "3 3" and i != "2 2" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif((app.rolls[0] == 5 and app.rolls[1] == 6) or (app.rolls[1] == 5 and app.rolls[0] == 6)):
            if("5 6" in app.bets):
                app.bal += app.bets["5 6"] * 16
            if(app.currMode == "C"):
                if("pass" in app.bets):
                    app.bal += app.bets["pass"] * 2
                if("no pass" in app.bets):
                    app.dbal += app.bets["no pass"]
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "3 3" and i!= "2 2"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
            if(app.currMode == "P"):
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 2
                for i in app.bets:
                    if(i != "5 5" and i != "4 4" and i != "2 2" and i != "3 3" and i != "pass" and i != "no pass"):
                        app.dbal += app.bets[i]
                        app.bets[i] = 0
        elif(app.rolls[0] == 6 and app.rolls[1] == 6):
            if("6 6" in app.bets):
                app.bal += app.bets["6 6"]
            if(app.currMode == "C"):
                if("pass" in app.bets):
                    app.dbal += app.bets["pass"]
                if("no pass" in app.bets):
                    app.bal += app.bets["no pass"] * 2
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 4
                if("any craps" in app.bets):
                    app.bal += app.bets["any craps"] * 7
            if(app.currMode == "P"):
                if("field" in app.bets):
                    app.bal += app.bets["field"] * 4
                if("any craps" in app.bets):
                    app.bal += app.bets["any craps"] * 7
            for i in app.bets:
                if(i != "2 2" and i != "5 5" and i != "4 4" and i != "3 3"):
                    app.dbal += app.bets[i]
                    app.bets[i] = 0
        
                
    elif(x > 539 and x < 575 and y > 666 and y < 735):
        if(app.currBet > 10):
            app.currBet -= 10
    elif(x > 672 and x < 708 and y > 666 and y < 735):
        app.currBet += 10
        
    


runApp()

#'svg-cards/ace_of_spades.svg'