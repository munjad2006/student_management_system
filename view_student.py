import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import database as data

def view_students():
    def submit(selected_value):
        # Get the value from data.view_students
        if selected_value == "None":
            result = data.view_students()
        else:
            result = data.view_students(selected_value)
        
        # Clear the treeview
        for row in tree.get_children():
            tree.delete(row)
        
        # Insert new data into the treeview
        for row in result:
            tree.insert("", "end", values=row)

    window = tk.Tk()
    window.title("View Student")
    window.configure(bg='#CFFFDC')
    window.geometry()

    # Options for the dropdown menu
    options = ["None", "name", "id", "course"]
    selected_option = tk.StringVar(window)
    selected_option.set(options[0])  # Set default value to <none>

    def on_option_change(*args):
        submit(selected_option.get())

    # Trace the selected_option variable to detect changes
    selected_option.trace('w', on_option_change)

    # Create a frame to hold the label and dropdown menu
    frame = tk.Frame(window, bg='#CFFFDC')
    frame.pack(pady=10)

    tk.Label(frame, text="Table Sort by:", bg='#CFFFDC').pack(side=tk.LEFT)
    # Create the dropdown menu
    tk.OptionMenu(frame, selected_option, *options).pack(side=tk.LEFT, padx=10)

    # Create a Treeview widget
    columns = ("ID", "Name","Age", "Course", "Contact")
    tree = ttk.Treeview(window, columns=columns, show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Course", text="Course")
    tree.heading("Contact", text="Contact")
    tree.pack(pady=10, fill='x')

    tk.Button(window, text="Back", command=window.destroy).pack(pady=10)

    window.mainloop()

if __name__ == '__main__':
    view_students()