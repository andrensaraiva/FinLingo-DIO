# 4. User Flow

## Complete User Journey

### Step 1 — First Access
```
User opens the app
→ Splash screen with FinLingo logo + Fino mascot (1.5s)
→ Transitions to Welcome screen
```
- First impression: clean, colorful, inviting
- Fino waves and says: "Hey there! Ready to learn about money? 💰"
- CTA button: "Let's Go!"

### Step 2 — Onboarding (First-Time Only)
```
Welcome screen → 3 swipeable info cards → Name input → Level selection → Dashboard
```
1. **Card 1:** "Learn finance in bite-sized lessons" (illustration of lesson cards)
2. **Card 2:** "Ask Fino anything about money" (illustration of chat)
3. **Card 3:** "Track your progress and earn badges" (illustration of badges)
4. **Name input:** "What should I call you?" — text field, default: "Learner"
5. **Level selection:** Three cards to tap:
   - 🌱 "Total beginner — I'm just starting"
   - 📘 "I know some basics — I want to go deeper"
   - 🔄 "I want to review — refresh my knowledge"
6. **Result:** App recommends a starting path → user arrives at Dashboard

### Step 3 — Dashboard / Home
```
Dashboard shows:
├── Greeting: "Hey, [Name]! Ready to learn today?"
├── Current streak counter
├── Continue Learning card (last incomplete lesson)
├── Learning Paths overview (scrollable)
├── Quick Actions: [AI Chat] [Simulators] [Progress]
└── Daily tip from Fino
```

### Step 4 — Choosing a Learning Path
```
User taps "Learning Paths"
→ Sees vertical list of tracks with icons and progress bars
→ Taps on a track (e.g., "Credit Card Basics")
→ Sees lesson map with numbered nodes (1 → 2 → 3 → 4 → 5)
→ Completed nodes are green ✅, current node pulses, future nodes are locked 🔒
→ Taps on the current node to start the lesson
```

### Step 5 — Completing a Lesson
```
Lesson screen:
├── Title + track name
├── Scrollable content (text, key terms, examples, analogies)
├── "Did You Know?" callout
├── Progress indicator (page X of Y)
└── "Take the Quiz" button at the bottom
```
- Estimated reading time: 2–3 minutes
- Clean typography, generous spacing
- Fino appears in a corner with occasional comments

### Step 6 — Taking the Quiz
```
Quiz screen:
├── Question counter (1/5)
├── Question text
├── Answer options (tap to select)
├── "Check" button
├── Fino feedback animation (per question)
└── Summary at the end: score, XP earned, Fino reaction
```
- Correct: Green highlight + Fino happy face + "+10 XP"
- Incorrect: Orange highlight + correct answer shown + Fino encouraging face + "+2 XP (for trying)"
- End summary: "You scored 4/5! Great job! +50 XP total 🎉"

### Step 7 — Asking the AI Tutor Questions
```
User taps "AI Chat" (from dashboard or after a lesson)
→ Chat screen opens
├── Fino avatar + greeting
├── Suggested questions (based on last lesson)
├── Free-text input field
├── Send button
└── Chat history (session-based)
```
- User types: "What happens if I only pay the minimum on my credit card?"
- Fino responds with a clear, friendly explanation
- If the topic is sensitive: adds a disclaimer footer
- User can ask follow-ups within the same session

### Step 8 — Using Simulations
```
User taps "Simulators" from dashboard
→ Sees list of available simulators with icons
→ Taps one (e.g., "Installment Calculator")
├── Input fields (amount, interest rate, number of months)
├── "Calculate" button
├── Result panel (monthly payment, total cost, total interest)
└── Educational message from Fino: "Did you know? Paying in fewer installments usually saves you money!"
```

### Step 9 — Receiving Feedback
Feedback appears at multiple touchpoints:
- **After quizzes:** Score + personalized message
- **After simulations:** Educational takeaway
- **In AI chat:** Contextual explanations
- **On dashboard:** Streak reminders, milestone alerts
- **On badge unlock:** Celebration overlay with Fino

### Step 10 — Tracking Progress
```
User taps "Progress" from dashboard
→ Progress screen shows:
├── Total XP
├── Current level (with progress bar to next level)
├── Streak calendar (heatmap style)
├── Badges earned (grid with locked/unlocked states)
├── Tracks completed (list with percentages)
└── "Keep it up!" message from Fino
```

### Step 11 — Returning for Daily Usage
```
User opens app on Day 2+
→ Splash → Dashboard (skips onboarding)
├── "Welcome back, [Name]! Day [X] streak 🔥"
├── Continue from where they left off
├── Daily tip or challenge (Nice-to-have)
└── New content unlocked if previous lesson completed
```

---

## Flow Diagram (Simplified)

```
[Splash] → [Welcome] → [Onboarding] → [Dashboard]
                                            │
                    ┌───────────────┬────────┼────────┬──────────────┐
                    │               │        │        │              │
              [Learn Paths]   [AI Chat] [Simulators] [Progress] [Profile]
                    │
              [Lesson Map]
                    │
               [Lesson]
                    │
                [Quiz]
                    │
              [Feedback]
                    │
         [Back to Dashboard]
```
