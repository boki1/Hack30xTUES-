import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("purple")
wn.bgpic("background.gif")
wn.title("ГЪЛЪБ БЕЗ 1/2")
wn.setup(1200, 800, 0, 0)

turtle.register_shape("planefix.gif")

borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.penup()
borderPen.setposition(-550, -350)
borderPen.color("white")
borderPen.pendown()
borderPen.pensize(2)
borderPen.fd(1100)
borderPen.lt(90)
borderPen.fd(700)
borderPen.lt(90)
borderPen.fd(1100)
borderPen.lt(90)
borderPen.fd(700)
borderPen.lt(90)
borderPen.hideturtle()

"""
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-425, 200)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))
score_pen.hideturtle()
"""
"""
player = turtle.Turtle()
player.speed(0)
player.shape('planefix.gif')
player.color("purple")
player.penup()
player.setposition(0, -315)
#player.setposition(0, 0)
player.setheading(90)
playerspeed = 23
"""

class Player(turtle.Turtle):
    def __init__(self, spriteshape, color, q, p):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.shape(spriteshape)
        self.color(color)
        self.setposition(q, p)
        self.speed = 3

    def move(self):
        self.fd(self.speed)

    def turnLeft(self):
        self.speed = 3
        self.lt(180)
        self.fd(self.speed)

    def turnRight(self):
        self.speed = 3
        self.rt(180)
        self.fd(self.speed)

    def dontMove(self):
        self.speed = 0


player = Player("planefix.gif", "pink", 0, -315)

numberOfEnemies = 6
enemies = []

for i in range(numberOfEnemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("square")
    enemy.penup()
    enemy.shapesize(1.5)
    enemy.speed(0)
    enemy.goto(random.randint(-550, 550), random.randint(320, 335))

enemyspeed = 3

bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("pink")
bullet.penup()
bullet.speed()
bullet.shapesize(0.5)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 20
bulletstate = "ready"

"""
def moveLeft():
    x = player.xcor()
    x -= playerspeed
    if x < - 550:
        x = - 550
    player.setx(x)

def moveRight():
    x = player.xcor()
    x += playerspeed
    if x > 550:
        x = 550
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

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(player.turnLeft, "Left")
turtle.onkey(player.turnRight, "Right")
turtle.onkey(fireBullet, "space")
turtle.onkey(player.dontMove, "Up")
turtle.onkey(player.dontMove, "Down")

while True:
    player.move()
    """
    for enemy in enemies:
        if isCollision(bullet, enemy):
            print("GYLYB")
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, 1100)
            enemy.setposition(random.randint(-550, 550), random.randint(320, 535))

        if isCollision(player, enemy):
            for enemy in enemies:
                enemy.hideturtle()
                player.hideturtle()
                gameover = turtle.Screen()
                gameover.bgcolor("blue")
                bullet.hideturtle()
                bulletstate = "fire"
                break

        y = enemy.ycor()
        y -= 5
        enemy.sety(y)

        if bulletstate == "fire":
            y = bullet.ycor()
            y += bulletspeed
            bullet.sety(y)

        if bullet.ycor() > 350:
            bullet.hideturtle()
            bulletstate = "ready"
    """
    for enemy in enemies:
        if enemy.ycor() < -545:
            for enemy in enemies:
                enemy.hideturtle()
            player.hideturtle()
            gameover = turtle.Screen()
            gameover.bgpic('gameover.gif')
            bulletstate = "fire"
            break

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            enemy.goto(random.randint(-550, 550), random.randint(320, 335))
            #score += 10
            #scorestring = "Score: %s" % score
            #score_pen.clear()
            #score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))

        if isCollision(player, enemy):
            for enemy in enemies:
                enemy.hideturtle()
            player.hideturtle()
            gameover = turtle.Screen()
            gameover.bgpic('gameover.gif')
            bullet.hideturtle()
            bulletstate = "fire"
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 35:
        bullet.hideturtle()
        bulletstate = "ready"
