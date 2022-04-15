import sys
from tkinter import *
from pathlib import PurePath  # chemin de répertoire avec gestion multiplatforme
from subprocess import Popen  # lancer d'autres programmes

window=Tk()

window.title("Running Python Script")
window.geometry('720x1920')


def runsnake():
    # créer le chemin du répertoire de travail du jeu (ici ../snake ou ..\\snake avec windows)
    p = PurePath("..", "snake")
    # lancer le jeu avec le bon chemin (../snake/snake ou..\\snake\\snake) et dans le bon repertoire de travail (cwd = current working directory)
    p = Popen(str(p / PurePath("snake")), cwd=p)
    # p.wait()  # on peut attendre qu'il se termine... ou pas.

def rundemineur():
    p = PurePath("..", "demineur")
    p = Popen(str(p / PurePath("demineur")), cwd=p)
    # p.wait()  # on peut attendre qu'il se termine... ou pas.

def runpong():
    p = PurePath("..", "pong")
    p = Popen(str(p / PurePath("pong")), cwd=p)
    # p.wait()  # on peut attendre qu'il se termine... ou pas.

snake_img = PhotoImage(file='snake.png')
demineur_img = PhotoImage(file='demineur.png')
pong = PhotoImage(file='téléchargement.png')

button1 = Button(window, image=snake_img, command=runsnake,borderwidth =10)
button1.pack(pady= 20)
button2 = Button(window, image=demineur_img, command=rundemineur ,borderwidth =10)
button2.pack(pady= 20)
button3 = Button(window, image=pong, command=runpong,borderwidth =10)
button3.pack(pady= 20)
window.mainloop()
