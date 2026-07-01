import streamlit as st

st.title("Color Change Project")

if st.button("Change to Red"):
    st.markdown(
        """
        <div style="
            width:200px;
            height:100px;
            background-color:red;
            border:2px solid black;">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <div style="
            width:200px;
            height:100px;
            background-color:gray;
            border:2px solid black;">
        </div>
        """,
        unsafe_allow_html=True
    )