"""
FinLingo — Onboarding Page
First-time user setup flow.
"""

import streamlit as st
from app.services.user_service import save_user_data
from app.config import APP_NAME, MASCOT_NAME


def render_onboarding():
    """Render the onboarding flow."""

    if "onboarding_step" not in st.session_state:
        st.session_state.onboarding_step = 0

    step = st.session_state.onboarding_step

    if step == 0:
        _render_welcome()
    elif step == 1:
        _render_info_cards()
    elif step == 2:
        _render_name_input()
    elif step == 3:
        _render_level_selection()
    elif step == 4:
        _render_ready()


def _render_welcome():
    """Welcome splash screen."""
    st.markdown("---")
    st.markdown(
        f"<h1 style='text-align: center; font-size: 2.5rem;'>🦊 {APP_NAME}</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; font-size: 1.2rem; color: #475569;'>"
        "Learn money. One lesson at a time.</p>",
        unsafe_allow_html=True
    )
    st.markdown("")
    st.markdown(
        f"<p style='text-align: center; font-size: 1.1rem;'>"
        f"Hey there! 👋 I'm <strong>{MASCOT_NAME}</strong>, your finance buddy.<br>"
        f"Ready to learn about money? 💰</p>",
        unsafe_allow_html=True
    )
    st.markdown("")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Let's Go!", use_container_width=True, type="primary"):
            st.session_state.onboarding_step = 1
            st.rerun()


def _render_info_cards():
    """Three info cards explaining the app."""
    st.markdown("### Welcome to FinLingo! Here's what you'll get:")
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div style='text-align: center; padding: 20px; background: #F0FDF4;
                        border-radius: 12px; border: 1px solid #D1FAE5; color: #1E293B;'>
                <div style='font-size: 2rem;'>📚</div>
                <strong>Bite-Sized Lessons</strong><br>
                <span style='color: #475569; font-size: 0.85em;'>Learn finance in 2-3 minute lessons</span>
            </div>
            """, unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style='text-align: center; padding: 20px; background: #EFF6FF;
                        border-radius: 12px; border: 1px solid #DBEAFE; color: #1E293B;'>
                <div style='font-size: 2rem;'>🦊</div>
                <strong>AI Tutor</strong><br>
                <span style='color: #475569; font-size: 0.85em;'>Ask Fino anything about money</span>
            </div>
            """, unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style='text-align: center; padding: 20px; background: #FFF7ED;
                        border-radius: 12px; border: 1px solid #FED7AA; color: #1E293B;'>
                <div style='font-size: 2rem;'>🏆</div>
                <strong>Earn & Grow</strong><br>
                <span style='color: #475569; font-size: 0.85em;'>Track progress and earn badges</span>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Continue →", use_container_width=True, type="primary"):
            st.session_state.onboarding_step = 2
            st.rerun()


def _render_name_input():
    """User name input."""
    st.markdown("### What should I call you?")
    st.markdown(f"*{MASCOT_NAME} loves getting to know new learners!*")

    name = st.text_input(
        "Your name",
        value=st.session_state.user_data.get("user_name", ""),
        placeholder="Enter your name...",
        max_chars=30
    )

    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Next →", use_container_width=True, type="primary"):
            st.session_state.user_data["user_name"] = name if name.strip() else "Learner"
            st.session_state.onboarding_step = 3
            st.rerun()


def _render_level_selection():
    """Experience level selection."""
    st.markdown(f"### Nice to meet you, {st.session_state.user_data.get('user_name', 'Learner')}!")
    st.markdown("How would you describe your financial knowledge?")
    st.markdown("")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🌱\n\n**Total Beginner**\n\nI'm just starting", use_container_width=True):
            st.session_state.user_data["experience_level"] = "beginner"
            st.session_state.onboarding_step = 4
            st.rerun()

    with col2:
        if st.button("📘\n\n**Some Basics**\n\nI know a bit", use_container_width=True):
            st.session_state.user_data["experience_level"] = "intermediate"
            st.session_state.onboarding_step = 4
            st.rerun()

    with col3:
        if st.button("🔄\n\n**Review Mode**\n\nRefresh my knowledge", use_container_width=True):
            st.session_state.user_data["experience_level"] = "review"
            st.session_state.onboarding_step = 4
            st.rerun()


def _render_ready():
    """Final onboarding screen."""
    name = st.session_state.user_data.get("user_name", "Learner")

    st.markdown(
        f"<h2 style='text-align: center;'>🎉 You're all set, {name}!</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='text-align: center; font-size: 1.1rem; color: #475569;'>"
        f"{MASCOT_NAME} has prepared your personalized learning path.<br>"
        f"Let's start your financial education journey!</p>",
        unsafe_allow_html=True
    )
    st.markdown("")

    st.info(
        "💡 **Recommended first track:** Credit Card Basics — "
        "understanding credit is one of the most important financial skills!"
    )

    st.markdown("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Start Learning!", use_container_width=True, type="primary"):
            st.session_state.user_data["onboarding_complete"] = True
            from datetime import datetime
            st.session_state.user_data["created_at"] = datetime.now().isoformat()
            save_user_data(st.session_state.user_data)
            st.session_state.current_page = "home"
            del st.session_state.onboarding_step
            st.rerun()
