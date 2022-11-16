from turtle import *
from tkinter import *

from PIL import ImageTk, Image

# create screen
window = Tk()
window.title("LightGame")
window.configure(width=800, height=450)

img =Image.open('resources/background.jpg')
bg = ImageTk.PhotoImage(img)

# move window center
winWidth = window.winfo_reqwidth()
winwHeight = window.winfo_reqheight()
posRight = int(window.winfo_screenwidth() / 2 - winWidth / 2)
posDown = int(window.winfo_screenheight() / 2 - winwHeight / 2)
window.geometry("+{}+{}".format(posRight, posDown))


# code of games or path to files(in the next version)
def game1():
    print("Game1")


def game2():
    print("Game2")


def game3():
    print("Game3")


def game4():
    print("Game4")


def game5():
    print("Game5")


Label(window, image=bg).place(x = -2,y = -2)


Button(window, text='Game1!', command=game1, height= 4, width=9).place(x=40, y=120)

Button(window, text='Game2!', command=game2, height= 4, width=9).place(x=190, y=120)

Button(window, text='Game3!', command=game3, height= 4, width=9).place(x=340, y=120)

Button(window, text='Game4!', command=game4, height= 4, width=9).place(x=490, y=120)

Button(window, text='Game5!', command=game5, height= 4, width=9).place(x=640, y=120)

Button(window, text='Exit.', command=exit).place(x=720, y=410)


welcome_text="Привіт!\nВ цьому застосунку у Вас є вибір з 5 простих, добре знайомих Вам ігор. Ви можете обрати будь-яку з них!"
Label(master=window, text=welcome_text, bg='#2485e0', width=80, bd=15).place(x=10, y=10)


window.mainloop()
