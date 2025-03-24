import streamlit as st

def display_research_section():
    st.title("Research & Market Analysis")

    # ✅ Ensure the iframe points to the Research Agent
    st.markdown(
        """
        <iframe src="http://localhost:8505" width="100%" height="700px" style="border:none;"></iframe>
        """,
        unsafe_allow_html=True
    )
