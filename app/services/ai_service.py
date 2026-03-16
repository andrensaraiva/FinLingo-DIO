"""
FinLingo — AI Service Module
Handles communication with AI providers (OpenAI / Gemini).
"""

from app.config import (
    AI_PROVIDER, OPENAI_API_KEY, OPENAI_MODEL,
    GOOGLE_API_KEY, GEMINI_MODEL,
    AI_TEMPERATURE, AI_MAX_TOKENS, SYSTEM_PROMPT
)


def build_system_prompt(user_context: dict) -> str:
    """Build a personalized system prompt with user context."""
    return SYSTEM_PROMPT.format(
        user_name=user_context.get("user_name", "Learner"),
        current_track=user_context.get("current_track", "None"),
        last_lesson=user_context.get("last_lesson", "None"),
        level=user_context.get("level", 1)
    )


def get_ai_response(user_message: str, user_context: dict, chat_history: list = None) -> str:
    """
    Get a response from the configured AI provider.

    Args:
        user_message: The user's question or message.
        user_context: Dict with user_name, current_track, last_lesson, level.
        chat_history: Optional list of {"role": str, "content": str} dicts.

    Returns:
        The AI's response as a string.
    """
    system_prompt = build_system_prompt(user_context)

    if AI_PROVIDER == "openai":
        return _call_openai(system_prompt, user_message, chat_history)
    elif AI_PROVIDER == "gemini":
        return _call_gemini(system_prompt, user_message, chat_history)
    else:
        return _fallback_response(user_message)


def _call_openai(system_prompt: str, user_message: str, chat_history: list = None) -> str:
    """Call OpenAI API."""
    if not OPENAI_API_KEY:
        return _fallback_response(user_message)

    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        messages = [{"role": "system", "content": system_prompt}]

        if chat_history:
            messages.extend(chat_history[-10:])  # Keep last 10 messages for context

        messages.append({"role": "user", "content": user_message})

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=AI_TEMPERATURE,
            max_tokens=AI_MAX_TOKENS
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Oops! I had trouble processing that. Error: {str(e)}\n\nTry again or ask a different question!"


def _call_gemini(system_prompt: str, user_message: str, chat_history: list = None) -> str:
    """Call Google Gemini API."""
    if not GOOGLE_API_KEY:
        return _fallback_response(user_message)

    try:
        import google.generativeai as genai
        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            system_instruction=system_prompt
        )

        # Build conversation history
        history = []
        if chat_history:
            for msg in chat_history[-10:]:
                role = "user" if msg["role"] == "user" else "model"
                history.append({"role": role, "parts": [msg["content"]]})

        chat = model.start_chat(history=history)
        response = chat.send_message(user_message)

        return response.text

    except Exception as e:
        return f"Oops! I had trouble processing that. Error: {str(e)}\n\nTry again or ask a different question!"


def _fallback_response(user_message: str) -> str:
    """Provide a helpful fallback when no AI API is configured."""
    user_lower = user_message.lower()

    responses = {
        "credit card": (
            "A credit card lets you borrow money from a bank to make purchases. "
            "You pay it back monthly. If you pay in full by the due date, no interest is charged. "
            "If you carry a balance, interest accumulates — often at 20%+ APR. "
            "The key to using credit cards wisely: only charge what you can pay off each month!\n\n"
            "💡 *This is for educational purposes only.*"
        ),
        "interest": (
            "Interest is the cost of using someone else's money. When you borrow, you pay interest "
            "to the lender. When you save, the bank pays you interest for using your money. "
            "Simple interest is calculated on the original amount, while compound interest is "
            "calculated on the principal plus accumulated interest — it grows faster over time!\n\n"
            "💡 *This is for educational purposes only.*"
        ),
        "emergency fund": (
            "An emergency fund is money saved for unexpected expenses — job loss, medical bills, "
            "car repairs. Experts recommend 3-6 months of essential expenses. Start small: "
            "even $500 is a great first goal. Keep it in a separate savings account where "
            "it's safe and accessible.\n\n"
            "💡 *This is for educational purposes only.*"
        ),
        "sav": (
            "Saving is setting aside money for future use. The best strategies: pay yourself first "
            "(save on payday before spending), automate transfers to a savings account, and start "
            "small — even $25/month adds up. The key is consistency, not amount!\n\n"
            "💡 *This is for educational purposes only.*"
        ),
        "invest": (
            "Investing means putting money into something with the expectation of growth over time. "
            "Common types: savings accounts (low risk), bonds (medium risk), stocks (higher risk), "
            "and index funds (diversified). For beginners, start with understanding risk tolerance "
            "and consider index funds for diversification.\n\n"
            "💡 *This is for educational purposes only. Not financial advice.*"
        ),
        "budget": (
            "A budget is a plan for your money. The popular 50/30/20 rule suggests: 50% for needs "
            "(rent, food, utilities), 30% for wants (entertainment, dining), and 20% for savings "
            "and debt repayment. Track your spending for a month to see where your money goes, "
            "then adjust!\n\n"
            "💡 *This is for educational purposes only.*"
        ),
    }

    for keyword, response in responses.items():
        if keyword in user_lower:
            return f"🦊 Great question! {response}"

    return (
        "🦊 That's a great question! I'm currently running without an AI API key, "
        "so my answers are limited. Here are some things you can ask me about:\n\n"
        "- Credit cards\n- Interest rates\n- Emergency funds\n- Saving money\n"
        "- Investing basics\n- Budgeting\n\n"
        "To get full AI-powered responses, add your OpenAI or Gemini API key to the `.env` file!\n\n"
        "💡 *This is for educational purposes only.*"
    )


def get_quiz_explanation(question: str, correct_answer: str, user_answer: str, user_context: dict) -> str:
    """Generate an AI-enhanced explanation for a quiz question."""
    prompt = (
        f"The user answered a quiz question.\n"
        f"Question: {question}\n"
        f"Correct answer: {correct_answer}\n"
        f"User's answer: {user_answer}\n"
        f"The user got it {'right' if user_answer == correct_answer else 'wrong'}.\n\n"
        f"Give a brief, encouraging explanation (2-3 sentences) in Fino's friendly style. "
        f"If they got it wrong, explain why the correct answer is right without being condescending."
    )
    return get_ai_response(prompt, user_context)


def get_simulation_insight(simulation_type: str, inputs: dict, results: dict, user_context: dict) -> str:
    """Generate an AI-powered educational insight after a simulation."""
    prompt = (
        f"The user just ran a '{simulation_type}' simulation.\n"
        f"Inputs: {inputs}\n"
        f"Results: {results}\n\n"
        f"Give a brief, educational takeaway (2-3 sentences) in Fino's friendly style. "
        f"Explain what the numbers mean in practical terms and offer one actionable tip."
    )
    return get_ai_response(prompt, user_context)
