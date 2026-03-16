"""
FinLingo — Profile & Settings Page
User profile management and settings.
"""

import streamlit as st
from app.services.user_service import save_user_data, reset_progress
from app.services.gamification_service import get_current_level
from app.config import APP_NAME, APP_VERSION, MASCOT_NAME


def render_profile():
    """Render the profile/settings screen."""
    user = st.session_state.user_data

    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        st.markdown("### 👤 Profile & Settings")

    st.markdown("---")

    # ─── User Info ──────────────────────────────────
    st.markdown("#### Your Profile")

    name = st.text_input("Display Name", value=user.get("user_name", "Learner"), max_chars=30)

    if name != user.get("user_name"):
        if st.button("Save Name", type="primary"):
            st.session_state.user_data["user_name"] = name
            save_user_data(st.session_state.user_data)
            st.success("Name updated! ✅")
            st.rerun()

    xp = user.get("xp", 0)
    level_info = get_current_level(xp)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Level", f"{level_info['level']}")
    with col2:
        st.metric("Title", level_info["title"])
    with col3:
        st.metric("Total XP", f"{xp}")

    st.markdown("---")

    # ─── Experience Level ───────────────────────────
    st.markdown("#### Experience Level")
    exp_level = st.selectbox(
        "Your financial knowledge level:",
        options=["beginner", "intermediate", "review"],
        index=["beginner", "intermediate", "review"].index(
            user.get("experience_level", "beginner")
        ),
        format_func=lambda x: {
            "beginner": "🌱 Total Beginner",
            "intermediate": "📘 Some Basics",
            "review": "🔄 Review Mode"
        }[x]
    )

    if exp_level != user.get("experience_level"):
        st.session_state.user_data["experience_level"] = exp_level
        save_user_data(st.session_state.user_data)
        st.success("Experience level updated! ✅")

    st.markdown("---")

    # ─── Stats ──────────────────────────────────────
    st.markdown("#### Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"- **Lessons completed:** {user.get('total_lessons_completed', 0)}")
        st.markdown(f"- **Quizzes taken:** {user.get('total_quizzes_completed', 0)}")
        st.markdown(f"- **AI chats:** {user.get('total_ai_chats', 0)}")
    with col2:
        st.markdown(f"- **Simulations run:** {user.get('total_simulations', 0)}")
        st.markdown(f"- **Best streak:** {user.get('max_streak', 0)} days")
        st.markdown(f"- **Badges earned:** {len(user.get('badges_earned', []))}/10")

    st.markdown("---")

    # ─── Danger Zone ────────────────────────────────
    st.markdown("#### ⚠️ Danger Zone")

    with st.expander("Reset All Progress"):
        st.warning(
            "This will reset ALL your progress — XP, levels, streaks, badges, and lesson completion. "
            "Your name will be kept. This action cannot be undone."
        )
        if st.button("🗑️ Reset Progress", type="secondary"):
            st.session_state.user_data = reset_progress(st.session_state.user_data)
            save_user_data(st.session_state.user_data)
            st.success("Progress has been reset.")
            st.rerun()

    st.markdown("---")

    # ─── About ──────────────────────────────────────
    st.markdown("#### About")
    st.markdown(f"**{APP_NAME}** v{APP_VERSION}")
    st.markdown(f"*Learn money. One lesson at a time.*")
    st.markdown("")
    st.markdown(
        f"🦊 {MASCOT_NAME} is an AI-powered educational assistant. "
        f"{APP_NAME} is designed for learning purposes only and does not provide "
        f"real financial advice. For personal financial decisions, always consult "
        f"a qualified professional."
    )
    st.markdown("")
    st.markdown(
        "Built with ❤️ using Python, Streamlit, and Generative AI."
    )
