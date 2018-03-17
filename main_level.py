from tkinter import *
import turtle
import random
import math
import time

# import pdb; pdb.set_trace()
# the window
wn = turtle.Screen()
wn.setup(1100, 700, 0, 0)
wn.bgcolor("black")

#turtle.register_shape("C:/Users/vili/Documents/exercises/HackTues meetings/Space Invaders/gameover.gif")

# Set up the player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("triangle")
player.color("blue")
player.setposition(0, -350)
player.setheading(90)

playerSpeed = 15

# Enemies
enemies = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemies.append(turtle.Turtle())



for enemy in enemies:
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    y = random.randint(360, 390)
    x = random.randint(-550, 550)
    enemy.setposition(x, y)

enemyspeed = 5



enemyBullet = turtle.Turtle()
enemyBullet.shape("circle")
enemyBullet.color("white")
enemyBullet.speed(0)
enemyBullet.shapesize(0.5)
enemyBullet.hideturtle()

bulletSpeed = 20

bulletState = "ready"

"""
turtle.done()
#Player's bullet
#bullet = turtle.Turtle()
#bullet.shape("triangle")
#bullet.color("white")
#bullet.penup()
#bullet.speed(0)
#bullet.shapesize(0.5)
#bullet.hideturtle()

bulletSpeed = 20

"""


# Movement
def moveLeft():
    x = player.xcor()
    x -= playerSpeed
    player.setx(x)


def moveRight():
    x = player.xcor()
    x += playerSpeed
    player.setx(x)


# On click
turtle.listen()
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")

"""
move = False


def startMovement():
   global move
   move = True

def stopMovement():
   global move
   move = False


while True:
   if move and sys.pyautokey.press('left'):
       player.moveLeft()

"""

while True:

    # Enemies' movement

    for enemy in enemies:
        y = enemy.ycor()
        y -= enemyspeed
        enemy.sety(y)

    if enemy.ycor() < -350:
        for enemy in enemies:
            enemy.hideturtle()
        player.hideturtle()

        gameover = turtle.Screen()
        gameover.bgcolor("purple")
        #gameover.bgpic("C:/Users/vili/Documents/exercises/HackTues meetings/Space Invaders/gameover.gif")
        bulletstate = "fire"
        



    def shooting():
        global bulletState
        if bulletState == "ready":
            bulletState = "fire"
            x = enemy.xcor()
            y = enemy.ycor()
            enemyBullet.setposition(x, y)
            enemyBullet.showturtle()

        while True:
            time.sleep(2)
            enemy.shooting()