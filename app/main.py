"""
FinLingo — Main Application Entry Point
Run with: streamlit run app/main.py
"""

import streamlit as st
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.config import APP_NAME, APP_TAGLINE, CUSTOM_CSS
from app.services.user_service import load_user_data, save_user_data, record_activity
from app.services.gamification_service import update_streak, check_badge_eligibility

# ─── Page Config ────────────────────────────────────
st.set_page_config(
    page_title=f"{APP_NAME} — {APP_TAGLINE}",
    page_icon="🦊",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ─── Custom CSS ─────────────────────────────────────
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def init_session_state():
    """Initialize session state with user data."""
    if "user_data" not in st.session_state:
        st.session_state.user_data = load_user_data()

    if "current_page" not in st.session_state:
        if st.session_state.user_data.get("onboarding_complete"):
            st.session_state.current_page = "home"
        else:
            st.session_state.current_page = "onboarding"

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "quiz_state" not in st.session_state:
        st.session_state.quiz_state = None

    # Update streak on app load
    st.session_state.user_data = update_streak(st.session_state.user_data)
    st.session_state.user_data = record_activity(st.session_state.user_data)
    save_user_data(st.session_state.user_data)


def navigate_to(page: str, **kwargs):
    """Navigate to a different page."""
    st.session_state.current_page = page
    for key, value in kwargs.items():
        st.session_state[key] = value
    st.rerun()


def save_and_refresh():
    """Save current user data and rerun."""
    save_user_data(st.session_state.user_data)
    st.rerun()


def check_new_badges():
    """Check for newly earned badges and display celebrations."""
    new_badges = check_badge_eligibility(st.session_state.user_data)
    for badge in new_badges:
        st.session_state.user_data.setdefault("badges_earned", []).append(badge["id"])
        st.toast(f"🏅 Badge Unlocked: {badge['icon']} {badge['name']}!", icon="🎉")
    if new_badges:
        save_user_data(st.session_state.user_data)


# ─── Main Router ────────────────────────────────────
def main():
    init_session_state()
    check_new_badges()

    page = st.session_state.current_page

    if page == "onboarding":
        from app.pages.onboarding import render_onboarding
        render_onboarding()
    elif page == "home":
        from app.pages.home import render_home
        render_home()
    elif page == "learning_paths":
        from app.pages.learning_paths import render_learning_paths
        render_learning_paths()
    elif page == "lesson":
        from app.pages.lesson import render_lesson
        render_lesson()
    elif page == "quiz":
        from app.pages.quiz import render_quiz
        render_quiz()
    elif page == "chat":
        from app.pages.chat import render_chat
        render_chat()
    elif page == "simulators":
        from app.pages.simulators import render_simulators
        render_simulators()
    elif page == "progress":
        from app.pages.progress import render_progress
        render_progress()
    elif page == "profile":
        from app.pages.profile import render_profile
        render_profile()
    else:
        from app.pages.home import render_home
        render_home()


if __name__ == "__main__":
    main()
