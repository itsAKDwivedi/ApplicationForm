import tkinter as tk
from tkcalendar import DateEntry,Calendar
from tkinter import ttk
win=tk.Tk()
win.resizable(False,False)

win.title("Application Form")
win.geometry("650x720")
win.config(bg="#9FD996")

info_frame=tk.LabelFrame(win,text="Applicant's Details")
info_frame.grid(row=0,column=0,padx=20,pady=10)

title_label=tk.Label(info_frame,text="Title")
title_label.grid(row=0,column=0,padx=10,pady=5)
fname_label=tk.Label(info_frame,text="First Name")
fname_label.grid(row=0,column=1,padx=10,pady=5)
lname_label=tk.Label(info_frame,text="Last Name")
lname_label.grid(row=0,column=2,padx=10,pady=5)

title_combo=ttk.Combobox(info_frame,values=["Ms.","Mr.","Mrs."],state="readonly")
title_combo.grid(row=1,column=0,padx=10,pady=5)
fname_entry=tk.Entry(info_frame)
fname_entry.grid(row=1,column=1,padx=10,pady=5)
lname_entry=tk.Entry(info_frame)
lname_entry.grid(row=1,column=2,padx=10,pady=5)

dob_label=tk.Label(info_frame, text="D.O.B.(DD/MM/YYYY)")
dob_label.grid(row=3,column=0,padx=10,pady=5)
contact_label=tk.Label(info_frame,text="Contact No")
contact_label.grid(row=3,column=1,padx=10,pady=5)
email_label=tk.Label(info_frame,text="Email")
email_label.grid(row=3,column=2,padx=10,pady=5)
gender_label=tk.Label(info_frame,text="Gender")
gender_label.grid(row=3,column=3,padx=10,pady=5)

dob_entry=DateEntry(info_frame,date_pattern="dd/mm/yyyy")
dob_entry.grid(row=4,column=0,padx=10,pady=5)
contact_entry=tk.Entry(info_frame)
contact_entry.grid(row=4,column=1,padx=10,pady=5)
email_entry=tk.Entry(info_frame)
email_entry.grid(row=4,column=2,padx=10,pady=5)
gender_var=tk.StringVar()
gender_var.set(" ")
male=tk.Radiobutton(info_frame,text="Male",variable=gender_var,value="Male")
male.grid(row=4,column=3,padx=10,pady=5)
female=tk.Radiobutton(info_frame,text="Female",variable=gender_var,value="Female")
female.grid(row=4,column=4,padx=10,pady=5)

edu_frame=tk.LabelFrame(win,text="Academic Details")
edu_frame.grid(row=1,column=0,padx=10,pady=5)

acad_label=tk.Label(edu_frame,text="Academic Level")
acad_label.grid(row=0,column=0,padx=67,pady=5)
cgpa_label=tk.Label(edu_frame,text="CGPA")
cgpa_label.grid(row=0,column=1,padx=67,pady=5)
year_label=tk.Label(edu_frame,text="Year of Passing")
year_label.grid(row=0,column=2,padx=67,pady=5)

label10=tk.Label(edu_frame,text="10th Class")
label10.grid(row=1,column=0,padx=15,pady=10)
cgpa10=tk.Entry(edu_frame)
cgpa10.grid(row=1,column=1,padx=15,pady=10)
year10=tk.Entry(edu_frame)
year10.grid(row=1,column=2,padx=15,pady=10)

label12=tk.Label(edu_frame,text="12th Class")
label12.grid(row=2,column=0,padx=15,pady=10)
cgpa12=tk.Entry(edu_frame)
cgpa12.grid(row=2,column=1,padx=15,pady=10)
year12=tk.Entry(edu_frame)
year12.grid(row=2,column=2,padx=15,pady=10)

high_label=tk.Label(edu_frame,text="Highest Degree")
high_label.grid(row=3,column=0,padx=15,pady=10)

high_combo=ttk.Combobox(edu_frame,values=["B.tech.","B.A.","B.Com.","B.Sc.","BCA","BBA","Any other"],state="readonly")
high_combo.grid(row=4,column=0,padx=15,pady=10)
high_cgpa=tk.Entry(edu_frame)
high_cgpa.grid(row=4,column=1,padx=15,pady=10)
high_year=tk.Entry(edu_frame)
high_year.grid(row=4,column=2,padx=15,pady=10)

prog_frame=tk.LabelFrame(win,text="Programming Skills")
prog_frame.grid(row=2,column=0,padx=10,pady=5)

c=tk.Checkbutton(prog_frame,text="C")
c.grid(row=0,column=0,padx=51,pady=10)
cpp=tk.Checkbutton(prog_frame,text="C++")
cpp.grid(row=0,column=1,padx=51,pady=10)
java=tk.Checkbutton(prog_frame,text="Java")
java.grid(row=0,column=2,padx=51,pady=10)
python=tk.Checkbutton(prog_frame,text="Python")
python.grid(row=0,column=3,padx=51,pady=10)

level_label=tk.Label(prog_frame,text="Level:")
level_label.grid(row=1,column=0,padx=10,pady=10)
level_scale=tk.Scale(prog_frame,from_=0, to=5,orient="horizontal")
level_scale.grid(row=1,column=1,padx=10,pady=10)

reason_frame=tk.Frame(win)
reason_frame.grid(row=3,column=0,padx=10,pady=5)

reason=tk.Label(reason_frame,text="Describe briefly why should we hire you?")
reason.grid(row=0,column=0,padx=10,pady=5)
reason_box=tk.Text(reason_frame,width=72,height=5)
reason_box.grid(row=1,column=0,padx=10,pady=5)
scroll=ttk.Scrollbar(reason_frame,orient="vertical",command=reason_box.yview)
scroll.grid(row=1,column=1)
reason_box['yscrollcommand']=scroll.set

submit=tk.Button(win,text="Submit")
submit.grid(row=4,column=0,padx=10,pady=10)

win.mainloop()