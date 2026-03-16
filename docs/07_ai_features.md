# 7. AI Features

## How Generative AI Is Used in FinLingo

### 7.1 AI Tutor Chat (Fino Chat)

The core AI feature is a **conversational financial tutor** that users access from the dashboard or after completing lessons.

**Capabilities:**

| Capability | Example |
|---|---|
| **Answer beginner finance questions** | "What is compound interest?" → Clear, jargon-free explanation |
| **Explain concepts in simple language** | "Explain APR like I'm 15" → Age-appropriate analogy |
| **Contextualize to current lesson** | User just finished Credit Card Basics → AI references that context in answers |
| **Generate motivational feedback** | "You're making great progress! You've covered 3 tracks already." |
| **Support FAQs** | Pre-defined common questions with AI-enhanced answers |
| **Scenario explanations** | "What happens if I invest $100/month for 10 years at 7%?" |

### 7.2 Context-Aware Responses

The AI tutor tracks the user's **current session context**:

```python
context = {
    "user_name": "Alex",
    "current_track": "Credit Card Basics",
    "last_lesson": "Interest Rates and Minimum Payments",
    "lessons_completed": 8,
    "level": 3,
    "xp": 340
}
```

This context is injected into the AI prompt so responses feel **personalized**:
- "Since you just learned about minimum payments, here's a deeper look at how interest compounds on unpaid balances…"
- "At Level 3, you're ready to explore how loans work — want me to explain?"

### 7.3 AI-Enhanced Quiz Feedback

When a user gets a quiz question wrong, the AI can generate a **custom explanation** beyond the static correct answer:

```
User selects: "A credit card is free money"  ❌
Static feedback: "Actually, a credit card is a loan from the bank."
AI-enhanced: "Good try! Think of it this way — when you use a credit card, 
you're borrowing from the bank. If you don't pay it back by the due date, 
you'll owe interest. It's more like a short-term loan than free money."
```

### 7.4 Simulation Explanations

After a user runs a financial simulation, the AI generates a **contextual educational takeaway**:

```
User simulates: $5,000 loan at 12% for 3 years
AI output: "Over 3 years, you'd pay about $966 in interest alone — that's 
almost 20% of your original loan! This shows why comparing interest rates 
before borrowing can save you hundreds."
```

### 7.5 Suggested Questions

To reduce blank-page anxiety, the AI chat offers **starter questions** based on context:

```
Suggested for you:
💬 "What's the difference between a debit and credit card?"
💬 "How do I start an emergency fund on a small income?"
💬 "What does APR actually mean?"
```

---

## AI System Prompt Design

The system prompt configures the AI's behavior. Here's the recommended structure:

```
You are Fino, the FinLingo AI financial tutor — a friendly, patient, and 
encouraging guide who explains financial concepts in simple, beginner-friendly 
language.

RULES:
1. Always explain concepts clearly using plain language and relatable analogies.
2. Never give specific financial advice (e.g., "You should invest in X").
3. Always include this disclaimer when relevant: "This is for educational 
   purposes only. For personal financial decisions, consult a qualified 
   professional."
4. If a user asks something outside of personal finance education, politely 
   redirect: "Great question, but that's outside my area! I'm best at 
   explaining money concepts. Try asking me about savings, credit, or loans!"
5. Never invent financial data, statistics, or rates. If unsure, say so.
6. Keep responses concise — aim for 3-5 sentences unless the user asks for 
   more detail.
7. Use encouraging language. Never make the user feel dumb.
8. If the user shares personal financial information, do NOT store it or 
   reference it beyond the current session.
9. Use the user's current lesson context to make answers relevant.
10. End responses with a follow-up question or suggestion when appropriate.

CONTEXT (injected per request):
- User name: {user_name}
- Current track: {current_track}
- Last completed lesson: {last_lesson}
- Level: {level}
```

---

## Guardrails and Safety

### What the AI Should Do
| Situation | Response |
|---|---|
| User asks a basic finance question | Answer clearly with educational framing |
| User asks "Should I invest in Bitcoin?" | "I can explain how cryptocurrency works, but I can't recommend specific investments. For personal advice, talk to a licensed financial advisor." |
| User asks about a specific bank product | "I can explain how that type of product generally works! But for details on your specific account, check directly with your bank." |
| User shares personal financial details | "Thanks for sharing — I'll use that context for our conversation, but I don't store any personal data. For personalized advice, consider speaking with a financial planner." |
| User asks something off-topic (e.g., cooking) | "Ha! I wish I could help with that, but I'm really only good at money stuff. 😄 Try asking me about budgeting or savings!" |
| User expresses financial stress/anxiety | "I hear you — money stuff can be stressful. Learning is a great first step, and you're already doing it. If you're feeling overwhelmed, talking to a financial counselor can really help. 💚" |

### What the AI Should Never Do
- ❌ Recommend specific financial products, stocks, or services
- ❌ Provide tax advice or legal guidance
- ❌ Store or recall personal data between sessions (MVP)
- ❌ Generate fake statistics or interest rates
- ❌ Make promises about financial outcomes
- ❌ Shame or judge the user's financial situation
- ❌ Pretend to be a licensed financial advisor

### Disclaimer Placement
- **In every AI chat response footer:** *"💡 Fino is an educational AI assistant. This is not financial advice."*
- **On the AI chat screen header:** *"Fino helps you learn — for personal decisions, consult a professional."*
- **After simulations:** *"This simulation is for learning purposes. Actual results may vary based on real-world conditions."*

---

## AI Integration Architecture

```
┌─────────────────────────────────────────────┐
│                  User Input                  │
│         "What is compound interest?"         │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│              Context Builder                 │
│  Injects: user name, current lesson,         │
│  level, last completed track                 │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│              System Prompt                   │
│  Fino personality + rules + guardrails       │
│  + injected context                          │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│           AI API (OpenAI / Gemini)           │
│  Model: GPT-4o-mini or Gemini 1.5 Flash     │
│  Temperature: 0.7                            │
│  Max tokens: 500                             │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│            Response Formatter                │
│  Add disclaimer footer                       │
│  Format for display (markdown → HTML)        │
│  Sanitize output                             │
└───────────────────┬─────────────────────────┘
                    │
                    ▼
┌─────────────────────────────────────────────┐
│             Displayed to User                │
│       Fino avatar + formatted response       │
│       + disclaimer + follow-up suggestions   │
└─────────────────────────────────────────────┘
```
