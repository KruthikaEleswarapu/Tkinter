'''from tkinter import *
from PIL import ImageTk,Image
root=Tk()
# tkinter variables are different than normal py vars
r=IntVar() # this is used to keep track of the changes to the variable
# for string we use StringVar()
#we could use r.set("2") to set to option 2 prior if we didn't use r.set it wouldnt be set to any 

def clicked(value):
    myLabel=Label(root,text=value).pack()

Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()
myLabel=Label(root,text=r.get()).pack()
#we can do to button as well
root.mainloop()

'''#we can use loops to create a number of radiobuttons for this we use list
from tkinter import *
from PIL import ImageTk,Image
root=Tk()

MODES=[("pepperoni",1),("cheese",2),("mushroom",3),("jalpaneos",4)] #(option name visible on form,value assigned to it)
pizza=StringVar()
pizza.set("1")

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack()#here they all are centered
    #to put them to left we use .pack(anchor=W)

def clicked(value):
    myLabel=Label(root,text=value).pack()

b=Button(root,text="Click", command=lambda: clicked(pizza.get())).pack()
 
root.mainloop()
