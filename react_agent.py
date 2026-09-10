import streamlit as st

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain_core.globals import set_debug

load_dotenv()

# Enable LangChain debug logging
set_debug(True)

# Create Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# Load external tools
tools = load_tools(
    [
        "wikipedia",
        "ddg-search"
    ]
)

# System prompt
prompt = """
You are an AI agent that solves problems using a ReAct-style approach.

For every task:

1. Understand what the user is asking.
2. Think about what information is required.
3. Use an appropriate tool when necessary.
4. Examine the tool's result.
5. Decide whether another tool call is required.
6. Continue until you have enough reliable information.
7. Provide a clear and well-structured final answer.

IMPORTANT:
- For current, recent, unfamiliar, or factual topics, use the available
  search tools to verify the information before answering.
- Do not make up facts when you are uncertain.
- When you have sufficient information, stop using tools and provide the
  final answer to the user.
"""
# Create the ReAct-style agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt
)

# Streamlit UI
st.title("ReAct Agent")

st.write("Using Gemnini 2.5 Flash with ReAct-style reasoning to answer your questions.")

task = st.text_input("Assign me a Task!")

# Run the agent
if task:

    with st.spinner("Agent is thinking..."):

        result = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": task
                    }
                ]
            }
        )

    final_message = result["messages"][-1]

    content = final_message.content

    # Extract only the text from Gemini's response
    if isinstance(content, str):

        final_answer = content

    elif isinstance(content, list):

        text_parts = []

        for block in content:

            if isinstance(block, dict):

                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

            elif isinstance(block, str):

                text_parts.append(block)

        final_answer = "\n".join(text_parts)

    else:

        final_answer = str(content)

#displays final answer
    st.subheader("Answer")
    st.write(final_answer)