import os
import google.generativeai as genai
import streamlit as st

# Configure the API key
genai.configure(api_key="AIzaSyDbvCxfCvbXhe5aIP9VKNb8M2IWBybmlsU") 

# Streamlit app title
st.title("QuickIQ App")


# Prompt input from the user
prompt = st.text_input("Enter your Question:")

# Button to generate response
if st.button("Generate Response"):
    if prompt:
        with st.spinner("Generating Response..."):
            try:
                # Define generation configuration
                generation_config = {
                    "temperature": 1,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }
                
                model = genai.GenerativeModel(model_name="gemini-1.5-pro-002",generation_config=generation_config,)

                chat_session = model.start_chat(history=[])
                
                # Generate response using generate_text
                response = chat_session.send_message(prompt)
                
                if response:
                    st.subheader("Model response: ")

                # Display the response
                    st.write("Response:", response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter the prompt before generating the response")