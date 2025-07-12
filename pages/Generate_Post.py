import streamlit as st
import requests

# --- Page Config ---
st.set_page_config(page_title="Generate Post | LinkedIn Post Generator", page_icon="📝")
st.title("📝 Generate Your LinkedIn Post")
st.markdown("Craft a professional, engaging LinkedIn post in just seconds using AI ⚡")

# --- API Key from secrets.toml ---
OPENROUTER_API_KEY = st.secrets["openrouter"]["api_key"]

# --- DeepSeek API Call Function ---
def generate_linkedin_post(prompt_text):
    system_prompt = (
        "You are a professional LinkedIn content creator. Given a short description of an achievement or event, "
        "generate an engaging, authentic, and professional LinkedIn post. Include emojis and a positive tone. "
        "Do not exceed 150 words."
    )

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost",  # Use your domain if deploying (e.g. "https://utsav.streamlit.app")
        "X-Title": "LinkedIn Post Generator",
        "Content-Type": "application/json"
    }

    data = {
        "model": "tngtech/deepseek-r1t2-chimera:free",
        "messages": [
            {"role": "user", "content": system_prompt}
        ],
        "temperature": 0.7
    }

    res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)

    if res.status_code == 200:
        return res.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ Error {res.status_code}: {res.text}"

# --- Input UI ---
st.subheader("💬 What would you like to post?")
user_input = st.text_area(
    label="",
    placeholder="e.g. I just completed a data science internship at Flipkart, where I worked on recommendation models.",
    height=150
)

# --- Suggestions Below Text Area ---
with st.expander("💡 Need inspiration? Here are 5 examples you can try:"):
    st.markdown("""
- 🎓 *“I just wrapped up my MBA in Big Data Analytics from GIM!”*  
- 👨‍💻 *“Finished a 6-month backend internship at Microsoft — learned so much about microservices.”*  
- 📚 *“Completed Google’s Data Analytics certification. Excited for what’s next!”*  
- 🌍 *“Spoke at a TEDx event on AI and sustainability — what an experience!”*  
- 💼 *“Started my new role as a Product Analyst at Zomato! Day 1 = ✅”*
    """)

# --- Button & Output ---
if st.button("🚀 Generate LinkedIn Post"):
    if user_input.strip():
        with st.spinner("Crafting your LinkedIn masterpiece..."):
            result = generate_linkedin_post(user_input)
        st.balloons()
        st.success("✅ Here's your LinkedIn post:")
        st.markdown(f"```markdown\n{result}\n```")
    else:
        st.warning("⚠️ Please enter a description to generate a post.")