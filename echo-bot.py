# import streamlit as st
# import numpy as np
# 
# with st.chat_message("assistant"):
#    st.write("What's Up Turd-Ball??? 👋")
#    st.bar_chart(np.random.randn(30, 3))

import streamlit as st

st.title("Echo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
if user_input := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": f"Echo: {user_input}"})
    st.rerun()
