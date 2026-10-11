#REcreating the data entry form from scratch.
import tkinter #this would import the library tkinter that enables us to create GUI applications
from tkinter import ttk #this imports a module from tkinter that allows one to create more modern looking applications.
from tkinter import messagebox #This function is used to create pop up windows.
import os
import openpyxl #the python library that helps us use excel tools in python.
def enter_data(): #the function to be runned when the button is clicked.
  first_name = first_name_entry.get()
  last_name = last_name_entry.get()
  title = title_combobox.get()
  age = age_spinbox.get()
  nationality = nationality_combobox.get() 
  courses = courses_spinbox.get()
  semester = semester_spinbox.get()
  registration = status_var.get()
  agree = agree_var.get()
  if first_name and last_name:
    if agree == "Agreed":
      print(f"first_name: {first_name} last_name: {last_name} \ntitle:{title} age:{age} \nnationality:{nationality} \ncourses:{courses} semester:{semester} \nregistration:{registration} agree:{agree}")
      print("-------------------------------------------------------")
      filepath = "C:/Users/Dell/OneDrive/Desktop/LearningPython/registrationData.xlsx" #This is used to store the filepath for the excel file to be used
      if not os.path.exists(filepath): #This checks whether the file specified in filepath exists or not
        workbook = openpyxl.Workbook() #This is used to open an excel workbook
        sheet = workbook.active #This tells python to use the sheet that's currently open.
        heading = ["FirstName","Last Name", "Title", "Age", "Nationaliity", "#Courses", "#Semesters", "Registration Status"] #This creates the content of the heading cell in your excel file using array.
        sheet.append(heading) #This adds the content of the array to each cell accordingly to how it's listed in heading.
        workbook.save(filepath)
      workbook = openpyxl.load_workbook(filepath)
      sheet = workbook.active
      sheet.append([first_name,last_name,title,age,nationality,courses,semester,registration])
      workbook.save(filepath)
    else:
      tkinter.messagebox.showwarning(title = "Errorr", message = "You need to accept our terms and conditions.")
  else:
    tkinter.messagebox.showwarning(title = "Error", message = "First Name and Last Name is required.")
window = tkinter.Tk() #this creates the main window where all the elements created would be displayed in.
window.title("Data Entry Form") #This creates the title of the window and displays it at the top part close to the position of tkinter logo.

frame = tkinter.Frame(window) #this is the frame that is created inside of the window.
frame.pack() #this is a geometric manager that is used to decide where the widget is placed in the parent widget, by default it places the widget in the center of the parent widget.

#The first sub frame.
user_info_frame = tkinter.LabelFrame(frame, text='User Information') #This does not create a frame but a labelframe like it creates a subframe inside the frame.
user_info_frame.grid(row=0, column=0, sticky="news",padx=20, pady=10) #this involves the geometric manager grid and the row and column must be specified in this geometric manager. This frame won't necesarrily show in the window if it has no content in it i.e if no widget is placed in the userinfoframe it won't show in the window.

first_name_label = tkinter.Label(user_info_frame, text='First Name')
first_name_label.grid(row=0, column=0)

last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry = tkinter.Entry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)

title_combobox = ttk.Combobox(user_info_frame, values=['','Miss','Mr.', 'Ms.', 'Dr.'])
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text='Age')
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_= 18, to='infinity')
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text='Nationality')
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame, values=['','Nigeria','Algeria','America','South Africa', 'Austrailia', 'Other'])
nationality_combobox.grid(row=3, column=1)

#code to add equal padding to all widget in subFrame1
for widget in user_info_frame.winfo_children():
  widget.grid_configure(padx = 5, pady=5)

#Second SubFrame
courses_info_frame = tkinter.LabelFrame(frame)
courses_info_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10) 

status_label = tkinter.Label(courses_info_frame, text="Registration Status")
status_var = tkinter.StringVar(value="Not Registered")
status_check = tkinter.Checkbutton(courses_info_frame, text = "Currently Registered", variable=status_var, onvalue="Registered", offvalue="Not Registered")
status_label.grid(row=0, column=0)
status_check.grid(row=1, column=0)

courses_label = tkinter.Label(courses_info_frame, text="#Completed Courses")
courses_spinbox = ttk.Spinbox(courses_info_frame, from_=0, to='infinity')
courses_label.grid(row=0, column=1)
courses_spinbox.grid(row=1, column=1)

semester_label = tkinter.Label(courses_info_frame, text="#Semesters")
semester_spinbox = ttk.Spinbox(courses_info_frame, from_=0, to='infinity')
semester_label.grid(row=0, column=2)
semester_spinbox.grid(row=1, column=2)

#code to add equal padding in all widget in subFrame2
for widget in courses_info_frame.winfo_children():
  widget.grid_configure(padx = 10, pady=5)

#third sub frame
tandc_info_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
tandc_info_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

agree_var = tkinter.StringVar(value="Agreed")
agree_checkbox = tkinter.Checkbutton(tandc_info_frame, text="I accept the terms and conditions.",variable=agree_var,onvalue="Agreed", offvalue="Not Agreed")
agree_checkbox.grid(row=0, column=0)

#button created with the parent frame.
button = tkinter.Button(frame, text="Enter Data", command= enter_data) #the "command" listens to the button and whenever the button is clicked it runs the function "enter_data"
button.grid(row=3, column=0, sticky="news", padx=20,pady=5)

window.mainloop() #this ensures that the window would keep on running infinitely until it's terminated, without this line of code the window would show for only a split second and close.
