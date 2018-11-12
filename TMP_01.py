import turtle

turtle.pencolor("black")
turtle.pensize(3)
turtle.penup()
turtle.goto(-150, 100)
turtle.pendown()

# 正方形
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)

# 圆形-左眼
turtle.pencolor("red")
turtle.penup()
turtle.goto(-90, 50)
turtle.pendown()
turtle.circle(10, 360)

# 圆形-右眼
turtle.pencolor("red")
turtle.penup()
turtle.goto(90, 50)
turtle.pendown()
turtle.circle(10, 360)

# 长方形-鼻子
turtle.pencolor("black")
turtle.penup()
turtle.goto(-20, -30)
turtle.pendown()
turtle.forward(30)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(30)
turtle.right(90)
turtle.forward(10)

# 嘴-线形
turtle.pencolor("black")
turtle.penup()
turtle.goto(-10, -100)
turtle.pendown()
turtle.forward(40)

turtle.penup()
turtle.mainloop()
