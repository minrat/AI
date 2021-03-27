import turtle

turtle.pensize(2)
turtle.pencolor("black")
turtle.penup()
# 填色设定
turtle.fillcolor("red")
## 填色开始
turtle.begin_fill()
# # 1
# turtle.goto(0, 100)
# turtle.pendown()
# turtle.circle(50, 360)
# turtle.penup()
# # 2
# turtle.goto(0, 0)
# turtle.pendown()
# turtle.circle(50, 360)
# turtle.penup()
#
# # 3
# turtle.goto(0, -100)
# turtle.pendown()
# turtle.circle(50, 360)
# turtle.penup()
#
# # 4
# turtle.goto(0, -200)
# turtle.pendown()
# turtle.circle(50, 360)
# turtle.penup()
count = 0
location = 100
while count < 5:
    turtle.goto(0, location)
    turtle.pendown()
    turtle.circle(50, 360)
    turtle.penup()
    # 条件增长
    count += 1
    location -= 100
## 填色结束
turtle.end_fill()

# 竹签
turtle.goto(0, -350)
turtle.pensize(10)
turtle.pendown()
turtle.left(90)
turtle.forward(600)

turtle.mainloop()
