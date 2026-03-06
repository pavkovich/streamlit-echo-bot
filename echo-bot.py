import streamlit as st

prompt = st.chat_input("What's Up Dog???")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
