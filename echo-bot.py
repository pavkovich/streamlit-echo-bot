import streamlit as st

prompt = st.chat_input("What is your question?")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
