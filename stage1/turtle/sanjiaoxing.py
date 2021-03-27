import turtle

turtle.pensize(1)
turtle.pencolor("black")

turtle.colormode(255)
turtle.penup()
count = 0
location = 120
color = 0
deviation = 5
turtle.goto(0, 0)

# # 三角形
# while count < 12:
#     turtle.fillcolor(255-color, 255-color, 255-color)
#     turtle.begin_fill()
#     turtle.pendown()
#     if count == 0:
#         deviation = 5
#     else:
#         deviation = 120
#     turtle.left(deviation+5)
#     turtle.forward(200)
#     turtle.left(120)
#     turtle.forward(200)
#     turtle.left(120)
#     turtle.forward(200)
#     turtle.end_fill()
#     count += 1
#     turtle.penup()

# 花型
while count < 12:
    turtle.fillcolor(255-color, 255-color, 255-color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.left(5)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.end_fill()
    count += 1
    color += 21
    turtle.penup()


# turtle.left(125)
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)
# turtle.left(120)
# turtle.forward(200)

turtle.done()
