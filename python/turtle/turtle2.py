import turtle
import time

turtlee = turtle.Turtle()

turtlee.shape('turtle')
#turtlee.shapesize(2, 2, 3)
turtlee.fillcolor('green')

turtlee.left(90)
turtlee.forward(100)
time.sleep(0.5)

turtlee.right(135)
turtlee.forward(100)
time.sleep(0.5)

turtlee.left(45)
turtlee.backward(100)
time.sleep(0.5)

turtlee.circle(100)
turtlee.setposition(100, 100)
turtlee.setposition(0, 0)
