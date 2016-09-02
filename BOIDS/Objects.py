from agents import *

WIDTH = 800
HEIGHT = 600

def isValid(pos):
    return (pos[0] >= 0 and pos[0] < WIDTH and pos[1] >= 0 and pos[1] < HEIGHT)

class Circle():
    colors = ["red","green","blue","yellow"]

    def __init__(self, x, y,canvas):
        self.x = x
        self.y = y
        self.r = 3
        circle = canvas.create_oval(x,y,x+2*self.r,y+2*self.r, fill = self.colors[random.randrange(0,4)])

    def getRadius(self):
        return self.r

class BOID(Agent):
    def __init__(self, vel, canvas):
        self.vel = vel #x,y
        self.pos = [random.randrange(0,WIDTH),random.randrange(0,HEIGHT)] #x,y
        self.circle = Circle(self.pos[0],self.pos[1],canvas)

    def setPos(self, pos):
        if (isValid(pos)):
            self.pos = pos

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def setVel(self, v):
        self.vel = v

    def getRadius(self):
        return self.circle.getRadius()
