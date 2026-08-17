import pandas as pd
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Mock Dashboard", page_icon="📊", layout="wide")

st.markdown(
    """
    <style>
        :root {
            --bg: #1f2430;
            --bg-2: #2a3040;
            --card: rgba(35, 42, 55, 0.95);
            --soft: rgba(255,255,255,0.08);
            --text: #f2f5fa;
            --muted: #8f99ad;
            --orange: #f7b748;
            --yellow: #f3d35a;
            --blue: #4ea3ff;
            --pink: #ff7f7b;
            --green: #67d4b0;
            --cyan: #52d1ff;
        }

        html, body, [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #3c4658 0%, #272e3b 100%);
            color: var(--text);
        }

        [data-testid="stHeader"] {
            background: rgba(0,0,0,0);
        }

        .dashboard {
            padding: 1.2rem 0.6rem 2rem;
        }

        .card {
            background: rgba(42, 49, 62, 0.88);
            border: 1px solid rgba(255,255,255,0.05);
            border-radius: 18px;
            padding: 1rem 1.2rem 1.1rem;
            min-height: 240px;
            box-shadow: 0 8px 32px rgba(15, 17, 24, 0.25);
        }

        .small-card {
            min-height: 180px;
        }

        .title {
            font-size: 0.92rem;
            color: var(--muted);
            margin: 0 0 0.5rem 0;
            font-weight: 600;
        }

        .value {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text);
            margin: 0;
        }

        .kpi {
            font-size: 1.95rem;
            font-weight: 700;
            color: var(--text);
            margin: 0.1rem 0 0.6rem;
        }

        .sub {
            color: var(--muted);
            font-size: 0.8rem;
        }

        .chart-wrap {
            margin-top: 0.6rem;
        }

        .donut-box {
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 180px;
        }

        .big-number {
            position: absolute;
            font-size: 1.9rem;
            font-weight: 700;
            color: var(--text);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

weeks = ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]
revenue_values = [20, 35, 30, 26, 42, 55, 52]
bar_values = [42, 39, 46, 52, 48, 58, 63]

revenue_df = pd.DataFrame({"Week": weeks, "Revenue": revenue_values})

st.markdown('<div class="dashboard">', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1.1], gap="medium")

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<p class="title">Revenue</p>', unsafe_allow_html=True)
    st.markdown('<p class="kpi">23k</p>', unsafe_allow_html=True)
    st.line_chart(revenue_df.set_index("Week")["Revenue"], color="#f7b748", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card small-card">', unsafe_allow_html=True)
    st.markdown('<p class="title">Total sales</p>', unsafe_allow_html=True)
    st.markdown('<p class="kpi">$10,643</p>', unsafe_allow_html=True)
    st.bar_chart(pd.DataFrame({"Sales": [18, 28, 24, 32, 38, 36, 42]}, index=weeks), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

col3, col4, col5 = st.columns(3, gap="medium")

with col3:
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Done", "Left"],
                values=[68, 32],
                hole=0.72,
                sort=False,
                direction="clockwise",
                textinfo="none",
                hoverinfo="skip",
                marker=dict(
                    colors=["#51c0ff", "rgba(120, 130, 145, 0.25)"],
                    line=dict(color="rgba(0,0,0,0)", width=0),
                ),
            )
        ]
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.markdown('<div class="card small-card">', unsafe_allow_html=True)
    st.markdown('<p class="title">Successful transaction</p>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<div style="margin-top:-150px; text-align:center; font-size:1.2rem; font-weight:700;">68%</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col4:
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Done", "Left"],
                values=[82, 18],
                hole=0.72,
                sort=False,
                direction="clockwise",
                textinfo="none",
                hoverinfo="skip",
                marker=dict(
                    colors=["#f7b748", "rgba(120, 130, 145, 0.25)"],
                    line=dict(color="rgba(0,0,0,0)", width=0),
                ),
            )
        ]
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.markdown('<div class="card small-card">', unsafe_allow_html=True)
    st.markdown('<p class="title">Returning customer rate</p>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<div style="margin-top:-150px; text-align:center; font-size:1.2rem; font-weight:700;">82%</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col5:
    fig = go.Figure(
        data=[
            go.Pie(
                labels=["Done", "Left"],
                values=[34, 66],
                hole=0.72,
                sort=False,
                direction="clockwise",
                textinfo="none",
                hoverinfo="skip",
                marker=dict(
                    colors=["#f5a3a2", "rgba(120, 130, 145, 0.25)"],
                    line=dict(color="rgba(0,0,0,0)", width=0),
                ),
            )
        ]
    )
    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    st.markdown('<div class="card small-card">', unsafe_allow_html=True)
    st.markdown('<p class="title">Sales Target Completed</p>', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
    st.markdown('<div style="margin-top:-150px; text-align:center; font-size:1.2rem; font-weight:700;">34%</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
