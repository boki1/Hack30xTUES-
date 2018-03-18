import turtle
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
#wn.bgpic("background.gif")
wn.title("ГЪЛЪБ БЕЗ 1/2")
wn.setup(600, 800, 0, 0)

turtle.register_shape("planefix.gif")
turtle.register_shape("Chance Vought  F4U-1D Corsair.gif")

borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.penup()
borderPen.setposition(-250, -400)
borderPen.color("grey")
borderPen.pendown()
borderPen.pensize(2)
borderPen.fd(500)
borderPen.lt(90)
borderPen.fd(800)
borderPen.lt(90)
borderPen.fd(500)
borderPen.lt(90)
borderPen.fd(800)
borderPen.lt(90)
borderPen.hideturtle()


score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-245, 420)
scorestring = "Score: %s" % score
score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))
score_pen.hideturtle()

class Player(turtle.Turtle):
    def __init__(self, spriteshape, color, q, p):
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.shape(spriteshape)
        self.color(color)
        self.setposition(q, p)
        self.speed = 5

    def move(self):
        self.fd(self.speed)

    def turnLeft(self):
        self.speed = 5
        self.lt(180)
        self.fd(self.speed)

    def turnRight(self):
        self.speed = 5
        self.rt(180)
        self.fd(self.speed)

    def dontMove(self):
        self.speed = 0

player = Player("planefix.gif", "pink", 0, -365)

pupesh = player.xcor()

if pupesh > 235:
    pupesh = 235
    player.setx(pupesh)

if pupesh < -235:
    pupesh = -235
    player.setx(pupesh)

numberOfEnemies = 6
enemies = []

for i in range(numberOfEnemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    #enemy.shape("square")
    enemy.shape("Chance Vought  F4U-1D Corsair.gif")
    enemy.penup()
    enemy.shapesize(1.5)
    enemy.speed(0)
    enemy.goto(random.randint(-235, 235), random.randint(365, 385))

enemyspeed = 3

bullet = turtle.Turtle()
bullet.shape("triangle")
bullet.color("purple")
bullet.penup()
bullet.speed()
bullet.shapesize(0.5)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 5
bulletstate = "ready"

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

    for enemy in enemies:
        y = enemy.ycor()
        y -= 1
        enemy.sety(y)

    for enemy in enemies:
        if enemy.ycor() < -385:
            for enemy in enemies:
                enemy.hideturtle()
            player.hideturtle()
            gameover = turtle.Screen()
            gameover.bgpic('gameover1.gif')
            gameover.bgcolor("red")
            bulletstate = "fire"
            break

        if isCollision(bullet, enemy):
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(-500, 0)
            enemy.goto(random.randint(-235, 235), random.randint(365, 385))
            score += 10
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))

        if isCollision(player, enemy):
            for enemy in enemies:
                enemy.hideturtle()
            player.hideturtle()
            gameover = turtle.Screen()
            gameover.bgpic('gameover1.gif')
            gameover.bgcolor("red")
            bullet.hideturtle()
            bulletstate = "fire"
            break

    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 405:
        bullet.hideturtle()
        bulletstate = "ready"
