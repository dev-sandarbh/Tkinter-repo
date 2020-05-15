# first things first! Import tkinter
import tkinter
# make an object of tkinter class
root = tkinter.Tk()

# defining the font-style for our button
fontStyle = ("Helvetica",20,"bold")

# let us make a label to define the options we use in our button
l = tkinter.Label(root, text="Button with font-style, fg, bg, padding, width, height, activebackground and activeforeground as well!")
l.pack()

# define the btnClicked function here! 
def btnClicked():
    ''' this button is invoked/called every single time the button is clicked!'''
    print("Button has been Clicked!")

# make an object of Button class defined in tkinter module
btn1 = tkinter.Button(root,text="Click Me!!", font=fontStyle, fg="yellow",bg="red",padx=10, pady=10, width=20, height=5, activeforeground="white", activebackground="brown", command=btnClicked)
# pack that button
btn1.pack()

# define the infinite loop
root.mainloop()

''' 
Button Object takes a number of keyword arguments such as activebackground, activeforeground, background, borderwidth, cursor, disabledforeground, font, foreground, padx, pady, relief, text, textvariable, command, height, state, width. 

We will explore most of these options/arguments one by one.

Also we can bind our button to make a certain action whenever it is clicked either by using lambda functions or tje keyword argument command options!.

Here is a list of available cursor options in tkinter:-
"arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart",
"man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan",
"star", "target", "tcross", "trek", "watch"!

'''