import turtle
import random

enemies = []
numOfEnemies = 6

for i in range(numOfEnemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.shape("circle")
    enemy.color("red")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-550, 550)
    y = random.randint(-350, 350)
    enemy.setposition(x, y)
    enemyspeed = 5

    #if enemy.xcor() < -150 and enemy.ycor() < 100 and enemy.ycor() > 100:
    #   x = enemy.xcor()
    #    x +=  enemyspeed
    #    enemy.setx(x)

    #if enemy.xcor() > 150 and enemy.ycor() < 100 and enemy.ycor > 100:
    #    x = enemy.xcor()
    #    x -= enemyspeed
    #    enemy.setx(x)


turtle.done()

