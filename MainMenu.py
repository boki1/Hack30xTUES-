from tkinter import *
import turtle

#Main menu
#1) Start button

mainMenu = Tk()
isTheGameRunning = BooleanVar(value=True)

def runTheProgram():
    mainMenu.destroy()
    player = turtle.Turtle()
    player.speed(0)
    player.penup()
    player.shape('triangle')
    player.color('blue')
    player.setheading(90)

    playerspeed = 15

startButton = Button(mainMenu, text = 'START', command = runTheProgram)
startButton.pack()

#2) Shop button

def buy():
    shopWindow = Tk()
    mainMenu.destroy()
shopButton = Button(mainMenu, text = 'SHOP', command = buy)
shopButton.pack()

def close():
    exit()

closeButton = Button(mainMenu, text = 'CLOSE THE GAME', command = close)
closeButton.pack()


mainMenu.mainloop()