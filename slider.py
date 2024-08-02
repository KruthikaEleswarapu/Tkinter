from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.geometry("400x400") # gives a window of that size
def slide():
    label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+str(vertical.get()))
vertical=Scale(root,from_=0,to=250)
vertical.pack()
horizontal=Scale(root,from_=0,to=250,orient=HORIZONTAL)
label=Label(root,text=horizontal.get())
horizontal.pack()

btn=Button(root,text="Click me",command=slide).pack()
root.mainloop()