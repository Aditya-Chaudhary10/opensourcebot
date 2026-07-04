import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:
    sys.path.append(str(ROOT_DIR))

import streamlit as st

from chatbot.chatbot import Chatbot
st.set_page_config(
    page_title="Open Source Chatbot",
    page_icon="🤖",
    layout="wide",
)

# ----------------------------
# Session State
# ----------------------------

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# Sidebar
# ----------------------------

with st.sidebar:

    st.title("🤖 Open Source Chatbot")

    st.markdown("---")

    st.write("### Current Model")
    st.success("Gemma 3 (Ollama)")

    st.markdown("---")

    if st.button("🗑 Clear Chat", use_container_width=True):

        st.session_state.messages = []

        if hasattr(st.session_state.chatbot, "memory"):
            st.session_state.chatbot.memory.clear()

        elif hasattr(st.session_state.chatbot, "messages"):
            st.session_state.chatbot.messages = []

        st.rerun()

    st.markdown("---")

    st.caption("Built with ❤️ using LangChain + Ollama")

# ----------------------------
# Title
# ----------------------------

st.title("🤖 Open Source Chatbot")

st.caption("Powered by LangChain + Ollama")

# ----------------------------
# Display Chat
# ----------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ----------------------------
# User Input
# ----------------------------

if prompt := st.chat_input("Type your message..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = st.session_state.chatbot.chat(prompt)

            st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )