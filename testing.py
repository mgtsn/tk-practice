from tkinter import *
from tkinter import ttk
from card import Card


def card(card_parent):
    for i in range(2):
        for j in range(2):
            ttk.Button(card_parent, text="New Button").grid(row=i, column=j)


def button_test(*args):
    print(f"Pushed button {args[0]}")


root = Tk()
root.title("Testing")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

player1 = ttk.Frame(root, padding=10)
player2 = ttk.Frame(root, padding=10)

for i in range(4):
    Card(player1).face.grid(row=0, column=i)
    Card(player2).face.grid(row=0, column=i)

player1.grid(row=0, column=0, sticky=N)
player2.grid(row=1, column=0, sticky=S)

root.mainloop()
