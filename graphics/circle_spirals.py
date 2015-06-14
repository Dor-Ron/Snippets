#!/usr.bin.env python

from time import sleep
from turtle import Pen, circle, right, pencolor, width

canvas = Pen()
colors = ["brown", "gray", "purple", "red"]
for num in xrange(450):
        canvas.width(0.8)
        canvas.pencolor(colors[num % 4])
        canvas.circle(num)
        canvas.right(91)

sleep(500)

