# 🤖 AI Personal Assistant Agent (ReAct-Based)

## 📌 Overview

This project implements a modular AI Personal Assistant Agent using clean software architecture and design patterns.
The agent simulates intelligent behavior by analyzing user input and selecting appropriate tools.

Due to external API limitations, a mock reasoning layer is used while preserving full system architecture and extensibility.

---

## 🎯 Objectives

* Design a modular AI agent
* Apply SOLID principles
* Implement Strategy and Factory patterns
* Simulate the ReAct (Reason → Act → Observe) loop
* Ensure scalability and maintainability

---

## 🏗️ Architecture

The system is divided into independent components:

* **Agent** – controls logic and decision-making
* **MemoryManager** – stores conversation history
* **ToolRegistry** – dynamically manages tools
* **Tools** – independent functional modules

---

## 🔁 ReAct Pattern

The agent follows:

1. Reason – interpret user input
2. Act – select tool
3. Observe – get result
4. Respond – output answer

---

## 🧰 Tools

| Tool       | Description                           |
| ---------- | ------------------------------------- |
| Calculator | Evaluates expressions                 |
| Time       | Returns current time (Riga timezone)  |
| Translator | Translates text (real implementation) |
| Weather    | Returns predefined Riga weather       |

---

## ⚙️ Features

* Natural language interaction
* Context-aware responses
* Modular architecture
* Tool-based reasoning
* Riga-specific time and weather handling

---

## 📂 Project Structure

```
ai-agent/
│
├── agent.py
├── memory.py
├── tool_registry.py
├── main.py
├── README.md
│
└── tools/
    ├── base_tool.py
    ├── calculator_tool.py
    ├── time_tool.py
    ├── translator_tool.py
    └── weather_tool.py
```

---

## 🚀 How to Run

```
pip install deep-translator pytz
python main.py
```

---

## 🧪 Example Usage

```
You: 2+2
Assistant: 4

You: what time is it
Assistant: 2026-03-29 15:00:00

You: weather
Assistant: The weather in Riga is cloudy, 10°C

You: translate hello to spanish
Assistant: hola
```

---

## ⚠️ Challenges & Solutions

### ❌ Gemini API Quota Issue

The Gemini API required billing activation, which was not available in this environment.

### ✅ Solution

A mock reasoning layer was implemented to simulate AI behavior while maintaining full architecture.

---

## 💡 Design Decisions

* Focused on architecture over external API dependency
* Ensured system extensibility
* Implemented tool-based reasoning instead of direct API reliance

---

## 📈 Future Improvements

* Integrate real AI API
* Add GUI
* Improve NLP understanding
* Expand tools

---

## 🏁 Conclusion

This project demonstrates how to build a scalable AI agent system using proper software architecture and design patterns, even without relying on external AI APIs.

---

## 🔗 GitHub

(Your repository link here)
