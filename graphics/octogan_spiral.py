#!/usr/bin/env python

from time import sleep
from turtle import *

canvas = Pen()
bgcolor("black")
sides = 8
colors = ["red", "green", "brown", "blue", "pink", "purple"]
for num in xrange(540):
        pencolor(colors[num % 6])
        forward(num * 3 / sides + 3)
        left(360 / sides + 1)
        width(num * sides / 300)

sleep(500)

