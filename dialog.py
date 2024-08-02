'''
#this opens file immediately
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
#to open a file we use filedialog

root=Tk()
#to get filelocation & name, wont open file
root.filename=filedialog.askopenfilename(initialdir="/Users/ASUS/Creative Cloud Files/Desktop/Tkinter",title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))# (which directory to start(what directory to show when box popsup), title, what type of files to be shown)
label=Label(root,text=root.filename).pack()
img=ImageTk.PhotoImage(Image.open(root.filename))
my_img=Label(image=img).pack()
root.mainloop()

'''
#this asks user to open file
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
def open():
    global img
    root.filename=filedialog.askopenfilename(initialdir="/Users/ASUS/Creative Cloud Files/Desktop/Tkinter",title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))
    label=Label(root,text=root.filename).pack()
    img=ImageTk.PhotoImage(Image.open(root.filename))
    my_img=Label(image=img).pack()

btn=Button(root,text="open file",command=open).pack()
root.mainloop()
#'''