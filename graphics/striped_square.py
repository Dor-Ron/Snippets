#!/usr/bin/env python

from time import sleep
from turtle import Pen, forward, right, width, pencolor


colors = ["green", "pink","blue", "orange"]
canvas = Pen()

for num in xrange(435):
        canvas.pencolor(colors[num % 4])
        canvas.width(0.7)
        canvas.forward(num)
        canvas.right(90)

sleep(500)

