from tkinter import *
root=Tk()
def Click():
    myLabel=Label(root,text="I clicked!!")
    myLabel.pack()

myButton=Button(root,text="Click me")#it is clickable but does nothing
myButton=Button(root,text="Click me",command=Click)
#myButton=Button(root,text="Click me",command=Click()) this prints the text without us clicking the button yet
#myButton=Button(root,text="Click me",state=DISABLED,padx=50,pady=50,fg="blue",bg="#000000")make the button disabled, increases button size in x dimension,increases button size in y dimension,foreground color,background color
#for colors we can use hex values as well
myButton.pack()
root.mainloop()