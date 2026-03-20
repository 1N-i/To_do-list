import tkinter as tk

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

        self.task_entry = tk.Entry(
            input_frame,
            font = ("Helvetica", 12),
            width = 30
        )
        self.task_entry.pack(side = "left", padx = (0, 10))

        add_button = tk.Button(
            input_frame,
            text = "Add task",
            font = ("Helvetica", 11, "bold"),
            bg = "#27ae60",
            fg = "white",
            padx = 10,
            command = self.add_task
        )
        add_button.pack(side = "left")

    

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

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()