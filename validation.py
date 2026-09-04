def validate_task_title(title):
    """
    Validates that the task title is a non-empty string.
    """
    if not isinstance(title, str):
        return False
    if len(title.strip()) == 0:
        return False
    return True


def validate_task_id(task_id, tasks):
    """
    Validates that task_id is a valid integer index within tasks list.
    """
    try:
        idx = int(task_id)
        if 0 <= idx < len(tasks):
            return True
        return False
    except ValueError:
        return False