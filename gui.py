import os
import main as MLD
import src.download_path as download_path
import src.most_recent as most_recent
import src.relocate as relocate
from tkinter import *

# import filedialog module
from tkinter import filedialog

WINDOW_WIDTH = "600"
WINDOW_HEIGHT = "400"

DIR = ""

def all(target_dir):
  dp = download_path.find()
  mr = most_recent.find(dp)
  relocate.move(mr,dp,target_dir)

# Function for opening the 
# file explorer window
def browseFiles():
    filename = filedialog.askdirectory(initialdir = "/", title = "Select Directory")
    label_file_explorer.configure(text="File Opened: " + filename)
    return filename
     
	
																								
# Create the root window
window = Tk()

# Set window title
window.title('Move Latest Download')

# Set window size
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window, text = "Move Latest Download", width = 0, height = 4, fg = "blue")
	
button_explore = Button(window, text = "Browse Files", command = browseFiles) 

button_one = Button(window, text = "MOVE Most Recent Download",	command = exit) 
button_all = Button(window, text = "MOVE All", command = MLD.all(label_file_explorer.nametowidget)) 
button_undo = Button(window, text = "Undo",	command = exit) 
button_redo = Button(window, text = "Redo",	command = exit) 

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 0, row = 1)

button_explore.grid(column = 0, row = 2)

button_one.grid(column = 0,row = 3)
button_all.grid(column = 1,row = 3)
button_undo.grid(column = 2,row = 3)
button_redo.grid(column = 3,row = 3)

# Let the window wait for any events
window.mainloop()
