import turtle
import random

robot = turtle.Turtle()
print(robot)
robot.shape("turtle")
robot.color('CornflowerBlue')

# def draw_shape(num):
#     angle = 360/num
#     for i in range(num):
#         robot.forward(100)
#         robot.right(angle)

# for i in range(3,11):
#     draw_shape(i)

moves = [robot.right(90),robot.left(90),robot.forward(100),robot.backward(100)]


my_screen = turtle.Screen()
my_screen.exitonclick()

