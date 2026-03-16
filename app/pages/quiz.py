"""
FinLingo — Quiz Page
Interactive quiz with immediate feedback.
"""

import streamlit as st
from app.services.quiz_service import load_quiz, check_answer, score_quiz
from app.services.user_service import save_user_data, update_user_xp, record_quiz_score
from app.services.gamification_service import get_encouragement_message
from app.services.lesson_service import load_tracks
from app.config import MASCOT_NAME


def render_quiz():
    """Render the quiz screen."""
    track_id = st.session_state.get("quiz_track")
    lesson_id = st.session_state.get("quiz_lesson")

    if not track_id:
        st.error("No quiz selected.")
        if st.button("← Go Back"):
            st.session_state.current_page = "home"
            st.rerun()
        return

    questions = load_quiz(track_id, lesson_id)

    if not questions:
        st.warning("No quiz questions available for this lesson yet.")
        if st.button("← Back to Learning Paths"):
            st.session_state.current_page = "learning_paths"
            st.session_state.selected_track = track_id
            st.rerun()
        return

    # Initialize quiz state
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_answers = []
        st.session_state.quiz_submitted = False
        st.session_state.quiz_results = None

    # ─── Header ─────────────────────────────────────
    tracks = load_tracks()
    track = next((t for t in tracks if t["id"] == track_id), None)
    track_name = track["title"] if track else track_id

    st.markdown(f"### 🧠 Quiz: {track_name}")

    # Check if quiz is complete
    if st.session_state.quiz_results is not None:
        _render_results(questions, track_id, lesson_id)
        return

    idx = st.session_state.quiz_index
    total = len(questions)

    # Progress
    st.progress((idx + 1) / total, text=f"Question {idx + 1} of {total}")
    st.markdown("---")

    # ─── Question ───────────────────────────────────
    question = questions[idx]
    st.markdown(f"**{question['question']}**")
    st.markdown("")

    if question["type"] == "true_false":
        _render_true_false(question, idx)
    else:
        _render_multiple_choice(question, idx)


def _render_multiple_choice(question: dict, idx: int):
    """Render a multiple choice question."""
    answer_key = f"answer_{idx}"

    if not st.session_state.quiz_submitted:
        selected = st.radio(
            "Select your answer:",
            options=range(len(question["options"])),
            format_func=lambda i: question["options"][i],
            key=answer_key,
            label_visibility="collapsed"
        )

        st.markdown("")
        if st.button("Check Answer ✓", type="primary"):
            result = check_answer(question, selected)
            st.session_state.quiz_answers.append(selected)
            st.session_state.quiz_submitted = True
            st.session_state.last_result = result
            st.rerun()
    else:
        _show_feedback(question, st.session_state.last_result)


def _render_true_false(question: dict, idx: int):
    """Render a true/false question."""
    if not st.session_state.quiz_submitted:
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ True", use_container_width=True, key=f"true_{idx}"):
                result = check_answer(question, True)
                st.session_state.quiz_answers.append(True)
                st.session_state.quiz_submitted = True
                st.session_state.last_result = result
                st.rerun()
        with col2:
            if st.button("❌ False", use_container_width=True, key=f"false_{idx}"):
                result = check_answer(question, False)
                st.session_state.quiz_answers.append(False)
                st.session_state.quiz_submitted = True
                st.session_state.last_result = result
                st.rerun()
    else:
        _show_feedback(question, st.session_state.last_result)


def _show_feedback(question: dict, result: dict):
    """Show feedback for the current question."""
    if result["is_correct"]:
        st.success(f"🎯 Correct! +{result['xp_earned']} XP")
        st.markdown(f"🦊 *{get_encouragement_message('correct')}*")
    else:
        st.error(f"Not quite! The correct answer: **{result['correct_answer']}**")
        st.markdown(f"🦊 *{get_encouragement_message('incorrect')}*  (+{result['xp_earned']} XP for trying!)")

    if result.get("explanation"):
        st.info(f"💡 **Explanation:** {result['explanation']}")

    st.markdown("")

    questions = load_quiz(st.session_state.quiz_track, st.session_state.quiz_lesson)
    idx = st.session_state.quiz_index

    if idx < len(questions) - 1:
        if st.button("Next Question →", type="primary"):
            st.session_state.quiz_index += 1
            st.session_state.quiz_submitted = False
            st.session_state.last_result = None
            st.rerun()
    else:
        if st.button("See Results →", type="primary"):
            # Score the full quiz
            results = score_quiz(questions, st.session_state.quiz_answers)
            st.session_state.quiz_results = results

            # Update user data
            user = st.session_state.user_data
            user = update_user_xp(user, results["xp_earned"])
            user = record_quiz_score(
                user,
                f"{st.session_state.quiz_track}_{st.session_state.quiz_lesson}",
                results["score"],
                results["total"]
            )
            st.session_state.user_data = user
            save_user_data(user)
            st.rerun()


def _render_results(questions: list, track_id: str, lesson_id: str):
    """Render the quiz results summary."""
    results = st.session_state.quiz_results

    st.markdown("---")

    # Score display
    if results["is_perfect"]:
        st.markdown("## 🎉 Perfect Score!")
        st.balloons()
    elif results["percentage"] >= 80:
        st.markdown("## 🌟 Great Job!")
    elif results["percentage"] >= 50:
        st.markdown("## 📚 Good Effort!")
    else:
        st.markdown("## 💪 Keep Practicing!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Score", f"{results['score']}/{results['total']}")
    with col2:
        st.metric("Percentage", f"{results['percentage']}%")
    with col3:
        st.metric("XP Earned", f"+{results['xp_earned']}")

    st.markdown("")
    message = get_encouragement_message(
        "quiz_complete", score=results["score"], total=results["total"]
    )
    st.markdown(f"🦊 **{MASCOT_NAME}:** *{message}*")

    st.markdown("---")

    # Action buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🏠 Home", use_container_width=True):
            _cleanup_quiz_state()
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        if st.button("📚 Continue Learning", use_container_width=True, type="primary"):
            _cleanup_quiz_state()
            st.session_state.current_page = "learning_paths"
            st.session_state.selected_track = track_id
            st.rerun()
    with col3:
        if st.button("💬 Ask Fino", use_container_width=True):
            _cleanup_quiz_state()
            st.session_state.current_page = "chat"
            st.rerun()


def _cleanup_quiz_state():
    """Clean up quiz-related session state."""
    for key in ["quiz_index", "quiz_answers", "quiz_submitted", "quiz_results",
                "quiz_track", "quiz_lesson", "last_result"]:
        if key in st.session_state:
            del st.session_state[key]
