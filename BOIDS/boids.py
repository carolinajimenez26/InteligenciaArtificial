import time
from Tkinter import *
from Objects import *

WIDTH = 800
HEIGHT = 600

def draw_boids(canvas, animation, all_boids):
    for i in range(0,len(all_boids)):
        pos = all_boids[i].getPos()
        canvas.move(i,pos[0],pos[1])
        animation.update()
        time.sleep(0.05)

def move_all_boids_to_new_positions(all_boids):
    for b in all_boids:
        b.updatePosition()

def main():
    animation = Tk()
    canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
    canvas.pack()
    all_boids = []

    b = BOID([5,5],canvas)
    all_boids.insert(0,b)

    for i in range(0,100):
        b = BOID([5,5],canvas)
        all_boids.insert(i,b)

    while True:
        draw_boids(canvas, animation, all_boids)
        move_all_boids_to_new_positions(all_boids)


if __name__ == "__main__":
    main()
