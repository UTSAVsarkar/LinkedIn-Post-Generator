import streamlit as st
import time

# --- Page Config ---
st.set_page_config(page_title="LinkedIn Post Generator", page_icon="💼")

# --- Entrance Animation ---
with st.spinner("Launching your AI Content Assistant..."):
    time.sleep(1)
st.snow()

# --- Heading ---
st.markdown("## 💼 Welcome to LinkedIn Post Generator")
st.markdown("Craft professional, engaging LinkedIn posts using **AI powered by DeepSeek Chimera** 🤖")

# --- What this app does ---
st.markdown("### 🚀 What is this?")
st.markdown("""
This app helps you turn **simple thoughts** into **well-written LinkedIn posts** that are:
- ✅ Concise (under 150 words)
- ✅ Authentic and human-like
- ✅ Enriched with relevant emojis 😎
- ✅ Perfect for professionals, students, and creators

Just tell us **what you want to share**, and let the AI handle the writing.
""")

# --- How it works ---
st.markdown("### ⚙️ How it works")
st.markdown("""
1. ✍️ You describe your achievement or idea in plain language  
2. 🤖 AI (DeepSeek R1T2 Chimera) transforms it into a polished LinkedIn post  
3. 📋 You copy and publish it — that’s it!

> No need to overthink — focus on your message, we’ll polish the delivery.
""")

# --- Who it's for ---
st.markdown("### 👥 Who is this for?")
st.markdown("""
- MBA students showcasing internships or certifications  
- Professionals announcing promotions, projects, or transitions  
- Anyone who struggles to write but wants to stay active on LinkedIn  
""")

# --- Motivation ---
st.caption("💡 *“Done is better than perfect. Just share your journey.”*")

# --- Sidebar Tip ---
st.markdown("---")
st.markdown("👉 Use the **sidebar** to get started with generating your first post!")