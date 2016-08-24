from agents import *

WIDTH = 800
HEIGHT = 600

class Circle():
    colors = ["red","green","blue","yellow"]
    i = 0

    def __init__(self, x, y,canvas):
        self.x = x
        self.y = y
        r = 5
        circle = canvas.create_oval(x,y,x+2*r,y+2*r, fill = "red")
        self.i += 1
        if (self.i >= 4):
            self.i = 0

class BOID(Thing):
    def __init__(self, vel, canvas):
        self.vel = vel #x,y
        self.pos = [random.randrange(0,WIDTH),random.randrange(0,HEIGHT)] #x,y
        self.circle = Circle(self.pos[0],self.pos[1],canvas)

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def updatePosition(self):
        pos = self.getPos()
        self.setPos([ pos[0] + 5, pos[0] + 5 ] )
        #se mueve segun sus reglas
