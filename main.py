import turtle
import random

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor('pale turquoise')

t = turtle.Turtle()
t.hideturtle()
t2 = turtle.Turtle()
t2.hideturtle()
t3 = turtle.Turtle()
t3.hideturtle()

t.speed(0)

t.penup()
t.goto(0, 50)
t.pendown()
t.write("All About Me", font=("arial", 24, "bold"), align="center")


t.penup()
t.goto(0, -50)
t.pendown()
t.write("Namrata Rai", font=("arial", 24, "bold"), align="center")
t.pensize(2)
t.pencolor('white')
t.fillcolor('light steel blue')

t.begin_fill()
t.penup()
t.goto(0,-175)
t.showturtle()
t.pendown()
t.circle(55)
t.setheading(0)
t.penup()
t.end_fill()

t2.penup()
t2.goto(-150,150)
t2.pendown()
turtle.addshape("leaf.gif")
t2.shape("leaf.gif")
a = t2.stamp()

t2.penup()
t2.goto(150,-150)

turtle.addshape("matcha.gif")
t2.shape("matcha.gif")
b = t2.stamp()

t2.goto(0,0)

enter = input("Press Enter to Start")
t.clear()
t2.clear()
#removestamps

screen.bgcolor('orange')
#2nd Screen
t.penup()
t.goto(0, 25)
t.pendown()
t.write("Favorite Foods", font=("arial", 24, "bold"), align="center")

t.penup()
t.goto(0, -50)
t.pendown()
t.write("Mac & Cheese, Dumplings, Noodles, ", font=("arial", 15, "bold"), align="center")

t2.penup()
t2.goto(-150,150)
t2.pendown()
turtle.addshape("dumpling.gif")
t2.shape("dumpling.gif")
a = t2.stamp()

t2.penup()
t2.goto(150,-150)
turtle.addshape("mac.gif")
t2.shape("mac.gif")
b = t2.stamp()

t2.penup()
t2.goto(150,150)
turtle.addshape("noodle.gif")
t2.shape("noodle.gif")
c = t2.stamp()

t.pencolor('white')
t.fillcolor('plum')

t.penup()
t.goto(-150,-175)
t.pendown()
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.penup()
t.goto(-100, -100)
t.penup()
t.end_fill()

t2.goto(0,0)

enter = input("Press Enter to Switch Page")
t.clear()
t2.clear()
#removestamps

screen.bgcolor('pink')
#thirdscreen
t.penup()
t.goto(0, 50)
t.pendown()
t.write("Hobbies", font=("arial", 24, "bold"), align="center")

t.penup()
t.goto(0, 0)
t.pendown()
t.write(" Drawing, Running, Baking, Crochet ", font=("arial", 15, "bold"), align="center")

t2.penup()
t2.goto(150,-200)
turtle.addshape("run.gif")
t2.shape("run.gif")
a = t2.stamp()

t2.penup()
t2.goto(150,150)
turtle.addshape("draw.gif")
t2.shape("draw.gif")
b = t2.stamp()

t2.penup()
t2.goto(-150,150)
turtle.addshape("bake.gif")
t2.shape("bake.gif")
c = t2.stamp()

t2.penup()
t2.goto(-150,-150)
turtle.addshape("crochet.gif")
t2.shape("crochet.gif")
d = t2.stamp()

t.pencolor('blue')
# heading-90 radius 60
t.fillcolor('steel blue')
t.penup()
t.goto(130,-80)
t.pendown()
t.setheading(90)
t.begin_fill()
t.circle(60)
t.end_fill()
t.fillcolor('misty rose')

t.goto(70,-80)
t.setheading(0)
t.begin_fill()
t.circle(30,180)
t.end_fill()

t.penup()
t.goto(70,-88)
t.pendown()

t.setheading(90)
t.begin_fill()
t.circle(30,180)
t.end_fill()

t.penup()
t.goto(70,-80)
t.pendown()

t.setheading(180)
t.begin_fill()
t.circle(30,180)
t.end_fill()

t.penup()
t.goto(70,-80)
t.pendown()

t.setheading(270)
t.begin_fill()
t.circle(30,180)
t.end_fill()


t2.goto(0,0)

enter = input("Press Enter to Switch Page")
t.clear()
t2.clear()
#removestamps

screen.bgcolor('medium purple')
#fourthscreen
t.pencolor('black')
t.penup()
t.goto(0, -50)
t.pendown()
t.write("Favorite Movie", font=("arial", 24, "bold"), align="center")

t.penup()
t.goto(0, 0)
t.pendown()
t.write("Moana and Coraline", font=("arial", 15, "bold"), align="center")


t2.penup()
t2.goto(-150,150)
t2.pendown()
turtle.addshape("coraline.gif")
t2.shape("coraline.gif")
a = t2.stamp()

t2.penup()
t2.goto(150,150)
turtle.addshape("moana.gif")
t2.shape("moana.gif")
b = t2.stamp()

t.penup()
t.goto(20, -100)
t.pencolor('blue')
t.fillcolor('aqua')
t.pendown()
t.begin_fill()
t.circle(30,180)
t.end_fill()



t2.goto(0,0)
enter = input("Press Enter to Switch Page")
t.clear()
t2.clear()
#removestamps

screen.bgcolor('pale green')
#fifthscreen
t.pencolor('black')

t.penup()
t.goto(0, 50)
t.pendown()
t.write("Favorite Sport", font=("arial", 24, "bold"), align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.write("Lacrosse", font=("arial", 15, "bold"), align="center")
t2.penup()
t2.goto(-150,150)
t2.pendown()
turtle.addshape("lax.gif")
t2.shape("lax.gif")
a = t2.stamp()

t2.penup()
t2.goto(150,150)
turtle.addshape("field.gif")
t2.shape("field.gif")
b = t2.stamp()

t.pencolor('white')
t.fillcolor('light coral')

t.penup()
t.goto(0,-150)
t.pendown()

t.begin_fill()
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.forward(50)
t.left(45)
t.end_fill()

t2.goto(0,0)

enter = input("Press Enter to Switch Page")
t.clear()
t2.clear()
#removestamps

screen.bgcolor('tomato')
#endscreen
t.pencolor('white')
t.penup()
t.goto(0,0)
t.pendown()
t.write("The End!", font=("arial", 24, "bold"), align="center")



turtle.done()