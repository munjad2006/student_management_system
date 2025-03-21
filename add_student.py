import tkinter as tk
from tkinter import messagebox
import database as data

def add_student(bg_color='#CFFFDC', fg_color='black'):
    def submit():
        name = entry_name.get()
        age = entry_age.get()
        course = entry_course.get()
        contact = entry_contact.get()
        
        # Call the add_student function from database.py with the input values
        data.add_student(student=(name, age, course, contact))
        
        # Show a message box
        messagebox.showinfo("Student Added", f"Name: {name}\nAge: {age}\nCourse: {course}\nContact: {contact}")
        
        # Clear the entries after submission
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_course.delete(0, tk.END)
        entry_contact.delete(0, tk.END)
        window.destroy()

    window = tk.Tk()
    window.title("Add Student")
    window.configure(bg=bg_color)
    window.geometry('300x200')

    tk.Label(window, text="Name", bg=bg_color, fg=fg_color).grid(row=0, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=0, column=1)

    tk.Label(window, text="Age", bg=bg_color, fg=fg_color).grid(row=1, column=0)
    entry_age = tk.Entry(window)
    entry_age.grid(row=1, column=1)

    tk.Label(window, text="Course", bg=bg_color, fg=fg_color).grid(row=2, column=0)
    entry_course = tk.Entry(window)
    entry_course.grid(row=2, column=1)

    tk.Label(window, text="Contact", bg=bg_color, fg=fg_color).grid(row=3, column=0)
    entry_contact = tk.Entry(window)
    entry_contact.grid(row=3, column=1)

    tk.Button(window, text="Submit", command=submit).grid(row=4, column=0, columnspan=2)
    tk.Button(window, text="Back", command=window.destroy).grid(row=4, column=2, columnspan=1)

    window.mainloop()
