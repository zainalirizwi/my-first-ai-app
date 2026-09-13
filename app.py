import streamlit as st
from groq import Groq

# --- Page setup ---
st.title("🤖 My First AI Chatbot")
st.write("Ask me anything and I'll try to help!")

# --- Connect to Groq ---
# The API key is stored safely in Streamlit "Secrets" (never in this file).
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# --- User input ---
question = st.text_input("Your question:")

if st.button("Get Answer"):
    if question.strip() == "":
        st.warning("Please type a question first.")
    else:
        with st.spinner("Thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",   # a free Groq model
                messages=[
                    {"role": "user", "content": question}
                ],
            )
        st.write(response.choices[0].message.content)
