from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Widget Practice")

def b1(*args):
    print("button 1")

# first frame, goes on top
frame1 = ttk.Frame(root)
frame1.grid(column=0, row=0)

# access the button's text, as well as change it. can be done before it is placed on the grid
button1 = ttk.Button(frame1, text="First Button", command=)
button1["text"] = "New text"
button1.grid(column=0, row=1)

# second frame, goes below first
frame2 = ttk.Frame(root)
frame2.grid(column=0, row=1)

button2 = ttk.Button(frame2, text="Second Button")
button2.grid(column=0, row=0)

for c in root.winfo_children():
    print(c.winfo_name())

root.mainloop()
