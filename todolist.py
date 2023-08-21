import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, width=40)
        self.task_listbox.pack(pady=10)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack()

        self.font_button = tk.Button(root, text="Change Font", command=self.change_font)
        self.font_button.pack()

        self.font = tkfont.Font(family="Helvetica", size=12)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            self.tasks.pop(index)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def change_font(self):
        new_font = tkfont.Font(family="Arial", size=16)
        self.font = new_font
        self.update_font()

    def update_font(self):
        self.task_entry.config(font=self.font)
        self.add_button.config(font=self.font)
        self.remove_button.config(font=self.font)
        self.font_button.config(font=self.font)
        self.task_listbox.config(font=self.font)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
