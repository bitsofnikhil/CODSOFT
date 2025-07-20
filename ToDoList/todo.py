tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Invalid task number.")

while True:
    print("\nOptions: 1. Add  2. View  3. Delete  4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        index = int(input("Enter task number to delete: ")) - 1
        delete_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
