from tkinter import *

master = Tk()

three=Button(master, justify = LEFT)
photoThree=PhotoImage(file="buttonExit.gif")
three.config(image=photoThree,width="90",height="50")
three.pack(side=BOTTOM)

two=Button(master, justify = LEFT)
photoTwo=PhotoImage(file="buttonShop.gif")
two.config(image=photoTwo,width="90",height="50")
two.pack(side=BOTTOM)

one=Button(master, justify = LEFT)
photo=PhotoImage(file="buttonStart.gif")
one.config(image=photo,width="90",height="50")
one.pack(side=BOTTOM)

master.mainloop()


