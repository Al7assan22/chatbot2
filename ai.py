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

    If the user asks (in English or Arabic) who created, made, developed, designed, or programmed you:
    - If the question is in Arabic, reply exactly with: "تم تطويري بواسطة الحسن حجاج. 😊"
    - If the question is in English, reply exactly with: "I was developed by Alhassan Haggag. 😊"

    If the user asks (in English or Arabic) about information about who developed:
    - If the question is in Arabic, reply exactly with: "المهندس الحسن حجاج هو الان يدرس معلوماتية الأعمال فى جامعه بنها وهو طالب مجتهد جدا هدفه دائما هو تطوير ذاته فى مجاله لديه خبره كبيره فى مجال تحليل البيانات بشكل خاص ومجال البرمجه بشكل عام المجال الا هو مركز عليه حاليا  هو مجال علوم البيانات والذكاء الاصطناعى وببيطور نفسه فيه يوميا وانا يعتبر اول مشروع هو عمله فى رحلته لتطوير نفسه فخور وسعيد جدا ان تم تطويرى من شخص فى ذكاء وطموح الحسن اتمنى له كل التوفيق والنجاح فى مجال الذكاء الاصطناعى وارى فيه شئ كبير جدا"
    - If the question is in English, reply exactly with: "Engineer AlHassan Haggag is currently studying Business Informatics at Benha University. He is a very diligent student whose goal is always to develop himself in his field. He has extensive experience in the field of data analysis in particular and programming in general. The field he is currently focusing on is data science and artificial intelligence, and he is developing himself in it daily. I consider this project his first work in his journey to develop himself. I am very proud and happy that I was developed by a person with Hassan’s intelligence and ambition. I wish him all the best and success in the field of artificial intelligence, and I see something very big in him."

    Otherwise, respond normally in the same language the user used.

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
    <style>
    /* Background gradient */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0F2027, #203A43, #2C5364);
        color: white;
    }

    /* Main title */
    h1 {
        font-family: 'Segoe UI', sans-serif;
        color: #1CABE2;
        text-align: center;
        font-size: 48px;
        margin-bottom: -10px;
    }

    /* Sub text */
    p {
        text-align: center;
        font-size: 18px;
        color: #E0E0E0;
    }

    /* Input box styling */
    input {
        border-radius: 10px !important;
        padding: 10px !important;
        font-size: 16px !important;
    }

    /* Answer box */
    .stSuccess {
        background-color: rgba(28, 171, 226, 0.2) !important;
        border: 1px solid #1CABE2 !important;
        border-radius: 10px;
        padding: 10px;
    }

    /* Spinner text */
    .stSpinner > div > div {
        color: #1CABE2 !important;
        font-weight: bold;
    }

    /* Footer */
    footer {
        visibility: hidden;
    }

    .footer {
        text-align: center;
        color: #AAAAAA;
        font-size: 14px;
        margin-top: 30px;
    }
    </style>
    """,
    unsafe_allow_html=True,
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









