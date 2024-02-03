from cmu_graphics import *
import random
from PIL import Image as img

def onAppStart(app):
    app.width = 800
    app.height = 800
    app.background = rgb(29, 94, 67)
    app.grid = createGrid(app)
    app.prob = 5
    app.gameOver = False
    app.clicked = 0

    # images
    explosion = img.open('mines_assets/explosion.png')
    diamond = img.open('mines_assets/gems.png')
    app.diamondList = []
    app.explosionList = []
    dy = dx = 30
    for j in range(6):
        for k in range(7):
            d = diamond.crop((k*dx, j*dy,(k+1)*dx, (j+1)*dy))
            app.diamondList.append(CMUImage(d.resize((75,75))))

    dy = dx = 100

    for j in range(5):
        for k in range(5):
            e = explosion.crop((k*dx, j*dy,(k+1)*dx, (j+1)*dy))
            app.explosionList.append(CMUImage(e.resize((200,200))))
    app.gemImgIndex = 0
    app.explosionImageIndex = 0


def redrawAll(app):
    drawLabel("Mines", app.width//2, app.height//10, align = 'center', font = 'monospace', size = 50, fill = 'white',  bold = True)
    drawGrid(app, app.grid)

def onStep(app):
    app.gemImgIndex += 1
    if app.gameOver: 
        app.explosionImageIndex += 1
    if app.clicked == 20:
        app.gameOver = True

def createGrid(app, x = 5 , y = 5):
    grid = []
    for i in range(x):
        temp = []
        for j in range(y):
            temp.append(Grid(app, i, j))
        grid.append(temp)
    return grid

def onMousePress(app, x, y):
    if not app.gameOver:
        if x > 150 and x < 650 and y > 150 and y < 650:
            currx = (x - 150)//100
            curry = (y - 225)//100
            for i in app.grid:
                for g in i:
                    if g.x == currx and g.y == curry:
                        if not g.clicked:
                            g.click()
                        else:
                            break
            pass

def drawGrid(app, grid):
    for row in grid:
        for currGrid in row:
            x = 150 + currGrid.x*currGrid.width
            y = 225 + currGrid.y*currGrid.height
            width = currGrid.width
            height = currGrid.height
            drawRect(x, y, width, height, fill = currGrid.color, border = currGrid.border)
    for row in grid:
        for currGrid in row:
            x = 150 + currGrid.x*currGrid.width
            y = 225 + currGrid.y*currGrid.height
            if currGrid.clicked and ((not app.gameOver) or app.clicked == 20):
                drawImage(app.diamondList[(app.gemImgIndex//4)%39], x+12.5, y+12.5)
            elif currGrid.clicked and app.gameOver and not currGrid.mine:
                if app.explosionImageIndex//2 < 25:
                    drawImage(app.explosionList[(app.explosionImageIndex//2)], x-50, y-50)

            

class Grid:
    def __init__(self,app, x, y, width = 100, height = 100, color = "darkslategrey", border = "black"):
        self.app = app
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border = border
        self.clicked = False
        self.clicked = False

    def click(self):
        currval = random.randrange(0,100,1)
        if currval < self.app.prob:
            self.clicked = True
            self.mine = True
            self.color = 'red'
            self.app.gameOver = True
        else:
            self.app.prob += 2
            self.app.clicked += 1
            self.clicked = True
            self.mine = False
            self.color = 'lightSlateGrey'


if __name__ == "__main__":
    runApp()
