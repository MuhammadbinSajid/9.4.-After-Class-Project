import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
pen = turtle.Turtle()

# Define the side length of the square
side_length = 100

# Draw a square
for _ in 4*[None]:
    pen.forward(side_length)  # Move forward by the side length
    pen.right(90)  # Turn 90 degrees to the right

# Hide the turtle
pen.hideturtle()

# Close the window on click
screen.exitonclick()
