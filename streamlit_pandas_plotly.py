# streamlit, pandas, plotly 를 통한  데이터 시각화 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# 데이터 생성
data = {
    '날짜': pd.date_range(start='2023-01-01', periods=100),
    '값': np.random.randn(100).cumsum()
}
df = pd.DataFrame(data)

# Streamlit 앱 제목
st.title("Plotly를 이용한 간단한 반응형 시각화")

# 데이터프레임 표시
st.subheader("데이터프레임")
st.write(df)

# Plotly 선 그래프 시각화
st.subheader("선 그래프")
fig = px.line(df, x='날짜', y='값', title='시간에 따른 값 변화')
st.plotly_chart(fig)

# Plotly 산점도 시각화
st.subheader("산점도")
fig_scatter = px.scatter(df, x='날짜', y='값', title='값의 분포')
st.plotly_chart(fig_scatter)
