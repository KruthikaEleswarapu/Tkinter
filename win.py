'''from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Old window")

top=Toplevel()
top.title("New")
img=ImageTk.PhotoImage(Image.open("images/py.png"))
lbl=Label(top,text="New Window").pack()
lbl1=Label(top,image=img).pack()
mainloop()
'''

#if u want window to open only when a dropdown box or something:
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Old window")

#the image wouldn't be dispalyed as it is local variable and python dumps it as garbage collection so we have to use global
def open():
    global img
    top=Toplevel()
    top.title("New")
    img=ImageTk.PhotoImage(Image.open("images/py.png"))
    lbl=Label(top,text="New Window").pack()
    lbl1=Label(top,image=img).pack()
    #to close second window
    btn2=Button(top,text="Close",command=top.destroy).pack()
btn=Button(root,text="Open seecond window",command=open).pack()
mainloop()
#'''
