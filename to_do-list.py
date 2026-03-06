tasks = []

def show_menu():
    print("To do list \n1- Add task \n2- View tasks \n3- Mark task as done \n4- Delete task \n5- Close app")
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
    print("Adding task...\n")

def view_task():
    print("Viewing task...\n")

def task_done():
    print("Setting task as done...\n")

def delete_task():
    print("Deleting task...\n")

show_menu()