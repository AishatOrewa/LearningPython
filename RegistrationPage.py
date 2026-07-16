#Create a registration page that contains four frame, a frame is for user information that contains; first-name, last-name,title,age,nationality. a frame is for Registration Status that contains; completed courses, semesters, currently registered. Third frame would be for terms and conditions that has a checkbox that asks user if they accept the terms and conditions, the last frame is for submit data, a button.
import tkinter
from tkinter import ttk

window = tkinter.Tk()

window.title('Data Entry Form')

#frame1
User_frame = tkinter.LabelFrame(text='User Information', padx=10, pady=10,font=('Arial'))

User_fname = tkinter.Label(User_frame, text='First Name')
User_fname.grid(row=3, column=1)

User_Fname = tkinter.Entry(User_frame)
User_Fname.grid(row=4, column=1, pady=5, padx=5)

User_lname = tkinter.Label(User_frame, text='Last Name')
User_lname.grid(row=3, column=2)

User_Lname = tkinter.Entry(User_frame)
User_Lname.grid(row=4, column=2, pady=5, padx=5)

User_Title = tkinter.Label(User_frame, text='Title')
User_Title.grid(row=3, column=3)

User_title = ttk.Combobox(User_frame,values=['Mr','Mrs','Miss'])
User_title.grid(row=4, column=3, pady=5,padx=5)

User_Age = tkinter.Label(User_frame, text='Age')
User_Age.grid(row=5, column=1)

User_age = tkinter.Spinbox(User_frame, from_= 18, to= 30)
User_age.grid(row=6, column=1,pady=5,padx=5)

User_Nationality = tkinter.Label(User_frame, text='Nationality')
User_Nationality.grid(row=5, column=2)

User_nationality = ttk.Combobox(User_frame, values=['Nigeria', 'America', 'Others'])
User_nationality.grid(row=6, column=2, pady=5, padx=5)

User_frame.grid(padx=15,pady=15)

#frame2
status_frame = tkinter.LabelFrame(text='Registration Status',font=('Arial'), padx=20, pady=3)

course = tkinter.Label(status_frame, text='#Completed Courses')
course.grid(row=8, column=1)

course_entry = tkinter.Spinbox(status_frame,values=['GST111','GST122','MTH101','MTH111','STA112'])
course_entry.grid(row=9, column=1,padx=5)

semester = tkinter.Label(status_frame, text='#Semesters')
semester.grid(row=8, column=2)

semester_entry = tkinter.Spinbox(status_frame, values=['First semester','Second semester'])
semester_entry.grid(row=9, column=2, padx=5)

registration = tkinter.Checkbutton(status_frame, text='Currently Registered')
registration.grid(row=9, column=0)

status_frame.grid(padx=15)

#frame3
terms_frame = tkinter.LabelFrame(text='Terms & Conditions', font=('Arial'), padx=128)

accept_terms = tkinter.Checkbutton(terms_frame,text='I accept the terms and conditions.')
accept_terms.grid(column=0)

terms_frame.grid(pady=15)
#frame4
submit_frame = tkinter.Frame()

window.geometry('500x450')
window.mainloop()