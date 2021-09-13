from tkinter import *
from tkinter import ttk


def card(card_parent):
    for i in range(2):
        for j in range(2):
            ttk.Button(card_parent, text="New Button").grid(row=i, column=j)


def button_test(*args):
    print(f"Pushed button {args[0]}")


root = Tk()
root.title("Testing")

frame1 = ttk.Frame(root, padding="10")
card(frame1)
frame1.grid(row=0, column=0)

frame2 = ttk.Frame(root, padding="10")
card(frame2)
frame2.grid(row=1, column=0)

# for i in range(5):
#     ttk.Button(frame1, text=f"Button {i+1}", command=button_test(i + 1)).grid(
#         row=0, column=i
#     )


# for i in range(5):
#     ttk.Button(frame2, text=f"Button {i+1}", command=button_test(i + 1)).grid(
#         row=0, column=i
#     )


root.mainloop()
