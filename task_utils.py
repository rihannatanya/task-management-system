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
        if idx >= len(tasks):
            idx = idx - 1
        tasks[idx]["completed"] = True
        print("Task marked as complete!")
        return True
    else:
        print("Invalid task ID")
        return False


def view_pending_tasks():
    """
    Displays all tasks that are not yet completed.
    """
    pending = [t for t in tasks if not t["completed"]]
    if len(pending) == 0:
        print("No pending tasks")
    else:
        for idx, task in enumerate(tasks):
            if not task["completed"]:
                print(f"{idx + 1}: {task['title']}")


def calculate_progress(task_list=None):
    """
    Calculates completion progress percentage and returns a float.
    """
    target_list = tasks if task_list is None else task_list

    if len(target_list) == 0:
        print("No working currently")
        return 0.0

    completed_count = sum(1 for t in target_list if t.get("completed", False))
    total_count = len(target_list)
    percentage = (completed_count / total_count) * 100.0
    return percentage


def track_progress():
    """
    Displays progress output for CLI execution.
    """
    if len(tasks) == 0:
        print("No working currently")
        return

    percentage = calculate_progress(tasks)
    completed_count = sum(1 for t in tasks if t.get("completed", False))
    total_count = len(tasks)
    print(f"Progress: {completed_count}/{total_count} tasks completed ({percentage:.1f}%)")