import streamlit as st

st.set_page_config(page_title="المعلّم الذكي", page_icon="🎓")

st.title("🎓 المعلّم الذكي للصف التاسع")

st.write("مرحبًا بك في مساعدك التعليمي الذكي!")

name = st.text_input("ما اسمك أيها الطالب؟")

if name:
st.success(f"أهلًا بك يا {name}!")

st.subheader("📚 اختر المادة الدراسية")

subject = st.selectbox(
"المادة",
["الرياضيات", "العلوم", "اللغة العربية", "اللغة الإنجليزية"]
)

st.write(f"المادة المختارة: {subject}")
