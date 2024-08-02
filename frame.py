from tkinter import *
from PIL import ImageTk,Image
#in window we have to use pack() or grid for all the buttons not both(for label we used pack() => we have to use pack() for button as well) but for frame we can use both
root=Tk()
root.title("Frame")
frame=LabelFrame(root,text="This is frame",padx=5,pady=5) #this padding increase the spacing in the window --> inside the frame
frame.pack(padx=10,pady=10) #this padding increase the size of the windowi.e., inc the space b/w frame and window --> outside the frame

b1=Button(frame,text="Click1")
b1.grid(row=0,column=0)

b2=Button(frame,text="Click2")
b2.grid(row=1,column=0)

root.mainloop()