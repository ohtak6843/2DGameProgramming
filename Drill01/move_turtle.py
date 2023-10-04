import turtle

def moving_w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def moving_a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def moving_s():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def moving_d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()


def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(moving_w, 'w')
turtle.onkey(moving_a, 'a')
turtle.onkey(moving_s, 's')
turtle.onkey(moving_d, 'd')

turtle.onkey(restart, 'Escape')

turtle.listen()

turtle.exitonclick()
