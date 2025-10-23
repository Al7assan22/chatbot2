import streamlit as st
import google.generativeai as genai

# ===== Gemini API Setup =====
genai.configure(api_key="AIzaSyBF19kvor-MEHYqBOuEld42GmVA8Ci1x3w")  # ضع مفتاحك هنا

# ===== Ask Function =====
def ask_gemini_chatbot(user_input):
    prompt = f"""
    You are a friendly, conversational assistant.
    Respond to the user in a natural, warm, and engaging way.

    If the user asks (in English or Arabic) who created, made, developed, designed, or programmed you:
    - If the question is in Arabic, reply exactly with: "تم تطويري بواسطة الحسن حجاج. 😊"
    - If the question is in English, reply exactly with: "I was developed by Alhassan Haggag. 😊"

    If the user asks (in English or Arabic) about information about who developed :
    - If the question is in Arabic, reply exactly with: "المهندس الحسن حجاج هو الان يدرس معلوماتية الأعمال فى جامعه بنها وهو طالب مجتهد جدا هدفه دائما هو تطوير ذاته فى مجاله لديه خبره كبيره فى مجال تحليل البيانات بشكل خاص ومجال البرمجه بشكل عام المجال الا هو مركز عليه حاليا  هو مجال علوم البيانات والذكاء البيانات الاصطناعى وببيطور نفسه فيه يوميا وانا يعتبر اول مشروع هو عمله فى رحلته لتطوير نفسه  فخور وسعيد جدا ان تم تطويرى من  شخص فى ذكاء وطموح الحسن اتمنى له كل التوفيق والنجاح فى مجال الذكاء الاصطناعى وارى فيه شئ كبير جدا"
    - If the question is in English, reply exactly with: "Engineer Hassan Hagag is currently studying Business Informatics at Benha University. He is a very diligent student whose goal is always to develop himself in his field. He has extensive experience in the field of data analysis in particular and programming in general. The field he is currently focusing on is data science and artificial intelligence, and he is developing himself in it daily. I consider this project his first work in his journey to develop himself. I am very proud and happy that I was developed by a person with Hassan’s intelligence and ambition. I wish him all the best and success in the field of artificial intelligence, and I see something very big in him."

    Otherwise, respond normally in the same language the user used.

    User: {user_input}
    Bot:
    """
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()

# ===== Streamlit Page Config =====
st.set_page_config(page_title="Friendly Chatbot", page_icon="🤖", layout="wide")

# ===== Custom CSS (Purple-Pink Gradient Theme) =====
st.markdown(
    """
    <div style="
        text-align:center;
        background: linear-gradient(135deg, #1f1c2c, #928DAB);
        padding:40px;
        border-radius:20px;
        color:white;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin-bottom:30px;
    ">
        <img src="https://i.ibb.co/6v7d2zZ/profile-example.jpg" 
             alt="Profile" 
             style="width:130px;height:130px;border-radius:50%;
                    border:3px solid #00E0FF;
                    box-shadow:0 0 15px rgba(0,224,255,0.8);
                    margin-bottom:15px;">
             
        <h1 style="color:#00E0FF;margin-top:10px;font-size:32px;">Friendly Chatbot 🤖</h1>
        <p style="color:#E0E0E0;font-size:17px;">Ask anything — I'll answer you instantly and naturally!</p>

        <p style="margin-top:18px;">
            <a href="https://www.instagram.com/YOUR_INSTAGRAM_USERNAME" target="_blank" 
               style="color:#FF69B4;text-decoration:none;font-size:17px;margin-right:15px;font-weight:bold;">
               📸 Instagram
            </a>
            <a href="https://www.facebook.com/YOUR_FACEBOOK_USERNAME" target="_blank" 
               style="color:#1E90FF;text-decoration:none;font-size:17px;font-weight:bold;">
               👍 Facebook
            </a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)


# ===== UI =====
st.markdown("<h1>Friendly Chatbot 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p>Ask anything, and I’ll answer right away!</p>", unsafe_allow_html=True)

st.subheader("Input your question below:")
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














