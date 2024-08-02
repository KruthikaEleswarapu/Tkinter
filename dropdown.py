from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry("400x400")
clicked=StringVar()

options=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
clicked.set(options[0])
drop=OptionMenu(root,clicked,*options).pack()
def show():
    label=Label(root,text=clicked.get()).pack()
btn=Button(root,text="Show",command=show).pack()

#drop=OptionMenu(root,clicked,"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
#drop.pack()

#clicked.set("Monday")#sets default value as Monday
#root.mainloop()