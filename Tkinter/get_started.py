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


'''
Some of the below modifications should work when triggerd like on a buton click. 
It should be covered later in the learning process
'''
# get() function helps us getting the value of entry text entered by the user for further processing 
name = entry.get()

# delete() function is used to delete a character ir a range  of charcaters from the Entry
entry.delete(0)
entry.delete(0, 4) #index 4 is not included and orks just like string slicing
entry.delete(0, tk.END) #tk.END will delete the text till the end 

# Similarly, we can also insert the text in Entry widget at the index position
entry.insert(0, "Python")

'''
Text is similar to the Entry having all supported functions but with a larger text
However, usage of get, delete, insert is little different. 
You have to assume a text box as a table (row, col) of characters for better understanding the modification functions.
'''
text_label = tk.Label(text="This is a Text Box Below!")
text_box = tk.Text()

# Here are some usage of the Text widget modifictions
'''
#===============================GET===================================
text_box.get()                          #will return error
text_box.get("1.0")                     #return one character at row 1 and col 0
text_box.get("1.0", "1.5")              #return a text starting from first character of first row till 5th character of first row
text_box.get("1.0", tk.END)             #return all the text from the text box
#===============================DELETE================================
text_box.delete("1.0", tk.END)          #delete works exactly like get
#===============================INSERT================================
text_box.insert("1.0", "Hello")         #insert also works similar way
                                        #   This inserts the word Hello at the beginning of the text box, 
                                        #   using the same "<line>.<column>" format used by .get() to specify the insertion position
text_box.insert(tk.END, "Put me at the end!")
text_box.insert(tk.END, "\nPut me on a new line!")      #\n is also a character 

.insert() will do one of two things:
#Insert text at the specified position if there’s already text at or after that position.
#Append text to the specified line if the character number is greater than the index of the last character in the text box.



'''

# Add the widgets to window using pack. It centers the widgets as per its behaviour
greeting.pack()
label.pack()
label2.pack()

button.pack()

entry.pack()

name_label.pack()
name_entry.pack()

text_label.pack()
text_box.pack()

# Start the Tkinter event loop. It will manages the interactions of all the widgets and act accordingly
window.mainloop()