import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------
# CONFIG
# --------------------------------------------------
st.set_page_config(page_title="Web Log Analytics Dashboard", layout="wide")

DATA_DIR = os.path.expanduser("/home/Harshini/log_results")
PLOTS_DIR = os.path.join(DATA_DIR, "plots")

# --------------------------------------------------
# CSV Loader
# --------------------------------------------------
def load_csv_from_dir(filename):
    path = os.path.join(DATA_DIR, filename)
    if os.path.exists(path):
        return pd.read_csv(path, header=None, names=["key", "value"])
    else:
        return None

# --------------------------------------------------
# UI HEADER
# --------------------------------------------------
st.title("📊 Web Log Analytics Dashboard")
st.write("Interactive dashboard generated from Apache-style access logs.")

tabs = st.tabs([
    "📈 Daily Traffic",
    "📅 Weekly Traffic",
    "📟 Status Codes",
    "🌐 Top IPs",
    "📨 Top Requests",
    "🗂 Raw CSV Data",
])

# --------------------------------------------------
# TAB 1 – DAILY TRAFFIC
# --------------------------------------------------
with tabs[0]:
    st.header("📈 Daily Traffic Trend")
    path = os.path.join(PLOTS_DIR, "daily_trend.png")
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning("daily_trend.png not found.")

# --------------------------------------------------
# TAB 2 – WEEKLY TRAFFIC
# --------------------------------------------------
with tabs[1]:
    st.header("📅 Weekly Traffic Trend")
    path = os.path.join(PLOTS_DIR, "weekly_trend.png")
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning("weekly_trend.png not found.")

# --------------------------------------------------
# TAB 3 – STATUS CODES
# --------------------------------------------------
with tabs[2]:
    st.header("📟 Status Code Distribution")
    path = os.path.join(PLOTS_DIR, "status_codes.png")
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning("status_codes.png not found.")

# --------------------------------------------------
# TAB 4 – TOP IPs
# --------------------------------------------------
with tabs[3]:
    st.header("🌐 Top IPs")
    path = os.path.join(PLOTS_DIR, "top_ips.png")
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning("top_ips.png not found.")

# --------------------------------------------------
# TAB 5 – TOP REQUESTS
# --------------------------------------------------
with tabs[4]:
    st.header("📨 Top Requests")
    path = os.path.join(PLOTS_DIR, "top_requests.png")
    if os.path.exists(path):
        st.image(path, use_container_width=True)
    else:
        st.warning("top_requests.png not found.")

# --------------------------------------------------
# TAB 6 – RAW CSV DATA
# --------------------------------------------------
with tabs[5]:
    st.header("🗂 Raw CSV Tables")

    # Auto-detect all CSV files in directory
    csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]

    file_choice = st.selectbox("Choose a CSV to view:", csv_files)

    df = load_csv_from_dir(file_choice)
    if df is not None:
        st.dataframe(df, use_container_width=True)
    else:
        st.error(f"{file_choice} not found.")

