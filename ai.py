import streamlit as st
import google.generativeai as genai
import os

# ===== Gemini API Setup =====
genai.configure(api_key=("AIzaSyBF19kvor-MEHYqBOuEld42GmVA8Ci1x3w"))  

# ===== Ask Function =====
def ask_gemini_chatbot(user_input):
    # Check if the user is asking who developed the bot (Arabic or English)
    dev_questions = [
        "who developed you", "who created you", "who made you","who designed you","who create you","who design you","who develop you","who make you","who programming you"
        "مين اللي صممك", "مين صممك", "مين الا طورك", "مين الا صممك", "من صنعك","مين الا صنعك","مين الا طورك","مين الا عملك","مين الا شغلك","مين اللى طورك", "مين اللى صممك","مين اللى صنعك","مين اللى طورك","مين اللى عملك","مين اللى شغلك","مين اللي صممك
    ]
    if any(q in user_input.lower() for q in dev_questions):
        return "I was developed by Alhassan Haggag. 😊"
    
    # Normal friendly chat
    prompt = f"""
    You are a friendly, conversational assistant.
    Respond to the user in a natural, warm, and engaging way.
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




