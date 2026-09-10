# ReAct AI Agent with Gemini 2.5 Flash

A simple **ReAct-style AI agent** built with **LangChain, Google Gemini 2.5 Flash, and Streamlit**. The agent can understand user tasks, decide when external information is required, use tools to gather information, analyze the results, and provide a structured final response.

## 🚀 Features

- 🤖 **Gemini 2.5 Flash** as the underlying LLM
- 🧠 **ReAct-style agent** for iterative problem solving
- 🔎 **DuckDuckGo Search** for retrieving current and unfamiliar information
- 📚 **Wikipedia** for general knowledge and factual information
- 🖥️ **Streamlit UI** for an interactive web interface
- 🐛 **LangChain Debug Mode** for observing agent execution
- 🔐 Environment variable support using `.env`

## 🏗️ How It Works

The agent follows a ReAct-style workflow:

```text
User Task
    ↓
Understand the Task
    ↓
Determine Required Information
    ↓
Select Appropriate Tool
    ↓
Wikipedia / DuckDuckGo Search
    ↓
Analyze Tool Results
    ↓
Need More Information?
   ↙        ↘
 Yes         No
 ↓            ↓
Use Tool    Final Answer
 Again
```

The agent is instructed to verify information using available search tools when dealing with current, recent, unfamiliar, or factual topics instead of relying purely on the model's existing knowledge.

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **Google Gemini 2.5 Flash**
- **LangChain Community Tools**
- **Wikipedia**
- **DuckDuckGo Search**
- **Streamlit**
- **python-dotenv**

## 📂 Project Structure

```text
ReAct-Agent/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd ReAct-Agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

> Never commit your `.env` file or expose your API key publicly.

### 4. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## 💡 Example Tasks

You can ask the agent questions such as:

```text
Who is the current CEO of Microsoft?
```

```text
Explain the difference between LangChain and LangGraph.
```

```text
Who was the first person to walk on the Moon?
```

```text
What is the capital of Australia?
```

For questions requiring external information, the agent can use **Wikipedia or DuckDuckGo Search** before generating its final response.

## 🎯 Project Objective

The main objective of this project is to understand how **AI agents differ from traditional LLM-based applications** by giving the model access to external tools and allowing it to determine when those tools are needed.

This project serves as a foundation for building more advanced agentic applications involving **APIs, databases, enterprise tools, automation, and multi-step workflows**.

## 🔮 Future Improvements

- Add custom tools and APIs
- Integrate enterprise APIs such as **Zoho**
- Add conversation/memory support
- Display agent/tool execution steps in the UI
- Add multiple specialized agents
- Implement structured outputs
- Add database integration
- Deploy the application using Streamlit Cloud or AWS
