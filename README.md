# 🤖 AI Personal Assistant Agent (ReAct-Based)

## 📌 Overview

This project implements a modular AI Personal Assistant Agent designed using modern software engineering principles.
The agent simulates intelligent behavior by maintaining memory, reasoning about user input, and dynamically selecting tools to execute tasks.

The system follows a structured architecture inspired by real-world AI agents, emphasizing scalability, maintainability, and extensibility.

---

## 🎯 Objectives

* Build an adaptive AI agent using clean architecture
* Apply SOLID principles in practice
* Implement design patterns (Strategy, Factory)
* Simulate the ReAct (Reason → Act → Observe) loop
* Create a modular and extensible system

---

## 🏗️ Architecture

The system is divided into independent components:

### 🔹 Agent

Controls the execution loop and decision-making process.

### 🔹 MemoryManager

Stores conversation history and maintains context.

### 🔹 ToolRegistry

Handles dynamic tool registration and execution (Factory Pattern).

### 🔹 Tools

Independent modules implementing specific functionality (Strategy Pattern).

---

## 🔁 ReAct Pattern Implementation

The agent follows the ReAct loop:

1. **Reason** → Understand user input
2. **Act** → Select appropriate tool
3. **Observe** → Get tool result
4. **Respond** → Return output

---

## 🧰 Tools Implemented

| Tool       | Description                            |
| ---------- | -------------------------------------- |
| Calculator | Evaluates mathematical expressions     |
| Time       | Returns current system time            |
| Translator | Translates text using external library |
| Weather    | Provides mock weather information      |

---

## ⚙️ Technologies Used

* Python 3.10+
* OOP (Object-Oriented Programming)
* SOLID Principles
* Design Patterns:

  * Strategy Pattern
  * Factory Pattern
* CLI (Command Line Interface)

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

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/ai-agent.git
cd ai-agent
```

### 2. Install dependencies

```
pip install deep-translator
```

### 3. Run the agent

```
python main.py
```

---

## 🧪 Example Usage

```
You: 2+2
Assistant: 4

You: what time is it
Assistant: 2026-03-29 14:21:00

You: translate hello to spanish
Assistant: hola

You: good morning in french
Assistant: bonjour

You: weather in Tashkent
Assistant: The weather in Tashkent is sunny, 25°C
```

---

## ⚠️ Challenges Faced & Solutions

### ❌ 1. Gemini API Quota Error

**Error:**

```
429 RESOURCE_EXHAUSTED
quota = 0
```

**Cause:**

* Free tier access not enabled
* API key had no usage quota

**Solution:**

* Attempted new project and API keys
* Verified configuration
* Final approach: replaced live API with mock agent

---

### ❌ 2. Deprecated Library Issue

**Error:**

```
google.generativeai is deprecated
```

**Solution:**

* Attempted migration to new SDK (`google.genai`)
* Faced compatibility issues
* Switched to mock implementation for stability

---

### ❌ 3. Model Not Found Error

**Error:**

```
404 model not found
```

**Cause:**

* Incorrect model name
* API version mismatch

**Solution:**

* Tested multiple models
* Confirmed API limitations
* Removed dependency on external API

---

### ❌ 4. Translation Logic Bug

**Problem:**

```
Translated ''hello'' to spanish
```

**Cause:**

* Incorrect string parsing
* Duplicate quotation marks

**Solution:**

* Cleaned input text
* Improved parsing logic using:

```
split("to", 1)
```

---

### ❌ 5. Input Misinterpretation

**Problem:**
User entered:

```
Translated 'hello' to spanish
```

**Solution:**

* Clarified correct input format
* Added support for:

```
hello in spanish
```

---

## 💡 Design Decisions

* Used mock AI layer due to API limitations
* Prioritized architecture over API dependency
* Ensured all components follow SRP
* Avoided hardcoded logic using ToolRegistry

---

## 📈 Future Improvements

* Integrate real AI API (Gemini / OpenAI)
* Add GUI interface
* Improve natural language parsing
* Add persistent database for memory
* Expand tool ecosystem

---

## 👨‍💻 Author

Student: Temur Tursunboev
Built with focus on architecture and design patterns

---

## ⭐ Conclusion

This project demonstrates how to design a scalable AI agent system using clean architecture principles, even without relying on external AI services.

It highlights the importance of:

* Proper system design
* Separation of concerns
* Extensibility
* Robust error handling

---
