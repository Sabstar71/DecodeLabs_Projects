import streamlit as st


def feature_cards():

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
<div class="card">

<h2>Rule Chat</h2>

<p>
Offline chatbot using predefined intents.
</p>

</div>
""",
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            """
<div class="card">

<h2>AI Chat</h2>

<p>
OpenRouter powered intelligent assistant.
</p>

</div>
""",
            unsafe_allow_html=True,
        )