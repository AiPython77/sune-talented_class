import turtle

turtlee = turtle.Turtle()

turtlee.shape('turtle')
#turtlee.shapesize(2, 2, 3)
turtlee.fillcolor('green')

"""turtlee.setposition(100, 0)
turtlee.setposition(-100, 0)
turtlee.setposition(0, 0)

turtlee.setposition(0, 100)
turtlee.setposition(0, -100)"""

turtlee.setposition(100, 0)
turtlee.backward(200)
turtlee.penup()

turtlee.setposition(0, 100)
turtlee.pendown()
turtlee.left(90)
turtlee.backward(200)

