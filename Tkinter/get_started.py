import tkinter as tk
# import tkinter.ttk as ttk #for themed tkinter widgets

# Window is the main container to hold the other UI elements called widgets in tkinter
window = tk.Tk()

'''
Each widget in Tkinter is defined by a class. Here are some of the widgets:

Class |	Description
----- | -----------
Label |	A widget used to display text on the screen
Button|	A button that can contain text and can perform an action when clicked
Entry |	A text entry widget that allows only a single line of text
Text  |	A text entry widget that allows multiline text entry
Frame |	A rectangular region used to group related widgets or provide padding between widgets
'''
# Add a label widget to display some text on UI
greeting = tk.Label(text="Hello, Tkinter")

# Add a label with modified UI
'''
Different color names like red,orange, yellow, green, purple are also supported an dthe hex codes are also supported like HTML
Get more HTML Hex Codes here: https://htmlcolorcodes.com/
'''
label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="#34A2FE"  # Set the background color to black
)

# Shorter form 
#label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")

label2 = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=10, #measured in text units
    height=10 #measured in text units
)

# Buttons are just like labels but are clickable 
button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

# Entry widget is for onle liner or short text inputs like name and email
# Other properties are similar to teh label and button
entry = tk.Entry(fg="yellow", bg="blue", width=50)

# sample usage of entry with a label
name_label = tk.Label(text="Name")
name_entry = tk.Entry()

# get() function helps us getting the value of entry text entered by the user for further processing 
name = entry.get()

# delete() function is used to delete a character ir a range  of charcaters from the Entry
entry.delete(0)
entry.delete(0, 4) #index 4 is not included and orks just like string slicing
entry.delete(0, tk.END) #tk.END will delete the text till the end 

# Similarly, we can also insert the text in Entry widget at the index position
entry.insert(0, "Python")

# Add the widgets to window using pack. It centers the widgets as per its behaviour
greeting.pack()
label.pack()
label2.pack()
button.pack()
entry.pack()

name_label.pack()
name_entry.pack()

# Start the Tkinter event loop. It will manages the interactions of all the widgets and act accordingly
window.mainloop()