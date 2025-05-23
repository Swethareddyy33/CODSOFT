from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append(task)
        cursor.execute("INSERT INTO tasks VALUES (?)", (task,))
        update_list()
        task_entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

def delete_task():
    try:
        task = task_listbox.get(ACTIVE)
        tasks.remove(task)
        cursor.execute("DELETE FROM tasks WHERE title = ?", (task,))
        update_list()
    except:
        messagebox.showerror("Delete Error", "No task selected.")

def delete_all():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        cursor.execute("DELETE FROM tasks")
        update_list()

def update_list():
    task_listbox.delete(0, END)
    for t in tasks:
        task_listbox.insert(END, t)

def load_tasks():
    cursor.execute("SELECT title FROM tasks")
    for row in cursor.fetchall():
        tasks.append(row[0])

def on_close():
    conn.commit()
    conn.close()
    root.destroy()

root = Tk()
root.title("To-Do List")
root.geometry("400x400")
root.protocol("WM_DELETE_WINDOW", on_close)

conn = sql.connect("tasks.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (title TEXT)")
tasks = []
load_tasks()

task_entry = Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

Button(root, text="Add Task", command=add_task).pack()
Button(root, text="Delete Task", command=delete_task).pack()
Button(root, text="Delete All", command=delete_all).pack()

task_listbox = Listbox(root, width=45, height=10)
task_listbox.pack(pady=10)

update_list()
root.mainloop()
