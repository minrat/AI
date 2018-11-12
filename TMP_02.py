import turtle

turtle.mode("standard")
turtle.pensize(3)
turtle.pencolor("red")

turtle.begin_poly()
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.end_poly()

p=turtle.get_poly()
turtle.register_shape("aaa",p)

pic = turtle.Pen()

pic.shape("aaa")
pic.fd(300)
turtle.mainloop()
