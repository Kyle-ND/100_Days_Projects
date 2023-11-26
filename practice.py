import turtle
from time import sleep

robot = turtle.Turtle()
kyle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=500,height=400)
robot.penup()
robot.goto(x=-230,y=50)
kyle.penup()
kyle.goto(x=-230,y=0)

sleep(1)
user_bet = screen.textinput(title="Command prompt",prompt="Enter a command for your robot?: ")

if "forward" in user_bet:
    user_bet = user_bet.split()
    robot.fd(int(user_bet[1]))
    sleep(1)
    user_bet = screen.textinput(title="Command prompt",prompt="Enter a command for your robot?: ")




screen.exitonclick()