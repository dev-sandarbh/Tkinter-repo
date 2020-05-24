import tkinter

root = tkinter.Tk()
fontStyle = ('Arial',20,'bold')

# variable for storing our name that we will get from our entry field
_name = tkinter.StringVar()
_name.set("A PLACEHOLDER NAME....")

# function for printing the name entered by user on the output screen in editor
def printName():
    _f = _name.get()
    print("Your Name is: "+_f)

# heading label
heading = tkinter.Label(root, text="Welcome to Entry Widget Tutorial 2", padx=15, pady=15, font = fontStyle, foreground='#e600e6', background='#33ff33')
heading.pack(side=tkinter.TOP)

# label for name of person
nameLabel = tkinter.Label(root,text="Your Name: ", padx=10, pady=10, background='#ffff66', foreground='#e600e6')
nameLabel.pack(side=tkinter.LEFT)

# entry field for getting that name
entryField_1 = tkinter.Entry(root, textvariable=_name, width=30, foreground='#e600e6', background='#33ff33')
entryField_1.pack(side=tkinter.LEFT)

# a button for printing that name
_btn = tkinter.Button(root, text="Click Me to get name", command=printName, foreground="#C4E538", background="#EE5A24", activeforeground="#C4E538", activebackground="#EE5A24")
_btn.pack(side=tkinter.BOTTOM, expand=tkinter.YES)

root.configure(background='#ffff66')
root.mainloop()