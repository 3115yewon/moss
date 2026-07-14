import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="이끼 공기 정화 실험",
    page_icon="🥦",
    layout="wide"
)

control = [4511, 906, 408, 401, 407]
moss = [411, 408, 412, 403, 409]
labels = ["1차", "2차", "3차", "4차", "5차"]
minutes = [0, 10, 20, 30, 40]

chart_df = pd.DataFrame({
    "측정 차수": labels,
    "시간(분)": minutes,
    "대조군(ppm)": control,
    "실험군(ppm)": moss,
})
chart_df["차이(ppm)"] = chart_df["대조군(ppm)"] - chart_df["실험군(ppm)"]

control_drop = control[0] - control[-1]
moss_change = moss[0] - moss[-1]
first_gap = control[0] - moss[0]

change_labels = ["1→2차", "2→3차", "3→4차", "4→5차"]
control_change = [control[i] - control[i - 1] for i in range(1, len(control))]
moss_change_list = [moss[i] - moss[i - 1] for i in range(1, len(moss))]

st.markdown(
    """
    <style>
    .main {
        background: linear-gradient(180deg, 
