import math
from threading import Timer
import random
import turtle as t
from tkinter import *
#import pdb; pdb.set_trace()


mainMenu = Tk()

bulletspeed = 20
bulletstate = "ready"



def close():
    exit()

def buy():
    shopWindow = Tk()
    mainMenu.destroy()


def runTheProgram():
    class Bullets(t.Turtle):
        def __init__(self, spriteshape, color, startx, starty):
            t.Turtle.__init__(self, shape=spriteshape)
            self.speed(0)
            self.penup()
            self.color(color)
            self.shape(spriteshape)
            self.goto(startx, starty)
            self.hideturtle()

        bulletstate = StringVar()

        def fireBullet(self):
            global bulletstate
            global bulletspeed
            if bulletstate == "ready":
                bulletstate = "fire"
                x = player.xcor()
                y = player.ycor()
                self.setposition(x, y)
                self.showturtle()

    bullet = Bullets("triangle", "blue", -1200, -1200)
    mainMenu.destroy()
		
    wn = t.Screen()
    wn.setup(1100, 700, 0, 0)
    wn.bgcolor("black")
    wn.title("Space Invaders")

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
    player.setposition(0, -320)
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
        #enemy.shape("square")
        enemy.shape("circle")
        enemy.penup()
        enemy.shapesize(2)
        enemy.speed(10)
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


    def moveLeft():
        x = player.xcor()
        x -= playerspeed
        if x < - 530:
            x = - 530
        player.setx(x)

"""
for enemy in enemies:
    enemyBullet = t.Turtle()
    enemyBullet.speed(0)
    enemyBullet.penup()
    enemyBullet.shape("circle")
    enemyBullet.color("white")
    enemyBullet.shapesize(0.5)
    enemyBullet.hideturtle()
"""

    def moveRight():
        x = player.xcor()
        x += playerspeed
        if x > 530:
            x = 530
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

    def gameover():
        global bulletstate
        gameover = t.Screen()
        gameover.bgcolor("purple")
        gameover.title("AIR WARS END")
        bulletstate = "fire"

    t.listen()
    t.onkey(moveLeft, "Left")
    t.onkey(moveUp, "Up")
    #t.onkey(fireBullet, "space" )



	def fireEnemies():
		eBulletSpeed = 20
		x = enemy.xcor()
		y = enemy.ycor()
		enemyBullet.setposition(x, y)
		y -= eBulletSpeed
		enemy.sety(y)

		
	time = Timer(30.0, fireEnemies)
	time.start()
	
	def isCollision(t1, t2):
		distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
		if distance < 15:
			return True
		else:
			return False



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
			
			




buttonExit=Button(mainMenu, justify = LEFT, command = close)
photobuttonExit=PhotoImage(file="buttonExit.gif")
buttonExit.config(image=photobuttonExit,width="600",height="65")
buttonExit.pack(side=BOTTOM)

buttonShop=Button(mainMenu, justify = LEFT, command = buy)
photobuttonShop=PhotoImage(file="buttonShop.gif")
buttonShop.config(image=photobuttonShop,width="600",height="65")
buttonShop.pack(side=BOTTOM)

buttonStart=Button(mainMenu, justify = LEFT, command = runTheProgram)
photo=PhotoImage(file="buttonStart.gif")
buttonStart.config(image=photo,width="600",height="65")
buttonStart.pack(side=BOTTOM)




		"""
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

		"""



t.done()
mainMenu.mainloop()

