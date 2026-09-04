try:
    from task_manager.task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress, calculate_progress, tasks
except ModuleNotFoundError:
    from task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress, calculate_progress, tasks


def main():
    while True:
        try:
            choice = input().strip()
        except EOFError:
            break

        if choice == '1':
            title = input()
            add_task(title)
        elif choice == '2':
            task_id = input()
            mark_task_complete(task_id)
        elif choice == '3':
            view_pending_tasks()
        elif choice == '4':
            track_progress()
        elif choice == '5':
            break


if __name__ == "__main__":
    main()