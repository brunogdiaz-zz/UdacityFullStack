import turtle
from random import randint
def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('black')
    brad.speed(1000)
    for x in [randint(0,15)*5 for x in xrange(1,2000)]:
        brad.forward(x)
        brad.right(x)
    window.exitonclick()

draw_square()