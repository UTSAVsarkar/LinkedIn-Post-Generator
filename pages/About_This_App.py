import streamlit as st

st.set_page_config(page_title="About | LinkedIn Post Generator", page_icon="📄")

st.title("📄 About This App")
st.markdown("#### 💬 Create Impactful LinkedIn Posts Effortlessly")
st.toast("👋 Welcome, Rockstar!", icon="💼")

st.markdown("""
Welcome to the **LinkedIn Post Generator** – your AI-powered assistant for writing professional, authentic, and emoji-rich LinkedIn posts in seconds.  
""")

# --- How It Works ---
st.markdown("""
Here's a simple 3-step workflow of how this app operates:
""")

# --- Visual Step Flow ---
step_cols = st.columns(3)

with step_cols[0]:
    st.image("https://cdn-icons-png.flaticon.com/512/18896/18896308.png", width=60)
    st.markdown("**Step 1:** You enter your description (e.g. _“I completed a data science internship at Flipkart”_)")

with step_cols[1]:
    st.image("https://img.icons8.com/color/96/artificial-intelligence.png", width=60)
    st.markdown("**Step 2:** AI model **DeepSeek R1T2 Chimera** generates a post based on your input")

with step_cols[2]:
    st.image("https://img.icons8.com/fluency/96/share.png", width=60)
    st.markdown("**Step 3:** You copy & share your ready-to-post content on LinkedIn 🚀")

# --- Tech Stack ---
st.markdown("### 🧠 Tech Stack")

st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWQ0a3ZpMGY2b2czczN0N3BpZzhrczJ3cmFwNG4xa2J0ZmJjbHVrbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/SWoSkN6DxTszqIKEqv/giphy.gif", caption="Example: Writing a LinkedIn post in seconds", use_container_width=True)

st.markdown("""
- **LLM**: [DeepSeek R1T2 Chimera](https://openrouter.ai/models/tngtech/deepseek-r1t2-chimera:free) via [OpenRouter](https://openrouter.ai)  
- **Frontend**: [Streamlit](https://streamlit.io) with multipage layout  
- **Deployment**: Streamlit Cloud or localhost  
- **Security**: API key stored securely in `.streamlit/secrets.toml`  
""")

# --- About the Creator ---
st.markdown("### 👨‍💻 About the Creator")
st.markdown("""
Built with ❤️ by [**Utsav Sarkar**](https://www.linkedin.com/in/utsav-sarkar-49892325a/)  
            
📍 Data + AI Enthusiast | MBA (Big Data Analytics) | Ex-MAQ Software
            
🤝 Feel free to connect, collaborate, or drop feedback on LinkedIn!
""")

st.caption("🎯 Let the AI handle your words. You focus on your wins.")
