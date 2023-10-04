from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from random import choice,randint,shuffle
import array
import pyperclip

def save():
    Name = Name_entry.get()
    Email = Email_entry.get()
    Feedback = Feedback_entry.get()
    is_ok = messagebox.askokcancel(
            title=Name, message=f"These are the details entered: \nEmail:{Email}\nFeedback:{Feedback}\n")
    if is_ok:
        with open("data.txt", "a") as data_file:
            data_file.write(f"{Name}  |  {Email}  |  {Feedback} \n")
            Name_entry.delete(0, END)
            Email_entry.delete(0, END)
            Feedback_entry.delete(0, END)
           

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Feedback Manager")
window.config(padx=390, pady=125)
canvas = Canvas(height=200, width=200)
canvas.grid(row=0, column=1)
Name_label = Label(text="Name")
Name_label.grid(row=1, column=0)
Email_label = Label(text="Email/Username")
Email_label.grid(row=2, column=0)
Feedback_label = Label(text="Feedback")
Feedback_label.grid(row=3, column=0)
Name_entry = Entry(width=35)
Name_entry.grid(row=1, column=1)
Name_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(row=2, column=1)
Email_entry.focus()
Feedback_entry = Entry(width=21)
Feedback_entry.grid(row=3, column=1)
add_button = Button(text="ADD", width=36, command=save)
add_button.grid(row=4, column=1)
window.mainloop()