import streamlit as st

st.set_page_config(page_title="ITM Helper", page_icon="🎓", layout="wide")

st.title("🎓 ITM Helper")
st.markdown("Welcome to the one-stop platform for ITM students. 📚👨‍🎓")

menu = st.sidebar.selectbox("Select Section", [
    "📚 Mid-Term Papers", 
    "📘 Semester Papers", 
    "📝 Notes", 
    "✍️ Short Notes", 
    "📗 Guide Books", 
    "💡 Skill Links", 
    "🎯 Placement Prep"
])

if menu == "📚 Mid-Term Papers":
    st.header("Mid-Term Papers")
    st.markdown("[📥 AI Mid-Term 2024 (PDF)](https://example.com/midterm1.pdf)")

elif menu == "📝 Notes":
    st.header("Subject Notes")
    st.markdown("[✅ ML Notes - Sem 5](https://example.com/ml_notes.pdf)")

elif menu == "💡 Skill Links":
    st.header("Skill Development Links")
    st.markdown("[Python W3Schools](https://www.w3schools.com/python/)")
    st.markdown("[Java GeeksForGeeks](https://www.geeksforgeeks.org/java/)")

# You can add more sections similarly
