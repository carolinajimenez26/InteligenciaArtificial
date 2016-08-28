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

    ans = [cx/(len(all)-1),cy/(len(all)-1)]

    # Se mueve un 1%
    return [(ans[0] - pos[0])/100,(ans[1] - pos[1])/100]

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

    vx = vx / (len(all) - 1)
    vy = vy / (len(all) - 1)

    return [(vx - vel[0])/8,(vy - vel[1])/8]

def draw_boids(canvas, animation, all_boids):
    for i in range(0,len(all_boids)):
        pos = all_boids[i].getPos()
        canvas.move(i,pos[0],pos[1])
        animation.update()
        time.sleep(0.01)

def move_all_boids_to_new_positions(all_boids):
    for b in all_boids:
        v1 = rule1(b,all_boids)
        v2 = rule2(b,all_boids)
        v3 = rule3(b,all_boids)

        vx = b.getVel()[0] + v1[0] + v2[0] + v3[0]
        vy = b.getVel()[1] + v1[1] + v2[1] + v3[1]

        px = b.getPos()[0] + vx
        py = b.getPos()[1] + vy

        b.setVel([vx,vy])
        b.setPos([px,py])

def main():
    animation = Tk()
    canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
    canvas.pack()
    all_boids = []

    for i in range(0,500):
        b = BOID([1,1],canvas)
        all_boids.insert(i,b)

    while True:
        draw_boids(canvas, animation, all_boids)
        move_all_boids_to_new_positions(all_boids)


if __name__ == "__main__":
    main()
