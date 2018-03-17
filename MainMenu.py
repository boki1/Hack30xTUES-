from tkinter import *
import turtle

mainMenu = Tk()

def moveDown():
    player.speed = 12
    player.setheading(270)
    player.fd(10)

def moveUp():
    player.speed = 12
    player.setheading(90)
    player.fd(10)

#START BUTTON
def runTheProgram():
    mainMenu.destroy()
    player = turtle.Turtle()
    player.speed(0)
    player.penup()
    player.shape('triangle')
    player.color('blue')
    player.setheading(90)
    player.setpos(0, -500)

    turle.listen()
    turtle.onkey(moveDown, "Down")
    turtle.onkey(moveUp, "Up")

    turtle.done()


#EXIT BUTTON
def close():
    exit()

def buy():
    shopWindow = Tk()
    mainMenu.destroy()


buttonExit=Button(mainMenu, justify = LEFT, command = close)
photobuttonExit=PhotoImage(file="buttonExit.gif")
buttonExit.config(image=photobuttonExit,width="90",height="50")
buttonExit.pack(side=BOTTOM)

buttonShop=Button(mainMenu, justify = LEFT, command = buy)
photobuttonShop=PhotoImage(file="buttonShop.gif")
buttonShop.config(image=photobuttonShop,width="90",height="50")
buttonShop.pack(side=BOTTOM)

buttonStart=Button(mainMenu, justify = LEFT, command = runTheProgram)
photo=PhotoImage(file="buttonStart.gif")
buttonStart.config(image=photo,width="90",height="50")
buttonStart.pack(side=BOTTOM)

mainMenu.mainloop()