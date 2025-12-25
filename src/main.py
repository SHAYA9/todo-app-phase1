# In-Memory Python Console Todo Application

# Global state variables
tasks = []  # List to store task dictionaries
task_id_counter = 1  # Counter to ensure unique task IDs

def display_menu():
    """Displays the main menu to the user."""
    print("\n--- Todo Application Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
    print("6. Exit")

def add_task():
    """Adds a new task to the list."""
    global task_id_counter
    title = input("Enter task title: ")
    if title:
        tasks.append({"id": task_id_counter, "title": title, "completed": False})
        print(f"Task '{title}' added with ID {task_id_counter}.")
        task_id_counter += 1
    else:
        print("Task title cannot be empty.")

def view_tasks():
    """Displays all current tasks."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}")

def update_task():
    """Updates an existing task's title."""
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        for task in tasks:
            if task["id"] == task_id:
                new_title = input("Enter the new title: ")
                if new_title:
                    task["title"] = new_title
                    print(f"Task {task_id} updated successfully.")
                    return
        print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def mark_task_complete():
    """Toggles the completion status of a task."""
    try:
        task_id = int(input("Enter the ID of the task to mark as complete: "))
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                status = "Complete" if task["completed"] else "Incomplete"
                print(f"Task {task_id} marked as {status}.")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def delete_task():
    """Deletes a task."""
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
        task_to_delete = None
        for task in tasks:
            if task["id"] == task_id:
                task_to_delete = task
                break
        if task_to_delete:
            tasks.remove(task_to_delete)
            print(f"Task {task_id} deleted successfully.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def main():
    """Main function to run the application."""
    while True:
        display_menu()
        choice_input = input("Enter your choice (1-6): ")
        
        try:
            choice = int(choice_input)
            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                update_task()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                mark_task_complete()
            elif choice == 6:
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

