"""
Tests for FinLingo Quiz Service.
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from app.services.quiz_service import load_quiz, check_answer, score_quiz


# ─── Load Quiz Tests ─────────────────────────────────

class TestLoadQuiz:
    def test_load_existing_quiz(self):
        """Should load quiz questions from a known track/lesson."""
        questions = load_quiz("credit_card_basics", "ccb_01")
        assert questions is not None
        assert len(questions) > 0

    def test_load_quiz_has_required_fields(self):
        """Each question should have required fields."""
        questions = load_quiz("credit_card_basics", "ccb_01")
        for q in questions:
            assert "id" in q
            assert "type" in q
            assert "question" in q
            assert "correct_answer" in q

    def test_load_nonexistent_quiz(self):
        """Should return empty list for nonexistent quiz."""
        questions = load_quiz("nonexistent_track", "nonexistent_lesson")
        assert questions == [] or questions is None

    def test_load_all_track_questions(self):
        """Loading with track only should get all questions for that track."""
        questions = load_quiz("credit_card_basics")
        assert questions is not None
        assert len(questions) > 0


# ─── Check Answer Tests ─────────────────────────────

class TestCheckAnswer:
    def test_correct_multiple_choice(self):
        question = {
            "id": "test_q1",
            "type": "multiple_choice",
            "question": "What is 1+1?",
            "options": ["1", "2", "3"],
            "correct_answer": 1,
            "explanation": "1+1=2"
        }
        result = check_answer(question, 1)
        assert result["is_correct"] is True
        assert result["xp_earned"] > 0

    def test_incorrect_multiple_choice(self):
        question = {
            "id": "test_q2",
            "type": "multiple_choice",
            "question": "What is 1+1?",
            "options": ["1", "2", "3"],
            "correct_answer": 1,
            "explanation": "1+1=2"
        }
        result = check_answer(question, 0)
        assert result["is_correct"] is False

    def test_correct_true_false(self):
        question = {
            "id": "test_q3",
            "type": "true_false",
            "question": "The sky is blue.",
            "correct_answer": True,
            "explanation": "Yes, generally."
        }
        result = check_answer(question, True)
        assert result["is_correct"] is True

    def test_incorrect_true_false(self):
        question = {
            "id": "test_q4",
            "type": "true_false",
            "question": "The sky is blue.",
            "correct_answer": True,
            "explanation": "Yes, generally."
        }
        result = check_answer(question, False)
        assert result["is_correct"] is False


# ─── Score Quiz Tests ────────────────────────────────

class TestScoreQuiz:
    def test_perfect_score(self):
        questions = [
            {"id": "q1", "type": "true_false", "question": "T?",
             "correct_answer": True, "explanation": "Yes"},
            {"id": "q2", "type": "true_false", "question": "T?",
             "correct_answer": False, "explanation": "No"},
        ]
        answers = [True, False]
        result = score_quiz(questions, answers)
        assert result["score"] == 2
        assert result["total"] == 2
        assert result["percentage"] == 100
        assert result["is_perfect"] is True

    def test_zero_score(self):
        questions = [
            {"id": "q1", "type": "true_false", "question": "T?",
             "correct_answer": True, "explanation": "Yes"},
            {"id": "q2", "type": "true_false", "question": "T?",
             "correct_answer": False, "explanation": "No"},
        ]
        answers = [False, True]
        result = score_quiz(questions, answers)
        assert result["score"] == 0
        assert result["total"] == 2
        assert result["percentage"] == 0
        assert result["is_perfect"] is False

    def test_xp_earned_is_positive(self):
        questions = [
            {"id": "q1", "type": "true_false", "question": "T?",
             "correct_answer": True, "explanation": "Yes"},
        ]
        answers = [True]
        result = score_quiz(questions, answers)
        assert result["xp_earned"] > 0
