import streamlit as st
import google.generativeai as genai
import os

# ===== Gemini API Setup =====
genai.configure(api_key=("AIzaSyBF19kvor-MEHYqBOuEld42GmVA8Ci1x3w"))  # حط مفتاحك هنا

# ===== Ask Function =====
def ask_gemini_chatbot(user_input):
    prompt = f"""
    You are a friendly, conversational assistant.
    Respond to the user in a natural, warm, and engaging way.

    If the user asks (in English or Arabic) who created, made, developed, designed, or programmed you —
    always reply exactly with:
    "I was developed by Alhassan Haggag. 😊"

    Otherwise, chat normally in a friendly and natural tone.

    User: {user_input}
    Bot:
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()
# ===== Streamlit UI =====
st.set_page_config(page_title="Friendly Chatbot", page_icon="🤖", layout="wide")

st.markdown(
    """
    <div style="text-align:center;">
        <h1 style="color:#1CABE2;">Friendly Chatbot 🤖</h1>
        <p style="color:white;font-size:16px;">Ask anything, I'll answer directly!</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.subheader("💬 Ask anything:")
user_message = st.text_input("Input your Question here...")

if user_message.strip():
    with st.spinner("⏳ Thinking..."):
        answer = ask_gemini_chatbot(user_message)
    st.success(f"**✅ Answer:** {answer}")

# ===== Footer =====
st.markdown(
    """
    <hr>
    <p style="text-align:center;color:#AAAAAA;font-size:12px;">
    Developed by <strong>Alhassan Mohamed Haggag</strong>
    </p>
    """,
    unsafe_allow_html=True
)
