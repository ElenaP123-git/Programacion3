import turtle
def pintaCuadro(color,lado,x,y):
    turtle.goto(x,y)

    for i in range(4):
        turtle.color(color)
        turtle.forward(lado)
        turtle.right(90)

pintaCuadro("blue", 100, 0, 0)
pintaCuadro("red",100,200,200)
pintaCuadro("yellow",100,-200,-200)

turtle.hideturtle()
turtle.done()