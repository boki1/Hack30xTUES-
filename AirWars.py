import math
import random
import turtle
from tkinter import *

mainMenu = Tk()

bulletspeed = 20
bulletstate = "ready"



def close():
    exit()

def buy():
    shopWindow = Tk()
    mainMenu.destroy()


def runTheProgram():
    class Bullets(turtle.Turtle):
        def __init__(self, spriteshape, color, startx, starty, bulletstate):
            turtle.Turtle.__init__(self, shape=spriteshape)
            self.speed(0)
            self.penup()
            self.color(color)
            self.shape(spriteshape)
            self.goto(startx, starty)
            self.speed = 9
            self.bulletstate = StringVar()
            self.hideturtle()

        def fireBullet(self):
            if bulletstate == "ready":
                global bulletstate
                bulletstate = "fire"
                x = player.xcor()
                y = player.ycor()
                self.setposition(x, y)
                self.showturtle()

    mainMenu.destroy()

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
    player.setposition(0, -320)
    player.setheading(90)
    player.speed()
    player.shapesize(1.9)

    playerspeed = 14

    numberOfEnemies = 6
    enemies = []
    for i in range(numberOfEnemies):
        enemies.append(turtle.Turtle())

    for enemy in enemies:
        enemy.color("green")
        # enemy.shape("square")
        enemy.shape("circle")
        enemy.penup()
        enemy.shapesize(2)
        enemy.speed(10)
        x = random.randint(-550, 550)
        y = random.randint(200, 350)
        enemy.setposition(x, y)

    enemyspeed = 9

    bullet = turtle.Turtle()
    bullet.shape("triangle")
    bullet.color("pink")
    bullet.penup()
    bullet.speed()
    bullet.shapesize(0.5)
    bullet.hideturtle()

    """
    def firebullet():
        global bulletstate
        if bulletstate == "ready":
            bulletstate = "fire"
            x = player.xcor()
            y = player.ycor()

            bullet.setposition(x, y)
            bullet.showturtle()
    """

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
    


    def gameover():
        gameover = turtle.Screen()
        gameover.bgcolor("purple")
        gameover.title("AIR WARS END")
        bulletstate = "fire"

    turtle.listen()
    turtle.onkey(moveLeft, "Left")
    turtle.onkey(moveUp, "Up")
    turtle.onkey(moveRight, "Right")
    turtle.onkey(moveDown, "Down")
    turtle.onkey(fireBullet, "space")

    while True:
        for enemy in enemies:
            y = enemy.ycor()
            y -= enemyspeed
            enemy.sety(y)
            if enemy.ycor() < -350:
                gameover()

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

        if bullet.ycor() > 350:
            bullet.hideturtle()
            bulletstate = "ready"






"""
wn = turtle.Screen()
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