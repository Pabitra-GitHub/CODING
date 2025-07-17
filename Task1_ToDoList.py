todo_list = []

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        todo_list.append(task)
        print("Task added.")
    elif choice == '2':
        print("\n--- Your Tasks ---")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
    elif choice == '3':
        task_num = int(input("Enter task number to update: ")) - 1
        if 0 <= task_num < len(todo_list):
            new_task = input("Enter new task: ")
            todo_list[task_num] = new_task
            print("Task updated.")
        else:
            print("Invalid task number.")
    elif choice == '4':
        task_num = int(input("Enter task number to delete: ")) - 1
        if 0 <= task_num < len(todo_list):
            deleted = todo_list.pop(task_num)
            print(f"Task '{deleted}' deleted.")
        else:
            print("Invalid task number.")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
