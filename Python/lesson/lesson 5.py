import turtle

screen = turtle.Screen()
screen.bgcolor("Black")

pen = turtle.Turtle()
pen.color("Blue")
pen.pensize(2)


# pen.forward(100)
# pen.right(90)
# pen.forward(50)
# pen.right(90)
# pen.forward(100)
# pen.right(90)
# pen.forward(50)


# pen.forward(100)
# pen.left(125)
# pen.forward(100)
# pen.left(120)
# pen.forward(100)

# for i in range(360):
#     pen.forward(1)
#     pen.right(1)

for i in range(6):
    pen.forward(i*5)
    pen.right(45)



turtle.done()