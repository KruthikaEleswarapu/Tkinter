import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

def resize_image(event):
    global img_resized, img_tk
    # Update the window to ensure its size is up-to-date
    root.update_idletasks()
    # Get the new size of the window
    new_width = root.winfo_width()
    new_height = root.winfo_height()
    
    # Resize the image to fit the new window size
    img_resized = img.resize((new_width, new_height), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img_resized)
    canvas.itemconfig(image_item, image=img_tk)

root = tk.Tk()
root.title("Background Image with Text")

# Load the original image
img = Image.open("img.png")

# Get the initial size of the screen
initial_width, initial_height = root.winfo_screenwidth(), root.winfo_screenheight()

# Resize the image to fit the initial screen size
img_resized = img.resize((initial_width, initial_height), Image.ANTIALIAS)
img_tk = ImageTk.PhotoImage(img_resized)

# Create a canvas with the initial image
canvas = tk.Canvas(root, width=initial_width, height=initial_height)
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)
canvas.pack(fill=tk.BOTH, expand=True)

# Add text on top of the image
text = "Hello, World!"
canvas.create_text(initial_width // 2, initial_height // 2, text=text, font=("Helvetica", 24), fill="white")

# Bind the resize event to the resize_image function
root.bind("<Configure>", resize_image)

root.mainloop()
