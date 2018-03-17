import turtle as t
import math
import random
from tkinter import *

mainMenu = Tk()

def close():
    exit()

def buy():
    shopWindow = Tk()
    mainMenu.destroy()

def runTheProgram():
    mainMenu.destroy()

    border = t.Turtle()
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

    player = t.Turtle()
    player.shape("square")
    player.color("purple")
    player.penup()
    player.setposition(0, 0)
    player.setheading(90)
    player.speed()
    player.shapesize(1.9)

    playerspeed = 14

    numberOfEnemies = 6
    enemies = []
    for i in range(numberOfEnemies):
        enemies.append(t.Turtle())

    for enemy in enemies:
        enemy.color("green")
        # enemy.shape("square")
        enemy.shape("circle")
        enemy.penup()
        enemy.shapesize(2)
        enemy.speed(3)
        x = random.randint(-550, 550)
        y = random.randint(200, 350)
        enemy.setposition(x, y)

    enemyspeed = 9

    bullet = t.Turtle()
    bullet.shape("triangle")
    bullet.color("pink")
    bullet.penup()
    bullet.speed()
    bullet.shapesize(0.5)
    bullet.hideturtle()

    bulletspeed = 20
    bulletstate = "ready"


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


    def fireBullet():
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "fire"
            x = player.xcor()
            y = player.ycor()
            bullet.setposition(x, y)
            bullet.showturtle()

    t.listen()
    t.onkey(moveLeft, "Left")
    t.onkey(moveUp, "Up")
    t.onkey(moveRight, "Right")
    t.onkey(moveDown, "Down")

    while True:
        for enemy in enemies:
            enemy.fd(100)
        if isCollision(player, enemy):
            for enemy in enemies:
                enemy.hideturtle()
                player.hideturtle()
                bullet.hideturtle()
                bulletstate = "fire"
                break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 275:
        bullet.hideturtle()
        bulletstate = "ready"


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

"""
wn = t.Screen()
wn.setup(1100, 700, 0, 0)
wn.bgcolor("black")
wn.title("Space Invaders")
"""

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

mainMenu.mainloop()