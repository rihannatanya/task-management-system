try:
    from task_manager.validation import validate_task_title, validate_task_id
except ModuleNotFoundError:
    from validation import validate_task_title, validate_task_id

tasks = []


def add_task(title):
    """
    Adds a new task dictionary to the global tasks list.
    """
    if validate_task_title(title):
        task = {
            "title": title.strip(),
            "completed": False
        }
        tasks.append(task)
        print("Task added successfully!")
        return True
    else:
        print("Invalid task title")
        return False


def mark_task_complete(task_id):
    """
    Marks the task at index task_id as completed.
    """
    if validate_task_id(task_id, tasks):
        idx = int(task_id)
        tasks[idx]["completed"] = True
        print("Task marked as complete")
        return True
    else:
        print("Invalid task ID")
        return False


def view_pending_tasks():
    """
    Displays all tasks that are not yet completed.
    """
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks")
    else:
        for idx, task in enumerate(tasks):
            if not task["completed"]:
                print(f"{idx}: {task['title']}")


def track_progress():
    """
    Calculates and displays current completion progress.
    """
    if len(tasks) == 0:
        print("No working currently")
        return

    completed_count = sum(1 for t in tasks if t["completed"])
    total_count = len(tasks)
    percentage = (completed_count / total_count) * 100
    print(f"Progress: {completed_count}/{total_count} tasks completed ({percentage:.1f}%)")