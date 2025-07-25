import streamlit as st
from agents import career_agent, skill_agent, job_agent

# --- Page Config ---
st.set_page_config(page_title="Career Mentor Agent", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
    * {
        font-family: 'Poppins', sans-serif;
    }
    .stApp {
        background: linear-gradient(to right top, #e6f0f3, #ffffff);
        padding: 0 1rem;
    }
    .main-title {
        font-size: 40px;
        font-weight: 700;
        color: #005f73;
        text-align: center;
        margin-bottom: 0;
    }
    .subtitle {
        font-size: 16px;
        text-align: center;
        color: #555;
        margin-bottom: 40px;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.6);
        border-radius: 16px;
        padding: 30px 25px;
        margin-bottom: 25px;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        backdrop-filter: blur(10px);
    }
    .glass-card h3 {
        color: #023e8a;
        margin-bottom: 10px;
    }
    .stButton > button {
        background-color: #007f7f !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 10px 25px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .footer {
        margin-top: 40px;
        text-align: center;
        font-size: 14px;
        color: #888;
    }
    input[type="text"], textarea {
        border: 2px solid #007f7f !important;
        border-radius: 8px !important;
        padding: 10px !important;
        box-shadow: 0 0 5px rgba(0,127,127,0.3) !important;
        outline: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- Title Section ---
st.markdown("<div class='main-title'>🤖 Career Mentor Agent</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>AI-Powered Career Planning: Get a complete roadmap from Interest to Job</div>", unsafe_allow_html=True)

# --- Input Card ---
st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
st.markdown("#### 💬 What are your interests?")
interest = st.text_input("E.g., AI, Graphic Design, Health, Marketing, etc.")
st.markdown("</div>", unsafe_allow_html=True)

# --- On Button Click ---
if st.button("🚀 Generate Career Plan"):
    if not interest:
        st.warning("⚠️ Please enter your interest first.")
        st.stop()

    # --- Career Field ---
    with st.spinner("🔍 Detecting career field..."):
        field = career_agent(interest)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 📌 Suggested Career Field")
    st.success(field)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Skill Roadmap ---
    with st.spinner("📘 Building your skill roadmap..."):
        roadmap = skill_agent(field)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 🧠 Skill Roadmap")
    st.info(roadmap)
    st.markdown("</div>", unsafe_allow_html=True)

    # --- Job Roles ---
    with st.spinner("💼 Fetching job roles..."):
        jobs = job_agent(field)
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("### 💼 Top Job Roles")
    st.write(jobs)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Footer ---
st.markdown("<div class='footer'>🔧 Developed with ❤️ by <b>CodeWithAhtii</b></div>", unsafe_allow_html=True)
