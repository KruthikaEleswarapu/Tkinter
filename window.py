'''from tkinter import *

root=Tk()#should be the first line whatever u do
myLabel=Label(root,text="Hello World!!")#creating a label Widget
myLabel.pack()#Shoving it onto the screen, it resizes if we minimise or maximise the window
#crete an event loop(constant loop)
root.mainloop()'''

''' Using Grid System'''
from tkinter import *

root=Tk()
myLabel1=Label(root,text="Hello World!!")
myLabel2=Label(root,text="I'm Kruthika")
#since python is OOP so we can do it as:
#myLabel2=Label(root,text="I'm Kruthika").grid(row=0,column=1)
#grid has relative positioning
myLabel1.grid(row=0,column=0)
myLabel2.grid(row=0,column=1)#resizing doesn't work i.e.,no change in the appearance of text when minimising or maximising window 
#myLabel2.grid(row=1,column=1)
#myLabel2.grid(row=1,column=0)
root.mainloop()

