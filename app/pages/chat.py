"""
FinLingo — AI Tutor Chat Page
Conversational AI interface with Fino.
"""

import streamlit as st
from app.services.ai_service import get_ai_response
from app.services.user_service import save_user_data, update_user_xp, increment_counter, get_user_context
from app.services.gamification_service import get_xp_for_action
from app.config import MASCOT_NAME


def render_chat():
    """Render the AI tutor chat screen."""

    # ─── Header ─────────────────────────────────────
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("← Back"):
            st.session_state.current_page = "home"
            st.rerun()
    with col2:
        st.markdown(f"### 🦊 Chat with {MASCOT_NAME}")

    st.markdown(
        f"<small style='color: #64748B;'>ℹ️ {MASCOT_NAME} is an educational AI assistant. "
        f"This is not financial advice.</small>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    # ─── Initialize Chat History ────────────────────
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Show greeting if chat is empty
    if not st.session_state.chat_history:
        user_name = st.session_state.user_data.get("user_name", "Learner")
        current_track = st.session_state.user_data.get("current_track")

        greeting = f"Hey {user_name}! 👋 I'm {MASCOT_NAME}, your AI finance tutor. "
        if current_track:
            greeting += f"I see you've been studying **{current_track.replace('_', ' ').title()}** — great progress! "
        greeting += "Ask me anything about money — no question is too basic. 😊"

        st.session_state.chat_history.append({
            "role": "assistant",
            "content": greeting
        })

    # ─── Display Chat History ───────────────────────
    for message in st.session_state.chat_history:
        if message["role"] == "assistant":
            with st.chat_message("assistant", avatar="🦊"):
                st.markdown(message["content"])
        else:
            with st.chat_message("user", avatar="👤"):
                st.markdown(message["content"])

    # ─── Suggested Questions ────────────────────────
    if len(st.session_state.chat_history) <= 1:
        st.markdown("**💬 Try asking:**")

        suggestions = _get_suggestions()

        cols = st.columns(2)
        for i, suggestion in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(f'"{suggestion}"', key=f"suggest_{i}", use_container_width=True):
                    _process_message(suggestion)

    # ─── Chat Input ─────────────────────────────────
    user_input = st.chat_input(f"Ask {MASCOT_NAME} a question...")

    if user_input:
        _process_message(user_input)

    # ─── Disclaimer Footer ─────────────────────────
    st.markdown("---")
    st.markdown(
        f"<div class='disclaimer'>💡 {MASCOT_NAME} is an educational AI assistant. "
        f"For personal financial decisions, consult a qualified professional.</div>",
        unsafe_allow_html=True
    )


def _process_message(user_message: str):
    """Process a user message and get AI response."""
    # Add user message to history
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_message
    })

    # Get AI response
    user_context = get_user_context(st.session_state.user_data)
    ai_response = get_ai_response(
        user_message,
        user_context,
        st.session_state.chat_history[:-1]  # Exclude the just-added message
    )

    # Add disclaimer to response if not already present
    if "educational purposes" not in ai_response.lower():
        ai_response += "\n\n*💡 This is for educational purposes only.*"

    # Add response to history
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": ai_response
    })

    # Award XP for chatting
    user = st.session_state.user_data
    xp = get_xp_for_action("ai_chat")
    user = update_user_xp(user, xp)
    user = increment_counter(user, "total_ai_chats")
    st.session_state.user_data = user
    save_user_data(user)

    st.rerun()


def _get_suggestions() -> list:
    """Get contextual question suggestions."""
    current_track = st.session_state.user_data.get("current_track")

    suggestions_map = {
        "credit_card_basics": [
            "What happens if I miss a credit card payment?",
            "How do I build my credit score?",
            "What's the difference between credit and debit?",
            "Are credit card rewards worth it?"
        ],
        "interest_and_installments": [
            "Can you explain compound interest simply?",
            "Why are installment plans more expensive?",
            "What's the difference between simple and compound interest?",
            "How do I calculate the true cost of a loan?"
        ],
        "emergency_fund": [
            "How much should I have in my emergency fund?",
            "Where should I keep my emergency fund?",
            "How do I start saving on a small income?",
            "What counts as a financial emergency?"
        ],
        "understanding_loans": [
            "Should I take a loan to pay off credit cards?",
            "What's the difference between secured and unsecured loans?",
            "How do I know if a loan is a good idea?",
            "What is amortization?"
        ],
        "spending_control": [
            "How do I stop impulse buying?",
            "What's the 50/30/20 budgeting rule?",
            "How do I figure out needs vs. wants?",
            "What small expenses add up the most?"
        ],
        "digital_banking_safety": [
            "How do I spot a phishing email?",
            "Is it safe to use public WiFi for banking?",
            "What makes a strong password?",
            "What should I do if I think I've been scammed?"
        ],
        "intro_to_investing": [
            "What's the simplest way to start investing?",
            "What's an index fund?",
            "What's the difference between saving and investing?",
            "How much risk should a beginner take?"
        ]
    }

    default = [
        "What is compound interest?",
        "How do I start an emergency fund?",
        "What's the 50/30/20 rule?",
        "How do credit cards really work?"
    ]

    return suggestions_map.get(current_track, default)
