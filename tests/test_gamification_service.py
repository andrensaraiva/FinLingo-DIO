"""
Tests for FinLingo Gamification Service.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from datetime import datetime, timedelta
from app.services.gamification_service import (
    load_levels, load_badges, get_current_level,
    calculate_level_progress, check_badge_eligibility,
    update_streak, get_encouragement_message, get_xp_for_action,
)


# ─── Level Tests ─────────────────────────────────────

class TestLevels:
    def test_load_levels(self):
        levels = load_levels()
        assert len(levels) > 0
        assert levels[0]["level"] == 1

    def test_level_1_at_zero_xp(self):
        level = get_current_level(0)
        assert level["level"] == 1
        assert level["is_max_level"] is False

    def test_level_increases_with_xp(self):
        level_low = get_current_level(0)
        level_high = get_current_level(500)
        assert level_high["level"] >= level_low["level"]

    def test_max_level(self):
        level = get_current_level(999999)
        assert level["is_max_level"] is True

    def test_level_info_has_required_fields(self):
        level = get_current_level(100)
        assert "level" in level
        assert "title" in level
        assert "xp_current" in level
        assert "xp_for_current" in level
        assert "is_max_level" in level


# ─── Level Progress Tests ───────────────────────────

class TestLevelProgress:
    def test_progress_at_start(self):
        progress = calculate_level_progress(0)
        assert 0.0 <= progress <= 1.0

    def test_progress_at_max(self):
        progress = calculate_level_progress(999999)
        assert progress == 1.0

    def test_progress_increases(self):
        p1 = calculate_level_progress(10)
        p2 = calculate_level_progress(50)
        assert p2 >= p1


# ─── Badge Tests ─────────────────────────────────────

class TestBadges:
    def test_load_badges(self):
        badges = load_badges()
        assert len(badges) > 0
        for badge in badges:
            assert "id" in badge
            assert "name" in badge
            assert "icon" in badge

    def test_no_badges_for_new_user(self):
        user = {
            "xp": 0,
            "total_lessons_completed": 0,
            "total_ai_chats": 0,
            "total_simulations": 0,
            "current_streak": 0,
            "tracks_completed": 0,
            "completed_tracks": [],
            "badges_earned": [],
            "has_perfect_quiz": False,
        }
        new_badges = check_badge_eligibility(user)
        assert len(new_badges) == 0

    def test_first_lesson_badge(self):
        user = {
            "xp": 15,
            "total_lessons_completed": 1,
            "total_ai_chats": 0,
            "total_simulations": 0,
            "current_streak": 0,
            "tracks_completed": 0,
            "completed_tracks": [],
            "badges_earned": [],
            "has_perfect_quiz": False,
        }
        new_badges = check_badge_eligibility(user)
        badge_ids = [b["id"] for b in new_badges]
        assert "first_step" in badge_ids

    def test_already_earned_badge_not_repeated(self):
        user = {
            "xp": 15,
            "total_lessons_completed": 1,
            "total_ai_chats": 0,
            "total_simulations": 0,
            "current_streak": 0,
            "tracks_completed": 0,
            "completed_tracks": [],
            "badges_earned": ["first_step"],
            "has_perfect_quiz": False,
        }
        new_badges = check_badge_eligibility(user)
        badge_ids = [b["id"] for b in new_badges]
        assert "first_step" not in badge_ids


# ─── Streak Tests ────────────────────────────────────

class TestStreak:
    def test_first_activity_sets_streak_to_1(self):
        user = {"current_streak": 0}
        updated = update_streak(user)
        assert updated["current_streak"] == 1

    def test_same_day_no_change(self):
        today = datetime.now().date().strftime("%Y-%m-%d")
        user = {"current_streak": 5, "last_activity_date": today, "max_streak": 5}
        updated = update_streak(user)
        assert updated["current_streak"] == 5

    def test_consecutive_day_increments(self):
        yesterday = (datetime.now().date() - timedelta(days=1)).strftime("%Y-%m-%d")
        user = {"current_streak": 3, "last_activity_date": yesterday, "max_streak": 5}
        updated = update_streak(user)
        assert updated["current_streak"] == 4

    def test_missed_day_resets(self):
        two_days_ago = (datetime.now().date() - timedelta(days=2)).strftime("%Y-%m-%d")
        user = {"current_streak": 10, "last_activity_date": two_days_ago, "max_streak": 10}
        updated = update_streak(user)
        assert updated["current_streak"] == 1

    def test_max_streak_preserved(self):
        yesterday = (datetime.now().date() - timedelta(days=1)).strftime("%Y-%m-%d")
        user = {"current_streak": 5, "last_activity_date": yesterday, "max_streak": 20}
        updated = update_streak(user)
        assert updated["max_streak"] == 20


# ─── Encouragement Messages Tests ───────────────────

class TestEncouragement:
    def test_correct_message(self):
        msg = get_encouragement_message("correct")
        assert isinstance(msg, str)
        assert len(msg) > 0

    def test_incorrect_message(self):
        msg = get_encouragement_message("incorrect")
        assert isinstance(msg, str)
        assert len(msg) > 0

    def test_quiz_complete_message(self):
        msg = get_encouragement_message("quiz_complete", score=3, total=5)
        assert isinstance(msg, str)

    def test_perfect_quiz_message(self):
        msg = get_encouragement_message("quiz_complete", score=5, total=5)
        assert isinstance(msg, str)


# ─── XP Action Tests ────────────────────────────────

class TestXPForAction:
    def test_known_actions(self):
        assert get_xp_for_action("lesson_complete") > 0
        assert get_xp_for_action("quiz_correct") > 0
        assert get_xp_for_action("ai_chat") > 0
        assert get_xp_for_action("simulation") > 0

    def test_unknown_action_returns_zero(self):
        assert get_xp_for_action("nonexistent_action") == 0
