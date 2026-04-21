import streamlit as st

from src.ui.base_layout import base_layout, base_background_dashboard

def professor_screen():
    base_layout()
    base_background_dashboard()
    st.header("Professor Screen")
    if st.button("Back"):
        st.session_state["login_type"] = None
        st.rerun()