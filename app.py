import streamlit as st
from ai_tutor import ask_tutor

st.set_page_config(page_title="AI Tutor", page_icon="📘")
st.title("📘 AI Tutor – Learn Math or English")

user_input = st.text_input("Ask your question (e.g., What is a verb? or How to solve 2x + 3 = 7?)")

if user_input:
    with st.spinner("Thinking..."):
        answer = ask_tutor(user_input)
    st.success("Here's the explanation:")
    st.write(answer)
