"""
FinLingo — User Service Module
Handles user data persistence and session management.
"""

import json
from pathlib import Path
from datetime import datetime
from app.config import STORAGE_DIR


DEFAULT_USER_DATA = {
    "user_name": "Learner",
    "experience_level": "beginner",
    "xp": 0,
    "current_streak": 0,
    "max_streak": 0,
    "last_activity_date": None,
    "completed_lessons": [],
    "completed_tracks": [],
    "quiz_scores": {},
    "badges_earned": [],
    "total_lessons_completed": 0,
    "total_quizzes_completed": 0,
    "total_ai_chats": 0,
    "total_simulations": 0,
    "has_perfect_quiz": False,
    "tracks_completed": 0,
    "onboarding_complete": False,
    "created_at": None,
    "current_track": None,
    "last_lesson": None,
    "activity_dates": []
}


def get_user_data_path() -> Path:
    """Get the path to the user data file."""
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    return STORAGE_DIR / "user_data.json"


def load_user_data() -> dict:
    """Load user data from storage."""
    filepath = get_user_data_path()
    if filepath.exists():
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Merge with defaults to ensure all keys exist
        return {**DEFAULT_USER_DATA, **data}
    return {**DEFAULT_USER_DATA, "created_at": datetime.now().isoformat()}


def save_user_data(data: dict) -> None:
    """Save user data to storage."""
    filepath = get_user_data_path()
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def update_user_xp(data: dict, xp_gained: int) -> dict:
    """Add XP to user data."""
    data["xp"] = data.get("xp", 0) + xp_gained
    return data


def mark_lesson_complete(data: dict, track_id: str, lesson_id: str) -> dict:
    """Mark a lesson as completed."""
    if lesson_id not in data.get("completed_lessons", []):
        data.setdefault("completed_lessons", []).append(lesson_id)
        data["total_lessons_completed"] = len(data["completed_lessons"])
        data["current_track"] = track_id
        data["last_lesson"] = lesson_id
    return data


def mark_track_complete(data: dict, track_id: str) -> dict:
    """Mark a track as completed."""
    if track_id not in data.get("completed_tracks", []):
        data.setdefault("completed_tracks", []).append(track_id)
        data["tracks_completed"] = len(data["completed_tracks"])
    return data


def record_quiz_score(data: dict, quiz_id: str, score: int, total: int) -> dict:
    """Record a quiz score."""
    data.setdefault("quiz_scores", {})[quiz_id] = {
        "score": score,
        "total": total,
        "percentage": round((score / total) * 100) if total > 0 else 0,
        "date": datetime.now().isoformat()
    }
    data["total_quizzes_completed"] = data.get("total_quizzes_completed", 0) + 1
    if score == total:
        data["has_perfect_quiz"] = True
    return data


def record_activity(data: dict) -> dict:
    """Record today's activity for streak tracking."""
    today = datetime.now().strftime("%Y-%m-%d")
    activity_dates = data.get("activity_dates", [])
    if today not in activity_dates:
        activity_dates.append(today)
        data["activity_dates"] = activity_dates[-90:]  # Keep last 90 days
    return data


def increment_counter(data: dict, counter_name: str) -> dict:
    """Increment a named counter (total_ai_chats, total_simulations, etc.)."""
    data[counter_name] = data.get(counter_name, 0) + 1
    return data


def reset_progress(data: dict) -> dict:
    """Reset all progress while keeping the user name."""
    user_name = data.get("user_name", "Learner")
    new_data = {**DEFAULT_USER_DATA}
    new_data["user_name"] = user_name
    new_data["created_at"] = datetime.now().isoformat()
    new_data["onboarding_complete"] = True  # Don't repeat onboarding
    return new_data


def get_user_context(data: dict) -> dict:
    """Extract AI-relevant context from user data."""
    from app.services.gamification_service import get_current_level
    level_info = get_current_level(data.get("xp", 0))
    return {
        "user_name": data.get("user_name", "Learner"),
        "current_track": data.get("current_track", "None"),
        "last_lesson": data.get("last_lesson", "None"),
        "level": level_info["level"]
    }
