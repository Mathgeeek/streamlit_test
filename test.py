import streamlit as st

st.set_page_config(
    page_title="나와 닮은 수학자는?",
    page_icon="🧠",
    layout="centered",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Gowun+Batang&family=Noto+Serif+KR:wght@200..900&family=Orbit&family=Poor+Story&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Orbit', sans-serif !important;
    }
    * {
        font-family: 'Orbit', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("테스트 페이지")
st.write("여기부터 내 Streamlit 앱의 본문 내용이 들어가요!")
