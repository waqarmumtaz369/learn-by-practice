# Frame widgets are important for organizing the layout of your widgets in an application.
import tkinter as tk

window = tk.Tk()

# Create two frames
frame_a = tk.Frame()
frame_b = tk.Frame()

# Add a label in frame_a
label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

# Add a label in frame_b
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Add the frames in Window in order
frame_a.pack()
frame_b.pack()

# Frames can have different border types called as relief
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

# relief_name is the key in above list and relief is the value 
for relief_name, relief in border_effects.items():
    # Create a frame in every loop iteration
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    # 
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

'''
tk.Label(text="Hello, Tkinter").pack()      # Call pack directly on a widget
'''
window.mainloop()