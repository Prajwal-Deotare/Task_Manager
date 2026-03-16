import task_operations as to

def menu():
    print("\n===== TASK MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    menu()

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            task = input("Enter task: ")
            to.add_task(task)

        elif choice == 2:
            to.view_tasks()

        elif choice == 3:
            number = int(input("Enter task number to delete: "))
            to.delete_task(number)

        elif choice == 4:
            print("Goodbye Prajwal !!! ")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")