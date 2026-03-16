FILE_NAME = "tasks.txt"

def add_task(task):
    try:
        with open(FILE_NAME, "a") as file:
            file.write(task + "\n")
        print("Task added successfully!")
    except Exception as e:
        print("Error while adding task:", e)


def view_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()
            if not tasks:
                print("No tasks found.")
                return
            
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")
    except FileNotFoundError:
        print("No task file found. Add a task first.")


def delete_task(task_number):
    try:
        with open(FILE_NAME, "r") as file:
            tasks = file.readlines()

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number!")
            return

        tasks.pop(task_number - 1)

        with open(FILE_NAME, "w") as file:
            file.writelines(tasks)

        print("Task deleted successfully!")

    except Exception as e:
        print("Error while deleting task:", e)