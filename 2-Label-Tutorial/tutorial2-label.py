''' TKinter comes with some predefined gui widgets such as button,entry field, labels, textbox, etc and many more! So let us work with them one by one.'''
import tkinter
root = tkinter.Tk() #made an object of tkinter module

# font-family
font_family = ('Helvetica',20,'bold')


# let's make a label first
label_1 = tkinter.Label(root,text="Hi, It's me Label_1", padx=15, pady=15, bg="cyan", fg="red", font=font_family, borderwidth=5,relief='raised')
label_1.pack()
root.mainloop()

''' Now let us understand how it works? 
step 1-> after importing tkinter lib we made an object of the tkinter class named as root.
step 2-> now let us make an object of label class which is present inside the tkinter module to get it working. Name of the object here is "label_1" of the "Label" class.
step 3-> label takes two main and mandatory arguments these are the name of the parent window/widget and the text you want on that label.
step 4-> basic syntax of the label becomes as shown above label_obj = Label(parent_window,text="Dummy text here")
step 5-> now we need to pack it onto the screen to get it on the screen. We will learn about this "pack" when we will talk about the grid managers!But for now just remember it as a function which puts your output on the screen.
step 6-> apply the infinite loop by root.mainloop()

And that's it. YOu have your label-code ready to be executed.

Now we can add some more arguments to make our label more impressive and attractive. Such as background-color, foreground-color, padding (on x and y), activeforeground, activebackground,font-family, font-size, border style or relief, borderwidth,etc. Let us make a program using that as well!
'''