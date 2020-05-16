# first things first
import tkinter

# make an object of Tk() class
root = tkinter.Tk()

# defining the font tuple for the radiobutton label
fontStyle = ('Helvetica',20,'bold')

# to make our radiobutton fully working it is necessary for us to define a variable which will be attached to the radio buttons
v = tkinter.IntVar()

def getValue():
    ''' this function help us getting the value associated with the specific radio button. And thereby prints the information on the label.'''
    _text = "You selected the option "+str(v.get())
    label.config(text=_text)

# make an object of radiobutton class;; when you will hover over that button you will see a plus on that label and button!

# button 1
_RadioBtn1 = tkinter.Radiobutton(root, text="Hi, I'm a RadioButton 1!", font=fontStyle, variable=v, value=1, cursor="plus", command=getValue)

# button 2
_RadioBtn2 = tkinter.Radiobutton(root, text="Hi, I'm a RadioButton 2!", font=fontStyle, variable=v, value=2, cursor="plus", command=getValue)

# button 3
_RadioBtn3 = tkinter.Radiobutton(root, text="Hi, I'm a RadioButton 3!", font=fontStyle, variable=v, value=3, cursor="plus", command=getValue)

# button 4
_RadioBtn4 = tkinter.Radiobutton(root, text="Hi, I'm a RadioButton 4!", font=fontStyle, variable=v, value=4, cursor="plus", command=getValue)

# pack all radiobuttons
_RadioBtn1.pack()
_RadioBtn2.pack()
_RadioBtn3.pack()
_RadioBtn4.pack()

# define a label to be placed after selecting an option
label = tkinter.Label(root)
label.pack()

# start the infinte loop
root.mainloop()

''' RadioButton can accept following items as argument(These are most oftenly used): 
activebackground, activeforeground, background, bd, bg, borderwidth, command, cursor,
disabledforeground, fg, font, foreground, height, image, justify, padx, pady, relief, state,
text, textvariable, underline, variable, width.

Here is a list of available cursor options in tkinter:-
"arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart",
"man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan",
"star", "target", "tcross", "trek", "watch"!

Remember that radiobutton alloes us to select a number of options from a given list of options.  
'''