import time
from Tkinter import *
from Objects import *

WIDTH = 800
HEIGHT = 600

# Boids se mueven segun el centro de masa de los demas
def rule1(b, all):
    cx = 0
    cy = 0
    for bi in all:
        posi = bi.getPos()
        cx += posi[0]
        cy += posi[1]

    # No se incluye a si mismo
    pos = b.getPos()
    cx -= pos[0]
    cy -= pos[1]

    ans = [float(cx/(len(all)-1)),float(cy/(len(all)-1))]

    # Se mueve un 1%
    return [float((ans[0] - pos[0])/100),float((ans[1] - pos[1])/100)]

# Boids tratan de tener una distancia con los demas
def rule2(b, all):
    pos = b.getPos()
    cx = 0
    cy = 0
    for bi in all:
        if bi != b:
            posi = bi.getPos()
            if (abs(posi[0] - pos[0]) < 100 and abs(posi[1] - pos[1]) < 100):
                cx -= posi[0] - pos[0]
                cy -= posi[1] - pos[1]

    return [cx,cy]

# Boids tratan de ir a una velocidad similar a los otros
def rule3(b, all):
    vel = b.getVel()
    vx = 0
    vy = 0
    for bi in all:
        if bi != b:
            veli = bi.getVel()
            vx += veli[0]
            vy += veli[1]

    vx = float(vx / (len(all) - 1))
    vy = float(vy / (len(all) - 1))

    return [float((vx - vel[0])/8),float((vy - vel[1])/8)]

def Bresenham(x0, y0, x1, y1, b, canvas, animation):
    moves = []
    dx = (x1 - x0)
    dy = (y1 - y0)
    #determinar que punto usar para empezar, cual para terminar
    if (dy < 0) :
        dy = -1*dy
        stepy = -1
    else :
        stepy = 1
    if (dx < 0) :
        dx = -1*dx
        stepx = -1
    else :
        stepx = 1
    x = x0
    y = y0
    moves.insert(cont,[x,y])

    if(dx > dy) :
        p = 2*dy - dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        while (x != x1) :
            x = x + stepx
            if (p < 0) :
                p = p + incE
            else :
                y = y + stepy
                p = p + incNE
            moves.insert(cont,[x,y])

    else :
        p = 2*dx - dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        while (y != y1) :
            y = y + stepy
            if (p < 0) :
                p = p + incE
            else :
                x = x + stepx
                p = p + incNE
            moves.insert(cont,[x,y])

    return moves

def draw_boids(canvas, animation, all_boids, prev_pos):
    for i in range(0, len(all_boids)): # movemos todos los Boids
        b = all_boids[i]
        prev = prev_pos[i] # desde donde
        pos = b.getPos() # hasta donde
        moves = Bresenham(int(prev[0]), int(prev[1]), int(pos[0]), int(pos[1]), i, canvas, animation)
        for j in range(1,len(moves)):
            inc_x = moves[j][0] - moves[j-1][0]
            inc_y = moves[j][1] - moves[j-1][1]
            canvas.move(i,inc_x,inc_y)
            animation.update()
            time.sleep(0.0001)
    del prev_pos

def move_all_boids_to_new_positions(all_boids):
    prev_pos = []
    for i in range(0,len(all_boids)) :
        b = all_boids[i]
        v1 = rule1(b,all_boids)
        v2 = rule2(b,all_boids)
        v3 = rule3(b,all_boids)

        vx = b.getVel()[0] + v1[0] + v2[0] + v3[0]
        vy = b.getVel()[1] + v1[1] + v2[1] + v3[1]

        px = b.getPos()[0] + vx
        py = b.getPos()[1] + vy

        b.setVel([vx,vy])
        prev_pos.insert(i, b.getPos())
        b.setPos([px,py])

    return prev_pos

def main():
    animation = Tk()
    canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
    canvas.pack()
    all_boids = []

    for i in range(0,150):
        b = BOID([1,1],canvas)
        all_boids.insert(i,b)

    while True:
        prev_pos = move_all_boids_to_new_positions(all_boids)
        draw_boids(canvas, animation, all_boids, prev_pos)

if __name__ == "__main__":
    main()
