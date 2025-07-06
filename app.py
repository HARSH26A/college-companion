import streamlit as st

st.set_page_config(page_title="College Companion", page_icon="🎓", layout="wide")

st.markdown("""
    <style>
        .main {background-color: #f8f9fa;}
        .title {text-align: center; color: #2c3e50; font-size: 40px;}
        .section-header {color: #0077b6; margin-top: 20px;}
        .stButton>button {
            color: white;
            background-color: #0077b6;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title">🎓 College Companion</h1>', unsafe_allow_html=True)
st.subheader("Your one-stop platform for papers, notes, and placements 📚")

menu = st.sidebar.selectbox("📂 Navigate to Section", [
    "📄 Mid-Term Papers", 
    "📘 Semester Papers", 
    "📝 Notes", 
    "📺 Skill Courses", 
    "🧠 Placement Prep",
    "📬 Contact/Feedback"
])

# MID TERM PAPERS
if menu == "📄 Mid-Term Papers":
    st.markdown("### 📄 Mid-Term Papers")
    st.write("Click to view or download:")
    st.download_button("Download AI Mid Term 2024", 
                       data="", 
                       file_name="ai_midterm_2024.pdf", 
                       key="ai_midterm")  # Replace `data` with real content or use links below

    st.markdown("[➡️ View PDF Online (Google Drive)](https://drive.google.com/yourlink)")

# SEMESTER PAPERS
elif menu == "📘 Semester Papers":
    st.markdown("### 📘 Previous Year Semester Papers")
    st.markdown("[Download Sem 3 Paper (AI)](https://drive.google.com/yourlink)")
    st.markdown("[Download Sem 4 Paper (ML)](https://drive.google.com/yourlink)")

# NOTES
elif menu == "📝 Notes":
    st.markdown("### 📝 Study Notes")
    st.markdown("[Download ML Notes (PDF)](https://drive.google.com/yourlink)")
    st.markdown("[Download DSA Short Notes](https://drive.google.com/yourlink)")

# SKILL COURSES
elif menu == "📺 Skill Courses":
    st.markdown("### 📺 Skill Development - YouTube Playlists")
    st.markdown("[Python Programming - CodeWithHarry](https://www.youtube.com/playlist?list=PLu0W_9lII9ajyk081To1Cbt2eI5913SsL)")
    st.markdown("[DSA in C++ - Apna College](https://www.youtube.com/playlist?list=PLfqMhTWNBTe0b2nM6JHVCnAkhQRGiZMSJ)")
    st.markdown("[Aptitude - Talent Battle](https://www.youtube.com/playlist?list=PLfEr2kn3s-br8FJas4U4kNmMxrFto9r-z)")
    st.markdown("[Resume & Interview - Great Learning](https://www.youtube.com/playlist?list=PL5c5yZtHvqWFeG2fYpMdpFy_d9e6p7lJ4)")

# PLACEMENT PREP
elif menu == "🧠 Placement Prep":
    st.markdown("### 🧠 Placement Preparation Zone")
    st.markdown("- Resume tips and templates")
    st.markdown("- Interview experiences from seniors")
    st.markdown("- Link to [GeeksForGeeks Interview Series](https://www.geeksforgeeks.org/tag/interview-corner/)")

# FEEDBACK
elif menu == "📬 Contact/Feedback":
    st.markdown("### 📬 Feedback or Suggestions?")
    st.markdown("If you'd like to share anything, send an email to [your-email@example.com](mailto:your-email@example.com) or DM me on Instagram.")

