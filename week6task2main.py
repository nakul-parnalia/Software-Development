# ============================================================
# Project: To-Do List Manager
# Purpose: Demonstrate the use of Python functions to create
#          a modular, reusable, and maintainable program.
# ============================================================

# List to store tasks
# Each task is stored as a dictionary with a name and status
todo_list = []

# ------------------------------------------------------------
# Function: add_task
# Description:
#   Adds a new task to the to-do list.
# ------------------------------------------------------------
def add_task(task_name):
    task = {
        "name": task_name,
        "completed": False
    }
    todo_list.append(task)
    print("Task added successfully.")

# ------------------------------------------------------------
# Function: mark_task_completed
# Description:
#   Marks a task as completed based on its number.
# ------------------------------------------------------------
def mark_task_completed(task_number):
    if 0 <= task_number < len(todo_list):
        todo_list[task_number]["completed"] = True
        print("Task marked as completed.")
    else:
        print("Invalid task number.")

# ------------------------------------------------------------
# Function: display_tasks
# Description:
#   Displays all tasks with their completion status.
# ------------------------------------------------------------
def display_tasks():
    if not todo_list:
        print("No tasks in the list.")
        return

    print("\nTo-Do List:")
    for index, task in enumerate(todo_list):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index + 1}. {task['name']} - {status}")

# ------------------------------------------------------------
# Main Program Loop
# Description:
#   Allows users to interact with the to-do list manager.
# ------------------------------------------------------------
while True:
    print("\nTo-Do List Manager")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. Display Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task_name = input("Enter task name: ")
        add_task(task_name)

    elif choice == "2":
        display_tasks()
        task_num = int(input("Enter task number to mark completed: ")) - 1
        mark_task_completed(task_num)

    elif choice == "3":
        display_tasks()

    elif choice == "4":
        print("Exiting To-Do List Manager. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

# ============================================================
# This program demonstrates:
# - Defining and using functions
# - Breaking a problem into modular components
# - Improving code readability and maintainability
# ============================================================
