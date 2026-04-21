import streamlit as st

from src.ui.base_layout import base_layout, base_background_dashboard

def student_screen():
    base_layout()
    base_background_dashboard()
    st.header("Welcome, Student 👋")
    if st.button("Back"):
        st.session_state["login_type"] = None
        st.rerun()