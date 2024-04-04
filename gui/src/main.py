import tkinter as tk
from tkinter import filedialog
import os

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename()
    # Here you can add the logic to load and display the file
    print(f"File selected: {file_path}")

# Function to open a project (this can be elaborated based on project requirements)
def open_project():
    print("Open Project functionality here")

# Initialize the main window
app = tk.Tk()
app.title("BmgPath - WSI Viewer")

# Set the window size
app.geometry("1200x800")

# Create the left column for the menu
menu_bar = tk.Frame(app, bg='white', width=200)
menu_bar.pack(side=tk.LEFT, fill=tk.Y)

# Add buttons to the menu
open_project_button = tk.Button(menu_bar, text="Open New Project", command=open_project)
open_project_button.pack(fill=tk.X)

open_file_button = tk.Button(menu_bar, text="Load WSI", command=open_file)
open_file_button.pack(fill=tk.X)

# Add more buttons as needed for other functionalities
# For example, Load Model, Predict, etc.

# Create the main area for image display and other interactions
main_area = tk.Frame(app, bg='grey')
main_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Start the GUI event loop
app.mainloop()

