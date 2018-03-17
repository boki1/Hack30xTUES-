import turtle
import math
import random
import winsound
from tkinter import *

mainMenu = Tk()

def close():
    exit()

def buy():
    shopWindow = Tk()
    mainMenu.destroy()

def runTheProgram():
    mainMenu.destroy()
    player.showturtle()

buttonExit=Button(mainMenu, justify = LEFT, command = close)
photobuttonExit=PhotoImage(file="buttonExit.gif")
buttonExit.config(image=photobuttonExit,width="90",height="50")
buttonExit.pack(side=BOTTOM)

buttonShop=Button(mainMenu, justify = LEFT, command = buy)
photobuttonShop=PhotoImage(file="buttonShop.gif")
buttonShop.config(image=photobuttonShop,width="90",height="50")
buttonShop.pack(side=BOTTOM)

buttonStart=Button(mainMenu, justify = LEFT, command = runTheProgram)
photo=PhotoImage(file="buttonStart.gif")
buttonStart.config(image=photo,width="90",height="50")
buttonStart.pack(side=BOTTOM)

wn = turtle.Screen()
wn.setup(1100, 700, 0, 0)
wn.bgcolor("black")
wn.title("Space Invaders")

border = turtle.Turtle()
border.speed(0)
border.penup()
border.setposition(-550, -350)
border.color("white")
border.pendown()
border.pensize(2)

border.fd(1100)
border.lt(90)
border.fd(700)
border.lt(90)
border.fd(1100)
border.lt(90)
border.fd(700)
border.lt(90)
border.hideturtle()

player = turtle.Turtle()
player.shape("square")
player.color("purple")
player.penup()
player.setposition(0, 0)
player.setheading(90)
player.speed()
player.shapesize(1.9)

playerspeed = 14

# Choose the number of enemies
numberOfEnemies = 6
# Create an empty list of enemies
enemies = []

# Add enemies to the list
for i in range(numberOfEnemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("green")
    # enemy.shape("square")
    enemy.shape("circle")
    enemy.penup()
    enemy.shapesize(2)
    enemy.speed(0)
    x = random.randint(-550, 550)
    y = random.randint(200, 350)
    enemy.setposition(x, y)

enemyspeed = 9



def moveLeft():
    x = player.xcor()
    x -= playerspeed
    if x < - 530:
        x = - 530
    player.setx(x)


def moveRight():
    x = player.xcor()
    x += playerspeed
    if x > 530:
        x = 530
    player.setx(x)


def moveUp():
    y = player.ycor()
    y += playerspeed
    if y > 330:
        y = 330
    player.sety(y)


def moveDown():
    y = player.ycor()
    y -= playerspeed
    if y < -330:
        y = -330
    player.sety(y)



turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveUp, "Up")
turtle.onkey(moveRight, "Right")
turtle.onkey(moveDown, "Down")
#turtle.onkey(fireBullet, "space")



mainMenu.mainloop()