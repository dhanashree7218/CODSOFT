def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_number):
    tasks = load_tasks()
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed}' removed.")
    else:
        print("Invalid task number.")

while True:
    choice = input("\nChoose: add/view/remove/exit: ").strip().lower()
    if choice == "add":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "view":
        view_tasks()
    elif choice == "remove":
        view_tasks()
        try:
            num = int(input("Enter task number to remove: "))
            remove_task(num)
        except ValueError:
            print("Enter a valid number.")
    elif choice == "exit":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")