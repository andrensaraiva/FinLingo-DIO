<h1 align="center">🦊 FinLingo</h1>
<p align="center"><strong>Learn money. One lesson at a time.</strong></p>

<p align="center">
  A Duolingo-inspired AI-powered micro-learning app for financial education — built with Python, featuring an AI tutor, gamified progression, and financial simulators.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/python-3.10+-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/streamlit-1.30+-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/AI-OpenAI%20%7C%20Gemini-10B981" alt="AI"/>
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>
</p>

---

## 📖 Description

**FinLingo** is a micro-learning financial education companion that combines the engaging format of Duolingo with AI-powered tutoring and interactive financial simulations. Users learn through short, themed lessons, reinforce knowledge with quizzes, ask an AI tutor (Fino) questions in natural language, and experiment with financial calculators — all while tracking progress through a gamified system of XP, streaks, levels, and badges.

The project is designed as a **portfolio-ready educational product** that demonstrates AI integration, UX/product design thinking, gamification, and practical Python development — while addressing the real-world problem of financial illiteracy.

> ⚠️ **Disclaimer:** FinLingo is an educational and demonstrative project. It does not provide real financial advice. For personal financial decisions, always consult a qualified professional.

---

## ✨ Features

### MVP (Current)
- 🎓 **7 Learning Tracks** — Credit cards, interest, emergency funds, loans, budgeting, digital safety, investing basics
- 📚 **23 Micro-Lessons** — Bite-sized, plain-language content with key terms and examples
- 🧠 **Interactive Quizzes** — Multiple choice, true/false, and immediate feedback with explanations
- 🤖 **AI Tutor Chat (Fino)** — Ask financial questions and get context-aware, beginner-friendly explanations
- 🔢 **Financial Simulators** — Installment calculator, loan simulator, savings planner, emergency fund calculator, purchase comparison
- 🎮 **Gamification** — XP points, 8 levels, daily streaks, 10 earnable badges, progress bars
- 📊 **Progress Tracking** — Track lessons completed, quiz scores, streaks, and achievements
- 🛡️ **Safety Guardrails** — Educational disclaimers, responsible AI boundaries, no personal financial advice

### Nice-to-Have (Planned)
- 🌙 Dark mode
- 📌 Bookmarked lessons
- 🎯 Daily challenge questions
- 🦊 Fino mood system (mascot reacts to engagement)

---

## 💡 Inspiration

FinLingo is inspired by:
- **Duolingo** — Micro-learning format, gamification, daily habits
- **Khan Academy** — Free, accessible education for everyone
- **Nubank / Revolut** — Clean fintech design, beginner-friendly banking
- **ChatGPT** — Conversational AI for learning and exploration

The core insight: *People learn finance the same way they learn languages — through short, daily practice with immediate feedback, not through textbooks.*

---

## 🧭 How It Works

```
1. Open FinLingo → Meet Fino, your AI finance buddy
2. Complete onboarding → Set your name and experience level
3. Choose a learning track → e.g., "Credit Card Basics"
4. Read a micro-lesson → 2-3 minutes of clear, friendly content
5. Take a quiz → Test what you learned, earn XP
6. Chat with Fino → Ask follow-up questions in natural language
7. Run a simulation → See how interest, loans, or savings work with real numbers
8. Track your progress → Watch your XP grow, maintain your streak, unlock badges
9. Come back tomorrow → Build a financial learning habit
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Language** | Python 3.10+ |
| **UI Framework** | Streamlit |
| **AI Integration** | OpenAI API (GPT-4o-mini) / Google Gemini API |
| **Data Storage** | JSON (content + user progress) |
| **Simulations** | Pure Python (math module) |
| **Styling** | Streamlit components + custom CSS |
| **Deployment** | Streamlit Community Cloud |

---

## 📁 Project Structure

```
FinLingo/
├── README.md                     # This file
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment variable template
├── .gitignore                    # Git ignore rules
│
├── app/                          # Application source code
│   ├── main.py                   # Entry point
│   ├── config.py                 # Configuration
│   ├── pages/                    # UI screens
│   │   ├── home.py               # Dashboard
│   │   ├── onboarding.py         # First-time setup
│   │   ├── learning_paths.py     # Track selection
│   │   ├── lesson.py             # Lesson viewer
│   │   ├── quiz.py               # Quiz interface
│   │   ├── chat.py               # AI tutor chat
│   │   ├── simulators.py         # Financial calculators
│   │   ├── progress.py           # Progress & achievements
│   │   └── profile.py            # Settings
│   ├── services/                 # Business logic
│   │   ├── ai_service.py         # AI API wrapper
│   │   ├── lesson_service.py     # Lesson management
│   │   ├── quiz_service.py       # Quiz scoring
│   │   ├── simulation_service.py # Financial calculations
│   │   ├── gamification_service.py # XP, levels, badges
│   │   └── user_service.py       # User data
│   ├── models/                   # Data models
│   └── utils/                    # Helpers
│
├── data/                         # Content (JSON)
│   ├── lessons/                  # Lesson content by track
│   ├── quizzes/                  # Quiz questions by track
│   ├── tracks.json               # Track metadata
│   ├── badges.json               # Badge definitions
│   ├── levels.json               # Level thresholds
│   └── tips.json                 # Fino's daily tips
│
├── docs/                         # Full project documentation
│   ├── 01_project_definition.md
│   ├── 02_brand_personality.md
│   ├── ...
│   └── 15_naming_tagline_final.md
│
├── storage/                      # Local persistence (auto-created)
│   └── user_data.json
│
└── tests/                        # Unit tests
    ├── test_simulation_service.py
    ├── test_quiz_service.py
    └── test_gamification_service.py
```

---

## 🚀 Installation

### Prerequisites
- Python 3.10 or higher
- (Optional) An API key from [OpenAI](https://platform.openai.com/) or [Google AI Studio](https://aistudio.google.com/) — the app works without one using built-in fallback responses

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/andrensaraiva/FinLingo-DIO.git
cd FinLingo-DIO

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env and add your API key:
# OPENAI_API_KEY=sk-your-key-here
# or
# GOOGLE_API_KEY=your-key-here

# 5. Run the app
streamlit run app/main.py
```

The app will open at `http://localhost:8501`.

---

## 📘 Usage

### Learning
- Navigate to **Learning Paths** from the dashboard
- Select a track (e.g., "Credit Card Basics")
- Read through the micro-lesson, then take the quiz
- Earn XP and progress to the next lesson

### AI Tutor
- Open **Chat with Fino** from the dashboard
- Type any financial question in plain language
- Fino responds with a clear, context-aware explanation
- Try: *"What is compound interest?"* or *"How do I start saving?"*

### Simulators
- Open **Simulators** from the dashboard
- Choose a calculator (installment, loan, savings, etc.)
- Enter your values and hit **Calculate**
- Read the educational takeaway from Fino

---

## 🔮 Future Improvements

| Priority | Feature | Description |
|---|---|---|
| 🔴 High | User authentication | Login/signup for persistent accounts |
| 🔴 High | Cloud data sync | Cross-device progress via Supabase/Firebase |
| 🟡 Medium | Daily challenges | One random question per day for bonus XP |
| 🟡 Medium | Spaced repetition | AI-driven review scheduling for retention |
| 🟡 Medium | More learning tracks | Taxes, retirement, insurance, crypto basics |
| 🟢 Low | Leaderboard | Weekly XP ranking (opt-in) |
| 🟢 Low | Voice interaction | Ask Fino questions by voice |
| 🟢 Low | Mobile app | React Native or Flutter wrapper |
| 🟢 Low | Multi-language | Portuguese, Spanish translations |

---

## 🏆 Portfolio Highlights

This project demonstrates:

| Skill | How It's Shown |
|---|---|
| **AI Integration** | OpenAI/Gemini API with prompt engineering, context injection, and safety guardrails |
| **Product Design** | Full user flow, onboarding, retention mechanics, pedagogical structure |
| **UX/UI Design** | Screen architecture, accessibility, visual direction, mascot design |
| **Python Development** | Clean architecture, service layer, data modeling, unit tests |
| **Gamification** | XP, levels, streaks, badges — purposeful engagement design |
| **Fintech Domain** | Financial literacy content, simulators, responsible messaging |
| **Responsible AI** | Disclaimers, topic boundaries, safety responses, transparent AI identity |

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [Duolingo](https://www.duolingo.com/) for the micro-learning inspiration
- [OpenAI](https://openai.com/) for the GPT API
- [Streamlit](https://streamlit.io/) for making Python UI development fast
- [Lucide Icons](https://lucide.dev/) for the icon set
- [Inter Font](https://rsms.me/inter/) for beautiful typography

---

<p align="center">
  <strong>FinLingo</strong> — Learn money. One lesson at a time. 🦊
</p>