"""
Task service — the app's business logic.

Owned by: Person 4 (Task Service)

The CLI never touches storage.py or task.py directly. It only talks to
TaskService. That's the Single Responsibility Principle in practice:
this class's one job is "manage the collection of tasks."
"""

from typing import List, Optional

from src.models.task import Task
from src.storage.storage import load_tasks, save_tasks
from src.utils.validators import validate_title, validate_priority


class TaskService:
    def __init__(self, storage_path: Optional[str] = None):
        self._storage_path = storage_path
        self._tasks: List[Task] = self._load()

    def _load(self) -> List[Task]:
        if self._storage_path:
            return load_tasks(self._storage_path)
        return load_tasks()

    def _save(self) -> None:
        if self._storage_path:
            save_tasks(self._tasks, self._storage_path)
        else:
            save_tasks(self._tasks)

    def _next_id(self) -> int:
        if not self._tasks:
            return 1
        return max(task.id for task in self._tasks) + 1

    def list_tasks(self) -> List[Task]:
        return list(self._tasks)

    def add_task(self, title: str, priority: str = "medium") -> Task:
        clean_title = validate_title(title)
        clean_priority = validate_priority(priority)
        task = Task(id=self._next_id(), title=clean_title, priority=clean_priority)
        self._tasks.append(task)
        self._save()
        return task

    def delete_task(self, task_id: int) -> bool:
        before = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.id != task_id]
        deleted = len(self._tasks) != before
        if deleted:
            self._save()
        return deleted

    def mark_complete(self, task_id: int) -> bool:
        task = self._find(task_id)
        if not task:
            return False
        task.mark_complete()
        self._save()
        return True

    def search_tasks(self, keyword: str) -> List[Task]:
        keyword_lower = keyword.strip().lower()
        return [t for t in self._tasks if keyword_lower in t.title.lower()]

    def _find(self, task_id: int) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None