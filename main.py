from task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress, tasks


def main():
    while True:
        print("\n--- Task Management System ---")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. Track Progress")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            task_id = input("Enter task ID to mark as complete: ")
            mark_task_complete(task_id)
        elif choice == '3':
            view_pending_tasks()
        elif choice == '4':
            track_progress()
        elif choice == '5':
            print("Exiting Task Management System.")
            break
        else:
            print("Invalid choice. Please choose 1-5.")


if __name__ == "__main__":
    main()