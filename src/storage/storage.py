"""
Persistence layer.

Owned by: Person 3 (Storage)

This is the only module in the app that knows tasks live in a JSON file
on disk. If the team ever swaps JSON for SQLite or a real database,
this is the only file that should need to change.
"""

import json
import os
from typing import List

from src.models.task import Task

DEFAULT_STORAGE_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "tasks.json",
)


def load_tasks(path: str = DEFAULT_STORAGE_PATH) -> List[Task]:
    """Load all tasks from the JSON file. Returns an empty list if the
    file doesn't exist yet or is empty."""
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        contents = f.read().strip()
        if not contents:
            return []
        raw = json.loads(contents)

    return [Task.from_dict(item) for item in raw]


def save_tasks(tasks: List[Task], path: str = DEFAULT_STORAGE_PATH) -> None:
    """Write all tasks back out to the JSON file, pretty-printed."""
    raw = [task.to_dict() for task in tasks]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(raw, f, indent=2)
        f.write("\n")