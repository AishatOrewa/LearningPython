#This is the tutorial on how to use the os library.
# import os
# shutdown = input("Do you want to shutdown? ").lower()
# if shutdown == 'no':
#   exit()
# else:
#   os.system("shutdown /s /t 1")

#Recreating a window that has three button, each button has a function for Restart, Shutdown and logout. for window OS.
import tkinter
import os
from tkinter import messagebox

window = tkinter.Tk()
window.title('Power')

window.configure(bg='#ffffff')
frame = tkinter.Frame(bg="#000000")

def shutdown():
  answer = messagebox.askyesno(
    "Confirm Shutdown",
    "Are you sure you want to shut down your computer?"
  )
  if answer:
    os.system("shutdown /s /t 1")
def restart():
  reply = messagebox.askyesno(
    "Confirm System Restart",
    "Do you really want to Restart your system?"
  )
  if reply:
    os.system("shutdown /r /t 1")
def logout():
  user = messagebox.askyesno(
    "Confirm User LogOut",
    "Do you really want to LogOut from your System?"
  )
  if user:
    os.system("shutdown /l")
PageTitle = tkinter.Label(frame, text='Power Options',bg="#000000", fg="#ffffff", font=('bold', 20))
PageTitle.grid(row=0, column=2)

Shutdown = tkinter.Button(frame, text="Shutdown", command=shutdown, bg="red", fg="black")
Shutdown.grid(row=1, column=1)

Logout = tkinter.Button(frame, text='LogOut', command=logout, bg="green", fg="black")
Logout.grid(row=1, column=2)

Restart = tkinter.Button(frame, text='Restart', command=restart, bg="orange", fg="black")
Restart.grid(row=1, column=3)

window.geometry('450x450')
frame.pack(side='top')
window.mainloop()