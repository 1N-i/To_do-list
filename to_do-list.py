import tkinter as tk
from tkinter import messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg = "#f0f4f7")

        self.tasks = []
        self.setup_ui()

    def setup_ui(self):
        title_label = tk.Label(
            self.root,
            text = "To-do List",
            font = ("Helvetica", 22, "bold"),
            bg = "#f0f4f7",
            fg = "#333"
        )
        title_label.pack(pady = 10)

        input_frame = tk.Frame(self.root, bg = "#f0f4f7")
        input_frame.pack(pady = 10)

    def empty_tasks(self):
        pass

    def add_task(self):
        pass

    def view_task(self):
        pass

    def task_done(self):
        pass

    def delete_task(self):
        pass
