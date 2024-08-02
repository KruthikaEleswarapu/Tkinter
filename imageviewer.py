from tkinter import *
#python image library(PIL)->old module for importing images
from PIL import ImageTk,Image#now we use pillow
root=Tk()
#image viewer
img1=ImageTk.PhotoImage(Image.open("images/py.png"))
img2=ImageTk.PhotoImage(Image.open("images/c++.png"))
img3=ImageTk.PhotoImage(Image.open("images/c.png"))
img4=ImageTk.PhotoImage(Image.open("images/java.png"))

image_list=[img1,img2,img3,img4]
mylabel=Label(image=img1)
mylabel.grid(row=0,column=0,columnspan=3)

def forward(img_no):
    global mylabel
    global button_forward
    global button_back
    mylabel.grid_forget()
    mylabel=Label(image=image_list[img_no])
    button_forward=Button(root,text=">",command=lambda: forward(img_no+1)).grid(row=1,column=2)
    button_back=Button(root,text="<",command=lambda: back(img_no-1)).grid(row=1,column=0)
    if img_no==4:
        button_forward=Button(root,text=">",state=DISABLED)

    mylabel.grid(row=0,column=0,columnspan=3)
def back(img_no):
    global mylabel
    global button_forward
    global button_back
    mylabel.grid_forget()
    mylabel=Label(image=image_list[img_no])
    button_forward=Button(root,text=">",command=lambda: forward(img_no+1)).grid(row=1,column=2)
    button_back=Button(root,text="<",command=lambda: back(img_no-1)).grid(row=1,column=0)
    if img_no==1:
        button_forward=Button(root,text=">",state=DISABLED)
    mylabel.grid(row=0,column=0,columnspan=3)

button_back=Button(root,text="<",command=back,state=DISABLED).grid(row=1,column=0)
button_forward=Button(root,text=">",command=lambda: forward(2)).grid(row=1,column=2)
button_quit=Button(root,text="Exit",command=root.quit).grid(row=1,column=1)
root.mainloop()