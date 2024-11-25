import tkinter as tk
from tkinter import messagebox, Label, PhotoImage

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, task, priority):
        # Insert the task in sorted order based on priority (highest priority first)
        new_task = (task, priority)
        if self.is_empty():
            self.queue.append(new_task)
        else:
            for i in range(len(self.queue)):
                if self.queue[i][1] < priority:
                    self.queue.insert(i, new_task)
                    break
            else:
                self.queue.append(new_task)

    def get_next_task(self):
        if self.is_empty():
            return "No tasks in the queue"
        return self.queue.pop(0)

    def delete_all(self):
        self.queue = []

    def display(self):
        if self.is_empty():
            return ["No tasks available"]
        return [f"Task: {task[0]}, Priority: {task[1]}" for task in self.queue]

# Initialize the priority queue
pq = PriorityQueue()

def add_task():
    task_name = task_name_entry.get()
    try:
        priority = int(priority_entry.get())
        if task_name and priority:
            pq.insert(task_name, priority)
            task_name_entry.delete(0, tk.END)
            priority_entry.delete(0, tk.END)
            refresh_task_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a valid task name and priority.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid priority.")

def get_next_task():
    next_task = pq.get_next_task()
    if next_task == "No tasks in the queue":
        messagebox.showwarning("No Tasks", "No tasks in the queue.")
    else:
        refresh_task_list()
        messagebox.showinfo("Next Task", f"Next task: {next_task[0]}, Priority: {next_task[1]}")

def delete_all_tasks():
    pq.delete_all()
    refresh_task_list()
    messagebox.showinfo("All Tasks Deleted", "All tasks have been deleted.")

def refresh_task_list():
    task_listbox.delete(0, tk.END)
    tasks = pq.display()
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Tkinter GUI setup
root = tk.Tk()
root.title("Task Management System")
root.geometry("1000x600")
root.config(bg="#C4AD9D")
root.resizable(False, False)

frame = tk.Frame(root, bg="#C4AD9D")
frame.pack(pady=30, anchor="w")

task_name_label = tk.Label(frame, text="Task Name:", bg="#C4AD9D", font=("Poppins", 16, "bold"))
task_name_label.grid(row=0, column=0, padx=130, pady=10)

task_name_entry = tk.Entry(frame, font=("Georgia", 14), width=30, bd=2, relief="solid", highlightthickness=2, highlightbackground="#ccc", highlightcolor="#C4AD9D", bg="white")
task_name_entry.grid(row=0, column=1, padx=10, pady=10)

priority_label = tk.Label(frame, text="Priority:", bg="#C4AD9D", font=("Poppins", 16, "bold"))
priority_label.grid(row=1, column=0, padx=0, pady=10)

priority_entry = tk.Entry(frame, font=("Georgia", 14), width=30, bd=2, relief="solid", highlightthickness=2, highlightbackground="#ccc", highlightcolor="#C4AD9D", bg="white")
priority_entry.grid(row=1, column=1, padx=10, pady=10)

add_button = tk.Button(root, bg="#A8D5BA", text="Add Task", command=add_task, font=("Poppins", 12, "bold"), width=20, relief="flat", bd=2, highlightbackground="#A8D5BA")
add_button.place(x=800, y=60)

next_button = tk.Button(root, bg="#FFCC00", text="Get-Next", command=get_next_task, font=("Raleway", 12, "bold"), width=20, relief="flat", bd=2, highlightbackground="#A8D5BA")
next_button.place(x=800, y=120)

delete_all_button = tk.Button(root, bg="#FF6F61", text="Delete All Tasks", command=delete_all_tasks, font=("Raleway", 12, "bold"), width=20, relief="flat", bd=2, highlightbackground="#FF6F61")
delete_all_button.place(x=800, y=180)

task_listbox = tk.Listbox(root, width=105, height=12, font=("Raleway", 12), bg="#f4f4f4", selectmode=tk.SINGLE, bd=2, relief="solid", highlightthickness=1, highlightbackground="#A8D5BA")
task_listbox.pack(pady=105)

logo = PhotoImage(file=r"C:\MyProjects\ds\taskschedulingapp\logofordsminiproj.png")
Label(image=logo, bg="#C4AD9D").place(x=25, y=35)

refresh_task_list()

root.mainloop()
