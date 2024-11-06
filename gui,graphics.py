import tkinter as tk
from tkinter import ttk

# Function to handle drawing based on selected shape
def draw_shape(event):
    x1, y1 = event.x - 30, event.y - 30  # Top-left corner
    x2, y2 = event.x + 30, event.y + 30  # Bottom-right corner
    
    if selected_shape.get() == "Rectangle":
        canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
    elif selected_shape.get() == "Circle":
        canvas.create_oval(x1, y1, x2, y2, fill="green")
    elif selected_shape.get() == "Line":
        canvas.create_line(x1, y1, x2, y2, fill="red", width=3)

# Set up the main application window
window = tk.Tk()
window.title("Interactive GUI Graphics")
window.geometry("500x500")

# Create a canvas widget for drawing
canvas = tk.Canvas(window, width=400, height=400, bg="white")
canvas.pack(pady=20)

# Variable to store the selected shape
selected_shape = tk.StringVar(value="Rectangle")

# Create radio buttons to select the drawing shape
shapes_frame = ttk.Frame(window)
shapes_frame.pack()

ttk.Radiobutton(shapes_frame, text="Rectangle", variable=selected_shape, value="Rectangle").pack(side="left")
ttk.Radiobutton(shapes_frame, text="Circle", variable=selected_shape, value="Circle").pack(side="left")
ttk.Radiobutton(shapes_frame, text="Line", variable=selected_shape, value="Line").pack(side="left")

# Bind mouse click event to drawing function
canvas.bind("<Button-1>", draw_shape)

# Start the GUI event loop
window.mainloop()
