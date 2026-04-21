import streamlit as st

from src.components.footer import footer
from src.components.header import header_home
from src.ui.base_layout import base_background_home, base_layout

def home_screen():
    base_layout()
    base_background_home()
    header_home()
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.header("I am a Student")
        st.markdown("""
            <div style='height:180px; display:flex; align-items:center; justify-content:center; margin-bottom: 10px;'>
                <img src="https://i.ibb.co/844D9Lrt/mascot-student.png" style="max-height:100%; max-width:100%;" />
            </div>
        """, unsafe_allow_html=True)
        if st.button("Student Portal", type='primary', key='student_login', icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login_type"] = "student"
            st.rerun()

    with col2:
        st.header("I am a Teacher")
        st.markdown("""
            <div style='height:180px; display:flex; align-items:center; justify-content:center; margin-bottom: 10px;'>
                <img src="https://i.ibb.co/CsmQQV6X/mascot-prof.png" style="max-height:100%; max-width:100%;" />
            </div>
        """, unsafe_allow_html=True)
        if st.button("Teacher Portal", type='primary', key='teacher_login', icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login_type"] = "teacher"
            st.rerun()
    
    footer()
