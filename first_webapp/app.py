# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """ 
    # 제 첫 웹페이지입니다.
    ## 부족하지만 많이 사랑해주십쇼
    ### 1$ 는 1300원 입니다.
    """
)

# 이미지 링크 삽입
st.image(
    "https://pixabay.com/get/gcaa95692587d71a176aee58233f8ede0154d1351fa34e8d9bfa408fd0cd5124a209e4b9556a0f548b30efd115fad7ce6627891860343018a36f87c628a0f92d2_1920.jpg"
)