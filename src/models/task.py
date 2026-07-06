"""
Task model.

Owned by: Person 2 (Task Model)

A Task is the core unit of data in the app. Keeping it in its own module
(and its own class) means nothing else in the codebase needs to know how
a task is stored internally — only how to ask it questions
(to_dict / from_dict) and read its fields.
"""

from dataclasses import dataclass, field
from typing import Optional

VALID_PRIORITIES = ("low", "medium", "high")


@dataclass
class Task:
    """A single to-do item."""

    id: int
    title: str
    completed: bool = False
    priority: str = "medium"

    def mark_complete(self) -> None:
        self.completed = True

    def mark_incomplete(self) -> None:
        self.completed = False

    def to_dict(self) -> dict:
        """Convert this Task into a plain dict, ready for JSON storage."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "priority": self.priority,
        }

    @staticmethod
    def from_dict(data: dict) -> "Task":
        """Rebuild a Task from a dict loaded out of JSON storage."""
        return Task(
            id=data["id"],
            title=data["title"],
            completed=data.get("completed", False),
            priority=data.get("priority", "medium"),
        )

    def __str__(self) -> str:
        status = "x" if self.completed else " "
        return f"[{status}] #{self.id} ({self.priority}) {self.title}"