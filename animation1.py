import time
from Tkinter import *

colors = ["red","green","blue","yellow"]

animation = Tk()
canvas = Canvas(animation, width = 800, height = 600)
canvas.pack()

circles = []

for i in range(0,10):
	circle = canvas.create_oval(10+i*i,10+i*i,50+i*i,50+i*i, fill = colors[i % 4])
	circles.append(circle)

for x in range(0,140):
		canvas.move(ALL,5,0)
		animation.update()
		time.sleep(0.03)

for x in range (0,140):
		canvas.move(ALL,-5,0)
		animation.update()
		time.sleep(0.03)
