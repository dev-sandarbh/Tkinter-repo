import tkinter

root = tkinter.Tk()
fontStyle = ('Arial',20,'bold')

# heading label
heading = tkinter.Label(root, text="Welcome to Entry Widget Tutorial", padx=15, pady=15, font = fontStyle, foreground='#e600e6', background='#33ff33')
heading.pack(side=tkinter.TOP)

nameLabel = tkinter.Label(root,text="First Name: ", padx=10, pady=10, background='#ffff66', foreground='#e600e6')
nameLabel.pack(side=tkinter.LEFT)

entryField_1 = tkinter.Entry(root, width=30, foreground='#e600e6', background='#33ff33')
entryField_1.pack(side=tkinter.LEFT)

root.configure(background='#ffff66')
root.mainloop()