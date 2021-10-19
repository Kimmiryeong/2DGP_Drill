import turtle

turtle.shape("turtle")

turtle.setheading(90)

def gofront():
    turtle.forward(50)


def turnright():
    turtle.right(90)


def turnleft():
    turtle.left(90)

def goback():
    turtle.backward(50)

def restart():
    turtle.reset()
    turtle.setheading(90)


turtle.onkeypress(gofront,'w')
turtle.onkeypress(turnright,'d')
turtle.onkeypress(turnleft,'a')
turtle.onkeypress(goback,'s')
turtle.onkeypress(restart,'Escape')

turtle.listen()
