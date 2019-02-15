# -*- coding: UTF-8 -*-
"""Fidget, inspired by fidget spinners.

Exercises

1. Change the spinner pattern.
2. Respond to mouse clicks.
3. Change its acceleration.
4. Make it go forwards and backwards.

"""

from turtle import *

state = {'turn': 0}

def spinner():
    # 构建基础背景
    clear()
    angle = state['turn'] / 10
    right(angle)
    forward(100)
    dot(120, 'red')
    # dot(60, 'red')
    back(100)
    right(120)
    # right(60)

    forward(100)
    dot(120, 'green')
    # dot(60, 'green')
    back(100)
    right(120)
    # right(60)

    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    # right(60)

    # forward(100)
    # dot(120, 'orange')
    # back(100)
    # right(120)
    update()

def animate():
    # Animate fidget spinner.
    if state['turn'] > 0:
        state['turn'] -= 1

    spinner()
    ontimer(animate, 20)

def flick():
    # Flick fidget spinner.
    state['turn'] += 20
    print("快速点击，加速！！！！")

def getpos(x, y):
    print("(", x, ",", y, ")")
    print("鼠标点击了....")
    return

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
width(20)
onkey(flick, 'space')
onscreenclick(getpos)
listen()
animate()
done()
