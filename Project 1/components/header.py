import streamlit as st


def show_header():

    st.markdown(
        """
<div class="hero">

<h1>SmartChat</h1>

<p>
Rule-Based + AI Assistant
</p>

</div>
""",
        unsafe_allow_html=True,
    )