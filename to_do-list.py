tasks = {}

def empty_tasks():
    if len(tasks) == 0:
        return True
    else:
        return False

def add_task():
    task = input("Task: ")
    tasks[task] = "X"
    print(f"{task} was added to the list.")

def view_task():
    if not empty_tasks():
        print("To-do list")
        i = 1
        for task in tasks:
            print(f"{i}- {task}: {tasks[task]}")
            i += 1
    else:
        print("Empty List")

def task_done():
    if not empty_tasks():
        view_task()
        i = len(tasks)
        options = list(range(1, i + 1))
        while True:
            try:
                task = int(input(f"Completed task (1-{i}): "))
                if task not in options:
                    raise ValueError
                completed_task = list(tasks.keys())[task - 1]
                tasks[completed_task] = "✓"
                print(f"Marked '{task}' as done!")
                break
            except ValueError:
                print("Task not found")
    else:
        print("Empty list")

def delete_task():
    if not empty_tasks():
        view_task()
        i = len(tasks)
        options = list(range(1, i + 1))
        while True:
            try:
                task = int(input(f"Task to delete (1-{i}): "))
                if task not in options:
                    raise ValueError
                completed_task = list(tasks.keys())[task - 1]
                del tasks[completed_task]
                print(f"'{task}' was deleted from the List!")
                break
            except ValueError:
                print("Task not found")
    else:
        print("Empty List")

while True:
    print("\nMenu: \n1- Add task \n2- View tasks \n3- Mark task as done \n4- Delete task \n5- Close app")
    action = input("\nAction (1-5): ")
    if action == "1":
        add_task()
    elif action == "2":
        view_task()
    elif action == "3":
        task_done()
    elif action == "4":
        delete_task()
    elif action == "5":
        print("Closing program...")
        break
    else:
        print("Invalid value")