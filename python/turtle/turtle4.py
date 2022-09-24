import turtle

turtlee = turtle.Turtle()

turtlee.shape('turtle')
#turtlee.shapesize(2, 2, 3)
turtlee.fillcolor('green')

turtlee.penup()
turtlee.forward(100)
print(turtlee.isdown())

turtlee.pendown()
turtlee.forward(500)
print(turtlee.isdown())
