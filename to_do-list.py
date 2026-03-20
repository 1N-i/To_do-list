from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("To-do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(bg = "#f0f4f7")
        self.tasks = []

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