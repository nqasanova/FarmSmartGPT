import streamlit as st
import pandas as pd
import numpy as np
import openai  # pip install openai
import constants

# Set your OpenAI API key
openai.api_key = constants.API_KEY

# Title and description
st.title('SmartFarm Chatbot')
st.write("""
Upload your data and ask questions about it. The chatbot will provide insights based on the data you provide.
""")

# File uploader
uploaded_file = st.file_uploader("Upload your NDVI file (CSV)", type=["csv"])

# Global variable to store NDVI data
ndvi_data = None

# Process the uploaded file
if uploaded_file is not None:
    file_type = uploaded_file.name.split('.')[-1]
    if file_type.lower() == 'csv':
        # Read CSV file
        ndvi_data = pd.read_csv(uploaded_file)
        st.success("NDVI data successfully uploaded and read as CSV.")
        st.write("Data Preview:")
        st.dataframe(ndvi_data.head())
    else:
        st.error("Unsupported file format. Please upload a CSV file.")

# Chatbot interface
if ndvi_data is not None:
    st.write("---")
    st.write("### Ask Questions About Your NDVI Data")

    # Initialize session state for chat history
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # User input
    user_input = st.text_input("Enter your question:", key="user_input")

    if user_input:
        # Prepare the data summary
        data_summary = ndvi_data.describe().to_string()

        # Construct the messages
        messages = [
            {"role": "system", "content": "You are an expert in remote sensing and agriculture."},
            {"role": "assistant", "content": f"NDVI data summary statistics:\n{data_summary}"},
            {"role": "user", "content": user_input}
        ]

        # Call the Chat Completion API
        try:
            response = openai.ChatCompletion.create(
                model='gpt-4',  # or 'gpt-4' if you have access
                messages=messages,
                max_tokens=500,
                temperature=0.7,
            )
            answer = response['choices'][0]['message']['content'].strip()
            st.session_state.chat_history.append((user_input, answer))

        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")

    # Display chat history
    if st.session_state.chat_history:
        st.write("### Chat History")
        for i, (question, answer) in enumerate(reversed(st.session_state.chat_history)):
            st.write(f"**You:** {question}")
            st.write(f"**Chatbot:** {answer}")
            st.write("---")
else:
    st.info("Please upload your NDVI data to start asking questions.")
