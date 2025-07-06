import streamlit as st
from PIL import Image

st.set_page_config(page_title="College Companion", page_icon="🎓", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        .main {background-color: #f1f3f6;}
        .title {text-align: center; color: #2c3e50; font-size: 42px; font-weight: bold;}
        .stButton>button {
            color: white;
            background-color: #0077b6;
            border-radius: 10px;
            padding: 8px 16px;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<h1 class="title">🎓 College Companion</h1>', unsafe_allow_html=True)
st.subheader("Your one-stop academic and placement support portal 📚")

# ---------- BRANCH SELECTOR ----------
st.sidebar.markdown("### 🏫 Select Your Branch")
branch = st.sidebar.radio("Choose branch:", [
    "CSE", "AI - ML", "DS", "IoT", "IT", "EC", "MECH", "CIVIL"
])

st.sidebar.markdown("---")

# ---------- SECTION SELECTOR ----------
menu = st.sidebar.selectbox("📂 Navigate to Section", [
    "📄 Mid-Term Papers", 
    "📘 Semester Papers", 
    "📝 Notes", 
    "📺 Skill Courses", 
    "🧠 Placement Prep",
    "📬 Contact/Feedback"
])

# ---------- BRANCH BANNER ----------
st.image("https://img.freepik.com/free-vector/university-campus-concept-illustration_114360-12404.jpg", use_column_width=True)

# ---------- MID TERM PAPERS ----------
if menu == "📄 Mid-Term Papers":
    st.markdown(f"### 📄 Mid-Term Papers - {branch}")
    if branch == "AI - ML":
        st.markdown("- [📄 Deep Learning Mid-Term (5th Sem)](https://drive.google.com/file/d/16beggVt8XA48fMYrhelBr3pX_ZA_jj09/view?usp=drivesdk)")

# ---------- SEMESTER PAPERS ----------
elif menu == "📘 Semester Papers":
    st.markdown(f"### 📘 Previous Year Semester Papers - {branch}")
    st.markdown("[Download Sem 3 Paper](https://drive.google.com/yourlink)")
    st.markdown("[Download Sem 4 Paper](https://drive.google.com/yourlink)")

# ---------- NOTES ----------
elif menu == "📝 Notes":
    st.markdown(f"### 📝 Study Notes - {branch}")
    st.markdown("[Download ML Notes (PDF)](https://drive.google.com/yourlink)")
    st.markdown("[Download DSA Short Notes](https://drive.google.com/yourlink)")

# ---------- SKILL COURSES ----------
elif menu == "📺 Skill Courses":
    st.markdown("### 📺 Skill Development - YouTube Playlists")

    st.markdown("#### 🌐 JavaScript Courses")
    st.markdown("- [Super Simple Dev](https://youtu.be/EerdGm-ehJQ?si=JxHKopXW_gWW3tUs)")
    st.markdown("- [FreeCodeCamp - JS Full Course](https://youtu.be/PkZNo7MFNFg?si=dKsq-uHE80B1xktn)")
    st.markdown("- [JavaScript by Apna College (Playlist)](https://youtube.com/playlist?list=PLGjplNEQ1it_oTvuLRNqXfz_v_0pq6unW&si=sSYkZ0NG7x1-XDl2)")
    st.markdown("- [JavaScript - CodeWithHarry (Playlist)](https://youtube.com/playlist?list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR&si=6uy_BsUjusmw4AWe)")

    st.markdown("#### 💻 Coding Practice Platforms")
    st.markdown("- [GeeksForGeeks](https://www.geeksforgeeks.org/)")
    st.markdown("- [LeetCode](https://leetcode.com/)")
    st.markdown("- [HackerRank](https://www.hackerrank.com/)")

# ---------- PLACEMENT PREP ----------
elif menu == "🧠 Placement Prep":
    st.markdown("### 🧠 Placement Preparation Zone")
    st.markdown("- [Resume templates (Drive)](https://drive.google.com/yourlink)")
    st.markdown("- [Interview experiences](https://www.geeksforgeeks.org/tag/interview-corner/)")

# ---------- FEEDBACK ----------
elif menu == "📬 Contact/Feedback":
    st.markdown("### 📬 Feedback or Suggestions?")
    st.markdown("If you'd like to share anything, send an email to [your-email@example.com](mailto:your-email@example.com) or DM me on Instagram.")
