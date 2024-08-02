from tkinter import *
#python image library(PIL)->old module for importing images
from PIL import ImageTk,Image#now we use pillow
root=Tk()
root.title('Hello!!')
root.iconbitmap("py.ico")
#tkinter has built-in system for images(supports only 2 types:GIF,PNM)
my_img=ImageTk.PhotoImage(Image.open("images/py.png"))
mylabel=Label(image=my_img)
mylabel.pack()

button_quit=Button(root,text="Exit",command=root.quit)
button_quit.pack()
root.mainloop()