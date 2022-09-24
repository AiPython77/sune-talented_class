import turtle
import random

rand_turtle = turtle.Turtle()
rand_turtle.shape('turtle')
rand_turtle.speed(0)

for count in range(1000):
    rand_turtle.forward(random.randint(1, 100))
    rand_turtle.setheading(random.randint(0, 360))
