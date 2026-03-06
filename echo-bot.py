import streamlit as st

prompt = st.chat_input("How can I help you...")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
