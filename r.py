


import ollama
import streamlit as st

# Streamlit UI setup
st.title("Chatbot with Ollama Model")
st.write("Ask anything and get a response!")

# Input field for the user
user_input = st.text_input("Your Question:")

if user_input:
    # Call the Ollama model
    response = ollama.chat(model='phi3', messages=[{
        'role': 'user',
        'content': user_input,
    }])

    # Get and display the model's response
    answer = response['message']['content']
    st.write(f"Model's Response: {answer}")