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

def Bresenham(x0,y0,x1,y1, b, canvas, animation):
    moves = []
    cont = 0
    print ("b : " , b)
    dx = (x1 - x0)
    print ("dx : ", dx)
    dy = (y1 - y0)
    print ("dy : ", dy)
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

    print ("x : ", x)
    print ("y : ", y)
    print ("gonna move!!")
    """canvas.move(b,x,y)
    animation.update()
    time.sleep(0.1)"""

    if(dx > dy) :
        print ("if")
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
            print ("new_x : ", x)
            print ("new_y : ", y)
            print ("gonna move!!")
            moves.insert(cont,[x,y])
            """canvas.move(b,x,y)
            animation.update()
            time.sleep(0.1)"""

    else :
        print ("else")
        p = 2*dx - dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        while (y != y1) :
            print ("y : ", y)
            print ("y1 : ", y1)
            y = y + stepy
            if (p < 0) :
                p = p + incE
            else :
                x = x + stepx
                p = p + incNE
            moves.insert(cont,[x,y])
            print ("new_x : ", x)
            print ("new_y : ", y)
            print ("gonna move!!")
            """canvas.move(b,x,y)
            animation.update()
            time.sleep(0.1)"""
    return moves

def draw_boids(canvas, animation, all_boids, prev_pos):
    for i in range(0, len(all_boids)): # movemos todos los Boids
        b = all_boids[i]
        prev = prev_pos[i] # desde donde
        #print ("prev_pos : ", prev_pos[i])
        pos = b.getPos() # hasta donde
        #print ("curr_pos : " , pos)
        Bresenham(int(prev[0]), int(prev[1]), int(pos[0]), int(pos[1]), i, canvas, animation)
    del prev_pos

def move_all_boids_to_new_positions(all_boids):
    prev_pos = []
    for i in range(0,len(all_boids)) :
        #print ("i : ", i)
        b = all_boids[i]
        #print ("b : ", b)
        v1 = rule1(b,all_boids)
        #print ("v1 : ", v1)
        v2 = rule2(b,all_boids)
        #print ("v2 : ", v2)
        v3 = rule3(b,all_boids)
        #print ("v3 : ", v3)

        vx = b.getVel()[0] + v1[0] + v2[0] + v3[0]
        #print ("vx : ", vx)
        vy = b.getVel()[1] + v1[1] + v2[1] + v3[1]
        #print ("vy : ", vy)

        px = b.getPos()[0] + vx
        #print ("px : ", px)
        py = b.getPos()[1] + vy
        #print ("py : ", py)

        b.setVel([vx,vy])
        prev_pos.insert(i, b.getPos())
        #print ("prev_pos : ", prev_pos)
        #print ("Anterior : ", b.getPos())
        b.setPos([px,py])
        #print("Nueva : ", b.getPos())
    return prev_pos

def main():
    animation = Tk()
    canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
    canvas.pack()
    all_boids = []
    b = BOID([5,5],canvas)
    b2 = BOID([5,5],canvas)
    """for i in range(0,150):
        b = BOID([1,1],canvas)
        all_boids.insert(i,b)

    while True:
        prev_pos = move_all_boids_to_new_positions(all_boids)
        #print ("prev_pos in while " , prev_pos)
        draw_boids(canvas, animation, all_boids, prev_pos)"""

    """for x in range(0,140):
        print("Hola Caro :) ")
        canvas.move(1,5,5)
        canvas.move(2,5,5)
        animation.update()
        time.sleep(0.5)
"""
    moves1 = Bresenham(b.getPos()[0],b.getPos()[1],500,500,1,canvas, animation)
    moves2 = Bresenham(b2.getPos()[0],b2.getPos()[1],500,500,2,canvas, animation)

    for i in range(1,len(moves1)):
        inc_x = moves1[i][0] - moves1[i-1][0]
        inc_y = moves1[i][1] - moves1[i-1][1]
        canvas.move(1,inc_x,inc_y)
        animation.update()
        time.sleep(0.1)

    for i in range(1,len(moves1)):
        inc_x = moves2[i][0] - moves2[i-1][0]
        inc_y = moves2[i][1] - moves2[i-1][1]
        canvas.move(2,inc_x,inc_y)
        animation.update()
        time.sleep(0.1)

if __name__ == "__main__":
    main()
