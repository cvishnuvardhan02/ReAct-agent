# 🤖 ReAct AI Agent 

> A tool-using AI agent built with **LangChain, Google Gemini 2.5 Flash, and Streamlit**, capable of reasoning through tasks and using external tools such as **Wikipedia** and **DuckDuckGo Search** to retrieve information.

---

## 📌 Overview

This project demonstrates how to build a **ReAct-style AI agent** using LangChain and Gemini 2.5 Flash.

Unlike a traditional LLM application that simply generates an answer from its existing knowledge, this agent can:

* Understand the user's task
* Determine whether additional information is required
* Select an appropriate external tool
* Retrieve and analyze information
* Perform additional tool calls when necessary
* Generate a final, structured response

The project is designed as a **foundation for building more advanced agentic AI applications** involving APIs, databases, automation, and enterprise systems.

---

## ✨ Features

| Feature                      | Description                                        |
| ---------------------------- | -------------------------------------------------- |
| 🤖 **Gemini 2.5 Flash**      | LLM powering the AI agent                          |
| 🧠 **ReAct Agent**           | Enables iterative tool-based problem solving       |
| 🔎 **DuckDuckGo Search**     | Retrieves current and unfamiliar information       |
| 📚 **Wikipedia**             | Provides general knowledge and factual information |
| 🖥️ **Streamlit UI**          | Simple and interactive web interface               |
| 🐛 **LangChain Debug Mode**  | Helps inspect agent execution                      |
| 🔐 **Environment Variables** | Secure API key configuration using `.env`          |

---

## 🏗️ Architecture

The agent follows a ReAct-style workflow where it determines whether it needs external information before producing its final answer.

```text
                    ┌─────────────────┐
                    │    User Task    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Understand Task │
                    └────────┬────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Need External Data?  │
                  └───────┬───────┬──────┘
                          │       │
                        Yes       No
                          │       │
                          ▼       │
                ┌─────────────────┐ │
                │ Select Tool     │ │
                └────────┬────────┘ │
                         │          │
              ┌──────────┴──────────┐
              ▼                     ▼
      ┌──────────────┐       ┌──────────────┐
      │  Wikipedia   │       │ DuckDuckGo   │
      └──────┬───────┘       │    Search    │
             │               └──────┬───────┘
             └──────────┬────────────┘
                        ▼
                ┌─────────────────┐
                │ Analyze Results │
                └────────┬────────┘
                         │
                         ▼
                 ┌───────────────┐
                 │ More Info     │
                 │ Required?     │
                 └───┬───────┬───┘
                     │       │
                    Yes      No
                     │       │
                     └───┐   ▼
                         │  ┌──────────────┐
                         └─►│ Final Answer │
                            └──────────────┘
```

---

## 🔄 How It Works

The agent is provided with a system prompt that instructs it to follow a ReAct-style approach:

```text
1. Understand the user's request
2. Determine what information is required
3. Select an appropriate tool when necessary
4. Examine the tool's response
5. Decide whether another tool call is required
6. Continue until sufficient information is available
7. Generate the final answer
```

For **current, recent, unfamiliar, or factual questions**, the agent is instructed to use external search tools rather than relying solely on the model's existing knowledge.

---

## 🛠️ Tech Stack

### Core Technologies

* 🐍 **Python**
* 🦜 **LangChain**
* ✨ **Google Gemini 2.5 Flash**
* 🎈 **Streamlit**

### Tools

* 📚 **Wikipedia**
* 🔎 **DuckDuckGo Search**

### Supporting Libraries

* `python-dotenv`
* `langchain-community`
* `langchain-google-genai`

---

## 📂 Project Structure

```text
ReAct-Agent/
│
├── react_agent.py         # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
└── README.md              # Project documentation
```

> ⚠️ Make sure `.env` is included in `.gitignore` before pushing the project to GitHub.

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone <your-repository-url>
cd ReAct-Agent
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

> 🔐 **Important:** Never commit your `.env` file or expose your API key on GitHub.

### 4️⃣ Run the Application

```bash
python -m streamlit run react_agent.py
```

The application will start locally and can be accessed through the URL provided by Streamlit.

---

## 💡 Example Queries

Once the application is running, you can provide tasks such as:

### Example 1 — Current Information

```text
Who is the current CEO of Microsoft?
```

The agent can use DuckDuckGo Search to retrieve up-to-date information.

### Example 2 — General Knowledge

```text
Who was the first person to walk on the Moon?
```

The agent can use Wikipedia to retrieve relevant information.


## 🎯 Project Objective

The primary objective of this project is to understand the fundamentals of **agentic AI systems** and how they differ from traditional LLM applications.

The project demonstrates how an LLM can be given access to external tools and allowed to determine **when and how those tools should be used** to solve a task.

This provides a foundation for developing more advanced systems such as:

* 🤖 AI assistants
* 🔌 API-powered agents
* 🗄️ Database agents
* 📧 Email automation agents
* 🏢 Enterprise AI agents
* 🔄 Multi-step workflow agents
* 📊 AI-powered analytics systems

---

## 🚀 Future Improvements

The project can be extended with several capabilities:

* [ ] 🔌 Add custom APIs and tools
* [ ] 📧 Integrate **Zoho Mail APIs**
* [ ] 🧠 Add conversation memory
* [ ] 🔍 Display agent/tool execution steps
* [ ] 🤖 Implement multiple specialized agents
* [ ] 📋 Add structured outputs
* [ ] 🗄️ Integrate databases
* [ ] 🔐 Improve authentication and security
* [ ] ☁️ Deploy using Streamlit Cloud or AWS
* [ ] 📊 Add agent performance analytics

---

## 🧠 What I Learned

Through this project, I explored:

* Building AI agents using **LangChain**
* Using **Gemini models** with LangChain
* Implementing **tool calling**
* Understanding the **ReAct agent architecture**
* Integrating external information sources
* Building interactive AI applications with **Streamlit**
* Managing API credentials using environment variables

---

## ⭐ Project Highlights

```text
LLM
 ↓
Gemini 2.5 Flash
 ↓
LangChain Agent
 ↓
ReAct-style Decision Making
 ↓
┌───────────────┬────────────────┐
│   Wikipedia   │ DuckDuckGo     │
│               │ Search         │
└───────────────┴────────────────┘
 ↓
Information Analysis
 ↓
Final Response
```

---

## 📜 License

This project is intended for **learning and experimentation with AI agents, LangChain, and tool-based LLM applications**.

---

### 👨‍💻 Author

**C Vishnu Vardhan**

If you found this project useful, consider giving the repository a ⭐ on GitHub!
