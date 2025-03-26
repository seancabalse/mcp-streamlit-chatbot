# File: app/main.py

import streamlit as st
from mcp_client import call_tool

st.set_page_config(page_title="MCP Chatbot", layout="wide")
st.title("MCP + Streamlit Chatbot")

# Chat history setup
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input area
if prompt := st.chat_input("Ask something about your documents or tools..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Tool usage simulation
    if "summarize" in prompt.lower():
        response = call_tool("summarize_pdf", {"path": "data/resume.pdf"})
    else:
        response = "[stubbed reply] This is where your LLM call (via OpenRouter) goes."

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
