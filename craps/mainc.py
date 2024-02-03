from cmu_graphics import *
import random
from PIL import Image as img

#slotmachine
#800x800
def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = rgb(29, 94, 67)
    app.isStart = True


def redrawAll(app):
    if (app.isStart):
        drawLabel("Blackjack", 400, 80, size=100, font='arial', bold=False, fill='white')
        


runApp()

#'svg-cards/ace_of_spades.svg'