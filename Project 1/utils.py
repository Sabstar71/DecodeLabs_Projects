import streamlit as st


def initialize_session():
    defaults = {
        "rule_messages": [],
        "ai_messages": [],
        "theme": "Light"
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def clear_rule_chat():
    st.session_state.rule_messages = []


def clear_ai_chat():
    st.session_state.ai_messages = []