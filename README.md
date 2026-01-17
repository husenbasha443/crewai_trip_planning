# 🧳 Trip Planning System using CrewAI

## 📌 Project Overview

This project implements an **AI-powered Trip Planning System** using **CrewAI**, where multiple intelligent agents collaborate to generate a **complete travel plan** for a user-specified destination.

The system uses a **multi-agent architecture** backed by a **Large Language Model (LLM)** to perform:

* Destination research
* Day-by-day itinerary planning
* Budget estimation and booking suggestions

Each agent handles a specialized responsibility, and together they generate a **comprehensive and personalized trip plan**.

---

## 🎯 Problem Statement

Travel planning can be challenging due to:

* Lack of information about destinations
* Difficulty in creating efficient itineraries
* Uncertainty around budget and bookings

This project solves the problem by simulating a **team of travel experts** using AI agents that collaboratively plan a trip based on user input.

---

## 🧠 Solution Architecture (Multi-Agent Workflow)

```
Travel Research Agent
        ↓
Itinerary Planner Agent
        ↓
Budget & Booking Advisor Agent
        ↓
Final Trip Plan
```

---

## 👥 Agents Description

### 1️⃣ Travel Research Agent

* Researches the destination provided by the user
* Identifies major attractions, best season, transport, and culture
* Produces a destination research summary

---

### 2️⃣ Itinerary Planner Agent

* Creates a structured day-by-day itinerary
* Optimizes sightseeing and travel flow
* Builds upon the research agent’s output

---

### 3️⃣ Budget & Booking Advisor Agent

* Estimates overall travel cost
* Suggests accommodation, transport, and booking tips
* Produces a budget-friendly travel recommendation

---

## 📂 Project Structure

```
crewai_trip_planning/
│
├── .venv/                          # Virtual environment
│
├── knowledge/                      # (Optional) RAG travel documents
│
├── src/
│   └── crewai_trip_planning/
│       ├── __init__.py
│       ├── crew.py                 # Agent & task orchestration
│       ├── main.py                 # Entry point (inputs & kickoff)
│       │
│       ├── config/
│       │   ├── agents.yaml         # Agent definitions
│       │   └── tasks.yaml          # Task definitions
│       │
│       └── tools/                  # (Optional) custom tools
│
├── tests/                          # (Optional) tests
│
├── .env                            # API keys (Groq / OpenAI / etc.)
├── .gitignore
├── pyproject.toml                  # Project dependencies
├── README.md                       # Project documentation
└── trip_report.md                  # Generated trip plan (optional)
```

---

## 📄 Configuration Files

### 🔹 agents.yaml

Defines:

* Agent roles
* Goals
* Background expertise

Each agent represents a **real-world travel planning role**.

---

### 🔹 tasks.yaml

Defines:

* Task descriptions
* Expected outputs
* Agent-task mapping
* Dynamic input binding using `{{ place }}`

Example:

```yaml
description: >
  Research the travel destination {{ place }} including attractions and travel tips.
```

---

## 📝 User Input

The user provides a **travel destination** at runtime.

Example input:

```python
inputs = {
  "place": "Goa"
}
```

This value is dynamically injected into all tasks and guides agent reasoning.

---

## ⚙️ Technologies Used

* **Python 3.11**
* **CrewAI**
* **LiteLLM**
* **Groq LLM (LLaMA 3.1)**
* **YAML (for configuration)**

---

## 🔐 Environment Variables (`.env`)

```env
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=your_groq_api_key
```

> ⚠️ Never commit API keys to GitHub.

---

## ▶️ How to Run the Project

### 1️⃣ Create Virtual Environment (using uv)

```bash
uv venv --python 3.11
```

### 2️⃣ Activate Virtual Environment (Windows)

```bash
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
uv pip install crewai crewai-tools
```

or

```bash
uv pip install -r requirements.txt
```

---

### 4️⃣ Set Environment Variables

Create a `.env` file and add your API keys.

---

### 5️⃣ Run the Crew

```bash
crewai run
```

---

## ✅ Output

The system generates a **complete trip plan**, including:

* Destination research
* Day-wise itinerary
* Estimated travel budget
* Booking and cost-saving tips

---

## 🧪 How to Verify LLM & Multi-Agent Execution

* Change the destination → output changes
* Each agent produces its own reasoning
* Output is not hardcoded
* Confirms real LLM-powered execution

---

## 🎓 Learning Outcomes

* Understanding multi-agent AI systems
* Practical usage of CrewAI
* LLM-driven planning workflows
* Prompt engineering with dynamic inputs
* Real-world AI system design

---

## Understanding Your Crew

The **Trip Planning Crew** consists of multiple AI agents, each with a unique role and goal. These agents collaborate through tasks defined in `config/tasks.yaml` and are configured in `config/agents.yaml`.

Together, they simulate how human travel planners research destinations, organize itineraries, and manage budgets.

---

## Support

For support, questions, or feedback regarding CrewAI:

* 📘 Documentation: [https://docs.crewai.com](https://docs.crewai.com)
* 🧑‍💻 GitHub: [https://github.com/joaomdmoura/crewai](https://github.com/joaomdmoura/crewai)
* 💬 Discord: [https://discord.com/invite/X4JWnZnxPb](https://discord.com/invite/X4JWnZnxPb)
* 🤖 Chat with docs: [https://chatg.pt/DWjSBZn](https://chatg.pt/DWjSBZn)

---

## 🏁 Conclusion

This project demonstrates how **LLM-powered multi-agent systems** can automate real-world planning tasks such as trip planning. The modular design allows easy extension to other domains like finance, healthcare, and customer support.

---


