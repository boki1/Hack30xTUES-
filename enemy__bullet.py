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

    
        
    

