import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠")

st.title("🧠 MBTI 기반 직업 추천기")
st.write("MBTI 유형을 선택하면, 해당 성격 유형에 어울리는 직업 3가지를 추천해드려요!")

# MBTI 유형 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 직업 추천 사전
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "소프트웨어 아키텍트", "연구 과학자"],
    "INTP": ["데이터 과학자", "이론 물리학자", "UX 디자이너"],
    "ENTJ": ["경영 컨설턴트", "스타트업 CEO", "기획 디렉터"],
    "ENTP": ["광고 기획자", "발명가", "비즈니스 개발 매니저"],
    "INFJ": ["상담 심리사", "작가", "비영리 단체 운영자"],
    "INFP": ["시인", "콘텐츠 크리에이터", "사회복지사"],
    "ENFJ": ["교사", "코치", "홍보 전문가"],
    "ENFP": ["마케팅 디자이너", "창작자", "이벤트 플래너"],
    "ISTJ": ["회계사", "공무원", "보안 분석가"],
    "ISFJ": ["간호사", "초등 교사", "행정 비서"],
    "ESTJ": ["프로젝트 매니저", "군 장교", "운영 관리자"],
    "ESFJ": ["병원 코디네이터", "고객 서비스 관리자", "초등 교사"],
    "ISTP": ["기계 엔지니어", "파일럿", "응급 구조사"],
    "ISFP": ["플로리스트", "패션 디자이너", "요리사"],
    "ESTP": ["세일즈 매니저", "기업가", "구조 대원"],
    "ESFP": ["연예인", "이벤트 MC", "관광 가이드"]
}

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", mbti_types)

# 추천 직업 출력
if selected_mbti:
    st.subheader(f"✅ {selected_mbti} 유형에게 추천하는 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
