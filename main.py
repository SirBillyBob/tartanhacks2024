from cmu_graphics import *
from PIL import Image as img
from mines import *

def onAppStart(app):
    app.games = Games(app)
    app.width = 800
    app.height = 800
    app.background = "black"
    app.running = False

    index = 0
    for i in range(2):
        for j in range(3):
            app.games.games[index].x = j
            app.games.games[index].y = i
            app.games.games[index].scx = 200 + app.games.games[index].x*200
            app.games.games[index].scy = 400 + app.games.games[index].y*200

            index += 1
    
    app.moneyGIF = []
    for i in range(30):
        temp = f'{i}' if i > 9 else "0" + str(i)
        name = f"frame_{temp}_delay-0.1s"
        curr = CMUImage(img.open(f'logo_assets/{name}.png'))
        app.moneyGIF.append(curr)
    app.moneyIDX = 0
    app.moneyAspect = 153/376


    


def redrawAll(app):
    if not app.running:
        for i in range(4):
            for j in range(10):
                drawImage(app.moneyGIF[app.moneyIDX%30], 4+i*199, 10+j*200*app.moneyAspect, width = 200, height = 200*app.moneyAspect)
        drawRect(app.width//2, app.height//5, 500, 125, align = 'center',fill = 'white', border = 'black')
        drawLabel("Cardboard Casino", app.width//2, app.height//5, align = 'center', fill = 'black', size = 50, font = "arial")
        for game in app.games.games:
            drawImage(game.logo, game.scx, game.scy, align = "center", width = game.size, height = game.size, border = "darkslategrey")
    else:
        app.games.RDA(app)

def onStep(app):
    if app.running:
        app.games.OS(app)
    else:
        app.moneyIDX += 1

def onMousePress(app,x,y):
    if not app.running:
        for game in app.games.games:
            if game.size == 175:
                app.running = True
                game.OAS(app)
    else:
        app.games.OMP(app, x, y)


def onKeyPress(app, key):
    pass

def onMouseMove(app, x, y):
    if not app.running:
        for game in app.games.games:
            if x > game.scx - 75 and x < game.scx + 75 and y < game.scy + 75 and y>game.scy - 75:
                game.size = 175
            else:
                game.size = 150
    else:
        app.games.OMM(app, x, y)

class Games:
    def __init__(self, app):
        self.games = [Game('Plinko', app, logo = CMUImage(img.open('logo_assets/istockphoto-1222357475-612x612.jpg'))),
                      Game('Mines', app, logo = CMUImage(img.open('logo_assets/istockphoto-1222357475-612x612.jpg'))),
                      Game('Slots', app, logo = CMUImage(img.open('logo_assets/istockphoto-1222357475-612x612.jpg'))),
                      Game('BlackJack', app, logo = CMUImage(img.open('logo_assets/istockphoto-1222357475-612x612.jpg'))),
                      Game('Roulette', app, logo = CMUImage(img.open('logo_assets/istockphoto-1222357475-612x612.jpg'))),
                      Game('Craps', app, logo = CMUImage(img.open('logo_assets/istockphoto-1222357475-612x612.jpg')))]
    def RDA(self, app):
        pass

    def OS(self, app):
        pass

    def OMM(self, app, x, y):
        pass

    def OMP(self, app, x, y):
        pass


class Game:
    def __init__(self, name, app, logo = None):
        self.app = app
        self.name = name
        self.logo = logo
        self.x = 0
        self.y = 0
        self.scx = 0
        self.scy = 0
        self.size = 150
    
    
    def OAS(self, app):
        if self.name == 'Plinko':
            pass

        if self.name == 'Mines':
            minesOAS(app)
            app.games.RDA = minesRDA
            app.games.OS = minesOS
            app.games.OMP = minesOMP

        if self.name == 'Slots':
            pass
        if self.name == 'BlackJack':
            pass
        if self.name == 'Roulette':
            pass
        if self.name == 'Craps':
            pass

if __name__ == "__main__":
    runApp()
