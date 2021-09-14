from tkinter import *
from tkinter import ttk

from item import Item



def task_label(*args):
    ttk.Label(frame, text=task_name.get()).grid(row=2, column=0)

root = Tk()


frame = ttk.Frame(root, padding="10")
frame.grid(column=0, row=0)

task_name = StringVar()
task_name_entry = ttk.Entry(frame, textvariable=task_name)
task_name_entry.grid(column=0, row=0)

ttk.Button(frame, text="Add Task", command=task_label).grid(column=1, row=0)

root.mainloop()