from tkinter import *
import turtle
import enemies
import enemy__bullet
import MainMenu
import player

#import pdb; pdb.set_trace()
#the window
wn = turtle.Screen()
wn.bgcolor("black")


#Set up the player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("triangle")
player.color("blue")
player.setposition(0, 0)
player.setheading(90)

playerspeed = 15

def moveLeft():
    x = player.xcor()
    x -= playerspeed
    player.setx(x)

def moveRight():
    x = player.xcor()
    x += playerspeed
    player.setx(x)

def moveUp():
    y = player.ycor()
    print(y)
    y += playerspeed
    player.sety(y)
    print(y)

def moveDown():
    y = player.ycor()
    y -= playerspeed
    player.sety(y)

#On click
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(moveUp, "Up")
turtle.onkey(moveDown, "Down")
turtle.listen()



root = Tk()
move = BooleanVar(value=False)
direction = IntVar()

button = Button(root, text="Left")
button.pack(side=LEFT)
button.bind('')

def startMovement():
    global move
    move = True

def stopMovement():
    global move
    move = False

def changeDirection():
    global button
    button =

turtle.done()













