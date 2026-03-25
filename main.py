import json

FILEPATH = "tasks.json"


def load_tasks():
    """Load tasks from storage (returns a list)."""
    try:
        with open(FILEPATH, "r", encoding="utf-8") as file:
            data = json.load(file)

        # Be tolerant to different shapes; prefer a list.
        if isinstance(data, list):
            return data
        if isinstance(data, dict) and isinstance(data.get("tasks"), list):
            return data["tasks"]
        return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        # If the file exists but is empty/corrupt, start fresh.
        return []


def save_tasks(tasks):
    """Persist the given tasks list into the JSON storage file."""
    with open(FILEPATH, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def _next_task_id(tasks):
    """Return the next task id (supports gaps in existing ids)."""
    return max((t.get("id", 0) for t in tasks), default=0) + 1


def _find_task(tasks, task_id):
    """Find a task by id; return None if not found."""
    return next((t for t in tasks if t.get("id") == task_id), None)


def add_task(description):
    """Add a new task with the given description."""
    description = (description or "").strip()
    if not description:
        print("Task description cannot be empty.")
        return

    tasks = load_tasks()
    tasks.append(
        {"id": _next_task_id(tasks), "description": description, "completed": False}
    )
    save_tasks(tasks)
    print(f"Task '{description}' added successfully.")


def view_tasks():
    """Print all tasks and their completion status."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for task in tasks:
        status = "✓" if task.get("completed") else "✗"
        print(f"{task.get('id')}. [{status}] {task.get('description')}")


def mark_task_completed(task_id):
    """Mark the task with `task_id` as completed."""
    tasks = load_tasks()
    task = _find_task(tasks, task_id)
    if not task:
        print(f"Task {task_id} not found.")
        return

    task["completed"] = True
    save_tasks(tasks)
    print(f"Task {task_id} marked as completed.")


def delete_task(task_id):
    """Delete a task by id only if it exists in storage."""
    tasks = load_tasks()
    updated_tasks = [t for t in tasks if t.get("id") != task_id]

    if len(updated_tasks) == len(tasks):
        print(f"Task {task_id} not found. Nothing deleted.")
        return

    save_tasks(updated_tasks)
    print(f"Task {task_id} deleted successfully.")


def main():
    """Interactive CLI menu loop."""
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter the task description: ")
            add_task(description)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter the task ID to mark as completed: "))
            mark_task_completed(task_id)
        elif choice == "4":
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
