import time
from Tkinter import *
from Objects import *

WIDTH = 800
HEIGHT = 600

def main():
    animation = Tk()
    canvas = Canvas(animation, width = WIDTH, height = HEIGHT)
    canvas.pack()

    b1 = BOID([100,100],[5,5],5,canvas)

    for x in range(0,140):
		canvas.move(ALL,5,0)
		animation.update()
		time.sleep(0.03)


if __name__ == "__main__":
    main()
