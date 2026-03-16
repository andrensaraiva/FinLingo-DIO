"""
FinLingo — Lesson Service Module
Handles loading and managing lesson content.
"""

import json
from pathlib import Path
from app.config import LESSONS_DIR, DATA_DIR


def load_tracks() -> list:
    """Load all track metadata."""
    with open(DATA_DIR / "tracks.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    return sorted(data["tracks"], key=lambda t: t["order"])


def load_track_lessons(track_id: str) -> list:
    """Load all lessons for a specific track."""
    filepath = LESSONS_DIR / f"{track_id}.json"
    if not filepath.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return sorted(data.get("lessons", []), key=lambda l: l["order"])


def get_lesson(track_id: str, lesson_id: str) -> dict | None:
    """Get a specific lesson by track and lesson ID."""
    lessons = load_track_lessons(track_id)
    for lesson in lessons:
        if lesson["id"] == lesson_id:
            return lesson
    return None


def get_next_lesson(track_id: str, current_lesson_id: str) -> dict | None:
    """Get the next lesson in a track after the current one."""
    lessons = load_track_lessons(track_id)
    for i, lesson in enumerate(lessons):
        if lesson["id"] == current_lesson_id and i + 1 < len(lessons):
            return lessons[i + 1]
    return None


def get_track_progress(track_id: str, completed_lessons: list) -> dict:
    """Calculate progress for a specific track."""
    lessons = load_track_lessons(track_id)
    total = len(lessons)
    completed = sum(1 for l in lessons if l["id"] in completed_lessons)

    return {
        "total_lessons": total,
        "completed_lessons": completed,
        "percentage": round((completed / total) * 100) if total > 0 else 0,
        "is_complete": completed >= total,
        "next_lesson": None if completed >= total else lessons[completed] if completed < len(lessons) else None
    }


def get_overall_progress(completed_lessons: list) -> dict:
    """Calculate overall progress across all tracks."""
    tracks = load_tracks()
    total_lessons = 0
    total_completed = 0
    track_progress = []

    for track in tracks:
        progress = get_track_progress(track["id"], completed_lessons)
        total_lessons += progress["total_lessons"]
        total_completed += progress["completed_lessons"]
        track_progress.append({
            "track_id": track["id"],
            "track_title": track["title"],
            "track_icon": track["icon"],
            **progress
        })

    return {
        "total_lessons": total_lessons,
        "total_completed": total_completed,
        "overall_percentage": round((total_completed / total_lessons) * 100) if total_lessons > 0 else 0,
        "tracks": track_progress
    }
