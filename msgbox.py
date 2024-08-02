from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("Message Box")

#types of boxes: showinfo, showwarning, showerror, askquestion, asokcancel, askyesno
'''
def popup():
    messagebox.showinfo("Popup","Hello World")#puts text on screen showinfo(title,message)
Button(root,text="Popup",command=popup).pack()

'''
def popup():
    response=messagebox.askyesno("Popup","Hello World")#puts text on screen showinfo(title,message)
    Label(root,text=response).pack()
    if response==1:
        Label(root,text="Ok").pack()
    else:
        Label(root,text="No?").pack()

Button(root,text="Popup",command=popup).pack()
#'''


mainloop()