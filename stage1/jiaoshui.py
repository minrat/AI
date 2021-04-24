import turtle

# 图片范围确定
turtle.penup()
turtle.pensize(0.5)
turtle.goto(-400, 300)
turtle.pendown()
turtle.fd(800)
turtle.right(90)
turtle.fd(600)
turtle.right(90)
turtle.fd(800)
turtle.right(90)
turtle.fd(600)
turtle.penup()

# 接水口
turtle.pensize(2.5)
turtle.goto(-5, -300)
turtle.fillcolor("black")
turtle.pendown()
turtle.begin_fill()
turtle.fd(20)
turtle.right(90)
turtle.fd(20)
turtle.right(90)
turtle.fd(20)
turtle.right(90)
turtle.fd(20)
turtle.right(90)
turtle.end_fill()
turtle.penup()

# 水管
turtle.pensize(3)
turtle.goto(0, -280)
turtle.pendown()
turtle.circle(100, 90)

turtle.penup()

# 喷头
turtle.pensize(3)
turtle.goto(0, 250)
turtle.pendown()
turtle.circle(30, 360)

turtle.penup()

# 花草
turtle.pensize(0.5)
turtle.goto(-400, 300)
turtle.pendown()
turtle.left(90)
turtle.circle(400, 180)
# # 边缘
turtle.penup()
turtle.goto(-400, 300)
turtle.pendown()
turtle.right(150)
turtle.circle(460, 120)
# #花盆
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.left(160)
turtle.circle(60, 360)

turtle.done()
