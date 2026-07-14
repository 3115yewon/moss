import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="이끼 공기 정화 실험",
    page_icon="🥦",
    layout="wide"
)

# 실험 데이터
control = [4511, 906, 408, 401, 407]
moss = [411, 408, 412, 403, 409]
labels = ["1차", "2차", "3차", "4차", "5차"]
minutes = [0, 10, 20, 30, 40]

# 표 데이터
chart_df = pd.DataFrame({
    "측정 차수": labels,
    "시간(분)": minutes,
    "대조군(ppm)": control,
    "실험군(ppm)": moss
})
chart_df["차이(ppm)"] = chart_df["대조군(ppm)"] - chart_df["실험군(ppm)"]

# 핵심 수치
control_drop = control[0] - control[-1]
moss_total_change = moss[0] - moss[-1]
first_gap = control[0] - moss[0]

# 스타일
st.markdown("""
<style>
.main {
    background: linear-gradient(180deg, #f4f7f1 0%, #eef5ec 100%);
}
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.97), rgba(226,239,228,0.93));
    border: 1px solid rgba(47,111,82,0.14);
    border-radius: 24px;
    padding: 28px 30px;
    box-shadow: 0 12px 30px rgba(27, 43, 31, 0.08);
    margin-bottom: 1.2rem;
}
.hero-kicker {
    display: inline-block;
    background: #dbe9de;
    color: #2f6f52;
    border-radius: 999px;
    padding: 7px 13px;
    font-size: 0.84rem;
    font-weight: 700;
    margin-bottom: 12px;
}
.small-note {
    font-size: 0.95rem;
    color: #607062;
}
.message-box {
    background: #f8fbf8;
    border-left: 6px solid #2f6f52;
    border-radius: 18px;
    padding: 20px;
    margin-top: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# 상단 설명
st.markdown("""
<div class="hero-box">
    <div class="hero-kicker">Moss CO₂ Experiment</div>
    <h1>이끼가 있는 비커는 CO₂ 농도가 더 빠르게 안정된 상태를 보였습니다.</h1>
    <p>
    같은 조건에서 향을 5초간 넣은 뒤 CO₂ 농도를 10분 간격으로 측정했습니다.
    대조군은 첫 측정에서 매우 높은 수치를 보인 뒤 급격히 감소했고,
    실험군은 처음부터 400ppm대에서 큰 변화 없이 유지되었습니다.
    </p>
</div>
""", unsafe_allow_html=True)

# 그래프
st.markdown("## 그래프")

line_fig = go.Figure()

line_fig.add_trace(go.Scatter(
    x=labels,
    y=control,
    mode="lines+markers",
    name="대조군",
    line=dict(color="#bf5a5a", width=4),
    marker=dict(size=10),
    hovertemplate="대조군 %{x}<br>%{y} ppm<extra></extra>"
))

line_fig.add_trace(go.Scatter(
    x=labels,
    y=moss,
    mode="lines+markers",
    name="실험군",
    line=dict(color="#2f6f52", width=4),
    marker=dict(size=10),
    hovertemplate="실험군 %{x}<br>%{y} ppm<extra></extra>"
))

line_fig.update_layout(
    title="시간에 따른 CO₂ 농도 변화",
    height=500,
    template="plotly_white",
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    margin=dict(l=20, r=20, t=70, b=20)
)
line_fig.update_xaxes(title="측정 차수")
line_fig.update_yaxes(title="CO₂ 농도 (ppm)", rangemode="tozero")

st.plotly_chart(line_fig, use_container_width=True)

# 그래프 해석 박스
st.markdown("""
<div class="message-box">
    <h3>그래프 해석 포인트</h3>
    <p>
    실험군이 일부 측정에서 대조군보다 조금 높게 보이는 구간이 있습니다.
    하지만 <b>대기 평균 CO₂ 농도가 434ppm이라는 점에서 실험군의 정화가 제대로 이루어졌음을 확인할 수 있습니다.
    </p>
    <ul>
        <li>대조군: 4511ppm에서 시작 후 급격히 감소</li>
        <li>실험군: 411ppm에서 시작 후 400ppm대 유지</li>
        <li>핵심: 실험군은 첫 측정부터 안정 상태</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# 실험 조건
st.markdown("## 실험 조건")
info1, info2, info3, info4 = st.columns(4)
info1.info("대조군: 이끼 없음")
info2.info("실험군: 이끼 있음")
info3.info("향 5초 주입 후 제거")
info4.info("비커 상단 파라필름 밀폐")

# 표
st.markdown("## 측정 데이터")

left_space, table_col, right_space = st.columns([1.2, 2.2, 1.2])

with table_col:
    st.dataframe(
        chart_df,
        use_container_width=False,
        hide_index=True,
        width=700
    )

# 결론 문장
st.success(
    "발표 핵심 문장: 실험군은 일부 시점에서 대조군보다 수치가 약간 높아 보이기도 했지만, "
    "전체적으로는 CO₂ 농도가 400ppm대로 유지되었습니다."
)
