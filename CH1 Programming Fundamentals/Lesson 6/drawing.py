import turtle
from random import randint
def draw_square():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.color('yellow')
    brad.speed(1000)
    for z in xrange(100):
        for x in xrange(40):
            for y in xrange(4):
                brad.forward(3000)
                brad.right(90)
            brad.right(10)
        brad.forward(20)
    window.exitonclick()

draw_square()