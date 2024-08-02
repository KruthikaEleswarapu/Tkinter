from tkinter import *

root = Tk()
root.title("Simple Calculator")

# Enable resizing for the calculator window
root.resizable(True, True)

# Set up an Entry widget
e = Entry(root, width=40, borderwidth=5, font=('Arial', 16), justify='right')
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define a function to handle button clicks
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

# Define a function to clear the entry
def button_clear():
    e.delete(0, END)

# Define a function to evaluate the expression
def button_equal():
    try:
        result = eval(e.get())
        e.delete(0, END)
        e.insert(0, str(result))
    except Exception as e:
        e.delete(0, END)
        e.insert(0, "Error")

# Define buttons for basic arithmetic operations
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]

# Create buttons and attach functions
for i in range(4):
    for j in range(4):
        if buttons[i][j] == '=':
            btn = Button(root, text=buttons[i][j], padx=40, pady=20, font=('Arial', 16), bg='orange', command=button_equal)
        else:
            btn = Button(root, text=buttons[i][j], padx=40, pady=20, font=('Arial', 16), command=lambda num=buttons[i][j]: button_click(num))
        btn.grid(row=i+1, column=j, padx=5, pady=5, sticky='nsew')

# Configure row and column weights for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
