import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")

enemies = []
numOfEnemies = 6
turtle1 = turtle.Turtle()

for i in range(numOfEnemies):
    enemies.append(turtle.Turtle())


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

