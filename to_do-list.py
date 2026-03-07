tasks = {"tk1": "X",
         "tk2": "X",
         "tk3": "X",
        }

def show_menu():
    print("\nMenu \n1- Add task \n2- View tasks \n3- Mark task as done \n4- Delete task \n5- Close app")
    options = list(range(1,6))
    while True:
        while True:
            try:
                action = int(input("\nAction: "))
                if action not in options:
                    raise ValueError
                break
            except ValueError:
                print("Invalid value")

        if action == 1:
            add_task()
        elif action == 2:
            view_task()
        elif action == 3:
            task_done()
        elif action == 4:
            delete_task()
        elif action == 5:
            print("Closing program...")
            break
        
        show_menu()
        break

def add_task():
    task = input("Task: ")
    tasks[task] = "X"

def view_task():
    print("To-do list")
    for task in tasks:
        print(f"{task}: {tasks[task]}")

def task_done():
    while True:
        try:
            task = input("Completed task: ")
            tasks[task] = "✓"
            break
        except KeyError:
            print("Task not found")

def delete_task():
    while True:
        try:
            task = input("Task to delete: ")
            del tasks[task]
            break
        except KeyError:
            print("Task not found")

show_menu()