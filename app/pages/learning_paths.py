"""
FinLingo — Learning Paths Page
Track overview and lesson map.
"""

import streamlit as st
from app.services.lesson_service import load_tracks, load_track_lessons, get_track_progress


def render_learning_paths():
    """Render learning paths screen."""
    user = st.session_state.user_data
    completed_lessons = user.get("completed_lessons", [])

    # Check if a specific track is selected
    selected = st.session_state.get("selected_track", None)

    if selected:
        _render_lesson_map(selected, completed_lessons)
    else:
        _render_track_list(completed_lessons)


def _render_track_list(completed_lessons: list):
    """Render the list of all tracks."""
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        st.markdown("## 📚 Learning Paths")

    st.markdown("Choose a track to start learning:")
    st.markdown("")

    tracks = load_tracks()

    for track in tracks:
        progress = get_track_progress(track["id"], completed_lessons)

        # Track card
        status_icon = "✅" if progress["is_complete"] else "🔵" if progress["completed_lessons"] > 0 else "⬜"
        difficulty = "⭐ Beginner" if track["difficulty"] == "beginner" else "⭐⭐ Intermediate"

        with st.container():
            col1, col2, col3 = st.columns([1, 4, 1])

            with col1:
                st.markdown(f"<div style='font-size: 2rem; text-align: center;'>{track['icon']}</div>",
                           unsafe_allow_html=True)

            with col2:
                st.markdown(f"**{track['title']}** {status_icon}")
                st.markdown(f"<small>{track['description']}</small>", unsafe_allow_html=True)
                st.progress(progress["percentage"] / 100,
                           text=f"{progress['completed_lessons']}/{progress['total_lessons']} lessons — {difficulty}")

            with col3:
                if st.button("Start →" if progress["completed_lessons"] == 0 else "Continue →",
                            key=f"select_{track['id']}"):
                    st.session_state.selected_track = track["id"]
                    st.rerun()

        st.markdown("---")


def _render_lesson_map(track_id: str, completed_lessons: list):
    """Render the lesson map for a selected track."""
    tracks = load_tracks()
    track = next((t for t in tracks if t["id"] == track_id), None)

    if not track:
        st.error("Track not found.")
        return

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.selected_track = None
            st.rerun()
    with col2:
        st.markdown(f"## {track['icon']} {track['title']}")

    progress = get_track_progress(track_id, completed_lessons)
    st.progress(progress["percentage"] / 100,
               text=f"Track Progress: {progress['completed_lessons']}/{progress['total_lessons']} lessons")

    st.markdown("")

    # Load lessons for this track
    lessons = load_track_lessons(track_id)

    for i, lesson in enumerate(lessons):
        is_completed = lesson["id"] in completed_lessons
        is_current = not is_completed and (
            i == 0 or lessons[i - 1]["id"] in completed_lessons
        )
        is_locked = not is_completed and not is_current

        if is_completed:
            icon = "✅"
            color = "#D1FAE5"
            border = "#10B981"
        elif is_current:
            icon = "🔵"
            color = "#DBEAFE"
            border = "#3B82F6"
        else:
            icon = "🔒"
            color = "#F1F5F9"
            border = "#CBD5E1"

        st.markdown(
            f"""
            <div style='background: {color}; padding: 16px; border-radius: 12px;
                        border: 1px solid {border}; margin-bottom: 8px;'>
                {icon} <strong>Lesson {i + 1}:</strong> {lesson['title']}
                {'<br><small style="color: #10B981;">✓ Completed</small>' if is_completed else ''}
                {'<br><small style="color: #3B82F6;">▶ Ready to start</small>' if is_current else ''}
                {'<br><small style="color: #94A3B8;">🔒 Complete previous lessons first</small>' if is_locked else ''}
            </div>
            """, unsafe_allow_html=True
        )

        if is_current or is_completed:
            label = "Review →" if is_completed else "Start Lesson →"
            if st.button(label, key=f"lesson_{lesson['id']}"):
                st.session_state.current_page = "lesson"
                st.session_state.current_lesson_track = track_id
                st.session_state.current_lesson_id = lesson["id"]
                st.rerun()

    st.markdown("")
