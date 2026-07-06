"""
Input validation helpers.

Owned by: Person 4 (paired with Task Service)

Keeping validation here — rather than scattered through the CLI or the
service layer — means every part of the app agrees on what a "valid"
title or priority looks like.
"""

from src.models.task import VALID_PRIORITIES


class ValidationError(ValueError):
    """Raised when user-provided task data is invalid."""


def validate_title(title: str) -> str:
    """Ensure a task title is non-empty and reasonably sized."""
    if title is None:
        raise ValidationError("Title is required.")
    cleaned = title.strip()
    if not cleaned:
        raise ValidationError("Title cannot be empty.")
    if len(cleaned) > 200:
        raise ValidationError("Title must be 200 characters or fewer.")
    return cleaned


def validate_priority(priority: str) -> str:
    """Ensure a priority is one of the values the app understands."""
    if priority is None:
        return "medium"
    cleaned = priority.strip().lower()
    if cleaned not in VALID_PRIORITIES:
        raise ValidationError(
            f"Priority must be one of {VALID_PRIORITIES}, got '{priority}'."
        )
    return cleaned