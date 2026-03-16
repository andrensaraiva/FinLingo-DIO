"""
FinLingo — Configuration Module
Centralized constants and settings for the application.
"""

import os
from dotenv import load_dotenv

load_dotenv()

# ─── App Info ────────────────────────────────────────
APP_NAME = "FinLingo"
APP_TAGLINE = "Learn money. One lesson at a time."
APP_VERSION = "1.0.0"
MASCOT_NAME = "Fino"

# ─── AI Configuration ───────────────────────────────
AI_PROVIDER = os.getenv("AI_PROVIDER", "openai")  # "openai" or "gemini"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
AI_TEMPERATURE = 0.7
AI_MAX_TOKENS = 500

# ─── Paths ───────────────────────────────────────────
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LESSONS_DIR = DATA_DIR / "lessons"
QUIZZES_DIR = DATA_DIR / "quizzes"
STORAGE_DIR = BASE_DIR / "storage"
ASSETS_DIR = BASE_DIR / "assets"

# ─── Gamification ────────────────────────────────────
XP_LESSON_COMPLETE = 15
XP_QUIZ_CORRECT = 10
XP_QUIZ_INCORRECT = 2
XP_QUIZ_COMPLETE_BONUS = 20
XP_QUIZ_PERFECT_BONUS = 30
XP_AI_CHAT = 5
XP_SIMULATION = 10
XP_DAILY_LOGIN = 5

# ─── AI System Prompt ───────────────────────────────
SYSTEM_PROMPT = """You are Fino, the FinLingo AI financial tutor — a friendly, patient, and \
encouraging guide who explains financial concepts in simple, beginner-friendly language.

RULES:
1. Always explain concepts clearly using plain language and relatable analogies.
2. Never give specific financial advice (e.g., "You should invest in X").
3. Always include this disclaimer when relevant: "This is for educational purposes only. \
For personal financial decisions, consult a qualified professional."
4. If a user asks something outside of personal finance education, politely redirect: \
"Great question, but that's outside my area! I'm best at explaining money concepts. \
Try asking me about savings, credit, or loans!"
5. Never invent financial data, statistics, or rates. If unsure, say so.
6. Keep responses concise — aim for 3-5 sentences unless the user asks for more detail.
7. Use encouraging language. Never make the user feel dumb.
8. If the user shares personal financial information, do NOT store it or reference it \
beyond the current session.
9. Use the user's current lesson context to make answers relevant.
10. End responses with a follow-up question or suggestion when appropriate.

CONTEXT:
- User name: {user_name}
- Current track: {current_track}
- Last completed lesson: {last_lesson}
- Level: {level}
"""

# ─── UI Styling (Streamlit Custom CSS) ───────────────
CUSTOM_CSS = """
<style>
    /* Global font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Primary colors */
    :root {
        --emerald: #10B981;
        --teal: #14B8A6;
        --navy: #1E293B;
        --amber: #F59E0B;
        --coral: #F87171;
        --sky: #38BDF8;
        --lavender: #A78BFA;
    }

    /* Cards */
    .stCard {
        border-radius: 16px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
    }

    /* Progress bars */
    .stProgress > div > div > div {
        background-color: var(--emerald);
    }

    /* Buttons */
    .stButton > button {
        border-radius: 9999px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        border: none;
        transition: all 0.15s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }

    /* Metric styling */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, #F0FDF4, #ECFDF5);
        padding: 16px;
        border-radius: 12px;
        border: 1px solid #D1FAE5;
    }

    /* Chat messages */
    .chat-message {
        padding: 12px 16px;
        border-radius: 12px;
        margin-bottom: 8px;
        line-height: 1.5;
    }
    .chat-fino {
        background: #F0FDF4;
        border: 1px solid #D1FAE5;
    }
    .chat-user {
        background: #EFF6FF;
        border: 1px solid #DBEAFE;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Disclaimer */
    .disclaimer {
        font-size: 12px;
        color: #94A3B8;
        text-align: center;
        padding: 8px;
        border-top: 1px solid #E2E8F0;
        margin-top: 16px;
    }
</style>
"""
