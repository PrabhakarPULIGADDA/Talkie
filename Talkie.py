import streamlit as st
from groq import Groq

st.title("Talkie")
st.markdown(" Hello! I'm here to assist you. What can I do for you today?")
st.write("")

# Directly set your Groq API key
api_key = "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"

# Initialize Groq client with the API key
client = Groq(api_key=api_key)

# Set a default model
if "groq_model" not in st.session_state:
    st.session_state["groq_model"] = "llama3-8b-8192"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("heyy! Write Something Here.....?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call Groq API and get assistant response
    with st.chat_message("assistant"):
        response = ""
        try:
            # Make the API call to generate the assistant's response
            chat_completion = client.chat.completions.create(
                model=st.session_state["groq_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            response = chat_completion.choices[0].message.content
            st.markdown(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
