from tkinter import *
import turtle
import enemies
import enemy__bullet
import MainMenu
import player
import math

import timeit

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


#Enemies

enemies = []
numOfEnemies = 6
turtle1 = turtle.Turtle()

for i in range(numOfEnemies):
    enemies.append(turtle.Turtle())

enemyBullet = turtle.Turtle()
enemyBullet.shape("circle")
enemyBullet.color("white")
enemyBullet.speed(0)
enemyBullet.shapesize(0.5)
enemyBullet.hideturtle()

bulletSpeed = 20

bulletState = "ready"




#Functions
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
	
def shooting():
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = enemy.xcor()
        y = enemy.ycor()
        enemyBullet.setposition(x, y)
        enemyBullet.showturtle()

def collision():
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 15:
        return True
    else:
        return False
	


	
#Binding functions and keys
turtle.onkey(moveLeft, "Left")
turtle.onkey(moveRight, "Right")
turtle.onkey(moveUp, "Up")
turtle.onkey(moveDown, "Down")
turtle.listen()
	
#Main game loop
#while True:
def main_loop():
	pass





while True:
    time.sleep(2)
    enemy.shooting()







for enemy in enemies:
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(700, 800)
    y = random.randint(-350, 350)
    enemy.setposition(x, y)



enemyspeed = 5




turtle.done()
















wn.mainloop()

