import tkinter as tk
from tkinter import messagebox
import database as data

def update_student():
    def submit():
        name = entry_name.get()
        age = entry_age.get()
        course = entry_course.get()
        contact = entry_contact.get()
        student_id = entry_id.get()
        
        # Call the add_student function from database.py with the input values
        data.update_student(student=(name, age, course, contact, student_id))
        
        # Show a message box
        messagebox.showinfo("Student data update", f"Name: {name}\nAge: {age}\nCourse: {course}\nContact: {contact}")
        
        # Clear the entries after submission
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_course.delete(0, tk.END)
        entry_contact.delete(0, tk.END)
        entry_id.delete(0, tk.END)
        window.destroy()

    window = tk.Tk()
    window.title("Update Student")
    window.configure(bg='#CFFFDC')
    window.geometry('300x200')

    tk.Label(window, text="Enter Existed student_id").grid(row=0, columnspan=2)
    tk.Label(window, text="student_id").grid(row=1, column=0)
    entry_id = tk.Entry(window)
    entry_id.grid(row=1, column=1)

    tk.Label(window, text="Name").grid(row=2, column=0)
    entry_name = tk.Entry(window)
    entry_name.grid(row=2, column=1)

    tk.Label(window, text="Age").grid(row=3, column=0)
    entry_age = tk.Entry(window)
    entry_age.grid(row=3, column=1)

    tk.Label(window, text="Course").grid(row=4, column=0)
    entry_course = tk.Entry(window)
    entry_course.grid(row=4, column=1)

    tk.Label(window, text="Contact").grid(row=5, column=0)
    entry_contact = tk.Entry(window)
    entry_contact.grid(row=5, column=1)

    tk.Button(window, text="Update", command=submit).grid(row=6, column=0, columnspan=2)
    tk.Button(window, text="Back", command=window.destroy).grid(row=6, column=2, columnspan=1)

    window.mainloop()

if __name__ == '__main__':
    update_student()
