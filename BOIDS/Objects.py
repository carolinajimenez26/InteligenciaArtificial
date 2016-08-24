from agents import *

class Circle():
    colors = ["red","green","blue","yellow"]
    i = 0

    def __init__(self, x, y, r,canvas):
        self.x = x
        self.y = y
        self.r = r
        circle = canvas.create_oval(x,y,x+2*r,y+2*r, fill = "red")
        self.i += 1
        if (self.i >= 4):
            self.i = 0

    def getPos(self):
        return [self.x, self.y]

class BOID(Thing):
    def __init__(self, pos, vel, r, canvas):
        self.vel = vel #x,y
        self.circle = Circle(pos[0],pos[1],r,canvas)

    def move(self, pos):
        self.pos = pos

    def getPos(self):
        return self.circle.getPos()

    def getVel(self):
        return self.vel
