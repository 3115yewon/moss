import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="이끼 공기 정화 실험",
    page_icon="🌿",
    layout="wide"
)

control = [4511, 906, 408, 401, 407]
moss = [411, 408, 412, 403, 409]
labels = ["1차", "2차", "3차", "4차", "5차"]
minutes = [0, 10, 20, 30, 40]

chart_df = pd.DataFrame({
    "측정 차수": labels,
    "시간(분)": minutes,
    "대조군": control,
    "실험군": moss,
})

st.title("🌿 이끼 공기 정화 실험 결과")
st.dataframe(chart_df, use_container_width=True, hide_index=True)
line_fig = go.Figure()

line_fig.add_trace(
    go.Scatter(
        x=labels,
        y=control,
        mode="lines+markers",
        name="대조군",
        line=dict(color="#c05050", width=4),
        marker=dict(size=10)
    )
)

line_fig.add_trace(
    go.Scatter(
        x=labels,
        y=moss,
        mode="lines+markers",
        name="실험군",
        line=dict(color="#2f6f52", width=4),
        marker=dict(size=10)
    )
)

line_fig.update_layout(
    title="시간에 따른 CO₂ 농도 변화",
    xaxis_title="측정 차수",
    yaxis_title="CO₂ 농도 (ppm)",
    height=500,
    template="plotly_white"
)

st.plotly_chart(line_fig, use_container_width=True)
st.success(
    "핵심: 실험군은 일부 측정에서 대조군보다 약간 높게 보이기도 했지만, "
    "전체적으로는 CO₂ 농도가 400대 진입한 것은 실험군이 더 빨랐습니다. "
)
