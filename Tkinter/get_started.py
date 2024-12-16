import tkinter as tk

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

# Add the label to window using pack
greeting.pack()

# Start the Tkinter event loop
window.mainloop()