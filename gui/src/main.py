import tkinter as tk

# Initialize the main window
app = tk.Tk()
app.title("WSI Viewer")

# Set the window size
app.geometry("800x600")

# Create the left column for the menu
menu_bar = tk.Frame(app, bg='white', width=200)
menu_bar.pack(side=tk.LEFT, fill=tk.Y)

# Add buttons to the menu
open_project_button = tk.Button(menu_bar, text="Open New Project")
open_project_button.pack(fill=tk.X)

open_folder_button = tk.Button(menu_bar, text="Open Folder")
open_folder_button.pack(fill=tk.X)

# Create the main area
main_area = tk.Frame(app, bg='grey')
main_area.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Start the GUI event loop
app.mainloop()

