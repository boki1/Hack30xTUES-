from tkinter import *

#Main menu
#1) Start button

mainMenu = Tk()

def runTheProgram():
    mainWindow = Tk()
    mainMenu.destroy()


startButton = Button(mainMenu, text = 'START', command = runTheProgram)
startButton.pack()

#2) Shop button

def buy():
    pass

shopButton = Button(mainMenu, text = 'SHOP', command = buy)
shopButton.pack()

def close():
    exit()

closeButton = Button(mainMenu, text = 'CLOSE THE GAME', command = close)
closeButton.pack()



mainMenu.mainloop()