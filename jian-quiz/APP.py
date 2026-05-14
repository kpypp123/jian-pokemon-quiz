import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="지안이 퀴즈",
    page_icon="🎮",
    layout="centered"
)

# 화면 상태 저장
if "page" not in st.session_state:
    st.session_state.page = "home"


def show_home():
    st.markdown(
        """
        <h1 style='text-align:center;'>🎮 지안이 퀴즈</h1>
        <h3 style='text-align:center;'>원하는 퀴즈를 골라보자!</h3>
        """,
        unsafe_allow_html=True
    )

    img_path = Path("images/home.png")

    if img_path.exists():
        st.image(str(img_path), use_container_width=True)

    st.write("")
    st.write("")
... 
...     col1, col2 = st.columns(2)
... 
...     with col1:
...         if st.button("👑 위인 퀴즈", use_container_width=True):
...             st.session_state.page = "great_person"
...             st.rerun()
... 
...     with col2:
...         if st.button("⚡ 포켓몬 퀴즈", use_container_width=True):
...             st.session_state.page = "pokemon"
...             st.rerun()
... 
... 
... def show_great_person_quiz():
...     import great_person_quiz
...     great_person_quiz.run()
... 
... 
... def show_pokemon_quiz():
...     import pokemon_quiz
...     pokemon_quiz.run()
... 
... 
... if st.session_state.page == "home":
...     show_home()
... 
... elif st.session_state.page == "great_person":
...     if st.button("🏠 홈으로"):
...         st.session_state.page = "home"
...         st.rerun()
... 
...     show_great_person_quiz()
... 
... elif st.session_state.page == "pokemon":
...     if st.button("🏠 홈으로"):
...         st.session_state.page = "home"
...         st.rerun()
... 
