"""
CLI menu.

Owned by: Person 5 (CLI Menu)

This module's only job is talking to the human: showing the menu,
reading input, and calling into TaskService. It contains no business
logic and knows nothing about how tasks are stored.
"""

from src.services.task_service import TaskService
from src.utils.validators import ValidationError

MENU_TEXT = """
==== Team Task Manager ====
1. List tasks
2. Add task
3. Complete task
4. Delete task
5. Search tasks
6. Exit
"""


def run(service: TaskService) -> None:
    while True:
        print(MENU_TEXT)
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            _list_tasks(service)
        elif choice == "2":
            _add_task(service)
        elif choice == "3":
            _complete_task(service)
        elif choice == "4":
            _delete_task(service)
        elif choice == "5":
            _search_tasks(service)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("That's not a valid option — try again.")


def _list_tasks(service: TaskService) -> None:
    tasks = service.list_tasks()
    if not tasks:
        print("No tasks yet — add one!")
        return
    for task in tasks:
        print(task)


def _add_task(service: TaskService) -> None:
    title = input("Task title: ")
    priority = input("Priority (low/medium/high) [medium]: ") or "medium"
    try:
        task = service.add_task(title, priority)
        print(f"Added: {task}")
    except ValidationError as e:
        print(f"Couldn't add task: {e}")


def _complete_task(service: TaskService) -> None:
    task_id = _read_task_id()
    if task_id is None:
        return
    if service.mark_complete(task_id):
        print(f"Task #{task_id} marked complete.")
    else:
        print(f"No task found with id #{task_id}.")


def _delete_task(service: TaskService) -> None:
    task_id = _read_task_id()
    if task_id is None:
        return
    if service.delete_task(task_id):
        print(f"Task #{task_id} deleted.")
    else:
        print(f"No task found with id #{task_id}.")


def _search_tasks(service: TaskService) -> None:
    keyword = input("Search keyword: ")
    results = service.search_tasks(keyword)
    if not results:
        print("No matching tasks.")
        return
    for task in results:
        print(task)


def _read_task_id():
    raw = input("Task id: ").strip()
    if not raw.isdigit():
        print("Please enter a numeric task id.")
        return None
    return int(raw)