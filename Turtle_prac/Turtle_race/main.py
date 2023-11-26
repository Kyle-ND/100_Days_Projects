from turtle import Turtle, Screen
from time import sleep
import random


is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ["red","orange","yellow","green","blue","purple","black","cyan"]
y_pos = [-70,-40,-10,20,50,80,110,140]
robots = []


for i in range(8):
    new_robot = Turtle(shape="turtle")
    new_robot.penup()
    new_robot.color(colors[i])
    new_robot.goto(x=-230, y=y_pos[i])
    robots.append(new_robot)

sleep(1)
user_bet = screen.textinput(title="Command prompt",prompt="Enter a color you think will win?: ")

if user_bet:
    is_race_on = True

while is_race_on:
    for robot in robots:
        if robot.xcor() > 230:
            is_race_on = False
            if robot.pencolor() == user_bet:
                print(f"You've won  the {user_bet} turtle won the race.")
            else:
                print(f"You've lost the {robot.pencolor()} turtle won the race.")
        robot.forward(random.randint(0,10))


screen.exitonclick()