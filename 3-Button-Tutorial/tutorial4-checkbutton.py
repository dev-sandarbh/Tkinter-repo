# first of all
import tkinter

# make an object of Tk() class
root = tkinter.Tk()

# defining the font tuple for the checkbutton label
fontStyle = ('Helvetica',20,'bold')

# make an object of checkbutton class;; when you will hover over that button you will see a star!
chkBtn1 = tkinter.Checkbutton(root, text="Hi, I'm a CheckButton!", font=fontStyle, fg="blue", bg="yellow", bd=2, activebackground="green", activeforeground="white", cursor="star")

# pack that checkbutton
chkBtn1.pack()

# start the infinte loop
root.mainloop()

''' CheckButton can accept following items as argument(These are most oftenly used): 
activebackground, activeforeground, background, bd, bg, borderwidth, command, cursor,
disabledforeground, fg, font, foreground, height, image, justify, padx, pady, relief, state,
text, textvariable, underline, variable, width.

Here is a list of available cursor options in tkinter:-
"arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart",
"man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan",
"star", "target", "tcross", "trek", "watch"!

Remember that a checkbutton is used to select only one option out of some given number of options. So you can select only one check value at a time. 
'''