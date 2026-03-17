"""
FinLingo — Lesson Page
Displays lesson content with pages.
"""

import streamlit as st
from app.services.lesson_service import get_lesson, get_next_lesson, get_track_progress, load_tracks
from app.services.user_service import (
    save_user_data, update_user_xp, mark_lesson_complete, mark_track_complete
)
from app.services.gamification_service import get_xp_for_action, get_encouragement_message
from app.config import MASCOT_NAME


def render_lesson():
    """Render a lesson screen."""
    track_id = st.session_state.get("current_lesson_track")
    lesson_id = st.session_state.get("current_lesson_id")

    if not track_id or not lesson_id:
        st.error("No lesson selected.")
        if st.button("← Go Back"):
            st.session_state.current_page = "learning_paths"
            st.rerun()
        return

    lesson = get_lesson(track_id, lesson_id)
    if not lesson:
        st.error("Lesson not found.")
        return

    # Page navigation state
    if "lesson_page" not in st.session_state:
        st.session_state.lesson_page = 0

    current_page = st.session_state.lesson_page
    total_pages = len(lesson.get("pages", []))

    # ─── Header ─────────────────────────────────────
    tracks = load_tracks()
    track = next((t for t in tracks if t["id"] == track_id), None)
    track_name = track["title"] if track else track_id

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.lesson_page = 0
            st.session_state.current_page = "learning_paths"
            st.session_state.selected_track = track_id
            st.rerun()
    with col2:
        st.markdown(f"### 📖 {lesson['title']}")
        st.markdown(f"<small style='color: #475569;'>📚 {track_name}</small>", unsafe_allow_html=True)

    # Progress indicator
    st.progress((current_page + 1) / total_pages,
               text=f"Page {current_page + 1} of {total_pages}")

    st.markdown("---")

    # ─── Content ────────────────────────────────────
    if current_page < total_pages:
        page = lesson["pages"][current_page]

        # Main content (supports markdown)
        st.markdown(page["content"])

        # Did You Know callout
        if page.get("did_you_know"):
            st.info(f"💡 **Did You Know?** {page['did_you_know']}")

        # Key terms
        if page.get("key_terms") and len(page["key_terms"]) > 0:
            with st.expander("📝 Key Terms in This Page"):
                for term in page["key_terms"]:
                    st.markdown(f"• **{term}**")

    st.markdown("---")

    # ─── Navigation ─────────────────────────────────
    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        if current_page > 0:
            if st.button("← Previous"):
                st.session_state.lesson_page = current_page - 1
                st.rerun()

    with col3:
        if current_page < total_pages - 1:
            if st.button("Next →", type="primary"):
                st.session_state.lesson_page = current_page + 1
                st.rerun()
        else:
            # Last page — complete lesson
            if st.button("✅ Complete & Take Quiz", type="primary"):
                _complete_lesson(track_id, lesson_id)

    # ─── Disclaimer ─────────────────────────────────
    st.markdown(
        "<div class='disclaimer'>💡 This content is for educational purposes only. "
        "Not financial advice.</div>",
        unsafe_allow_html=True
    )


def _complete_lesson(track_id: str, lesson_id: str):
    """Mark lesson as complete and navigate to quiz."""
    user = st.session_state.user_data

    # Award XP
    xp = get_xp_for_action("lesson_complete")
    user = update_user_xp(user, xp)

    # Mark complete
    user = mark_lesson_complete(user, track_id, lesson_id)

    # Check if track is complete
    progress = get_track_progress(track_id, user.get("completed_lessons", []))
    if progress["is_complete"]:
        user = mark_track_complete(user, track_id)

    st.session_state.user_data = user
    save_user_data(user)

    # Show completion message
    st.toast(f"📚 Lesson complete! +{xp} XP", icon="✅")

    # Navigate to quiz
    st.session_state.lesson_page = 0
    st.session_state.current_page = "quiz"
    st.session_state.quiz_track = track_id
    st.session_state.quiz_lesson = lesson_id
    st.rerun()
