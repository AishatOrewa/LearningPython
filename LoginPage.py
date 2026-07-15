#Siwes-day3
#learn about Libraries, Tikinter and Geometric managers; .pack(), .grid()

#Designing a login page with Tikinter

import tkinter #This would import the tkinter library, it could be imported as anything else i.e "import tkinter as Tk" this would let your call tkinter as Tk instead of writing the whole word.
from tkinter import messagebox
window = tkinter.Tk()# this tells the program that we want whatever we are doing to be displayed on the window screen.

window.title('LOGIN PAGE')#Just as the name specify this code specifies the title of whatever would be displayed on the window, it's  just like the title in html that would be displayed in the google tab, but this would be displayed on the window screen.
window.configure(bg="#6219EB") # this is used to make changes to the background of the window screen.
#window.geometry learn about this command

#The code below creates the brain behind your submit button this function decides what will happen if you click on the submit button, this here decides whether the message would be sent to the terminal or it would clear the screen just like the refresh button.
def enter():
  username = "Aishat"
  password = "12345"
  if password==password_entry.get() and username==username_entry.get():
    messagebox.showinfo(title= "Log in", message="Log in successfully")
    print(f"congratulations {username}, Login successful")
  else:
    messagebox.showerror(title="Error", message="INVALID LOGIN! Try Again")
    print("INVALID LOGIN DETAILS!")
  # username = username_entry.get()
  # password = password_entry.get()
  # print(f"My username is {username} and my password is {password}")

frame = tkinter.Frame(window, bg="#6219EB")

#The code below creates the dispayable label on the window screen, this label won't be displayed without the use of geometric managers; which is why .grid is being used here.
login_label = tkinter.Label(frame, text="LOGIN", fg="#6219EB", bg="#000000", padx=5, pady=5, font=("Arial", 20))
login_label.grid(row=0, column=1, sticky= "NEWS",)

username_label = tkinter.Label(frame, text="Username:", padx=10, pady=5, bg="#6219EB", fg="#000000", font=("Arial",15))
username_label.grid(row=1, column=0)

#This code below gives the user an input field to actually write and give back to the program, it's similar to the input method just that this one has a space that is used for writing iykyk.
username_entry = tkinter.Entry(frame)
username_entry.grid(row=1, column=1)

#same function explained in line 21
password_label = tkinter.Label(frame, text="Password:", padx=10, pady=5, bg="#6219EB", fg="#000000", font=("Arial", 15))
password_label.grid(row=2, column=0)

#This code performs the same function explained in line 28
password_entry = tkinter.Entry(frame, show="*")
password_entry.grid(row=2, column=1)

#This code is used to create a clickable button for the user to use, this sends whatever that was inputed by the user to the terminal.
submit_button = tkinter.Button(frame, text="SUBMIT", bg="#000000", fg="#6219EB", padx=5, pady=5, font=("Arial", 20), command= enter )
submit_button.grid(row=4, column=1, sticky="NEWS")

frame.pack()# This is 
window.mainloop()# this code allows what ever we write or use with tkinter to run without this code the program won't work i guess.