import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Global Page Configuration
st.set_page_config(page_title="Snap-to-Sheet Dashboard", layout="wide", initial_sidebar_state="collapsed")

# 2. Unified Interface Layout & Styling Injector
st.markdown("""
    <style>
    .stApp { background-color: #030313 !important; color: #FFFFFF !important; font-family: sans-serif; } 
    header, footer {visibility: hidden;}
    .hero-box { text-align: center; padding: 2rem 1rem; }
    .badge-premium { background: rgba(157, 23, 248, 0.15); color: #D36BFF; border: 1px solid rgba(157, 23, 248, 0.3); padding: 6px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; display: inline-block; }
    .title-gradient { font-size: 2.8rem; font-weight: 800; line-height: 1.2; margin: 1rem 0; background: linear-gradient(135deg, #FFFFFF 40%, #FF66C4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .subtitle-text { color: #8C8CA3; font-size: 1.05rem; max-width: 600px; margin: 0 auto 2rem auto; }
    .metrics-flex { display: flex; gap: 10px; margin-bottom: 2rem; }
    .metric-card { flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.2rem; text-align: center; }
    .m-label { color: #8C8CA3; font-size: 0.85rem; margin:0; }
    .m-val { font-size: 1.8rem; font-weight: 700; margin:0; }
    .m-delta { color: #00E676; font-size: 0.8rem; margin:0; }
    .sec-heading { text-align: center; font-size: 2rem; font-weight: 800; margin: 3.5rem 0 2rem 0; background: linear-gradient(135deg, #FFFFFF 60%, #9D17F8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .feat-card { background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem; }
    .feat-title { font-size: 1.15rem; margin:0 0 0.5rem 0; }
    .feat-desc { font-size: 0.9rem; color: #8C8CA3; margin:0; }
    .price-card { background: rgba(255,255,255,0.02); border: 1px solid #9D17F8; border-radius: 18px; padding: 2rem; text-align: center; max-width: 500px; margin: 0 auto; }
    .price-badge { background: #9D17F8; color: #FFFFFF; padding: 2px 14px; font-size: 0.75rem; font-weight: bold; border-radius: 12px; display: inline-block; }
    </style>
    
    <div class="hero-box">
        <span class="badge-premium">✨ Now with AI-powered insights</span>
        <h1 class="title-gradient">Snap-to-Sheet<br>Analytics Dashboard</h1>
        <p class="subtitle-text">Stop drowning in raw spreadsheets. Turn your data captures into instant, automated visual insights seamlessly.</p>
    </div>
    
    <div class="metrics-flex">
        <div class="metric-card"><p class="m-label">Total Syncs</p><p class="m-val">24,521</p><p class="m-delta">↑ 12% this week</p></div>
        <div class="metric-card"><p class="m-label">Active Pipes</p><p class="m-val">1,429</p><p class="m-delta">↑ 8% active</p></div>
        <div class="metric-card"><p class="m-label">Automated Revenue</p><p class="m-val">$48.2K</p><p class="m-delta">↑ 23% this month</p></div>
    </div>
    
    <h2 class="sec-heading">Powerful automated data pipelines</h2>
    
    <div class="feat-card"><h3 class="feat-title">📊 Real-Time Sheet Syncing</h3><p class="feat-desc">Track metrics instantly as files update with zero delay and beautiful visual dashboard trends.</p></div>
    <div class="feat-card"><h3 class="feat-title">⚡ Instant Spreadsheet Processing</h3><p class="feat-desc">Upload, process, and map data parameters across multi-column layouts automatically.</p></div>
    
    <h2 class="sec-heading">Simple, transparent pricing</h2>
    
    <div class="price-card">
        <span class="price-badge">Most Popular Plan</span>
        <h3 style="font-size: 1.4rem; margin: 1rem 0 0 0;">Pro Automated Dashboard</h3>
        <p style="color: #8C8CA3; font-size: 0.9rem; margin: 0 0 1rem 0;">For growing automated business workflows</p>
        <h2 style="font-size: 2.2rem; font-weight: bold; margin: 1rem 0;">$49 <span style="font-size: 1rem; color: #8C8CA3;">/ month</span></h2>
        <p style="color: #8C8CA3; font-size: 0.9rem; text-align: left; max-width: 320px; margin: 0 auto;">
            ✓ Unlimited live data retention panels<br>
            ✓ Seamless file integration pipelines<br>
            ✓ Priority automated customer support loops
        </p>
    </div>
""", unsafe_allow_html=True)

# 3. Functional File Uploader Panel
uploaded_file = st.file_uploader("", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        st.success("File uploaded successfully!")
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error processing document data: {e}")
