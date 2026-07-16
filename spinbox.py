import tkinter
window = tkinter.Tk()
window.title("Form")

User_fname = tkinter.Label(window, text='First Name:')
User_fname.pack()

User_FName = tkinter.Entry(window)
User_FName.pack()

User_lname = tkinter.Label(window, text="Last Name")
User_lname.pack()
User_LName = tkinter.Entry(window)
User_LName.pack()

User_age = tkinter.Label(window, text='What is your Age?')
User_age.pack()

spin_Age = tkinter.Spinbox(window, from_=0, to=100)
spin_Age.pack()

window.geometry('500x700')
window.mainloop()