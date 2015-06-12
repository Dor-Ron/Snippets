#!/usr/bin/env python

from turtle import Pen, bgcolor, pencolor, forward, left, width
from time import sleep

bgcolor("black") #set canvas background color
colors = ["red", "green", "orange", "purple", "yellow", "blue"]
canvas = Pen()

for num in xrange(360):
	canvas.pencolor(colors[num%6])
	canvas.width(num/100+1)
	canvas.forward(num) #so line length keeps increasing
	canvas.left(59) 
	
sleep(500) #so we have some time to admire the artwork, before it closes automatically
