"""
FinLingo — Quiz Service Module
Handles quiz loading, scoring, and feedback.
"""

import json
from app.config import QUIZZES_DIR


def load_quiz(track_id: str, lesson_id: str = None) -> list:
    """
    Load quiz questions for a track (optionally filtered by lesson).

    Args:
        track_id: The track identifier.
        lesson_id: Optional lesson ID to filter questions.

    Returns:
        List of question dicts.
    """
    filepath = QUIZZES_DIR / f"{track_id}_quiz.json"
    if not filepath.exists():
        return []

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    questions = []
    for quiz_set in data.get("quizzes", []):
        if lesson_id is None or quiz_set["lesson_id"] == lesson_id:
            questions.extend(quiz_set["questions"])

    return questions


def check_answer(question: dict, user_answer) -> dict:
    """
    Check if the user's answer is correct.

    Args:
        question: The question dict.
        user_answer: The user's selected answer (index for MC, bool for T/F).

    Returns:
        Dict with is_correct, correct_answer, explanation, xp_earned.
    """
    from app.config import XP_QUIZ_CORRECT, XP_QUIZ_INCORRECT

    if question["type"] == "true_false":
        is_correct = user_answer == question["correct_answer"]
        correct_display = "True" if question["correct_answer"] else "False"
    else:  # multiple_choice
        is_correct = user_answer == question["correct_answer"]
        correct_display = question["options"][question["correct_answer"]]

    return {
        "is_correct": is_correct,
        "correct_answer": correct_display,
        "explanation": question.get("explanation", ""),
        "xp_earned": XP_QUIZ_CORRECT if is_correct else XP_QUIZ_INCORRECT
    }


def score_quiz(questions: list, user_answers: list) -> dict:
    """
    Score a complete quiz.

    Args:
        questions: List of question dicts.
        user_answers: List of user answers (same order as questions).

    Returns:
        Dict with score, total, percentage, is_perfect, xp_earned, results.
    """
    from app.config import XP_QUIZ_COMPLETE_BONUS, XP_QUIZ_PERFECT_BONUS

    results = []
    correct_count = 0
    total_xp = 0

    for i, question in enumerate(questions):
        answer = user_answers[i] if i < len(user_answers) else None
        result = check_answer(question, answer)
        results.append(result)

        if result["is_correct"]:
            correct_count += 1
        total_xp += result["xp_earned"]

    # Bonus XP
    total_xp += XP_QUIZ_COMPLETE_BONUS  # Completion bonus
    is_perfect = correct_count == len(questions)
    if is_perfect:
        total_xp += XP_QUIZ_PERFECT_BONUS  # Perfect bonus

    return {
        "score": correct_count,
        "total": len(questions),
        "percentage": round((correct_count / len(questions)) * 100) if questions else 0,
        "is_perfect": is_perfect,
        "xp_earned": total_xp,
        "results": results
    }
