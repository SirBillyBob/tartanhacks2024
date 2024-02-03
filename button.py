from cmu_graphics import *

class Button:
    def __init__(self,text, x, y, width, height, textSize, color = "white", border = None, textColor = "black",):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.border = border
        self.textColor = textColor
        self.textSize = textSize
    
    def drawButton(self):
        drawRect(self.x,self.y,self.width,self.height,align = "center", fill = self.color, border = self.border)
        drawLabel(self.text,self.x,self.y,size = self.textSize, fill = self.textColor, align = "center")
    
    def buttonPressed(self, x, y, f, args):
        if x > self.x - self.width//2 and x <self.x + self.width//2 and y > self.y - self.height//2 and y < self.y + self.height//2:
            f(*args)