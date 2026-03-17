"""
FinLingo — Progress Page
Display user progress, badges, streaks, and stats.
"""

import streamlit as st
from app.services.gamification_service import get_current_level, calculate_level_progress, load_badges
from app.services.lesson_service import get_overall_progress
from app.config import MASCOT_NAME


def render_progress():
    """Render the progress tracking screen."""
    user = st.session_state.user_data

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        st.markdown("### 📊 Your Progress")

    st.markdown("---")

    # ─── XP & Level ─────────────────────────────────
    xp = user.get("xp", 0)
    level_info = get_current_level(xp)
    progress = calculate_level_progress(xp)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("⭐ Total XP", f"{xp}")
    with col2:
        st.metric("🏅 Level", f"{level_info['level']} — {level_info['title']}")
    with col3:
        if not level_info["is_max_level"]:
            remaining = level_info["xp_for_next"] - xp
            st.metric("📈 Next Level", f"{remaining} XP to go")
        else:
            st.metric("📈 Status", "Max Level! 🏆")

    if not level_info["is_max_level"]:
        st.progress(progress,
                   text=f"{xp} / {level_info['xp_for_next']} XP → {level_info['next_title']}")

    st.markdown("---")

    # ─── Streak ─────────────────────────────────────
    st.markdown("### 🔥 Streak")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Streak", f"{user.get('current_streak', 0)} days")
    with col2:
        st.metric("Best Streak", f"{user.get('max_streak', 0)} days")
    with col3:
        total_active_days = len(user.get("activity_dates", []))
        st.metric("Active Days", f"{total_active_days}")

    # Activity calendar (simplified heatmap)
    activity_dates = user.get("activity_dates", [])
    if activity_dates:
        st.markdown("**📅 Recent Activity:**")
        # Show last 30 days as a simple grid
        _render_activity_grid(activity_dates)

    st.markdown("---")

    # ─── Badges ─────────────────────────────────────
    st.markdown("### 🏅 Badges")

    all_badges = load_badges()
    earned_ids = user.get("badges_earned", [])

    cols = st.columns(5)
    for i, badge in enumerate(all_badges):
        with cols[i % 5]:
            is_earned = badge["id"] in earned_ids
            if is_earned:
                st.markdown(
                    f"<div style='text-align: center; padding: 12px; background: #F0FDF4; "
                    f"border-radius: 12px; border: 2px solid #10B981; margin-bottom: 8px; color: #1E293B;'>"
                    f"<div style='font-size: 2rem;'>{badge['icon']}</div>"
                    f"<span style='font-size: 0.85em;'><strong>{badge['name']}</strong></span>"
                    f"</div>", unsafe_allow_html=True)
            else:
                st.markdown(
                    f"<div style='text-align: center; padding: 12px; background: #F1F5F9; "
                    f"border-radius: 12px; border: 2px solid #CBD5E1; margin-bottom: 8px; "
                    f"opacity: 0.5; color: #1E293B;'>"
                    f"<div style='font-size: 2rem;'>❓</div>"
                    f"<span style='font-size: 0.85em;'>{badge['name']}</span>"
                    f"</div>", unsafe_allow_html=True)

    st.markdown(f"*{len(earned_ids)}/{len(all_badges)} badges earned*")

    st.markdown("---")

    # ─── Track Progress ─────────────────────────────
    st.markdown("### 📚 Learning Tracks")

    overall = get_overall_progress(user.get("completed_lessons", []))

    st.progress(
        overall["overall_percentage"] / 100,
        text=f"Overall: {overall['total_completed']}/{overall['total_lessons']} lessons ({overall['overall_percentage']}%)"
    )
    st.markdown("")

    for track in overall["tracks"]:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown(f"{track['track_icon']} **{track['track_title']}**")
            st.progress(track['percentage'] / 100,
                       text=f"{track['completed_lessons']}/{track['total_lessons']} lessons")
        with col2:
            if track["is_complete"]:
                st.markdown("✅ Complete")
            elif track["completed_lessons"] > 0:
                st.markdown("🔵 In Progress")
            else:
                st.markdown("⬜ Not Started")

    st.markdown("---")

    # ─── Stats Summary ──────────────────────────────
    st.markdown("### 📈 Stats")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Lessons", user.get("total_lessons_completed", 0))
    with col2:
        st.metric("Quizzes", user.get("total_quizzes_completed", 0))
    with col3:
        st.metric("AI Chats", user.get("total_ai_chats", 0))
    with col4:
        st.metric("Simulations", user.get("total_simulations", 0))

    # ─── Encouragement ──────────────────────────────
    st.markdown("")
    if overall["overall_percentage"] >= 100:
        st.success(f"🦊 **{MASCOT_NAME}:** You've completed ALL tracks! You're a Financial Sage! 🏆")
    elif overall["overall_percentage"] >= 50:
        st.info(f"🦊 **{MASCOT_NAME}:** Over halfway there! Your dedication is impressive! 🌟")
    elif overall["overall_percentage"] > 0:
        st.info(f"🦊 **{MASCOT_NAME}:** Great start! Keep the momentum going — every lesson counts! 💪")
    else:
        st.info(f"🦊 **{MASCOT_NAME}:** Your journey begins now! Start a learning track to earn XP and badges! 🚀")


def _render_activity_grid(activity_dates: list):
    """Render a simplified activity heatmap."""
    from datetime import datetime, timedelta

    today = datetime.now().date()
    days = []

    for i in range(29, -1, -1):
        day = today - timedelta(days=i)
        day_str = day.strftime("%Y-%m-%d")
        is_active = day_str in activity_dates
        days.append(("🟩" if is_active else "⬜"))

    # Display as 6 columns of 5 days
    rows = [days[i:i+10] for i in range(0, 30, 10)]
    for row in rows:
        st.markdown(" ".join(row))
