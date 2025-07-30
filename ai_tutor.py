### ai_tutor.py

import os

try:
    import openai
except ImportError:
    OpenAI = None

try:
    import streamlit as st
    api_key = st.secrets["OPENAI_API_KEY"]
except Exception:
    api_key = os.getenv("OPENAI_API_KEY", "sk-your-api-key-here")

def ask_tutor(question):
    if not OpenAI:
        return "OpenAI module is not available. Please install it using 'pip install openai'."

    
openai.api_key = api_key

    prompt = (
        "You are a friendly AI Tutor. Explain math or English concepts in simple, step-by-step terms.\n"
        "Encourage the student. Give examples when needed.\n"
        f"\nQuestion: {question}\nAnswer:"
    )

    try:
       response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly and helpful AI tutor."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.6,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"


### app.py

try:
    import streamlit as st
except ImportError:
    raise ImportError("Streamlit is not installed. Please install it with 'pip install streamlit'.")

from ai_tutor import ask_tutor

st.set_page_config(page_title="AI Tutor", page_icon="📘")
st.title("📘 AI Tutor – Learn Math or English")

user_input = st.text_input("Ask your question (e.g., What is a verb? or How to solve 2x + 3 = 7?)")

if user_input:
    with st.spinner("Thinking..."):
        answer = ask_tutor(user_input)
        st.success("Here's the explanation:")
        st.write(answer)


### test_ai_tutor.py

def test_basic_math():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is 2 + 2?")
    assert "4" in response

def test_english_definition():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is a noun?")
    assert "person" in response or "place" in response or "thing" in response

def test_addition_five_plus_five():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is 5 + 5?")
    assert "10" in response

def test_math_equation():
    from ai_tutor import ask_tutor
    response = ask_tutor("Solve 3x + 6 = 15")
    assert "x =" in response or "3x" in response

def test_encouraging_language():
    from ai_tutor import ask_tutor
    response = ask_tutor("What is a preposition?")
    assert any(word in response.lower() for word in ["great question", "let me explain", "don't worry"])
