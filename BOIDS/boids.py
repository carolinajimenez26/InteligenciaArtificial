import time
from Tkinter import *
from Objects import *

WIDTH = 800
HEIGHT = 600

def draw_boids(canvas, animation):
    canvas.move(ALL,5,0)
    animation.update()
    time.sleep(0.03)

def main():
    animation = Tk()
    canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
    canvas.pack()

    for i in range(0,100):
        b = BOID([5,5],canvas)

    """
    for i in range(0,140):
        canvas.move(ALL,5,0)
        animation.update()
        time.sleep(0.03)"""

    while True:
        draw_boids(canvas, animation)
        #move_all_boids_to_new_positions()


if __name__ == "__main__":
    main()
