import turtle

turtle.pensize(1)
turtle.pencolor("black")

turtle.colormode(255)
# turtle.fillcolor(100, 100, 100)
turtle.penup()
count = 0
location = 120
color = 0

# # 填色设定
# turtle.fillcolor("red")
# # 填色开始
# turtle.begin_fill()
# turtle.goto(0, -100)
# turtle.pendown()
# turtle.circle(100, 360)
# # 填色结束
# turtle.end_fill()
# turtle.penup()
#
# # 填色设定
# turtle.fillcolor("orange")
# # 填色开始
# turtle.begin_fill()
# turtle.goto(0, -80)
# turtle.pendown()
# turtle.circle(80, 360)
# # 填色结束
# turtle.end_fill()
# turtle.penup()
#
# # 填色设定
# turtle.fillcolor("grey")
# # 填色开始
# turtle.begin_fill()
# turtle.goto(0, -60)
# turtle.pendown()
# turtle.circle(60, 360)
# # 填色结束
# turtle.end_fill()
# turtle.penup()
# 颜色顺序数值如下：
# (232,52,151)
# (186,35,141)
# (110,220,189)
# (142,57,197)
# (247,112,86)

while count < 5:
    turtle.fillcolor(255-color, 255-color, 255-color)
    # 填色开始
    turtle.begin_fill()
    turtle.goto(0, 20 - location)
    turtle.pendown()
    turtle.circle(location - 20, 360)
    # 填色结束
    turtle.end_fill()
    turtle.penup()
    location -= 20
    color += 20
    if count == 4:
        turtle.pendown()
        turtle.right(90)
        turtle.forward(200)
    count += 1



turtle.done()
