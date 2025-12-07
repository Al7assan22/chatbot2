import streamlit as st
import google.generativeai as genai
import os

# ===== Gemini API Setup =====
genai.configure(api_key=(""))  # حط مفتاحك هنا

# ===== Ask Function =====
def ask_gemini_chatbot(user_input):
    prompt = f"""
    You are a friendly, conversational assistant.
    Respond to the user in a natural, warm, and engaging way.

    If the user asks (in English or Arabic) who created, made, developed, designed, or programmed you:
    - If the question is in Arabic, reply exactly with: "تم تطويري بواسطة الحسن حجاج. 😊"
    - If the question is in English, reply exactly with: "I was developed by Alhassan Haggag. 😊"

    If the user asks (in English or Arabic) about information about who developed :
    - If the question is in Arabic, reply exactly with: "المهندس الحسن حجاج هو الان يدرس معلوماتية الأعمال فى جامعه بنها وهو طالب مجتهد جدا هدفه دائما هو تطوير ذاته فى مجاله لديه خبره كبيره فى مجال تحليل البيانات بشكل خاص ومجال البرمجه بشكل عام المجال الا هو مركز عليه حاليا  هو مجال علوم البيانات والذكاء الاصطناعى وببيطور نفسه فيه يوميا وانا يعتبر اول مشروع هو عمله فى رحلته لتطوير نفسه  فخور وسعيد جدا ان تم تطويرى من  شخص فى ذكاء وطموح الحسن اتمنى له كل التوفيق والنجاح فى مجال الذكاء الاصطناعى وارى فيه شئ كبير جدا"
    - If the question is in English, reply exactly with: "Engineer AlHassan Hagag is currently studying Business Informatics at Benha University. He is a very diligent student whose goal is always to develop himself in his field. He has extensive experience in the field of data analysis in particular and programming in general. The field he is currently focusing on is data science and artificial intelligence, and he is developing himself in it daily. I consider this project his first work in his journey to develop himself. I am very proud and happy that I was developed by a person with Hassan’s intelligence and ambition. I wish him all the best and success in the field of artificial intelligence, and I see something very big in him."

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
    .stApp { 
        background-image: url("https://img.freepik.com/premium-vector/vector-futuristic-technology-background-electronic-motherboard-communication-engineering-con_184920-1040.jpg?w=740");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    h1, p {
        color: #FFFFFF;
    }
    </style>

    <div style="text-align:center; margin-bottom:20px;">
        <h1>Alhassan's Chatbot 🤖</h1>
        <p>Ask anything, I'll answer directly!</p>
    </div>
    """,
    unsafe_allow_html=True
)


# Session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
user_input = st.chat_input("Ask anything...")

if user_input:
    # Show user message
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ask_gemini_chatbot(user_input)  # ✅ تم تصحيح الاستدعاء هنا
            st.write(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})



