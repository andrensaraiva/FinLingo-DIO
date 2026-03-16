# 9. UX/UI Structure

## Main Screens

### 9.1 Splash / Welcome Screen
| Element | Description |
|---|---|
| Logo | FinLingo logo centered |
| Mascot | Fino waving animation |
| Background | Gradient (teal → emerald) |
| Duration | 1.5 seconds, auto-transition |
| Purpose | Brand recognition, loading state |

### 9.2 Onboarding (First-Time Only)
| Element | Description |
|---|---|
| Screen 1 | "Learn finance in bite-sized lessons" + illustration |
| Screen 2 | "Ask Fino anything about money" + chat illustration |
| Screen 3 | "Track your progress and earn badges" + badge illustration |
| Name input | "What should I call you?" — text field |
| Level picker | 3 cards: Beginner / Some basics / Review |
| CTA | "Start Learning!" |
| Skip option | Small "Skip" link in corner |
| Dots | Page indicator dots at bottom |

### 9.3 Dashboard / Home
```
┌──────────────────────────────────────┐
│  👋 Hey, Alex!          🔥 5   ⭐ 340 │
│                                      │
│  ┌──────────────────────────────┐    │
│  │ 📖 Continue Learning          │    │
│  │ Credit Card Basics — Lesson 3 │    │
│  │ [Continue →]                  │    │
│  └──────────────────────────────┘    │
│                                      │
│  ┌────┐ ┌────┐ ┌────┐               │
│  │ 💬 │ │ 🔢 │ │ 📊 │               │
│  │Chat│ │Sim │ │Prog│               │
│  └────┘ └────┘ └────┘               │
│                                      │
│  📚 Learning Paths                   │
│  ┌──────┐ ┌──────┐ ┌──────┐        │
│  │ 💳   │ │ 📊   │ │ 🛡️   │        │
│  │Credit│ │Inter.│ │Emerg.│        │
│  │ 67%  │ │ 33%  │ │  0%  │        │
│  └──────┘ └──────┘ └──────┘        │
│                                      │
│  💡 Fino's Tip of the Day           │
│  "Did you know? 76% of people who   │
│   budget feel more in control."      │
│                                      │
│  ────────────────────────────        │
│  🏠 Home | 📚 Learn | 💬 Chat | 👤  │
└──────────────────────────────────────┘
```

### 9.4 Learning Paths Screen
| Element | Description |
|---|---|
| Header | "Learning Paths" + back arrow |
| Track list | Vertical scrollable list |
| Track card | Icon + title + progress bar + lesson count |
| State indicators | ✅ Completed / 🔵 In Progress / 🔒 Locked |
| Layout | Stack of cards with rounded corners |

### 9.5 Lesson Map (Inside a Track)
| Element | Description |
|---|---|
| Header | Track title + overall progress |
| Node map | Vertical path with numbered lesson nodes |
| Node states | ✅ Green (done) / 🔵 Blue pulsing (current) / ⬜ Grey (locked) |
| Tap action | Opens lesson content |
| Bottom | "Track Progress: 2/5 lessons" |

### 9.6 Lesson Screen
| Element | Description |
|---|---|
| Header | Lesson title + track name |
| Progress | "Page 1 of 3" indicator |
| Content | Scrollable: text, key terms (highlighted), examples, callouts |
| Callout box | "💡 Did You Know?" — colored background, rounded |
| Key term | Highlighted word with tooltip/definition |
| Bottom CTA | "Take the Quiz →" (appears after reading) |
| Navigation | Swipe or "Next" button between pages |

### 9.7 Quiz Screen
| Element | Description |
|---|---|
| Header | "Quiz: [Track Name]" + question counter (1/5) |
| Question | Large, clear text |
| Options | 4 tappable cards (A, B, C, D) |
| Check button | "Check Answer" — appears after selection |
| Feedback | Green/orange highlight + Fino reaction + explanation |
| Progress | Animated bar at top |
| Summary | End screen: score, XP earned, Fino message, "Continue" button |

### 9.8 AI Tutor Chat Screen
```
┌──────────────────────────────────────┐
│  🦊 Chat with Fino                   │
│  ℹ️ Educational AI — not real advice  │
│──────────────────────────────────────│
│                                      │
│  🦊 Hey Alex! You just finished      │
│     learning about interest rates.   │
│     Got any questions? 😊            │
│                                      │
│  Try asking:                         │
│  ┌─────────────────────────────┐     │
│  │ "What is compound interest?"│     │
│  └─────────────────────────────┘     │
│  ┌─────────────────────────────┐     │
│  │ "Why are minimum payments   │     │
│  │  a trap?"                   │     │
│  └─────────────────────────────┘     │
│                                      │
│  👤 What happens if I miss a         │
│     credit card payment?             │
│                                      │
│  🦊 Great question! If you miss...   │
│     [detailed friendly response]     │
│                                      │
│  💡 This is for learning only.       │
│                                      │
│──────────────────────────────────────│
│  ┌──────────────────────┐  [Send]    │
│  │ Type your question...│            │
│  └──────────────────────┘            │
└──────────────────────────────────────┘
```

### 9.9 Simulator Screen
| Element | Description |
|---|---|
| Header | Simulator name + icon |
| Input section | Labeled fields with input validation |
| Calculate button | Primary CTA, centered |
| Results panel | Card with key metrics, color-coded |
| Comparison table | Side-by-side scenarios (where applicable) |
| Educational message | Fino callout at the bottom |
| Disclaimer | "This simulation is for learning purposes only." |

### 9.10 Progress Screen
| Element | Description |
|---|---|
| Header | "Your Progress" |
| XP counter | Large number + level title |
| Level progress bar | XP toward next level |
| Streak section | 🔥 counter + streak calendar (heatmap) |
| Badges grid | 2×5 grid of earned/locked badges |
| Track progress | List of all tracks with completion % |
| Stats | Total lessons / quizzes / simulations completed |

### 9.11 Profile / Settings
| Element | Description |
|---|---|
| Display name | Editable |
| Level + XP | Read-only display |
| Theme toggle | Light / Dark (Nice-to-have) |
| Reset progress | With confirmation dialog |
| About | App version, credits |
| Disclaimer | "FinLingo is an educational tool. Not financial advice." |

---

## UX Principles

### 1. Progressive Disclosure
Don't overwhelm — show one thing at a time. Lock advanced tracks until basics are done. Reveal depth on demand ("Learn more" links, AI follow-ups).

### 2. Immediate Feedback
Every action gets a visible response within 200ms — XP popup, color change, Fino reaction. Users should never wonder "did that work?"

### 3. Consistency
Same layout patterns across all screens. Same button styles, same card shapes, same feedback patterns. Predictability builds trust.

### 4. Safe Exploration
No irreversible actions. Users can retake quizzes, ask unlimited questions, run simulations repeatedly. Mistakes are celebrated as learning.

### 5. Minimal Cognitive Load
One clear CTA per screen. Short text. Generous whitespace. No decision paralysis — guide the user through the flow.

---

## Accessibility Considerations

| Area | Implementation |
|---|---|
| **Color contrast** | Minimum 4.5:1 ratio for text (WCAG AA) |
| **Font size** | Base 16px minimum, scalable |
| **Touch targets** | Minimum 44×44px for all interactive elements |
| **Screen reader** | Semantic HTML, ARIA labels on interactive elements |
| **Color alone** | Never rely only on color to convey meaning (add icons/text) |
| **Keyboard navigation** | Tab-navigable for web version |
| **Motion** | Respect prefers-reduced-motion for animations |
| **Language** | Plain language, readability level: Grade 7–8 |
| **Error messages** | Descriptive, actionable, non-technical |

---

## Beginner-Friendly Design Recommendations

1. **Default to simplicity** — If you can remove it and the experience still works, remove it.
2. **Use familiar patterns** — Card layouts, bottom navigation, rounded buttons — things users already know.
3. **Show progress everywhere** — Every screen should remind users how far they've come.
4. **Celebrate small wins** — Completing even one lesson should feel like an achievement.
5. **Avoid walls of text** — Use bullets, callouts, visuals, and spacing.
6. **Make the next step obvious** — Always have a clear "what do I do next?" answer visible.
7. **Provide safety nets** — "Are you sure?" dialogs, undo options, retry capabilities.
