import tkinter as tk
from tkinter import messagebox
import os

# File to save tasks
FILENAME = "tasks.txt"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            for task in file:
                task_listbox.insert(tk.END, task.strip())

def save_tasks():
    with open(FILENAME, "w") as file:
        for i in range(task_listbox.size()):
            file.write(task_listbox.get(i) + "\n")

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# GUI setup
window = tk.Tk()
window.title("To-Do List App")
window.geometry("300x400")

title = tk.Label(window, text="My Tasks", font=("Arial", 16))
title.pack(pady=10)

task_listbox = tk.Listbox(window, width=40, height=10)
task_listbox.pack(pady=10)

task_entry = tk.Entry(window, width=25)
task_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Task", width=10, command=add_task)
add_button.pack(pady=2)

delete_button = tk.Button(window, text="Delete Task", width=10, command=delete_task)
delete_button.pack(pady=2)

load_tasks()  # Load tasks on startup

window.mainloop()
