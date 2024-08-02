from tkinter import *
root=Tk()
e=Entry(root)
e.insert(0,"Enter ur name:")#enters a default value onto the textbox
#e.get():to do somrthing with the text entered
#e=Entry(root,width=50,fg="blue",bg="pink",borderwidth=5)inreases the width,increases borderwidth
#it prints whatever u have written in the text box followed by clicking the button
def Click():
    #we can also do
    #hello="Hello "+e.get()
    #myLabel=Label(root,text=hello)
    myLabel=Label(root,text=e.get())
    myLabel.pack()
myButton=Button(root,text="Click me",command=Click)
myButton.pack()
e.pack()
root.mainloop()