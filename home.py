import tkinter as tk
import add_student
import update_student
import view_student
import delete_student
import search_student
import database

# create the database
database.main()

# Create the main window
root = tk.Tk()
root.geometry('500x500')
root.title('Student Management System')
root.configure(bg='#CFFFDC')

def open_settings():
    def toggle_bg_color():
        if root.cget('bg') == '#CFFFDC':
            new_color = '#555555'
            text_color = 'white'
            text_bg_color = '#555555'
            toggle_button.config(text='Light Theme')
        else:
            new_color = '#CFFFDC'
            text_color = 'black'
            text_bg_color = '#68BA7F'
            toggle_button.config(text='Dark Theme')
        
        root.configure(bg=new_color)
        settings_window.configure(bg=new_color)
        top_frame.configure(bg=new_color)
        heading.configure(bg=new_color, fg=text_color)
        btn_add_student.configure(bg=text_bg_color, fg=text_color)
        btn_view_student.configure(bg=text_bg_color, fg=text_color)
        btn_update_student.configure(bg=text_bg_color, fg=text_color)
        btn_delete_student.configure(bg=text_bg_color, fg=text_color)
        btn_search_student.configure(bg=text_bg_color, fg=text_color)
        btn_exit_student.configure(bg=text_bg_color, fg=text_color)
        btn_settings.configure(bg=text_bg_color, fg=text_color)
        toggle_button.configure(bg=text_bg_color, fg=text_color)

    settings_window = tk.Toplevel(root)
    settings_window.geometry('300x200')
    settings_window.title('Settings')
    settings_window.configure(bg='#CFFFDC')

    toggle_button = tk.Button(settings_window, text='Dark Theme', command=toggle_bg_color, bg='#68BA7F')
    toggle_button.pack(pady=20)

# Create a frame to hold the label and settings button
top_frame = tk.Frame(root)
top_frame.configure(bg='#CFFFDC')
top_frame.pack(side='top', fill='x', padx=10, pady=10)

heading = tk.Label(top_frame, text="Student Management System",font=('Ariel 18'), bg='#CFFFDC')
heading.pack(side='left', pady=10)
btn_settings = tk.Button(top_frame, text='Settings', command=open_settings, bg='#68BA7F')
btn_settings.pack(side='right', padx=10)

# Create buttons with matching background color
btn_add_student = tk.Button(root, text='Add Student', command=add_student.add_student, bg='#68BA7F')
btn_view_student = tk.Button(root, text='View Student', command=view_student.view_students, bg='#68BA7F')
btn_update_student = tk.Button(root, text='Update Student', command=update_student.update_student, bg='#68BA7F')
btn_delete_student = tk.Button(root, text='Delete Student', command=update_student.update_student, bg='#68BA7F')
btn_search_student = tk.Button(root, text='Search Student', command=update_student.update_student, bg='#68BA7F')
btn_exit_student = tk.Button(root, text='Exit', command=root.quit, bg='#68BA7F')

# Place buttons
btn_add_student.pack(pady=10)
btn_view_student.pack(pady=10)
btn_update_student.pack(pady=10)
btn_delete_student.pack(pady=10)
btn_search_student.pack(pady=10)
btn_exit_student.pack(pady=10)

# Run the application
root.mainloop()