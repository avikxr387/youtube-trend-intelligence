import streamlit as st
import pandas as pd
import sqlite3

# ---------------------------------------------------
# Page Config
# ---------------------------------------------------
st.set_page_config(
    page_title="YouTube Trend Intelligence",
    layout="wide"
)

DB_PATH = "youtube.db"

# ---------------------------------------------------
# Modern Purple Theme CSS
# ---------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #0f0b1c, #1a1033);
    color: white;
}

/* Metric Cards */
.metric-card {
    background: #1f1636;
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    box-shadow: 0 6px 18px rgba(128,0,255,0.35);
    transition: 0.2s;
}
.metric-card:hover {
    transform: scale(1.02);
}
.metric-title {
    font-size: 15px;
    color: #cbb6ff;
}
.metric-value {
    font-size: 38px;
    font-weight: bold;
    color: #a855ff;
}

/* Wide Navigation Buttons */
.big-button button {
    width: 100%;
    height: 50px;
    font-size: 16px;
    border-radius: 10px;
    background-color: #1f1636;
    color: #cbb6ff;
    border: 1px solid rgba(168, 85, 247, 0.5);
    font-weight: 600;
}
.big-button button:hover {
    background-color: #2a1f4a;
    border-color: #a855ff;
    color: white;
}



/* Video Cards */
.card {
    background: #1f1636;
    border-radius: 12px;
    padding: 10px;
    margin-bottom: 15px;
    box-shadow: 0 4px 12px rgba(128, 0, 255, 0.3);
}

.title {
    font-size: 14px;
    font-weight: bold;
}

.meta {
    font-size: 12px;
    color: #cbb6ff;
}

.viral {
    background: #6d28d9;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 10px;
    margin-top: 4px;
    display: inline-block;
}

/* Full width Watch Button */
.watch-btn a {
    display: block;
    text-align: center;
    background: #7c3aed;
    color: white;
    padding: 8px;
    border-radius: 8px;
    margin-top: 8px;
    text-decoration: none;
    font-size: 13px;
    font-weight: 600;
}
.watch-btn a:hover {
    background: #6d28d9;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Header
# ---------------------------------------------------
st.markdown("""
<h1 style='text-align: center; font-size: 48px; margin-bottom: 5px;'>
YouTube Trend Intelligence
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    color: #cbb6ff;
    margin-top: -10px;
    margin-bottom: 25px;
    letter-spacing: 0.5px;
">
Real-Time Viral Detection • Early Trend Prediction
</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# Load Data
# ---------------------------------------------------
conn = sqlite3.connect(DB_PATH)

try:
    df = pd.read_sql("SELECT * FROM video_viral_status", conn)
except:
    df = pd.read_sql("SELECT * FROM video_trends", conn)

conn.close()

if len(df) == 0:
    st.warning("No data available yet")
    st.stop()

df = df.sort_values("view_velocity", ascending=False)

# ---------------------------------------------------
# Ensure required columns exist
# ---------------------------------------------------
if "is_viral" not in df.columns:
    threshold = df["view_velocity"].quantile(0.90)
    df["is_viral"] = (df["view_velocity"] >= threshold).astype(int)

if "engagement_rate" not in df.columns:
    df["engagement_rate"] = 0

# Thumbnail + URL
df["thumbnail"] = df["video_id"].apply(
    lambda x: f"https://img.youtube.com/vi/{x}/hqdefault.jpg"
)
df["url"] = df["video_id"].apply(
    lambda x: f"https://www.youtube.com/watch?v={x}"
)

# ---------------------------------------------------
# Metric Tiles
# ---------------------------------------------------
# -------- Metrics + Buttons (Aligned) --------

# -------- Metrics + Centered Buttons --------

total_videos = len(df)
viral_videos = int(df["is_viral"].sum())
avg_velocity = int(df["view_velocity"].mean())

c1, c2, c3 = st.columns(3)

# -------- Column 1 --------
with c1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Videos</div>
        <div class="metric-value">{total_videos}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # vertical spacing

    left, center, right = st.columns([2,3,2])
    with center:
        st.markdown('<div class="big-button">', unsafe_allow_html=True)
        show_all = st.button("Detailed Review", key="all")
        st.markdown('</div>', unsafe_allow_html=True)


# -------- Column 2 --------
with c2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Viral Videos</div>
        <div class="metric-value">{viral_videos}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([2,3,2])
    with center:
        st.markdown('<div class="big-button">', unsafe_allow_html=True)
        show_viral = st.button("Viral Videos", key="viral")
        st.markdown('</div>', unsafe_allow_html=True)


# -------- Column 3 --------
with c3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Average Velocity</div>
        <div class="metric-value">{avg_velocity}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    left, center, right = st.columns([2,3,2])
    with center:
        st.markdown('<div class="big-button">', unsafe_allow_html=True)
        show_early = st.button("Early Trending", key="early")
        st.markdown('</div>', unsafe_allow_html=True)



st.divider()

# ---------------------------------------------------
# Navigation Buttons
# ---------------------------------------------------
# Centered button layout
# left, b1, b2, b3, right = st.columns([1, 2, 2, 2, 1])

# with b1:
#     st.markdown('<div class="big-button">', unsafe_allow_html=True)
#     show_viral = st.button("Viral Videos")
#     st.markdown('</div>', unsafe_allow_html=True)

# with b2:
#     st.markdown('<div class="big-button">', unsafe_allow_html=True)
#     show_early = st.button("Early Trending")
#     st.markdown('</div>', unsafe_allow_html=True)

# with b3:
#     st.markdown('<div class="big-button">', unsafe_allow_html=True)
#     show_all = st.button("Detailed Review")
#     st.markdown('</div>', unsafe_allow_html=True)


# st.divider()

# ---------------------------------------------------
# Video Grid Function
# ---------------------------------------------------
def video_grid(data, title, max_items=24):
    st.subheader(title)
    cols = st.columns(4)

    for idx, row in enumerate(data.head(max_items).itertuples()):
        with cols[idx % 4]:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            # Thumbnail
            st.markdown(
                f'<a href="{row.url}" target="_blank">'
                f'<img src="{row.thumbnail}" width="100%" style="border-radius:8px;">'
                f'</a>',
                unsafe_allow_html=True
            )

            # Title
            st.markdown(f'<div class="title">{row.title[:80]}</div>', unsafe_allow_html=True)

            # Meta
            st.markdown(
                f'<div class="meta">'
                f'{row.channel}<br>'
                f'Velocity: {int(row.view_velocity)}/hr<br>'
                f'Age: {int(row.age_hours)} hrs'
                f'</div>',
                unsafe_allow_html=True
            )

            # Viral tag
            if row.is_viral == 1:
                st.markdown('<div class="viral">VIRAL</div>', unsafe_allow_html=True)

            # Full width watch button
            st.markdown(
                f'<div class="watch-btn"><a href="{row.url}" target="_blank">Watch Video</a></div>',
                unsafe_allow_html=True
            )

            st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# Detailed Metrics Cards
# ---------------------------------------------------
def detailed_cards(data, max_items=60):
    st.subheader("Detailed Video Analysis")
    cols = st.columns(3)

    for idx, row in enumerate(data.head(max_items).itertuples()):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="card">
                <div class="title">{row.title[:70]}</div>
                <div class="meta">
                Channel: {row.channel}<br>
                Velocity: {int(row.view_velocity)}/hr<br>
                Engagement: {round(row.engagement_rate, 3)}<br>
                Age: {int(row.age_hours)} hrs
                </div>
            </div>
            """, unsafe_allow_html=True)

# ---------------------------------------------------
# Sections
# ---------------------------------------------------
if show_viral:
    video_grid(df[df["is_viral"] == 1], "Currently Viral")

elif show_early:
    video_grid(df[df["age_hours"] <= 24], "Early Trending (Under 24 Hours)", max_items=32)

elif show_all:
    detailed_cards(df)

else:
    video_grid(df.head(24), "Top Performing Videos")
