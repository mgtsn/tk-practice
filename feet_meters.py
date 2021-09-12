from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        val = float(feet.get())
        meters.set(round(0.3408 * val, 2))
    except ValueError:
        pass


root = Tk()
root.title("FTM Calculator")

frame = ttk.Frame(root, padding="3 3 12 12")
frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


feet = StringVar()
feet_entry = ttk.Entry(frame, width=8, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Label(frame, text="Feet").grid(column=3, row=1, sticky=W)

meters = StringVar()
ttk.Label(frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Label(frame, text="Meters").grid(column=3, row=2, sticky=W)

ttk.Button(frame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=E)

for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)
feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
