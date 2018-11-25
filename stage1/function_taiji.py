#!/bin/bash/env python
# -*- coding: utf-8
import turtle
t = turtle.Pen()

def taiji_half(radius, color1, color2):
    t.width(3)
    t.color("black", color1)
    t.begin_fill()
    t.circle(radius/2, 180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius/2, 180)
    t.end_fill()
    t.left(90)
    t.up()
    t.fd(radius * 0.35)
    t.right(90)
    t.down()
    t.color(color1, color2)
    t.begin_fill()
    t.circle(radius * 0.15)
    t.end_fill()
    t.left(90)
    t.up()
    t.bk(radius * 0.35)
    t.down()
    t.left(90)

def taiji_full():
    t.reset()
    taiji_half(200, 'black', 'white')
    taiji_half(200, 'white', 'black')

if __name__ == '__main__':
    taiji_full()
    turtle.mainloop()
