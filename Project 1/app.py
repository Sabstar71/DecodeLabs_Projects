import streamlit as st

st.set_page_config(
    page_title="SmartChat",
    layout="wide"
)

from ui import (
    about,
    ai_chat,
    home,
    load_css,
    rule_chat,
    settings,
    sidebar,
)

load_css()

page = sidebar()

if page == "Home":
    home()

elif page == "Rule-Based Chat":
    rule_chat()

elif page == "AI Chat":
    ai_chat()

elif page == "Settings":
    settings()

elif page == "About":
    about()