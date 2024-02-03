from cmu_graphics import *
from PIL import Image as img
from mines import minesOAS, minesOS, minesOMP, minesRDA, minesOKP
from slots import slotsOAS, slotsOMD, slotsOMM, slotsOMP, slotsOMR, slotsOS, slotsRDA, slotsOKP
from roulette import rouletteOAS, rouletteOMP, rouletteOS, rouletteRDA, rouletteOKP
from craps import crapsOAS, crapsRDA, crapsOMP, crapsOKP
from blackjack import blackjackOAS, blackjackRA, blackjackOMM, blackjackOMP
from xrp import Server
from plinko import Plinko
import xrpl.account as account



def onAppStart(app):
    app.games = Games(app)
    app.width = 800
    app.height = 800
    app.background = "black"
    app.running = False
    app.loading = False
    app.reset = reset

    app.server = Server()
    app.clientWallet = app.server.create_wallet()
    app.clientAddress = app.clientWallet.address
    app.server.pay_server(app.clientWallet, 9000)  # start with 1000 tokens
    app.balance = account.get_balance(app.clientAddress, app.server.client) // 1000000

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


def reset(app):
    app.games = Games(app)
    app.width = 800
    app.height = 800
    app.background = "black"
    app.running = False
    
    wallet_balance = account.get_balance(app.clientAddress, app.server.client)
    wallet_balance /= 1000000
    if wallet_balance < app.balance:
        app.server.pay_client(app.clientWallet, (app.balance - wallet_balance))
    elif wallet_balance > app.balance:
        app.server.pay_server(app.clientWallet, (wallet_balance - app.balance))

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
    app.loading = False



def redrawAll(app):
    if app.loading:
        drawLabel("Making transactions...", app.width / 2, app.height / 2, size=30, bold=True, fill='lightSlateGray')
    elif not app.running:
        drawLabel(f"Balance: {app.balance} XRP", app.width / 2, 50, size=20, bold=True, fill='white')

        drawLabel(f"client wallet address: {app.clientAddress}", app.width // 4, app.height - 15, fill='white')
        drawLabel(f"server wallet address: {app.clientAddress}", 3*app.width // 4, app.height - 15, fill='white')

        #for i in range(4):
        #    for j in range(10):
        #        drawImage(app.moneyGIF[app.moneyIDX%30], 4+i*199, 10+j*200*app.moneyAspect, width = 200, height = 200*app.moneyAspect)
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
    if app.running:
        app.games.OKP(app, key)

def onMouseMove(app, x, y):
    if not app.running:
        for game in app.games.games:
            if x > game.scx - 75 and x < game.scx + 75 and y < game.scy + 75 and y>game.scy - 75:
                game.size = 175
            else:
                game.size = 150
    else:
        app.games.OMM(app, x, y)

def onMouseDrag(app, x, y):
    if app.running:
        app.games.OMD(app, x, y)

def onMouseRelease(app, x, y):
    if app.running:
        app.games.OMR(app, x, y)

class Games:
    def __init__(self, app):
        self.games = [Game('Plinko', app, logo = CMUImage(img.open('logo_assets/plinko-logo.jpg'))),
                      Game('Mines', app, logo = CMUImage(img.open('logo_assets/mines-logo.webp'))),
                      Game('Slots', app, logo = CMUImage(img.open('logo_assets/slots-logo.jpg'))),
                      Game('BlackJack', app, logo = CMUImage(img.open('logo_assets/blackjack-logo.jpg'))),
                      Game('Roulette', app, logo = CMUImage(img.open('logo_assets/roulette-logo.jpg'))),
                      Game('Craps', app, logo = CMUImage(img.open('logo_assets/craps-logo.jpg')))]

    def RDA(self, app):
        pass

    def OS(self, app):
        pass

    def OMM(self, app, x, y):
        pass

    def OMP(self, app, x, y):
        pass

    def OMD(self, app, x, y):
        pass

    def OMR(self, app, x, y):
        pass

    def OKP(self, app, key):
        pass


class Game:
    def __init__(self, name, app, logo = None):
        self.app = app
        self.gameApp = None
        self.name = name
        self.logo = logo
        self.x = 0
        self.y = 0
        self.scx = 0
        self.scy = 0
        self.size = 150


    def OAS(self, app):
        if self.name == 'Plinko':
            plinko = Plinko(self.app)
            app.games.RDA = plinko.redrawAll
            app.games.OS = plinko.onStep
            app.games.OMP = plinko.onMousePress
            app.games.OKP = plinko.onKeyPress

        if self.name == 'Mines':
            minesOAS(app)
            app.games.RDA = minesRDA
            app.games.OS = minesOS
            app.games.OMP = minesOMP
            app.games.OKP = minesOKP

        if self.name == 'Slots':
            slotsOAS(app)
            app.games.RDA = slotsRDA
            app.games.OS = slotsOS
            app.games.OMP = slotsOMP
            app.games.OMM = slotsOMM
            app.games.OMD = slotsOMD
            app.games.OMR = slotsOMR
            app.games.OKP = slotsOKP
            
        if self.name == 'BlackJack':
            blackjackOAS(app)
            app.games.RDA = blackjackRA
            app.games.OMM = blackjackOMM
            app.games.OMP = blackjackOMP

        if self.name == 'Roulette':
            rouletteOAS(app)
            app.games.RDA = rouletteRDA
            app.games.OMP = rouletteOMP
            app.games.OS = rouletteOS
            app.games.OKP = rouletteOKP

        if self.name == 'Craps':
            crapsOAS(app)
            app.games.RDA = crapsRDA
            app.games.OMP = crapsOMP
            app.games.OKP = crapsOKP



if __name__ == "__main__":
    runApp()
