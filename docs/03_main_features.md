# 3. Main Features

## MVP Features (Build First)

### 3.1 Onboarding Flow
- Welcome screen with Fino mascot
- Brief app explanation (3 swipeable cards)
- User selects a display name
- User picks their experience level: "Total beginner" / "I know some basics" / "I want to review"
- Recommended starting learning path based on selection

### 3.2 Learning Paths
- 5–7 themed tracks (e.g., "Credit Card Basics," "Saving Smart")
- Each track has 4–6 micro-lessons
- Tracks are presented in a vertical map (Duolingo-style)
- Locked/unlocked progression — complete lessons to advance
- Each track shows completion percentage

### 3.3 Micro-Lessons
- Short, scrollable content screens (200–400 words max)
- Mix of text, key definitions, examples, and fun analogies
- "Did You Know?" callout boxes
- Each lesson ends with a 3–5 question quiz

### 3.4 Quizzes
- Multiple choice questions (4 options)
- True/False questions
- Fill-in-the-blank (simple numeric or keyword)
- Immediate feedback per question with Fino's reaction
- Score summary at the end with XP earned

### 3.5 AI Tutor Chat (Fino Chat)
- Free-text input for financial questions
- AI responds in plain, friendly language
- Context-awareness: knows which lesson the user just completed
- Safety disclaimers on sensitive topics
- Suggested starter questions ("Try asking me…")
- Chat history within the session

### 3.6 Simple Financial Simulators
- Installment calculator
- Savings goal calculator
- Emergency fund planner
- Each simulator has input fields, a "Calculate" button, and a result panel
- Educational takeaway message after each result

### 3.7 Progress Tracking
- XP counter (earned from lessons, quizzes, chat interactions)
- Current streak (consecutive days of activity)
- Lesson completion map with checkmarks
- Simple progress bar per learning path

### 3.8 Gamification Layer
- XP points for every action
- Daily streak tracker
- 6–10 earnable badges
- Level indicator (Beginner → Intermediate → Advanced)
- Encouraging messages on milestones

---

## Nice-to-Have Features (Phase 2)

| Feature | Description |
|---|---|
| **Dark mode** | Toggle in settings |
| **FAQ Knowledge Base** | Searchable list of common financial questions |
| **Bookmarked lessons** | Save lessons for later review |
| **Daily challenge** | One random quiz question per day for bonus XP |
| **Fino mood system** | Mascot reacts to user's streak and engagement |
| **Session persistence** | Save progress across sessions using local storage or SQLite |
| **More simulators** | Loan comparison, purchase decision helper |
| **Lesson review mode** | Re-read completed lessons without re-taking quizzes |

---

## Advanced Future Features (Phase 3+)

| Feature | Description |
|---|---|
| **User authentication** | Login/signup with password or OAuth |
| **Cloud storage** | Firebase or Supabase for cross-device sync |
| **Leaderboard** | Weekly XP ranking among users |
| **Custom learning plans** | AI suggests a personalized track based on goals |
| **Voice interaction** | Ask Fino questions by voice |
| **Multi-language support** | Portuguese, Spanish translations |
| **Real-time financial data** | Pull live interest rates or currency values (read-only) |
| **Accessibility audit** | Full WCAG 2.1 AA compliance |
| **Mobile-native version** | React Native or Flutter wrapper |
