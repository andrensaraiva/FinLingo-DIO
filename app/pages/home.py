"""
FinLingo — Home / Dashboard Page
Main dashboard with user greeting, progress, and navigation.
"""

import streamlit as st
import random
import json
from app.config import APP_NAME, MASCOT_NAME, DATA_DIR
from app.services.gamification_service import get_current_level, calculate_level_progress
from app.services.lesson_service import load_tracks, get_track_progress


def render_home():
    """Render the home dashboard."""
    user = st.session_state.user_data
    name = user.get("user_name", "Learner")
    xp = user.get("xp", 0)
    streak = user.get("current_streak", 0)
    level_info = get_current_level(xp)

    # ─── Header ─────────────────────────────────────
    col1, col2, col3 = st.columns([3, 1, 1])
    with col1:
        st.markdown(f"### 👋 Hey, {name}!")
    with col2:
        st.metric("🔥 Streak", f"{streak} day{'s' if streak != 1 else ''}")
    with col3:
        st.metric("⭐ XP", f"{xp}")

    st.markdown(f"**{level_info['title']}** — Level {level_info['level']}")
    if not level_info["is_max_level"]:
        progress = calculate_level_progress(xp)
        st.progress(progress, text=f"{xp} / {level_info['xp_for_next']} XP to next level")

    st.markdown("---")

    # ─── Continue Learning Card ─────────────────────
    current_track = user.get("current_track")
    last_lesson = user.get("last_lesson")

    if current_track:
        tracks = load_tracks()
        track_info = next((t for t in tracks if t["id"] == current_track), None)
        if track_info:
            progress = get_track_progress(current_track, user.get("completed_lessons", []))
            st.markdown(
                f"""
                <div style='background: linear-gradient(135deg, #F0FDF4, #ECFDF5);
                            padding: 20px; border-radius: 12px; border: 1px solid #D1FAE5;
                            margin-bottom: 16px;'>
                    <strong>📖 Continue Learning</strong><br>
                    {track_info['icon']} {track_info['title']} — {progress['percentage']}% complete<br>
                </div>
                """, unsafe_allow_html=True
            )
            if st.button("Continue →", key="continue_btn", type="primary"):
                st.session_state.current_page = "learning_paths"
                st.session_state.selected_track = current_track
                st.rerun()
    else:
        st.info("📚 Start your first learning track to begin your journey!")

    st.markdown("")

    # ─── Quick Actions ──────────────────────────────
    st.markdown("### ⚡ Quick Actions")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("📚\nLearn", use_container_width=True):
            st.session_state.current_page = "learning_paths"
            st.rerun()
    with col2:
        if st.button("💬\nChat", use_container_width=True):
            st.session_state.current_page = "chat"
            st.rerun()
    with col3:
        if st.button("🔢\nSimulators", use_container_width=True):
            st.session_state.current_page = "simulators"
            st.rerun()
    with col4:
        if st.button("📊\nProgress", use_container_width=True):
            st.session_state.current_page = "progress"
            st.rerun()

    st.markdown("---")

    # ─── Learning Paths Overview ────────────────────
    st.markdown("### 📚 Learning Paths")
    tracks = load_tracks()

    cols = st.columns(3)
    for i, track in enumerate(tracks):
        with cols[i % 3]:
            progress = get_track_progress(track["id"], user.get("completed_lessons", []))
            status = "✅" if progress["is_complete"] else f"{progress['percentage']}%"

            if st.button(
                f"{track['icon']}\n{track['title']}\n{status}",
                key=f"track_{track['id']}",
                use_container_width=True
            ):
                st.session_state.current_page = "learning_paths"
                st.session_state.selected_track = track["id"]
                st.rerun()

    st.markdown("---")

    # ─── Daily Tip ──────────────────────────────────
    try:
        with open(DATA_DIR / "tips.json", "r", encoding="utf-8") as f:
            tips = json.load(f)["tips"]
        tip = random.choice(tips)
        st.markdown(
            f"""
            <div style='background: #FFF7ED; padding: 16px; border-radius: 12px;
                        border: 1px solid #FED7AA;'>
                🦊 <strong>{MASCOT_NAME}'s Tip of the Day</strong><br>
                {tip}
            </div>
            """, unsafe_allow_html=True
        )
    except FileNotFoundError:
        pass

    # ─── Footer Navigation ─────────────────────────
    st.markdown("---")
    _render_nav_bar()


def _render_nav_bar():
    """Render bottom navigation."""
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        if st.button("🏠 Home", key="nav_home", use_container_width=True):
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        if st.button("📚 Learn", key="nav_learn", use_container_width=True):
            st.session_state.current_page = "learning_paths"
            st.rerun()
    with col3:
        if st.button("💬 Chat", key="nav_chat", use_container_width=True):
            st.session_state.current_page = "chat"
            st.rerun()
    with col4:
        if st.button("📊 Progress", key="nav_progress", use_container_width=True):
            st.session_state.current_page = "progress"
            st.rerun()
    with col5:
        if st.button("👤 Profile", key="nav_profile", use_container_width=True):
            st.session_state.current_page = "profile"
            st.rerun()
