import turtle
import time
import enemies

enemyBullet = turtle.Turtle()
enemyBullet.shape("circle")
enemyBullet.color("white")
enemyBullet.speed(0)
enemyBullet.shapesize(0.5)
enemyBullet.hideturtle()

eBulletSpeed = 20

eBulletState = "ready"

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




for enemy in enemies:
    ebullet = turtle.Turtle()
    ebullet.shape("triangle")
    ebullet.color("white")
    ebullet.penup()
    ebullet.speed()
    ebullet.shapesize(0.5)
    ebullet.setheading(270)
    ebullet.hideturtle()

ebulletspeed = 15
ebulletstate = "ready"

def eFireBullet():
    global ebulletstate
    if ebulletstate == "ready":
        x = enemy.xcor()
        y = enemy.ycor()
        ebullet.setpos(x, y)
        ebullet.showturtle()


bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("purple")
bullet.penup()
bullet.speed()
bullet.shapesize(0.5)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 10
bulletstate = "ready"
        
    

