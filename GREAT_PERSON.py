import random
from pathlib import Path

import streamlit as st
import myapp


st.set_page_config(
    page_title="지안이 퀴즈",
    page_icon="🎮",
    layout="centered"
)


QUIZ_LIST = [{'hints': ['한글을 만든 조선의 왕이야!', '백성을 위해 과학과 문화 발전에 힘썼어!', '훈민정음을 만들어 사람들이 쉽게 글을 읽고 쓰게 했어!'], 'answer': '세종대왕'},
 {'hints': ['임진왜란 때 나라를 지킨 장군이야!', '거북선을 활용해 왜군과 싸웠어!', "유명한 말로 '신에게는 아직 열두 척의 배가 있습니다'가 있어!"], 'answer': '이순신'},
 {'hints': ['대한민국 임시정부에서 활동한 독립운동가야!', '백범일지를 쓴 인물이야!', '나라의 완전한 독립을 위해 평생 노력했어!'], 'answer': '김구'},
 {'hints': ['3·1운동 때 대한 독립 만세를 외친 독립운동가야!', '어린 나이에 나라의 독립을 위해 싸웠어!', '서대문형무소에서 순국한 인물이야!'], 'answer': '유관순'},
 {'hints': ['하얼빈에서 이토 히로부미를 저격한 독립운동가야!', '대한 독립을 위해 목숨을 바쳤어!', '동양 평화를 중요하게 생각한 인물이야!'], 'answer': '안중근'},
 {'hints': ['도시락 폭탄 의거로 유명한 독립운동가야!', '상하이 홍커우 공원에서 의거를 했어!', '나라를 위해 젊은 나이에 목숨을 바쳤어!'], 'answer': '윤봉길'},
 {'hints': ['일본 왕에게 폭탄을 던지려 했던 독립운동가야!', '대한민국의 독립을 세계에 알리려 했어!', '김구 선생과 함께 독립운동을 했어!'], 'answer': '이봉창'},
 {'hints': ['청산리 대첩을 승리로 이끈 독립군 장군이야!', '북로군정서군을 이끌었어!', '일제에 맞서 무장 독립운동을 펼쳤어!'], 'answer': '김좌진'},
 {'hints': ['봉오동 전투를 승리로 이끈 독립군 장군이야!', '일제강점기 무장 독립운동을 이끌었어!', '독립군을 이끌고 일본군과 싸운 장군이야!'], 'answer': '홍범도'},
 {'hints': ['하늘과 바람과 별과 시를 쓴 시인이야!', '일제강점기에 우리말로 시를 썼어!', "유명한 구절로 '하늘을 우러러 한 점 부끄럼이 없기를'이 있어!"], 'answer': '윤동주'},
 {'hints': ['어린이를 사랑한 인물이야!', '어린이날을 만드는 데 큰 역할을 했어!', '어린이를 낮춰 부르지 말고 존중하자고 주장했어!'], 'answer': '방정환'},
 {'hints': ['조선 시대의 과학자야!', '측우기와 물시계 제작에 힘썼어!', '신분은 낮았지만 뛰어난 재능으로 과학 발전에 기여했어!'], 'answer': '장영실'},
 {'hints': ['조선 시대의 여성 예술가야!', '그림과 글씨에 뛰어났어!', '율곡 이이의 어머니로도 알려져 있어!'], 'answer': '신사임당'},
 {'hints': ['우리말과 글을 지키기 위해 노력한 학자야!', '한글 문법 연구에 큰 업적을 남겼어!', '일제강점기에도 우리말의 소중함을 알렸어!'], 'answer': '주시경'},
 {'hints': ['독도를 지키기 위해 노력한 조선 시대 인물이야!', '울릉도와 독도가 우리 땅임을 주장했어!', '일본에 건너가 조선의 영토임을 알렸어!'], 'answer': '안용복'},
 {'hints': ['미국의 발명가야!', '전구를 발명한 인물로 유명해!', '많은 실패 끝에 발명을 성공시킨 노력의 상징이야!'], 'answer': '에디슨'},
 {'hints': ['전화기를 발명한 것으로 유명한 과학자야!', '소리를 멀리 전달하는 기술을 연구했어!', '사람들이 멀리서도 대화할 수 있게 도왔어!'], 'answer': '벨'},
 {'hints': ['만유인력의 법칙을 발견한 과학자야!', '사과가 떨어지는 모습을 보고 중력을 생각한 이야기로 유명해!', '수학과 과학 발전에 큰 영향을 준 인물이야!'], 'answer': '뉴턴'},
 {'hints': ['상대성이론을 만든 과학자야!', '천재 과학자의 대표 인물로 알려져 있어!', '유명한 공식 E=mc²와 관련된 인물이야!'], 'answer': '아인슈타인'},
 {'hints': ['라듐을 발견한 과학자야!', '노벨상을 받은 여성 과학자야!', '방사능 연구에 큰 업적을 남겼어!'], 'answer': '마리 퀴리'},
 {'hints': ['진화론을 주장한 과학자야!', '갈라파고스 제도를 탐사했어!', '생물이 오랜 시간에 걸쳐 변화한다고 설명했어!'], 'answer': '다윈'},
 {'hints': ['비행기를 처음으로 성공적으로 날린 형제야!', '하늘을 나는 기계를 만들기 위해 연구했어!', '인류의 항공 역사에 큰 업적을 남겼어!'], 'answer': '라이트 형제'},
 {'hints': ['지동설을 주장한 천문학자야!', '태양이 중심이고 지구가 돈다고 설명했어!', '우주를 바라보는 생각을 크게 바꾼 인물이야!'], 'answer': '코페르니쿠스'},
 {'hints': ['망원경으로 우주를 관찰한 과학자야!', '지동설을 지지했어!', "유명한 말로 '그래도 지구는 돈다'가 알려져 있어!"], 'answer': '갈릴레이'},
 {'hints': ['컴퓨터 과학의 발전에 큰 영향을 준 수학자야!', '암호 해독에 중요한 역할을 했어!', '인공지능과 컴퓨터의 기초를 만든 인물로 평가돼!'], 'answer': '앨런 튜링'},
 {'hints': ['모나리자를 그린 예술가야!', '그림뿐 아니라 과학과 발명에도 뛰어났어!', '르네상스 시대의 천재로 불려!'], 'answer': '레오나르도 다 빈치'},
 {'hints': ['해바라기 그림으로 유명한 화가야!', '별이 빛나는 밤을 그렸어!', '살아 있을 때보다 죽은 뒤에 더 유명해진 화가야!'], 'answer': '반 고흐'},
 {'hints': ['운명 교향곡을 만든 음악가야!', '귀가 잘 들리지 않게 된 뒤에도 음악을 만들었어!', '고난을 이겨낸 음악가로 유명해!'], 'answer': '베토벤'},
 {'hints': ['어린 시절부터 천재 음악가로 유명했어!', '마술피리와 작은 별 변주곡으로 알려져 있어!', '짧은 생애 동안 많은 음악을 남겼어!'], 'answer': '모차르트'},
 {'hints': ['노예 해방을 이끈 미국 대통령이야!', '미국 남북전쟁 시기의 지도자였어!', "유명한 말로 '국민의, 국민에 의한, 국민을 위한 정부'가 있어!"], 'answer': '링컨'},
 {'hints': ['인도의 독립운동을 이끈 인물이야!', '폭력이 아닌 비폭력 저항을 주장했어!', '소금 행진으로 유명해!'], 'answer': '간디'},
 {'hints': ['흑인 인권 운동을 이끈 목사야!', '차별 없는 세상을 꿈꿨어!', "유명한 연설로 '나에게는 꿈이 있습니다'가 있어!"], 'answer': '마틴 루터 킹'},
 {'hints': ['남아프리카공화국의 인종차별에 맞서 싸웠어!', '오랜 감옥 생활 뒤 대통령이 되었어!', '용서와 화해를 강조한 지도자야!'], 'answer': '넬슨 만델라'},
 {'hints': ['가난하고 아픈 사람들을 도운 수녀야!', '인도 콜카타에서 봉사활동을 했어!', '사랑과 봉사의 상징으로 알려져 있어!'], 'answer': '마더 테레사'},
 {'hints': ['전쟁터에서 다친 병사들을 돌본 간호사야!', '등불을 들고 환자를 돌본 이야기로 유명해!', '현대 간호학의 기초를 세운 인물이야!'], 'answer': '나이팅게일'},
 {'hints': ['백신과 세균 연구에 큰 업적을 남긴 과학자야!', '광견병 백신 개발로 유명해!', '음식을 안전하게 보관하는 살균법과도 관련이 있어!'], 'answer': '파스퇴르'},
 {'hints': ['페니실린을 발견한 과학자야!', '곰팡이에서 세균을 죽이는 물질을 발견했어!', '많은 사람의 생명을 구한 항생제 발전에 기여했어!'], 'answer': '플레밍'}]


PERSON_EXPLANATIONS = {'세종대왕': '세종대왕은 조선의 왕으로, 백성들이 쉽게 글을 읽고 쓸 수 있도록 한글을 만들었어.',
 '이순신': '이순신은 임진왜란 때 조선을 지킨 장군이야. 거북선을 활용하고 뛰어난 전략으로 많은 전투에서 승리했어.',
 '김구': '김구는 대한민국 임시정부에서 활동한 독립운동가야. 나라의 독립을 위해 평생 노력했어.',
 '유관순': '유관순은 3·1운동 때 대한 독립 만세를 외친 독립운동가야. 어린 나이에도 나라를 위해 용기 있게 행동했어.',
 '안중근': '안중근은 하얼빈에서 이토 히로부미를 저격한 독립운동가야. 동양 평화를 중요하게 생각했어.',
 '윤봉길': '윤봉길은 상하이 홍커우 공원에서 도시락 폭탄 의거를 한 독립운동가야.',
 '이봉창': '이봉창은 일본 왕에게 폭탄을 던지려 했던 독립운동가야. 우리나라의 독립 의지를 세계에 알리려 했어.',
 '김좌진': '김좌진은 청산리 대첩을 승리로 이끈 독립군 장군이야.',
 '홍범도': '홍범도는 봉오동 전투를 승리로 이끈 독립군 장군이야.',
 '윤동주': '윤동주는 일제강점기에 우리말로 시를 쓴 시인이야. 대표 작품으로 서시가 있어.',
 '방정환': '방정환은 어린이를 사랑하고 어린이날을 만드는 데 큰 역할을 한 인물이야.',
 '장영실': '장영실은 조선 시대 과학자로, 물시계와 측우기 같은 과학 기구 제작에 힘썼어.',
 '신사임당': '신사임당은 조선 시대의 예술가야. 그림과 글씨에 뛰어났고 율곡 이이의 어머니로도 알려져 있어.',
 '주시경': '주시경은 우리말과 한글을 연구하고 지키기 위해 노력한 학자야.',
 '안용복': '안용복은 울릉도와 독도가 우리 땅임을 알리기 위해 노력한 조선 시대 인물이야.',
 '에디슨': '에디슨은 전구와 축음기 등 여러 발명품으로 유명한 발명가야.',
 '벨': '벨은 전화기를 발명한 것으로 알려진 과학자야. 사람들이 멀리서도 대화할 수 있게 하는 기술 발전에 기여했어.',
 '뉴턴': '뉴턴은 만유인력의 법칙을 발견한 과학자야. 중력과 운동 법칙 연구로 과학 발전에 큰 영향을 주었어.',
 '아인슈타인': '아인슈타인은 상대성이론을 만든 과학자야. 현대 물리학 발전에 큰 영향을 준 인물이야.',
 '마리 퀴리': '마리 퀴리는 라듐과 방사능 연구로 유명한 과학자야. 노벨상을 받은 뛰어난 여성 과학자야.',
 '다윈': '다윈은 진화론을 주장한 과학자야. 생물이 오랜 시간에 걸쳐 변화한다고 설명했어.',
 '라이트 형제': '라이트 형제는 비행기를 만들어 하늘을 나는 데 성공한 형제야.',
 '코페르니쿠스': '코페르니쿠스는 태양을 중심으로 지구가 돈다는 지동설을 주장한 천문학자야.',
 '갈릴레이': '갈릴레이는 망원경으로 우주를 관찰하고 지동설을 지지한 과학자야.',
 '앨런 튜링': '앨런 튜링은 컴퓨터 과학과 인공지능의 기초를 세운 수학자야.',
 '레오나르도 다 빈치': '레오나르도 다 빈치는 모나리자를 그린 예술가이자 과학과 발명에도 뛰어난 르네상스 시대 인물이야.',
 '반 고흐': '반 고흐는 해바라기와 별이 빛나는 밤을 그린 화가야.',
 '베토벤': '베토벤은 운명 교향곡을 만든 음악가야. 귀가 잘 들리지 않게 된 뒤에도 훌륭한 음악을 만들었어.',
 '모차르트': '모차르트는 어린 시절부터 천재 음악가로 유명했고 많은 명곡을 남긴 작곡가야.',
 '링컨': '링컨은 미국의 대통령으로 노예 해방을 이끈 인물이야.',
 '간디': '간디는 인도의 독립운동을 비폭력으로 이끈 인물이야.',
 '마틴 루터 킹': '마틴 루터 킹은 흑인 인권 운동을 이끈 목사야. 차별 없는 세상을 꿈꿨어.',
 '넬슨 만델라': '넬슨 만델라는 남아프리카공화국의 인종차별에 맞서 싸운 지도자야.',
 '마더 테레사': '마더 테레사는 가난하고 아픈 사람들을 도운 수녀야.',
 '나이팅게일': '나이팅게일은 전쟁터에서 다친 병사들을 돌본 간호사야. 현대 간호학의 기초를 세웠어.',
 '파스퇴르': '파스퇴르는 세균과 백신 연구로 유명한 과학자야. 광견병 백신 개발로도 알려져 있어.',
 '플레밍': '플레밍은 페니실린을 발견한 과학자야. 항생제 발전에 큰 도움을 주었어.'}


def apply_style():
    # --- 폰트 및 스타일 설정 ---
    st.markdown("""
        <style>
        html, body, [class*="css"] {
            font-size: 18px;
        }
        .stAlert p {
            font-size: 24px !important;
            font-weight: bold;
        }
        input {
            font-size: 26px !important;
        }
        button p {
            font-size: 26px !important;
            font-weight: bold;
        }
        </style>
        """, unsafe_allow_html=True)


def reset_myapp_state():
    # pokemon_quiz.py에서 쓰는 세션 키 초기화
    for key in ["shuffled_list", "current_idx", "wrong_attempts", "correct_answer_given"]:
        if key in st.session_state:
            del st.session_state[key]


def reset_great_person_state():
    # 위인 퀴즈에서 쓰는 세션 키 초기화
    for key in [
        "gp_shuffled_list",
        "gp_current_idx",
        "gp_wrong_attempts",
        "gp_correct_answer_given",
        "gp_answer_revealed",
    ]:
        if key in st.session_state:
            del st.session_state[key]


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
    else:
        st.info("images/home.png 파일을 넣으면 여기에 홈 화면 사진이 나와요.")

    st.write("")
    st.write("")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("👑 위인 퀴즈", use_container_width=True):
            st.session_state.page = "great_person"
            st.rerun()

    with col2:
        if st.button("⚡ 포켓몬 퀴즈", use_container_width=True):
            st.session_state.page = "pokemon"
            st.rerun()


def show_great_person():
    if st.button("🏠 홈으로"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()
    st.title("🎮 위인 인물 퀴즈")

    # 세션 상태 초기화
    if "gp_answer_revealed" not in st.session_state:
        st.session_state.gp_answer_revealed = False

    if "gp_shuffled_list" not in st.session_state:
        shuffled = QUIZ_LIST.copy()
        random.shuffle(shuffled)
        st.session_state.gp_shuffled_list = shuffled

    if "gp_current_idx" not in st.session_state:
        st.session_state.gp_current_idx = 0

    if "gp_wrong_attempts" not in st.session_state:
        st.session_state.gp_wrong_attempts = 0

    if "gp_correct_answer_given" not in st.session_state:
        st.session_state.gp_correct_answer_given = False

    current_list = st.session_state.gp_shuffled_list
    idx = st.session_state.gp_current_idx

    # 퀴즈 실행 로직
    if idx < len(current_list):
        q = current_list[idx]
        ans = q["answer"]
        hints = q["hints"]
        explanation = PERSON_EXPLANATIONS.get(ans, "이 인물은 역사적으로 중요한 업적을 남긴 위인이야.")

        st.write("---")
        st.subheader(f"문제 {idx + 1} / {len(current_list)}")

        # 처음에는 힌트 1개만 보이고, 틀릴 때마다 하나씩 추가 표시
        visible_hint_count = min(1 + st.session_state.gp_wrong_attempts, len(hints))

        for i in range(visible_hint_count):
            st.info(f"💡 힌트 {i + 1}: {hints[i]}")

        # 2번 틀렸을 때 강력 힌트 추가
        if st.session_state.gp_wrong_attempts >= 2 and not st.session_state.gp_correct_answer_given:
            first_char = ans[0]
            last_char = ans[-1]
            answer_len = len(ans.replace(" ", ""))

            st.warning(
                f"🔥 강력 힌트: 정답은 **{answer_len}글자**이고, "
                f"**'{first_char}'**로 시작해서 **'{last_char}'**로 끝나!"
            )

        # 정답을 맞히거나 3번 틀려서 정답이 공개된 경우
        if st.session_state.gp_correct_answer_given:
            if st.session_state.gp_answer_revealed:
                st.error(f"😢 아쉽지만 정답은 **{ans}** 이야!")
            else:
                st.success(f"♥ 딩동댕! **{ans}** 정답입니다! 위인전 책 많이 읽었구나 ♥")
                st.balloons()

            st.markdown("### 📖 위인 설명")
            st.success(explanation)

            st.write(f"👏 지금까지 {idx + 1}문제를 풀었어!")

            if st.button("다음 문제 풀러 가기 ➡️"):
                st.session_state.gp_current_idx += 1
                st.session_state.gp_wrong_attempts = 0
                st.session_state.gp_correct_answer_given = False
                st.session_state.gp_answer_revealed = False
                st.rerun()

        # 아직 정답을 맞히지 않았고, 정답 공개도 안 된 경우
        else:
            user_ans = st.text_input("정답을 입력하세요:", key=f"gp_input_{idx}")

            if st.button("정답 확인!"):
                # 띄어쓰기 차이는 정답으로 인정
                clean_user_ans = user_ans.strip().replace(" ", "")
                clean_ans = ans.replace(" ", "")

                if clean_user_ans == clean_ans:
                    st.session_state.gp_correct_answer_given = True
                    st.session_state.gp_answer_revealed = False
                    st.rerun()
                else:
                    st.session_state.gp_wrong_attempts += 1

                    # 3번 틀리면 정답 공개 + 설명 표시
                    if st.session_state.gp_wrong_attempts >= 3:
                        st.session_state.gp_correct_answer_given = True
                        st.session_state.gp_answer_revealed = True
                        st.rerun()
                    else:
                        st.error("땡! 틀렸어. 힌트가 하나 더 열렸어!")
                        st.rerun()

    else:
        st.balloons()
        st.success("🎉 모든 퀴즈를 다 풀었어요! 완전 멋쟁이야! 🎉")

        if st.button("처음부터 다시 하기"):
            reset_great_person_state()
            st.rerun()


def show_myapp():
    if st.button("🏠 홈으로"):
        st.session_state.page = "home"
        st.rerun()

    st.divider()
    myapp.run()


def main():
    apply_style()

    if "page" not in st.session_state:
        st.session_state.page = "home"

    if st.session_state.page == "home":
        show_home()
    elif st.session_state.page == "great_person":
        show_great_person()
    elif st.session_state.page == "pokemon":
        show_myapp()
    else:
        st.session_state.page = "home"
        st.rerun()


main()
