# 12. Project Architecture

## Folder Structure

```
FinLingo/
│
├── 📄 README.md                    # Project documentation
├── 📄 requirements.txt             # Python dependencies
├── 📄 .env.example                 # Environment variable template
├── 📄 .gitignore                   # Git ignore rules
├── 📄 LICENSE                      # MIT License
│
├── 📂 app/                         # Main application code
│   ├── 📄 __init__.py
│   ├── 📄 main.py                  # App entry point (Streamlit) or Flask app
│   ├── 📄 config.py                # App configuration, constants
│   │
│   ├── 📂 pages/                   # UI screens / page modules
│   │   ├── 📄 __init__.py
│   │   ├── 📄 home.py              # Dashboard / Home screen
│   │   ├── 📄 onboarding.py        # Onboarding flow
│   │   ├── 📄 learning_paths.py    # Track overview + lesson map
│   │   ├── 📄 lesson.py            # Lesson content display
│   │   ├── 📄 quiz.py              # Quiz interface
│   │   ├── 📄 chat.py              # AI Tutor chat interface
│   │   ├── 📄 simulators.py        # Financial simulators UI
│   │   ├── 📄 progress.py          # Progress tracking screen
│   │   └── 📄 profile.py           # Profile and settings
│   │
│   ├── 📂 services/                # Business logic layer
│   │   ├── 📄 __init__.py
│   │   ├── 📄 ai_service.py        # AI API integration (OpenAI/Gemini)
│   │   ├── 📄 lesson_service.py    # Lesson loading and progression
│   │   ├── 📄 quiz_service.py      # Quiz logic and scoring
│   │   ├── 📄 simulation_service.py # Financial calculations
│   │   ├── 📄 gamification_service.py # XP, levels, badges, streaks
│   │   └── 📄 user_service.py      # User data management
│   │
│   ├── 📂 models/                  # Data models / schemas
│   │   ├── 📄 __init__.py
│   │   ├── 📄 user.py              # User model
│   │   ├── 📄 lesson.py            # Lesson model
│   │   ├── 📄 quiz.py              # Quiz/question model
│   │   └── 📄 progress.py          # Progress/achievement model
│   │
│   └── 📂 utils/                   # Utility functions
│       ├── 📄 __init__.py
│       ├── 📄 helpers.py           # Common helpers
│       ├── 📄 validators.py        # Input validation
│       └── 📄 formatters.py        # Display formatting
│
├── 📂 data/                        # Content data (JSON files)
│   ├── 📂 lessons/                 # Lesson content by track
│   │   ├── 📄 credit_card_basics.json
│   │   ├── 📄 interest_and_installments.json
│   │   ├── 📄 emergency_fund.json
│   │   ├── 📄 understanding_loans.json
│   │   ├── 📄 spending_control.json
│   │   ├── 📄 digital_banking_safety.json
│   │   └── 📄 intro_to_investing.json
│   │
│   ├── 📂 quizzes/                 # Quiz data by track
│   │   ├── 📄 credit_card_basics_quiz.json
│   │   ├── 📄 interest_and_installments_quiz.json
│   │   ├── 📄 emergency_fund_quiz.json
│   │   ├── 📄 understanding_loans_quiz.json
│   │   ├── 📄 spending_control_quiz.json
│   │   ├── 📄 digital_banking_safety_quiz.json
│   │   └── 📄 intro_to_investing_quiz.json
│   │
│   ├── 📄 tracks.json              # Track metadata (order, icons, descriptions)
│   ├── 📄 badges.json              # Badge definitions
│   ├── 📄 levels.json              # Level thresholds
│   └── 📄 tips.json                # Daily tips from Fino
│
├── 📂 storage/                     # Local data persistence
│   ├── 📄 user_data.json           # User profile and settings
│   └── 📄 finlingo.db              # SQLite database (alternative)
│
├── 📂 assets/                      # Static assets
│   ├── 📂 images/                  # Images and illustrations
│   │   ├── 📄 logo.png
│   │   ├── 📄 fino_waving.png
│   │   ├── 📄 fino_celebrating.png
│   │   ├── 📄 fino_thinking.png
│   │   └── 📄 fino_encouraging.png
│   │
│   ├── 📂 css/                     # Stylesheets (Flask approach)
│   │   └── 📄 style.css
│   │
│   └── 📂 js/                      # JavaScript (Flask approach)
│       └── 📄 app.js
│
├── 📂 templates/                   # HTML templates (Flask approach)
│   ├── 📄 base.html
│   ├── 📄 home.html
│   ├── 📄 lesson.html
│   ├── 📄 quiz.html
│   ├── 📄 chat.html
│   └── 📄 simulator.html
│
├── 📂 docs/                        # Project documentation
│   ├── 📄 01_project_definition.md
│   ├── 📄 02_brand_personality.md
│   ├── 📄 03_main_features.md
│   ├── 📄 04_user_flow.md
│   ├── 📄 05_learning_paths.md
│   ├── 📄 06_gamification.md
│   ├── 📄 07_ai_features.md
│   ├── 📄 08_simulations.md
│   ├── 📄 09_ux_ui_structure.md
│   ├── 📄 10_visual_direction.md
│   ├── 📄 11_technical_stack.md
│   ├── 📄 12_project_architecture.md
│   ├── 📄 13_portfolio_positioning.md
│   └── 📄 14_interview_talking_points.md
│
└── 📂 tests/                       # Test files
    ├── 📄 __init__.py
    ├── 📄 test_simulation_service.py
    ├── 📄 test_quiz_service.py
    └── 📄 test_gamification_service.py
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        PRESENTATION                          │
│                                                              │
│   pages/home  pages/lesson  pages/quiz  pages/chat  pages/sim│
│       │            │           │           │           │      │
└───────┼────────────┼───────────┼───────────┼───────────┼─────┘
        │            │           │           │           │
        ▼            ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────┐
│                      SERVICE LAYER                           │
│                                                              │
│  user_service  lesson_service  quiz_service  ai_service      │
│                simulation_service  gamification_service       │
│                                                              │
└───────┬────────────┬───────────┬───────────┬─────────────────┘
        │            │           │           │
        ▼            ▼           ▼           ▼
┌────────────┐ ┌──────────┐ ┌────────┐ ┌──────────────┐
│  storage/  │ │  data/   │ │ models │ │  External AI │
│  (SQLite/  │ │ (JSON)   │ │        │ │  API (OpenAI │
│   JSON)    │ │          │ │        │ │  / Gemini)   │
└────────────┘ └──────────┘ └────────┘ └──────────────┘
```

---

## Key Design Decisions

| Decision | Rationale |
|---|---|
| **JSON for lesson content** | Easy to edit, version-controllable, no database needed |
| **SQLite for user data** | Lightweight, built-in Python, single-file database |
| **Service layer pattern** | Separates business logic from UI — clean, testable |
| **No ORM** | Too complex for MVP, raw SQLite is fine |
| **Config via .env** | Secure API key management, standard practice |
| **Tests for services only** | Focus testing effort where logic lives |
| **Docs in project** | Everything in one place for portfolio reviewers |
