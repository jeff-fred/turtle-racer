

#Imports
import random as rand
from turtle import Screen, Turtle



#Variables:
gameOn = True
colors = ["red","blue","black","green","orange"]
turtles = []
count = 0
x_pos = -200

red = 0
blue = 0
black = 0
green = 0
orange = 0

#window creation
win = Screen()
win.title("Turtle Racer!")
win.bgcolor("lightgray")
win.setup(width=800, height=600)

#Finish line set up
fLine = Turtle()
fLine.speed(0)
fLine.color("red")
fLine.pu()
fLine.goto(-300, 250)
fLine.pendown()
fLine.goto(300, 250)
fLine.hideturtle()

#points leaderboard
points = Turtle()
points.speed(0)
points.hideturtle()
points.penup()
points.goto(-390, 0)
points.write("Red: {0} \nBlue: {1}\nBlack: {2}\nGreen: {3}\nOrange: {4}".format(red, blue, black, green, orange), align="left", font=("Cambria", 15, "bold"))

#Create turtles of different colors
def turtles_setup():
    global count
    global x_pos
    global turtles
    while count < 5:
        turtle = Turtle()
        turtle.color(colors[count])
        turtle.pu()
        turtle.shape("turtle")
        turtle.left(90)
        turtle.goto(x_pos, -250)
        count += 1
        x_pos += 100
        turtles.append(turtle)

def stop():
    global gameOn
    if gameOn == True:
        gameOn = False

win.listen()
win.onkey(stop, "space")

def add_point(color):
    global red, black, blue, green, orange
    if color == "red":
        red += 1
    elif color == "black":
        black += 1
    elif color == "blue":
        blue += 1
    elif color == "green":
        green += 1
    elif color == "orange":
        orange += 1

turtles_setup()

while gameOn:
    for turtle in turtles:
        turtle.forward(rand.randint(0,7))

        if turtle.ycor() >= 250:
            add_point(turtle.color()[1])
            points.clear()
            points.write("Red: {0} \nBlue: {1}\nBlack: {2}\nGreen: {3}\nOrange: {4}".format(red, blue, black, green, orange), align="left", font=("Cambria", 15, "bold"))
            for turtle in turtles:
                turtle.goto(turtle.xcor(),-250)


win.mainloop()