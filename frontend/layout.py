import streamlit as st

def render_navbar():
    """Renders a navigation sidebar for switching between pages."""
    st.sidebar.title("📌 Navigation")
    page = st.sidebar.radio("Go to", [
        "Home", "Input Form","Research","Planning","Blog Post", "Social Media Post",
        "Ad Copy", "Images", "Monitoring", "Strategy"
    ])
    return page
