import tkinter

root = tkinter.Tk()
fontStyle = ('Arial',20,'bold')
fontNoteStyle = ('Arial',12,'bold')
fontLabelStyle = ('Arial',12,'bold')
fontEntryStyle = ('Arial',12)
fontBtnStyle = ('Arial',15,'bold')

# defining variables to store the values of these variables
_name = tkinter.StringVar(root)
_email = tkinter.StringVar(root)
_contact = tkinter.StringVar(root)
_age = tkinter.StringVar(root)
_password = tkinter.StringVar(root)

def setPlaceholders():
    # setting placeholder values for every entry field
    _name.set("Your Name")
    _email.set("email@address.com")
    _contact.set("123456789")
    _age.set("100")

def delPlaceholders():
    # function for deleting the old values
    e_1.delete(0, tkinter.END)
    e_2.delete(0, tkinter.END)
    e_3.delete(0, tkinter.END)
    e_4.delete(0, tkinter.END)
    e_5.delete(0, tkinter.END)

def getData():
    # a function for accessing these values and getting them printed on the editor's output
    print("Data Entered is: ")
    # getting name
    print("Name of User: "+e_1.get())
    # getting email
    print("Email-ID of User: "+e_2.get())
    # getting age
    print("Age of User: "+e_3.get())
    # getting contact number
    print("Contact Number of User: "+e_4.get())
    print("We cannnot show a user's password. It is against our policy!!")
    print("####################Thanks for using our service###################")
    delPlaceholders()
    setPlaceholders()

# heading label
heading = tkinter.Label(root, text="Welcome to Entry Widget Tutorial", padx=15, pady=15, font = fontStyle, foreground='#e600e6', background='#33ff33')
heading.grid(row=0,columnspan=2)

# we will use GRID PACKAGING MANAGER in this program, so that we can conveniently place our widgets
# label for name of user
nameLabel = tkinter.Label(root,text="First Name: ", font=fontLabelStyle, padx=10, pady=10, background='#ffff66', foreground='#e600e6')
nameLabel.grid(row=1,column=0)

# label for user email address
emailLabel = tkinter.Label(root,text="Enter Email: ", font=fontLabelStyle, padx=10, pady=10, background='#ffff66', foreground='#e600e6')
emailLabel.grid(row=2,column=0)

# label for user age
ageLabel = tkinter.Label(root,text="Enter Your Age: ", font=fontLabelStyle, padx=10, pady=10, background='#ffff66', foreground='#e600e6')
ageLabel.grid(row=3,column=0)

# label for user contact number
conLabel = tkinter.Label(root,text="Enter Conatct No. : ", font=fontLabelStyle, padx=10, pady=10, background='#ffff66', foreground='#e600e6')
conLabel.grid(row=4,column=0)

# label for user password
passLabel = tkinter.Label(root,text="Enter Password: ", font=fontLabelStyle, padx=10, pady=10, background='#ffff66', foreground='#e600e6')
passLabel.grid(row=5,column=0)

#entry for name of user
e_1 = tkinter.Entry(root, textvariable=_name, width=30, font=fontEntryStyle, foreground='white', background='#4d004d')
e_1.grid(row=1,column=1)

#entry for email of user
e_2 = tkinter.Entry(root, textvariable=_email, width=30, font=fontEntryStyle, foreground='white', background='#4d004d')
e_2.grid(row=2,column=1)

#entry for age of user
e_3 = tkinter.Entry(root, textvariable=_age, width=30, font=fontEntryStyle, foreground='white', background='#4d004d')
e_3.grid(row=3,column=1)

#entry for contact number of user
e_4 = tkinter.Entry(root, textvariable=_contact, width=30, font=fontEntryStyle, foreground='white', background='#4d004d')
e_4.grid(row=4,column=1)

#entry for password of user
e_5 = tkinter.Entry(root, textvariable=_password, show="*", width=30, font=fontEntryStyle, foreground='white', background='#4d004d')
e_5.grid(row=5,column=1)

# a button to print all of the info
btnPrint = tkinter.Button(root, text="Click me to get output!", font=fontBtnStyle, pady=5, foreground="white", background="red", activeforeground="red", activebackground="white", command=getData)
btnPrint.grid(row=6,columnspan=2)

# noteLabel
_note = tkinter.Label(root, text="*Remove all the placeholder text and then fill your correct details!", padx=5, pady=5, foreground="blue", background="white", font=fontNoteStyle)
_note.grid(row=7,columnspan=2)

setPlaceholders()
root.configure(background='#ffff66')
root.mainloop()