import streamlit as st

def footer():
    st.markdown(f"""
            <div style='margin-top:2rem; display:flex; justify-content:center; align-items: center;'>
                <p style="font-weight: bold;">Created with ❤️ by <a href="https://shubhamxgupta.xyz"><strong>Shubham</strong></a>.</p>
            </div>
    """, unsafe_allow_html=True)