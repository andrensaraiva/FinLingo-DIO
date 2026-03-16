# 11. Technical Stack

## Approach A: Simple & Fast (Streamlit)

### Stack
| Component | Technology |
|---|---|
| **Frontend + Backend** | Python + Streamlit |
| **AI Integration** | OpenAI API (GPT-4o-mini) or Google Gemini API |
| **Data Storage** | JSON files (lessons, quizzes) + SQLite (user progress) |
| **Simulations** | Pure Python (math module) |
| **Deployment** | Streamlit Community Cloud (free) |

### Pros
- ✅ Single-language project (Python only)
- ✅ Very fast to prototype — build full UI in Python
- ✅ Free deployment on Streamlit Cloud
- ✅ Built-in session state for progress tracking
- ✅ Great for portfolio — shows rapid prototyping skills
- ✅ Ideal for students and junior developers

### Cons
- ❌ Limited UI customization (no custom CSS easily)
- ❌ Not a traditional web app architecture
- ❌ Reruns entire script on interaction (Streamlit model)
- ❌ Harder to create polished animations/transitions
- ❌ Not suitable for production-scale apps

### Best For
Portfolio demos, hackathons, proof of concept, Python-focused roles.

---

## Approach B: Polished & Professional (Flask)

### Stack
| Component | Technology |
|---|---|
| **Backend** | Python + Flask |
| **Frontend** | HTML5 + CSS3 (Tailwind CSS) + Vanilla JS |
| **AI Integration** | OpenAI API or Google Gemini API |
| **Data Storage** | JSON files (content) + SQLite (user data) |
| **Templating** | Jinja2 (Flask's built-in) |
| **Deployment** | Render / Railway / Vercel (free tiers) |

### Pros
- ✅ Real web app architecture (client-server separation)
- ✅ Full control over UI/UX — pixel-perfect design possible
- ✅ Demonstrates frontend + backend skills
- ✅ Tailwind CSS for rapid, beautiful styling
- ✅ REST API design for AI and simulations
- ✅ More impressive in interviews — shows full-stack thinking
- ✅ Easy to extend with authentication, databases, etc.

### Cons
- ❌ More code to write (HTML, CSS, JS in addition to Python)
- ❌ Requires basic frontend knowledge
- ❌ Slightly more complex deployment setup
- ❌ More files to maintain

### Best For
Full-stack portfolio projects, frontend-aware roles, professional-looking demos.

---

## Approach C: Modern Full-Stack (Optional / Advanced)

### Stack
| Component | Technology |
|---|---|
| **Backend** | Python + FastAPI |
| **Frontend** | React or Next.js |
| **AI Integration** | OpenAI API + LangChain (optional) |
| **Data Storage** | PostgreSQL or Supabase |
| **Auth** | Supabase Auth or Firebase Auth |
| **Deployment** | Vercel (frontend) + Railway (backend) |

### Pros
- ✅ Industry-standard architecture
- ✅ API-first design (can serve mobile apps too)
- ✅ Best performance and UX
- ✅ Maximum portfolio impact

### Cons
- ❌ Significantly more complex
- ❌ Requires JavaScript/TypeScript knowledge
- ❌ Longer development time
- ❌ May be overkill for a portfolio MVP

### Best For
Senior portfolio projects, startup-style MVPs, full-stack engineer roles.

---

## Recommended Approach

**Start with Approach A (Streamlit) for speed,** then migrate to **Approach B (Flask)** for polish. This gives you:
1. A working prototype in days (Streamlit)
2. A polished portfolio piece in weeks (Flask)
3. A natural migration story for interviews

---

## AI API Options

| Provider | Model | Cost | Best For |
|---|---|---|---|
| **OpenAI** | GPT-4o-mini | ~$0.15/1M input tokens | Best quality, most popular |
| **Google** | Gemini 1.5 Flash | Free tier available | Budget-friendly, fast |
| **Groq** | Llama 3.1 / Mixtral | Free tier available | Fast inference, open models |
| **Ollama** | Local models | Free (runs locally) | Offline development, no API costs |

### Recommendation
- **Development:** Use Gemini Flash (free tier) or Ollama (local)
- **Demo/Portfolio:** Use OpenAI GPT-4o-mini ($5 credit for new accounts)
- **Always:** Abstract the API behind a service layer so you can swap providers easily

---

## Key Libraries

```
# Core
streamlit>=1.30.0          # Approach A
flask>=3.0.0               # Approach B
python-dotenv>=1.0.0       # Environment variables

# AI
openai>=1.12.0             # OpenAI API
google-generativeai>=0.4.0 # Gemini API

# Data
sqlite3                    # Built-in Python
json                       # Built-in Python

# Utilities
math                       # Built-in Python (simulations)
datetime                   # Built-in Python (streaks)
```
