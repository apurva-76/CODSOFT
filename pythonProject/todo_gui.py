import tkinter as tk
from tkinter import messagebox
import os

TASK_FILE = "tasks.txt"
tasks = []

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            for line in f:
                tasks.append(line.strip())

def save_tasks():
    with open(TASK_FILE, "w") as f:
        for task in tasks:
            f.write(f"{task}\n")

def add_task():
    task = entry.get().strip()
    if not task:
        return messagebox.showwarning("Warning", "Please enter a task!")
    tasks.append(task)
    update_tasks(); save_tasks()
    entry.delete(0, tk.END)

def complete_task():
    selected_indices = listbox.curselection()
    if not selected_indices:
        return
    for idx in selected_indices:
        if not tasks[idx].startswith("✔ "):
            tasks[idx] = f"✔ {tasks[idx]}"
    update_tasks(); save_tasks()

def remove_completed():
    global tasks
    tasks = [t for t in tasks if not t.startswith("✔ ")]
    update_tasks(); save_tasks()

def update_tasks():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
    listbox.yview_moveto(1)

root = tk.Tk()
root.title("Todo List App")
root.geometry("380x500")
root.configure(bg="white")

tk.Label(root, text="Todo List", font=("Comic Sans MS", 22, "bold"), fg="purple", bg="white").pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), width=30, bd=2, relief="ridge")
entry.pack(pady=8)

tk.Button(root, text="Add Task", font=("Arial", 13), bg="#4C9AFF", fg="white", width=25, command=add_task).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    font=("Arial", 12),
    width=34,
    height=12,
    bd=2,
    relief="sunken",
    selectbackground="#8ED1FC",
    selectmode=tk.MULTIPLE  # Enable multiple selection
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scroll = tk.Scrollbar(frame)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scroll.set)
scroll.config(command=listbox.yview)

tk.Button(root, text="Complete Task", font=("Arial", 12), bg="#28A745", fg="white", width=18, command=complete_task).pack(pady=5)
tk.Button(root, text="Remove Completed", font=("Arial", 12), bg="#DC3545", fg="white", width=18, command=remove_completed).pack(pady=5)

load_tasks()
update_tasks()

root.mainloop()