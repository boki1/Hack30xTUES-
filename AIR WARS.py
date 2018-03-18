import turtle
import math
import random
import winsound


wn = turtle.Screen()
wn.bgcolor("light blue")
wn.bgpic("backgroundupdated.gif")
wn.title("AIM WARS")
wn.setup(1000, 820, 0, 0)

turtle.register_shape("planefix.gif")
turtle.register_shape("Chance Vought  F4U-1D Corsair.gif")
turtle.register_shape("bullet.gif")

borderPen = turtle.Turtle()
borderPen.speed(0)
borderPen.penup()
borderPen.setposition(-300, -400)
borderPen.color("grey")
borderPen.pendown()
borderPen.pensize(2)
borderPen.fd(600)
borderPen.lt(90)
borderPen.fd(800)
borderPen.lt(90)
borderPen.fd(600)
borderPen.lt(90)
borderPen.fd(800)
borderPen.lt(90)
borderPen.hideturtle()

winsound.PlaySound('planesound.wav', winsound.SND_ASYNC)

score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("black")
score_pen.penup()
score_pen.setposition(-425, 200)
scorestring = "Score: %s" %score
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
        self.speed = 6.5

    def move(self):
        self.fd(self.speed)

    def turnLeft(self):
        self.speed = 6.5
        self.lt(180)
        self.fd(self.speed)

    def turnRight(self):
        self.speed = 6.5
        self.rt(180)
        self.fd(self.speed)

    def dontMove(self):
        self.speed = 0

player = Player("planefix.gif", "pink", 0, -365)

pupesh = player.xcor()

numberOfEnemies = 4
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
    enemy.goto(random.randint(-300, 235), random.randint(410, 500))

enemyspeed = 2

bullet = turtle.Turtle()
bullet.shape("bullet.gif")
bullet.color("purple")
bullet.penup()
bullet.speed()
bullet.shapesize(0.5)
bullet.setheading(90)
bullet.hideturtle()

bulletspeed = 25
bulletstate = "ready"

def fireBullet():
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        x = player.xcor()
        y = player.ycor()
        bullet.setposition(x, y)
        bullet.showturtle()
    winsound.PlaySound('Gun+357+Magnum.wav', winsound.SND_ASYNC)

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
        y -= enemyspeed
        enemy.sety(y)

    for enemy in enemies:
        if enemy.ycor() < -585:
            for enemy in enemies:
                enemy.hideturtle()
            player.hideturtle()
            gameover = turtle.Screen()
            gameover.bgpic('gameoverfix.gif')
            gameover.bgcolor("black")
            bulletstate = "fire"
            break

        if isCollision(bullet, enemy):
            enemyspeed += 1
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(-500, 0)
            enemy.goto(random.randint(-300, 235), random.randint(765, 785))
            score += 5
            scorestring = "Score: %s" % score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 16, "normal"))

        if isCollision(player, enemy):
            for enemy in enemies:
                enemy.hideturtle()
            player.hideturtle()
            gameover = turtle.Screen()
            gameover.bgpic('gameoverfix.gif')
            gameover.bgcolor("black")
            bullet.hideturtle()
            bulletstate = "fire"
            break


        if isCollision(player, borderPen):
            player.speed = 0


    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    if bullet.ycor() > 605:
        bullet.hideturtle()
        bulletstate = "ready"
