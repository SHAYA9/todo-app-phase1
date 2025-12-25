# In-Memory Python Console Todo Application

# Global state variables
tasks = []  # List to store task dictionaries
task_id_counter = 1  # Counter to ensure unique task IDs

<<<<<<< HEAD
=======
def parse_tags(tags_str):
    """Parses a comma-separated string of tags into a list of cleaned-up strings."""
    if tags_str:
        return [tag.strip() for tag in tags_str.split(',') if tag.strip()]
    return []

def validate_priority(priority_str):
    """Validates if a string is a valid priority (High, Medium, Low)."""
    if priority_str and priority_str.lower() in ["high", "medium", "low"]:
        return priority_str.capitalize()
    return None

def get_task_by_id(task_id):
    """Retrieves a task dictionary by its ID."""
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None

>>>>>>> 002-enhanced-todo-features
def display_menu():
    """Displays the main menu to the user."""
    print("\n--- Todo Application Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Complete")
<<<<<<< HEAD
    print("6. Exit")
=======
    print("6. Search / Filter Tasks")
    print("7. Sort Tasks")
    print("8. Exit")
>>>>>>> 002-enhanced-todo-features

def add_task():
    """Adds a new task to the list."""
    global task_id_counter
<<<<<<< HEAD
    title = input("Enter task title: ")
    if title:
        tasks.append({"id": task_id_counter, "title": title, "completed": False})
        print(f"Task '{title}' added with ID {task_id_counter}.")
        task_id_counter += 1
    else:
        print("Task title cannot be empty.")
=======
    title = input("Enter task title (required): ")
    if not title:
        print("Task title cannot be empty.")
        return

    priority_input = input("Enter priority (High, Medium, Low, or leave blank for Medium): ")
    priority = validate_priority(priority_input) or "Medium"

    tags_input = input("Enter tags (comma-separated, or leave blank): ")
    tags = parse_tags(tags_input)

    tasks.append({"id": task_id_counter, "title": title, "completed": False, "priority": priority, "tags": tags})
    print(f"Task '{title}' added with ID {task_id_counter}.")
    task_id_counter += 1
>>>>>>> 002-enhanced-todo-features

def view_tasks():
    """Displays all current tasks."""
    print("\n--- Your Tasks ---")
    if not tasks:
        print("No tasks found.")
    else:
        for task in tasks:
            status = "Complete" if task["completed"] else "Incomplete"
<<<<<<< HEAD
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
=======
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, Tags: {', '.join(task['tags'])}")

def update_task():
    """Updates an existing task's title, priority, and tags."""
    try:
        task_id = int(input("Enter the ID of the task to update: "))
        task = get_task_by_id(task_id)
        if task:
            new_title = input(f"Enter new title (current: {task['title']}, leave blank to keep): ")
            if new_title:
                task["title"] = new_title

            priority_input = input(f"Enter new priority (High, Medium, Low, current: {task['priority']}, leave blank to keep): ")
            priority = validate_priority(priority_input)
            if priority:
                task["priority"] = priority
            elif priority_input: # If user entered something but it was invalid
                print("Invalid priority. Keeping current priority.")

            tags_input = input(f"Enter new tags (comma-separated, current: {', '.join(task['tags'])}, leave blank to keep): ")
            # Only update tags if input is not empty, otherwise keep existing tags
            if tags_input: 
                tags = parse_tags(tags_input)
                task["tags"] = tags
            elif tags_input == "": # If user explicitly cleared tags
                task["tags"] = []

            print(f"Task {task_id} updated successfully.")
            return
>>>>>>> 002-enhanced-todo-features
        print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

def mark_task_complete():
    """Toggles the completion status of a task."""
    try:
        task_id = int(input("Enter the ID of the task to mark as complete: "))
<<<<<<< HEAD
        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                status = "Complete" if task["completed"] else "Incomplete"
                print(f"Task {task_id} marked as {status}.")
                return
        print("Task not found.")
=======
        task = get_task_by_id(task_id)
        if task:
            task["completed"] = not task["completed"]
            status = "Complete" if task["completed"] else "Incomplete"
            print(f"Task {task_id} marked as {status}.")
        else:
            print("Task not found.")
>>>>>>> 002-enhanced-todo-features
    except ValueError:
        print("Invalid ID. Please enter a number.")

def delete_task():
    """Deletes a task."""
    try:
        task_id = int(input("Enter the ID of the task to delete: "))
<<<<<<< HEAD
        task_to_delete = None
        for task in tasks:
            if task["id"] == task_id:
                task_to_delete = task
                break
        if task_to_delete:
            tasks.remove(task_to_delete)
=======
        task = get_task_by_id(task_id)
        if task:
            tasks.remove(task)
>>>>>>> 002-enhanced-todo-features
            print(f"Task {task_id} deleted successfully.")
        else:
            print("Task not found.")
    except ValueError:
        print("Invalid ID. Please enter a number.")

<<<<<<< HEAD
=======
def search_filter_tasks():
    """Searches and filters tasks based on user criteria."""
    print("\n--- Search & Filter Tasks ---")
    if not tasks:
        print("No tasks to search or filter.")
        return

    filtered_tasks = list(tasks) # Start with all tasks

    # Keyword search
    keyword = input("Enter keyword to search in titles (leave blank for no keyword search): ").strip()
    if keyword:
        filtered_tasks = [task for task in filtered_tasks if keyword.lower() in task["title"].lower()]

    # Filter by status
    status_filter = input("Filter by status (completed/incomplete/all, leave blank for all): ").strip().lower()
    if status_filter in ["completed", "incomplete"]:
        is_completed = (status_filter == "completed")
        filtered_tasks = [task for task in filtered_tasks if task["completed"] == is_completed]
    elif status_filter and status_filter != "all":
        print("Invalid status filter. Showing all statuses.")

    # Filter by priority
    priority_filter_input = input("Filter by priority (High/Medium/Low/all, leave blank for all): ").strip()
    priority_filter = validate_priority(priority_filter_input)
    if priority_filter:
        filtered_tasks = [task for task in filtered_tasks if task["priority"] == priority_filter]
    elif priority_filter_input and priority_filter_input != "all":
        print("Invalid priority filter. Showing all priorities.")

    # Filter by tag
    tag_filter_input = input("Filter by tag (leave blank for all): ").strip()
    if tag_filter_input:
        filtered_tasks = [task for task in filtered_tasks if tag_filter_input.lower() in [t.lower() for t in task["tags"]]]

    print("\n--- Search/Filter Results ---")
    if not filtered_tasks:
        print("No tasks found matching your criteria.")
    else:
        for task in filtered_tasks:
            status = "Complete" if task["completed"] else "Incomplete"
            tags_display = ", ".join(task["tags"]) if task["tags"] else "None"
            print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, Tags: {tags_display}")

def sort_tasks():
    """Sorts tasks based on user criteria."""
    print("\n--- Sort Tasks ---")
    if not tasks:
        print("No tasks to sort.")
        return

    while True:
        print("Sort by:")
        print("1. Priority (High to Low)")
        print("2. Title (Alphabetical)")
        print("3. Back to Main Menu")
        sort_choice_input = input("Enter your sort choice (1-3): ")

        try:
            sort_choice = int(sort_choice_input)
            if sort_choice == 1:
                # Custom sort order for priority
                priority_order = {"High": 1, "Medium": 2, "Low": 3}
                sorted_tasks = sorted(tasks, key=lambda task: priority_order.get(task["priority"], 99))
                print("\n--- Tasks Sorted by Priority ---")
                for task in sorted_tasks:
                    status = "Complete" if task["completed"] else "Incomplete"
                    tags_display = ", ".join(task["tags"]) if task["tags"] else "None"
                    print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, Tags: {tags_display}")
                break
            elif sort_choice == 2:
                sorted_tasks = sorted(tasks, key=lambda task: task["title"].lower())
                print("\n--- Tasks Sorted by Title ---")
                for task in sorted_tasks:
                    status = "Complete" if task["completed"] else "Incomplete"
                    tags_display = ", ".join(task["tags"]) if task["tags"] else "None"
                    print(f"ID: {task['id']}, Title: {task['title']}, Status: {status}, Priority: {task['priority']}, Tags: {tags_display}")
                break
            elif sort_choice == 3:
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")

>>>>>>> 002-enhanced-todo-features
def main():
    """Main function to run the application."""
    while True:
        display_menu()
<<<<<<< HEAD
        choice_input = input("Enter your choice (1-6): ")
=======
        choice_input = input("Enter your choice (1-8): ")
>>>>>>> 002-enhanced-todo-features
        
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
<<<<<<< HEAD
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
=======
                search_filter_tasks()
            elif choice == 7:
                sort_tasks()
            elif choice == 8:
                print("Exiting application. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 8.")
>>>>>>> 002-enhanced-todo-features
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

