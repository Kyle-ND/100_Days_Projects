# import turtle

# robot = turtle.Turtle()
# print(robot)
# robot.shape("turtle")
# robot.color('CornflowerBlue')
# robot.forward(100)

# my_screen = turtle.Screen()
# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l" 
print(table)