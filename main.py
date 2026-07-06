"""
Entry point for the Team Task Manager CLI.

Run with:
    python main.py
"""

from src.services.task_service import TaskService
from src.cli import menu


def main() -> None:
    service = TaskService()
    menu.run(service)


if __name__ == "__main__":
    main()