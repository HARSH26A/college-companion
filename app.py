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
        .link-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin: 10px 0;
        }
    </style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown('<h1 class="title">🎓 College Companion</h1>', unsafe_allow_html=True)
st.subheader("Helping ITM students stay ahead in academics and placements")

# ---------- BRANCH SELECTOR ----------
st.sidebar.image("https://www.itmuniversity.ac.in/images/banner2.jpg", use_container_width=True)
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
    "🗂️ Project Ideas",
    "🧾 Useful Docs",
    "📬 Contact/Feedback"
])

# ---------- BANNER IMAGE ----------
st.image("https://images.unsplash.com/photo-1608492083503-1c518291b23b", use_container_width=True)

# ---------- MID TERM PAPERS ----------
if menu == "📄 Mid-Term Papers":
    st.markdown(f"### 📄 Mid-Term Papers - {branch}")
    with st.container():
        st.markdown("""
            <div class='link-box'>
                <strong>📘 Deep Learning Mid-Term (AI - ML, 5th Sem)</strong><br>
                <a href="https://drive.google.com/file/d/16beggVt8XA48fMYrhelBr3pX_ZA_jj09/view?usp=drivesdk" target="_blank">🔗 View on Google Drive</a>
            </div>
        """, unsafe_allow_html=True)

# ---------- SEMESTER PAPERS ----------
elif menu == "📘 Semester Papers":
    st.markdown(f"### 📘 Previous Year Semester Papers - {branch}")
    with st.container():
        st.markdown("""
            <div class='link-box'>
                📄 <a href="https://drive.google.com/yourlink" target="_blank">Download Sem 3 Paper</a><br>
                📄 <a href="https://drive.google.com/yourlink" target="_blank">Download Sem 4 Paper</a>
            </div>
        """, unsafe_allow_html=True)

# ---------- NOTES ----------
elif menu == "📝 Notes":
    st.markdown(f"### 📝 Study Notes - {branch}")
    with st.container():
        st.markdown("""
            <div class='link-box'>
                📘 <a href="https://drive.google.com/yourlink" target="_blank">ML Notes (PDF)</a><br>
                📕 <a href="https://drive.google.com/yourlink" target="_blank">DSA Short Notes</a>
            </div>
        """, unsafe_allow_html=True)

# ---------- SKILL COURSES ----------
elif menu == "📺 Skill Courses":
    st.markdown("### 📺 Skill Development - YouTube Playlists")
    with st.container():
        st.markdown("""
            <div class='link-box'>
                🌐 <strong>JavaScript Courses</strong><br>
                - <a href="https://youtu.be/EerdGm-ehJQ" target="_blank">Super Simple Dev</a><br>
                - <a href="https://youtu.be/PkZNo7MFNFg" target="_blank">FreeCodeCamp Full JS</a><br>
                - <a href="https://youtube.com/playlist?list=PLGjplNEQ1it_oTvuLRNqXfz_v_0pq6unW" target="_blank">Apna College JS</a><br>
                - <a href="https://youtube.com/playlist?list=PLu0W_9lII9ahR1blWXxgSlL4y9iQBnLpR" target="_blank">CodeWithHarry JS</a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div class='link-box'>
                💻 <strong>Practice Platforms</strong><br>
                - <a href="https://www.geeksforgeeks.org/" target="_blank">GeeksForGeeks</a><br>
                - <a href="https://leetcode.com/" target="_blank">LeetCode</a><br>
                - <a href="https://www.hackerrank.com/" target="_blank">HackerRank</a><br>
                - <a href="https://www.codechef.com/" target="_blank">CodeChef</a>
            </div>
        """, unsafe_allow_html=True)

# ---------- PLACEMENT PREP ----------
elif menu == "🧠 Placement Prep":
    st.markdown("### 🧠 Placement Preparation Zone")
    with st.container():
        st.markdown("""
            <div class='link-box'>
                🎯 <strong>Placement Roadmaps</strong><br>
                - <a href="https://youtu.be/m7VcIH_N9ZY?si=DO19-0cDFfJMRkUS" target="_blank">Apna College Placement Roadmap</a><br>
                - <a href="https://youtu.be/VY6003vijLw?si=t8uMFn_KMtHGmYHC" target="_blank">Love Babbar Final Year Roadmap</a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div class='link-box'>
                📘 <strong>DSA Learning Playlists</strong><br>
                - <a href="https://youtube.com/playlist?list=PLfqMhTWNBTe137I_EPQd34TsgV6IO55pt" target="_blank">Apna College DSA Playlist</a><br>
                - <a href="https://youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA" target="_blank">Love Babbar DSA Playlist</a><br>
                - <a href="https://youtube.com/playlist?list=PLu0W_9lII9ahIappRPN0MCAgtOu3lQjQi" target="_blank">CodeWithHarry DSA</a><br>
                - <a href="https://youtube.com/playlist?list=PL9gnSGHSqcnr_DxHsP7AW9ftq0AtAyYqJ" target="_blank">DSA with Java</a><br>
                - <a href="https://youtube.com/playlist?list=PLhR2IpV1b2FwWwviBHRrR118YAaSlyhTU" target="_blank">DSA with Python</a><br>
                - <a href="https://youtube.com/playlist?list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz" target="_blank">Striver A2Z DSA Practice</a>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
            <div class='link-box'>
                🧰 <strong>Practice Platforms</strong><br>
                - <a href="https://www.geeksforgeeks.org/" target="_blank">GeeksForGeeks</a><br>
                - <a href="https://leetcode.com/" target="_blank">LeetCode</a><br>
                - <a href="https://www.hackerrank.com/" target="_blank">HackerRank</a><br>
                - <a href="https://www.codechef.com/" target="_blank">CodeChef</a>
            </div>
        """, unsafe_allow_html=True)

# ---------- PROJECT IDEAS ----------
elif menu == "🗂️ Project Ideas":
    st.markdown("### 🗂️ Mini & Major Projects")
    st.markdown("- 💡 AI-based Student Feedback System")
    st.markdown("- 📱 Android App for Campus Navigation")
    st.markdown("- 📊 IoT Smart Attendance System")
    st.markdown("- 🌐 Weather App using APIs")

# ---------- USEFUL DOCUMENTS ----------
elif menu == "🧾 Useful Docs":
    st.markdown("### 🧾 Important Documents")
    st.markdown("- Bonafide Certificate Format")
    st.markdown("- Leave Application Template")
    st.markdown("- NOC Format for Internship")

# ---------- FEEDBACK ----------
elif menu == "📬 Contact/Feedback":
    st.markdown("### 📬 Feedback or Suggestions?")
    st.markdown("If you'd like to share anything, send an email to [your-email@example.com](mailto:your-email@example.com) or DM me on Instagram.")

# ---------- FOOTER ----------
st.sidebar.info("✅ Last updated: 6 July 2025")
