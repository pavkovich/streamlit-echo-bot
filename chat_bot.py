import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
    [
        "Hi there! How can I help you today?",
        "That’s an interesting question — let me think about that for a second.",
        "I can definitely help with that! Could you give me a bit more detail?",
        "Sure thing! Here’s what I found...",
        "Hey! How’s your day going so far?",
        "Absolutely! Let me walk you through the steps.",
        "Hmm, I’m not entirely sure — want me to look it up?",
        "Got it! I’ll take care of that right now.",
        "Thanks for letting me know. I’ll make a note of it!",
        "Would you like me to explain that in simple terms or more technically?",
        "Good question! The short answer is yes, but there’s more to it.",
        "Sounds great. What would you like to do next?",
        "No problem! Let’s fix that together.",
        "I like where this is going. Tell me more!",
        "Oops! That didn’t go as planned — let’s try again.",
        "Here’s a quick summary of what we discussed so far.",
        "Gotcha! I’ll remember that for next time.",
        "Nice choice! That’s actually a pretty popular option.",
        "Thanks for your patience — this won’t take long.",
        "Would you like me to recommend a few examples?",
        "Good catch! You’re absolutely right about that.",
        "Let’s double-check that to be sure.",
        "I can explain that with a quick example if you’d like.",
        "Haha, fair point! I’ll give you that one.",
        "All done! Anything else you’d like to ask while we’re at it?"
    ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
