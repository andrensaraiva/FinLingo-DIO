# 6. Gamification System

## Philosophy
FinLingo's gamification is **lightweight and motivational**, not manipulative. The goal is to build a healthy learning habit — not to create anxiety or addiction. Every gamification element should make the user feel **capable, rewarded, and curious to continue**.

Design principle: **"Celebrate effort, not just performance."**

---

## 6.1 XP (Experience Points)

### How XP Is Earned

| Action | XP Earned |
|---|---|
| Complete a micro-lesson (reading) | +15 XP |
| Answer a quiz question correctly | +10 XP |
| Answer a quiz question incorrectly (still trying) | +2 XP |
| Complete a full quiz (all questions) | +20 XP bonus |
| Perfect quiz score (no mistakes) | +30 XP bonus |
| Ask a question in AI Chat | +5 XP |
| Run a financial simulation | +10 XP |
| Log in for the day (daily visit) | +5 XP |

### XP Display
- Shown on the dashboard header
- Animated "+XP" popup after every action
- Running total visible on the Progress screen

---

## 6.2 Levels

XP accumulates into **levels**. Each level requires progressively more XP.

| Level | Title | XP Required (cumulative) |
|---|---|---|
| 1 | 🌱 Seedling | 0 XP |
| 2 | 🌿 Sprout | 100 XP |
| 3 | 🪴 Sapling | 300 XP |
| 4 | 🌳 Growing Tree | 600 XP |
| 5 | 💰 Money Maker | 1,000 XP |
| 6 | 🏦 Finance Explorer | 1,500 XP |
| 7 | 📊 Budget Master | 2,200 XP |
| 8 | 🏆 Financial Sage | 3,000 XP |

- Level-up triggers a **celebration overlay** with Fino doing a dance
- Level title appears on the Profile screen
- Progress bar shows current XP / next level threshold

---

## 6.3 Streaks

### How Streaks Work
- A streak counts **consecutive days** with at least one learning action
- "Learning action" = completing a lesson, taking a quiz, using AI chat, or running a simulation
- Missing a day resets the streak to 0

### Streak Display
- 🔥 Fire icon + number on the dashboard
- Streak calendar on the Progress screen (heatmap-style grid)
- Fino reacts to streak milestones:
  - Day 3: "Three days in a row! You're building a great habit!"
  - Day 7: "One full week! 🔥 You're on fire!"
  - Day 30: "30 days?! You're a financial learning legend!"

### Streak Protection (Nice-to-have)
- "Streak Freeze" — earned after 7 consecutive days — preserves streak for 1 missed day
- Limited to 1 freeze active at a time

---

## 6.4 Badges

Badges are earned for meaningful milestones. Each badge has a **name, icon, and description.**

| Badge | Icon | Condition |
|---|---|---|
| **First Step** | 👣 | Complete your first lesson |
| **Quiz Whiz** | 🧠 | Get a perfect score on any quiz |
| **Curious Mind** | 💬 | Ask your first question in AI Chat |
| **Number Cruncher** | 🔢 | Use a financial simulator for the first time |
| **Streak Starter** | 🔥 | Reach a 3-day streak |
| **Week Warrior** | 🗓️ | Reach a 7-day streak |
| **Path Completer** | ✅ | Complete an entire learning track |
| **Budget Boss** | 💼 | Complete the "Spending Control" track |
| **Safety Shield** | 🛡️ | Complete the "Digital Banking Safety" track |
| **Explorer** | 🧭 | Complete all 7 learning tracks |

### Badge Display
- Grid layout on the Progress screen
- Locked badges shown as greyed-out silhouettes with "??? — Keep learning to unlock"
- Unlocked badges animate in with a glow effect and Fino celebration

---

## 6.5 Progress Bar

| Where | What It Shows |
|---|---|
| Dashboard | Overall course completion (X% of all lessons done) |
| Track page | Track-specific completion (X/Y lessons done) |
| Lesson screen | Progress within the lesson (page indicator) |
| Quiz screen | Question counter (1/5, 2/5…) |
| Profile / Level | XP progress toward next level |

### Visual Style
- Rounded, filled bar with gradient (green → teal)
- Percentage text label
- Smooth animation on progress change

---

## 6.6 Encouraging Feedback Messages

FinLingo uses **positive reinforcement at every opportunity**, never shaming the user.

### After a Correct Answer
- "Nailed it! 🎯"
- "You're on a roll!"
- "Fino is impressed! 🦊"
- "That's the one! +10 XP"

### After an Incorrect Answer
- "Not quite, but you're learning — that's what counts!"
- "Close! Here's the right answer. You'll get it next time."
- "Mistakes are how we grow. Let's keep going!"
- "+2 XP for trying!"

### On Milestones
- "🎉 Level Up! You're now a Money Maker!"
- "🏅 New badge unlocked: Quiz Whiz!"
- "🔥 7-day streak! You're building an amazing habit!"
- "✅ Track complete! You've mastered Credit Card Basics!"

### On Return
- "Welcome back, [Name]! Let's keep the momentum going."
- "You were on lesson 3 of Interest & Installments — want to continue?"
- "Your streak is at 5 days. Let's make it 6! 💪"

---

## 6.7 Summary Table

| Element | Purpose | Frequency |
|---|---|---|
| XP | Reward every action | Every interaction |
| Levels | Show long-term growth | Every ~300 XP |
| Streaks | Build daily habit | Daily |
| Badges | Celebrate milestones | Event-based |
| Progress bars | Visualize completion | Always visible |
| Feedback messages | Encourage & motivate | After every action |
