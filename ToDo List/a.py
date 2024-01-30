import os
import json

# File to store the tasks
todo_file = "todo_list.json"

def load_tasks():
    if os.path.exists(todo_file):
        with open(todo_file, 'r') as file:
            tasks = json.load(file)
        return tasks
    else:
        return {}

def save_tasks(tasks):
    with open(todo_file, 'w') as file:
        json.dump(tasks, file, indent=2)

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, (task, status) in enumerate(tasks.items(), start=1):
            print(f"{index}. {task} - {'Done' if status else 'Not Done'}")

def add_task(tasks, task):
    tasks[task] = False
    print(f"Task '{task}' added to the To-Do List.")

def update_task_status(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        task = list(tasks.keys())[task_index - 1]
        tasks[task] = not tasks[task]
        print(f"Task '{task}' status updated.")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Update Task Status")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '3':
            display_tasks(tasks)
            task_index = int(input("Enter the task index to update status: "))
            update_task_status(tasks, task_index)
        elif choice == '4':
            save_tasks(tasks)
            print("To-Do List saved. Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
