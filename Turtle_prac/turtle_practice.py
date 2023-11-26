import turtle
import random

robot = turtle.Turtle()
print(robot)
robot.shape("turtle")
robot.color('CornflowerBlue')
turtle.colormode(255)

def draw_square():
    """Function that draws a Square"""
    for i in range(4):
        robot.forward(100)
        robot.right(90)

def draw_shape(num):
    """Function that draws shapes of different angles based on numbere of sides"""
    angle = 360/num
    for _ in range(num):
        robot.forward(100)
        robot.right(angle)

def draw_random_walk(colours):
    directions = [0, 90, 180, 270]
    robot.pensize(15)
    robot.speed("fastest")
    for _ in range(200):
        robot.color(random.choice(colours))
        robot.forward(30)
        robot.setheading(random.choice(directions))

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    return (r,g,b)

def draw_spirograph(size_of_gap):
    robot.speed("fastest")
    for _ in range(int(360 / size_of_gap)):
        robot.color(random_colour())
        robot.circle(100)
        robot.setheading(robot.heading() + size_of_gap)

        
my_screen = turtle.Screen()
my_screen.bgcolor("black")
draw_spirograph(3)


my_screen.exitonclick()