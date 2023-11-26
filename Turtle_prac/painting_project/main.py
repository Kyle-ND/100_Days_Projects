###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

# import package and making object 
import turtle 


pen = turtle.Turtle() 
screen = turtle.Screen()
screen.setup(width=600,height=600)
screen.setworldcoordinates(-200, -200, 200, 200)
screen.colormode(255)
pen.pensize(15)
pen.penup()
pen.goto(-170,-150)
pen.pendown()

# method to draw square with dots 
# space --> distance between dots 
# x	 --> side of square 
def draw(space,x): 
    for i in range(x): 
        for j in range(x): 
            
            # dot 
            pen.dot() 
            pen.color(random.choice(rgb_colors))
            # distance for another dot 
            pen.forward(space) 
        pen.backward(space*x) 
        
        # direction 
        pen.left(90) 
        pen.forward(space) 
        pen.right(90) 

# Main Section
# screen = turtle.Screen()
screen.setworldcoordinates(-200, -200, 200, 200) 
pen.penup() 
draw(50,10) 

# hide the turtle 
pen.hideturtle()


screen.exitonclick()