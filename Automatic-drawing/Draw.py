import turtle
import random

def draw_shape(shape, size, fill_color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()

    if shape == "circle":
        turtle.circle(size)
    elif shape == "square":
        for _ in range(4):
            turtle.forward(size)
            turtle.right(90)
    elif shape == "triangle":
        for _ in range(3):
            turtle.forward(size)
            turtle.right(120)

    turtle.end_fill()

# Prompt the user to enter the number of shapes
num_shapes = int(input("Enter the number of shapes: "))

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1920, height=1080)
screen.title("Artistic Shapes")

# Set up the turtle object
turtle.speed(0)  # Set the speed of drawing (0 is the fastest)

# Draw the shapes
shapes = ["circle", "square", "triangle"]

for _ in range(num_shapes):
    shape = random.choice(shapes)
    size = random.randint(50, 150)  # Random size between 50 and 150
    fill_color = random.choice(["red", "blue", "green", "orange", "purple"])  # Random fill color
    x = random.randint(-900, 900)  # Random x coordinate
    y = random.randint(-540, 540)  # Random y coordinate
    draw_shape(shape, size, fill_color, x, y)

turtle.exitonclick()
