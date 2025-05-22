import streamlit as st

    
# ---------- 페이지 설정 ----------
st.set_page_config(
    page_title="나와 닮은 수학자는?",
    page_icon="🧠",
    layout="centered",
)


# 원하는 폰트로 바꾸는 CSS (예: 나눔고딕, 구글폰트)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic:wght@700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Nanum Gothic', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("테스트 페이지")
st.write("여기부터 내 Streamlit 앱의 본문 내용이 들어가요!")
