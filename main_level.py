from tkinter import *
import turtle as t
import random
import math
from threading import Timer

#import pdb; pdb.set_trace()
# the window
wn = t.Screen()
wn.setup(1100, 700, 0, 0)
wn.bgcolor("black")

#turtle.register_shape("C:/Users/vili/Documents/exercises/HackTues meetings/Space Invaders/gameover.gif")

# Set up the player
player = t.Turtle()
player.speed(0)
player.penup()
player.shape("triangle")
player.color("blue")
player.setposition(0, -350)
player.setheading(90)

playerSpeed = 15

# Enemies
enemies = []
#numOfEnemies = 6

for i in range(6):
    enemies.append(t.Turtle())

for enemy in enemies:
    enemy.penup()
    enemy.speed(0)
    enemy.shape("circle")
    enemy.color("red")
    y = random.randint(360, 1000)
    x = random.randint(-550, 550)
    enemy.setpos(x, y)

enemyspeed = 5

for enemy in enemies:
    enemyBullet = t.Turtle()
    enemyBullet.speed(0)
    enemyBullet.penup()
    enemyBullet.shape("circle")
    enemyBullet.color("white")
    enemyBullet.shapesize(0.5)
    enemyBullet.hideturtle()


def moveLeft():
    x = player.xcor()
    x -= playerSpeed
    player.setx(x)


def moveRight():
    x = player.xcor()
    x += playerSpeed
    player.setx(x)

"""
def fireBullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()
"""

"""
def shooting(self):
    # Player's bullet
    bullet = t.Turtle()
    bullet.speed(0)
    bullet.penup()
    bullet.shape("triangle")
    bullet.color("white")
    bullet.shapesize(0.5)
    global bulletSpeed
    global bulletState
    bulletSpeed = 20
    bulletState = "ready"
    x = player.xcor()
    y = player.ycor()
    bullet.setpos(x, y)
    y += 3
    bullet.sety(y)

"""
def fireEnemies():
    eBulletSpeed = 20
    x = enemy.xcor()
    y = enemy.ycor()
    enemyBullet.setposition(x, y)
    y -= eBulletSpeed
    enemy.sety(y)

# On click
t.listen()
t.onkey(moveLeft, "Left")
t.onkey(moveRight, "Right")
t.onkey(fireEnemies, "space")


time = Timer(30.0, fireEnemies)
time.start()


def shooting():
    while True:
        global bullet
        bullet = t.Turtle()
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()



def collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
    if distance < 10:
        return True
    else:
        return False

def gameOver():
    global bulletState
    gameover = t.Screen()
    gameover.bgcolor("purple")
    #gameover.bgpic("C:/Users/vili/Documents/exercises/HackTues meetings/Space Invaders/gameover.gif")
    bulletState = "fire"


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
        gameOver()

        while True:
            time.sleep(2)
            enemy.eshooting()
        global bulletState
        if bulletState == "ready":
            bulletState = "fire"
            x = player.xcor()
            y = player.ycor()
            bullet.setposition(x, y)
            bullet.showturtle()

    if bulletState == "fire":
        y = bullet.sety(y)
    if bullet.ycor() > 350:
        bullet.hideturtle()
        bulletState = "ready"


    if collision(enemy, player):
        for enemy in enemies:
            enemy.hideturtle()
        gameOver()

t.done()
