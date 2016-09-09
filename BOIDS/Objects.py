from agents import *

WIDTH = 800
HEIGHT = 600

def isValid(pos):
    return (pos[0] >= 0 and pos[0] < WIDTH and pos[1] >= 0 and pos[1] < HEIGHT)

def isLimit(pos, error):
    return (pos[0] - error <= 0) or (pos[0] + error >= WIDTH) or (pos[1] - error <= 0) or (pos[1] + error >= HEIGHT)

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
        self.pos = [random.randrange(WIDTH/4,WIDTH - WIDTH/4),random.randrange(HEIGHT/4,HEIGHT - HEIGHT/4)] #x,y
        self.circle = Circle(self.pos[0],self.pos[1],canvas)

    def setPos(self, pos):
        if (isValid(pos)):
            if (isLimit(pos, self.getRadius()*2)):
                self.changeDir()
            else:
                self.pos = pos

    def getPos(self):
        return self.pos

    def getVel(self):
        return self.vel

    def setVel(self, v):
        self.vel = v

    def getRadius(self):
        return self.circle.getRadius()

    def changeDir(self):
        print ("change dir")
        pos = self.getPos()
        print ("pos : ", pos)
        r = self.getRadius()
        error = r*r*r
        if (pos[0] - error <= 0): # se acerca al limite izquierdo
            print ("limite izq")
            self.setPos([pos[0]+r*r*r,pos[1]])
        if (pos[0] + error >= WIDTH): # se acerca al limite derecho
            print ("limite der")
            self.setPos([pos[0]-r*r*r,pos[1]])
        if (pos[1] - error <= 0): # se acerca al limite superior
            print ("limite sup")
            self.setPos([pos[0],pos[1]+r*r*r])
        if (pos[1] + error >= HEIGHT): # se acerca al limite inferior
            print ("limite inf")
            self.setPos([pos[0],pos[1]-r*r*r])
