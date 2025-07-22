import os
import openai

# Set your API key from Streamlit secrets or environment
try:
    import streamlit as st
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    openai.api_key = os.getenv("OPENAI_API_KEY", "sk-your-api-key-here")

def ask_tutor(question):
    prompt = (
        "You are a friendly AI Tutor. Explain math or English concepts in simple, step-by-step terms.\n"
        "Encourage the student. Give examples when needed.\n"
        f"\nQuestion: {question}\nAnswer:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a friendly and helpful AI tutor."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.6,
        max_tokens=500
    )
    return response["choices"][0]["message"]["content"].strip()
