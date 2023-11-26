import turtle
from time import sleep

screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
di = [0,-20,-40]
parts = []

for i in range(3):
    snake = turtle.Turtle()
    snake.shape("square")
    snake.color("white")
    snake.penup()
    snake.goto(di[i],y=0)
    parts.append(snake)






screen.exitonclick()