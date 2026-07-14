import streamlit as st

from components.header import show_header
from components.cards import feature_cards

from ai import get_ai_response
from rules import get_rule_response
from utils import (
    clear_ai_chat,
    clear_rule_chat,
    initialize_session,
)


# ---------------- CSS ---------------- #

def load_css():
    try:
        with open("assets/style.css") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True,
            )
    except FileNotFoundError:
        pass


# ---------------- Sidebar ---------------- #

def sidebar():

    with st.sidebar:

        st.markdown("# SmartChat")

        st.caption("Rule-Based + AI Assistant")

        st.success("Online")

        st.divider()

        page = st.radio(
            "Navigation",
            [
                "Home",
                "Rule-Based Chat",
                "AI Chat",
                "Settings",
                "About",
            ],
        )

        st.divider()

        st.markdown(
            """
Developer

**Sabeeh Waheed**

DecodeLabs Internship

Version **1.0**
"""
        )

    return page


# ---------------- Home ---------------- #

def home():

    show_header()

    st.markdown("<br>", unsafe_allow_html=True)

    feature_cards()

    st.markdown("---")

    st.subheader("About SmartChat")

    st.write(
        """
SmartChat is a dual-mode chatbot developed for the DecodeLabs AI Internship.

It provides two chat modes:

• Rule-Based Chat for predefined responses.

• AI Chat powered by OpenRouter for intelligent conversations.

Choose any mode from the sidebar and start chatting.
"""
    )

    st.markdown("---")

    st.subheader("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Chat Modes", "2")
    col2.metric("Framework", "Streamlit")
    col3.metric("Language", "Python")
    col4.metric("AI", "OpenRouter")
# ---------------- Rule Chat ---------------- #

def rule_chat():

    st.title("Rule-Based Chat")

    st.caption("Offline Assistant")

    initialize_session()

    for message in st.session_state.rule_messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask something...")

    if prompt:

        st.session_state.rule_messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = get_rule_response(prompt)

        st.session_state.rule_messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        st.rerun()


# ---------------- AI Chat ---------------- #

def ai_chat():

    st.title("AI Chat")

    st.caption("Powered by OpenRouter")

    initialize_session()

    for message in st.session_state.ai_messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask anything...")

    if prompt:

        st.session_state.ai_messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        messages = [
            {
                "role": m["role"],
                "content": m["content"],
            }
            for m in st.session_state.ai_messages
        ]

        with st.spinner("Thinking..."):

            response = get_ai_response(messages)

        st.session_state.ai_messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        st.rerun()


# ---------------- Settings ---------------- #

def settings():

    st.title("Settings")

    initialize_session()

    st.subheader("Chat")

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Clear Rule Chat", use_container_width=True):

            clear_rule_chat()

            st.success("Rule chat cleared.")

    with col2:

        if st.button("Clear AI Chat", use_container_width=True):

            clear_ai_chat()

            st.success("AI chat cleared.")

    st.divider()

    st.subheader("Application")

    st.write("Theme: Follow Streamlit settings")

    st.write("Current Version: 1.0")


# ---------------- About ---------------- #

def about():

    st.title("About SmartChat")

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.metric("Version", "1.0")

        st.metric("Developer", "Sabeeh")

    with col2:

        st.metric("Framework", "Streamlit")

        st.metric("Backend", "Python")

    st.markdown("---")

    st.subheader("Project Overview")

    st.write(
        """
SmartChat is a dual-mode chatbot developed as part of the DecodeLabs AI Internship.

It combines a traditional Rule-Based Chatbot with a modern AI Assistant powered by OpenRouter.
"""
    )

    st.subheader("Features")

    st.write(
        """
- Rule-Based Responses

- AI Powered Conversations

- Clean Chat Interface

- Chat History

- Modern UI

- Streamlit Dashboard
"""
    )

    st.subheader("Technologies")

    st.write(
        """
Python

Streamlit

OpenRouter API

dotenv

Rule-Based NLP
"""
    )