import turtle
robot = turtle.Turtle()
screen  = turtle.Screen()
robot.shape("turtle")

def main():

    robot.color("red")
    screen.listen()
    screen.onkey(key="Up",fun=move)
    screen.onkey(key="Right",fun=turn_right)
    screen.onkey(key="Left",fun=turn_left)
    screen.onkey(key="Down",fun=backwards)
    screen.onkey(key="c",fun=clear)
    screen.exitonclick()

def move():
    robot.fd(10)

def turn_right():
    robot.right(90)

def turn_left():
    robot.left(90)

def backwards():
    robot.backward(10)

def clear():
    robot.reset()
    robot.color("red")

if __name__ == "__main__":
    main()