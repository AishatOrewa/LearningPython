#This is the tutorial on how to use the os library.
# import os
# shutdown = input("Do you want to shutdown? ").lower()
# if shutdown == 'no':
#   exit()
# else:
#   os.system("shutdown /s /t 1")

#Recreating a window that has three button, each button has a function for Restart, Shutdown and logout.
import tkinter
import os
from tkinter import messagebox

window = tkinter.Tk()
window.title('Power')

window.configure(bg='#ffffff')
frame = tkinter.Frame(bg="#000000",padx=5,pady=5)

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
PageTitle = tkinter.Label(frame, text='Power Options',bg="#000000", fg="#ffffff")
PageTitle.pack()

Shutdown = tkinter.Button(frame, text="Shutdown", command=shutdown, bg="#ffffff", fg="#000000")
Shutdown.pack()

Logout = tkinter.Button(frame, text='LogOut', command=logout, bg="#ffffff", fg="#000000")
Logout.pack()

Restart = tkinter.Button(frame, text='Restart', command=restart, bg="#ffffff", fg="#000000")
Restart.pack()


frame.pack()
window.mainloop()