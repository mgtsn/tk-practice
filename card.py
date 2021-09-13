from tkinter import *
from tkinter import ttk

ELEMENTS = ["F", "A", "W", "E"]


class Card:
    def add_buttons(self):
        count = 0
        for i in range(2):
            for j in range(2):
                ttk.Button(self.face, text=ELEMENTS[count]).grid(row=i, column=j)
                count += 1

    def __init__(self, card_parent) -> None:
        self.face = ttk.Frame(card_parent, padding=10)
        self.add_buttons()
