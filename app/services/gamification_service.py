"""
FinLingo — Gamification Service Module
XP, levels, badges, streaks, and progress tracking.
"""

import json
from datetime import datetime, timedelta
from app.config import (
    DATA_DIR, STORAGE_DIR,
    XP_LESSON_COMPLETE, XP_QUIZ_CORRECT, XP_QUIZ_INCORRECT,
    XP_QUIZ_COMPLETE_BONUS, XP_QUIZ_PERFECT_BONUS,
    XP_AI_CHAT, XP_SIMULATION, XP_DAILY_LOGIN
)


def load_levels() -> list:
    """Load level definitions from JSON."""
    with open(DATA_DIR / "levels.json", "r", encoding="utf-8") as f:
        return json.load(f)["levels"]


def load_badges() -> list:
    """Load badge definitions from JSON."""
    with open(DATA_DIR / "badges.json", "r", encoding="utf-8") as f:
        return json.load(f)["badges"]


def get_current_level(xp: int) -> dict:
    """Determine user's current level based on XP."""
    levels = load_levels()
    current = levels[0]
    next_level = levels[1] if len(levels) > 1 else None

    for i, level in enumerate(levels):
        if xp >= level["xp_required"]:
            current = level
            next_level = levels[i + 1] if i + 1 < len(levels) else None

    return {
        "level": current["level"],
        "title": current["title"],
        "xp_current": xp,
        "xp_for_current": current["xp_required"],
        "xp_for_next": next_level["xp_required"] if next_level else None,
        "next_title": next_level["title"] if next_level else None,
        "is_max_level": next_level is None
    }


def calculate_level_progress(xp: int) -> float:
    """Calculate progress percentage toward next level (0.0 to 1.0)."""
    level_info = get_current_level(xp)
    if level_info["is_max_level"]:
        return 1.0

    xp_in_level = xp - level_info["xp_for_current"]
    xp_needed = level_info["xp_for_next"] - level_info["xp_for_current"]

    return min(xp_in_level / xp_needed, 1.0) if xp_needed > 0 else 1.0


def check_badge_eligibility(user_data: dict) -> list:
    """
    Check which badges the user has newly earned.

    Args:
        user_data: Dict containing user progress data.

    Returns:
        List of newly earned badge IDs.
    """
    badges = load_badges()
    earned = user_data.get("badges_earned", [])
    new_badges = []

    conditions = {
        "complete_first_lesson": user_data.get("total_lessons_completed", 0) >= 1,
        "perfect_quiz_score": user_data.get("has_perfect_quiz", False),
        "first_ai_chat": user_data.get("total_ai_chats", 0) >= 1,
        "first_simulation": user_data.get("total_simulations", 0) >= 1,
        "streak_3": user_data.get("current_streak", 0) >= 3,
        "streak_7": user_data.get("current_streak", 0) >= 7,
        "complete_track": user_data.get("tracks_completed", 0) >= 1,
        "complete_spending_control": "spending_control" in user_data.get("completed_tracks", []),
        "complete_digital_safety": "digital_banking_safety" in user_data.get("completed_tracks", []),
        "complete_all_tracks": user_data.get("tracks_completed", 0) >= 7,
    }

    for badge in badges:
        if badge["id"] not in earned:
            condition_key = badge["condition"]
            if conditions.get(condition_key, False):
                new_badges.append(badge)

    return new_badges


def update_streak(user_data: dict) -> dict:
    """
    Update the user's streak based on their last activity date.

    Args:
        user_data: Dict containing last_activity_date and current_streak.

    Returns:
        Updated user_data with new streak info.
    """
    today = datetime.now().date()
    last_activity = user_data.get("last_activity_date")

    if last_activity:
        last_date = datetime.strptime(last_activity, "%Y-%m-%d").date()
        days_diff = (today - last_date).days

        if days_diff == 0:
            # Already active today, no change
            pass
        elif days_diff == 1:
            # Consecutive day — increment streak
            user_data["current_streak"] = user_data.get("current_streak", 0) + 1
        else:
            # Missed a day — reset streak
            user_data["current_streak"] = 1
    else:
        # First ever activity
        user_data["current_streak"] = 1

    user_data["last_activity_date"] = today.strftime("%Y-%m-%d")
    user_data["max_streak"] = max(
        user_data.get("max_streak", 0),
        user_data.get("current_streak", 1)
    )

    return user_data


def get_encouragement_message(action: str, score: int = None, total: int = None) -> str:
    """Generate an encouraging feedback message based on the action."""
    import random

    messages = {
        "correct": [
            "Nailed it! 🎯",
            "You're on a roll! 🔥",
            "Fino is impressed! 🦊",
            "That's the one! ✨",
            "Perfect answer! 💪"
        ],
        "incorrect": [
            "Not quite, but you're learning — that's what counts!",
            "Close! Here's the right answer. You'll get it next time. 💪",
            "Mistakes are how we grow. Let's keep going!",
            "Almost there! Keep that curiosity flowing. 🌟"
        ],
        "lesson_complete": [
            "Awesome! Another lesson in the books! 📚",
            "You're making great progress! 🚀",
            "Knowledge gained! Keep up the momentum! 💡",
            "One step closer to financial confidence! 🎓"
        ],
        "quiz_perfect": [
            "🎉 Perfect score! You absolutely crushed it!",
            "100%! You're a natural! 🌟",
            "Flawless! Fino is doing a happy dance! 🦊💃"
        ],
        "streak": [
            "🔥 Your streak is growing! Consistency is key!",
            "Another day, another lesson! You're building an amazing habit!",
            "Look at that streak! You're unstoppable! 💪"
        ],
        "level_up": [
            "🎉 Level up! You're growing as a financial learner!",
            "🏆 New level unlocked! The journey continues!",
            "📈 You've leveled up! Your dedication is paying off!"
        ]
    }

    if action == "quiz_complete" and score is not None and total is not None:
        if score == total:
            return random.choice(messages["quiz_perfect"])
        elif score >= total * 0.8:
            return f"Great job! {score}/{total} — almost perfect! 🌟"
        elif score >= total * 0.5:
            return f"Good effort! {score}/{total} — you're learning! 📚"
        else:
            return f"{score}/{total} — keep practicing, you'll get there! 💪"

    return random.choice(messages.get(action, messages["lesson_complete"]))


def get_xp_for_action(action: str) -> int:
    """Get XP amount for a specific action."""
    xp_map = {
        "lesson_complete": XP_LESSON_COMPLETE,
        "quiz_correct": XP_QUIZ_CORRECT,
        "quiz_incorrect": XP_QUIZ_INCORRECT,
        "quiz_complete": XP_QUIZ_COMPLETE_BONUS,
        "quiz_perfect": XP_QUIZ_PERFECT_BONUS,
        "ai_chat": XP_AI_CHAT,
        "simulation": XP_SIMULATION,
        "daily_login": XP_DAILY_LOGIN,
    }
    return xp_map.get(action, 0)
