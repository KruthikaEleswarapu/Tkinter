from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry("400x400")

var=StringVar()
c=Checkbutton(root, text="CheckBox",variable=var,onvalue="Checkbox",offvalue="Nothing selected")
c.deselect()#to prevent default selection
c.pack()

def show():
    label=Label(root,text=var.get()).pack()

btn=Button(root,text="Selection:",command=show).pack()

root.mainloop()