import turtle
import random

turtles = []

for index in range (5):
    new_turtle = turtle.Turtle()
    turtles.append(new_turtle)
    new_turtle.shape('turtle')
    new_turtle.penup()
    new_turtle.speed(0)

for count in range(100):
    for index in range(5):
        turtles[index].setheading(random.randint(0, 360))
        turtles[index].forward(random.randint(1, 100))
