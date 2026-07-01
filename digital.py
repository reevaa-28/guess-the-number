import streamlit as st
from datetime import datetime

st.title("Digital Clock")

current_time = datetime.now().strftime("%H:%M:%S")

st.markdown(
    f"<h1 style='text-align:center;'>{current_time}</h1>",
    unsafe_allow_html=True )

if st.button("Refresh Time"):
    st.rerun()