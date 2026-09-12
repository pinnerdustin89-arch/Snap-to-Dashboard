import streamlit as st
import pandas as pd
import plotly.express as px

# Set configuration values
st.set_page_config(page_title="Analytics Starter Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Inject theme directly via basic CSS styling
st.markdown("<style>.stApp { background-color: #030313 !important; color: #FFFFFF !important; font-family: sans-serif; } header, footer {visibility: hidden;}</style>", unsafe_html_allowed=True)

# Build out the gradient header section
st.markdown("<div style='text-align: center; padding: 2rem 1rem;'><span style='background: rgba(157, 23, 248, 0.15); color: #D36BFF; border: 1px solid rgba(157, 23, 248, 0.3); padding: 6px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: 600;'>✨ Now with AI-powered insights</span><h1 style='font-size: 2.8rem; font-weight: 800; line-height: 1.2; margin: 1rem 0; background: linear-gradient(135deg, #FFFFFF 40%, #FF66C4 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Analytics that<br>actually make sense</h1><p style='color: #8C8CA3; font-size: 1.05rem; max-width: 600px; margin: 0 auto 2rem auto;'>Stop drowning in data. Turn your metrics into actionable insights with AI-powered analytics that your whole team will love.</p></div>", unsafe_html_allowed=True)

# Add the interactive file uploader box
uploaded_file = st.file_uploader("", type=["csv", "xlsx"])

# Set up raw showcase metrics layout
st.markdown("<div style='display: flex; gap: 10px; margin-bottom: 2rem;'><div style='flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.2rem; text-align: center;'><p style='color: #8C8CA3; font-size: 0.85rem; margin:0;'>Total Users</p><p style='font-size: 1.8rem; font-weight: 700; margin:0;'>24,521</p><p style='color: #00E676; font-size: 0.8rem; margin:0;'>↑ 12%</p></div><div style='flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.2rem; text-align: center;'><p style='color: #8C8CA3; font-size: 0.85rem; margin:0;'>Active Now</p><p style='font-size: 1.8rem; font-weight: 700; margin:0;'>1,429</p><p style='color: #00E676; font-size: 0.8rem; margin:0;'>↑ 8%</p></div><div style='flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.2rem; text-align: center;'><p style='color: #8C8CA3; font-size: 0.85rem; margin:0;'>Revenue</p><p style='font-size: 1.8rem; font-weight: 700; margin:0;'>$48.2K</p><p style='color: #00E676; font-size: 0.8rem; margin:0;'>↑ 23%</p></div><div style='flex: 1; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.05); border-radius: 12px; padding: 1.2rem; text-align: center;'><p style='color: #8C8CA3; font-size: 0.85rem; margin:0;'>Conversion</p><p style='font-size: 1.8rem; font-weight: 700; margin:0;'>3.2%</p><p style='color: #00E676; font-size: 0.8rem; margin:0;'>↑ 0.4%</p></div></div>", unsafe_html_allowed=True)

# Build feature grid container fields
st.markdown("<h2 style='text-align: center; font-size: 2rem; font-weight: 800; margin: 3.5rem 0 2rem 0; background: linear-gradient(135deg, #FFFFFF 60%, #9D17F8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Powerful features that help you understand your data</h2>", unsafe_html_allowed=True)

# Display features description texts
st.markdown("<div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem;'><h3 style='font-size: 1.15rem; margin:0 0 0.5rem 0;'>📊 Real-time Analytics</h3><p style='font-size: 0.9rem; color: #8C8CA3; margin:0;'>Track metrics as they happen with sub-second latency and beautiful visual elements.</p></div>", unsafe_html_allowed=True)
st.markdown("<div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem;'><h3 style='font-size: 1.15rem; margin:0 0 0.5rem 0;'>✨ AI Insights</h3><p style='font-size: 0.9rem; color: #8C8CA3; margin:0;'>Get actionable business recommendations driven by machine learning pattern models.</p></div>", unsafe_html_allowed=True)
st.markdown("<div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem;'><h3 style='font-size: 1.15rem; margin:0 0 0.5rem 0;'>⚡ Lightning Fast</h3><p style='font-size: 0.9rem; color: #8C8CA3; margin:0;'>Queries finish in execution milliseconds, completely independent of total platform scale.</p></div>", unsafe_html_allowed=True)

# Display pricing header systems
st.markdown("<h2 style='text-align: center; font-size: 2rem; font-weight: 800; margin: 3.5rem 0 2rem 0; background: linear-gradient(135deg, #FFFFFF 60%, #9D17F8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>Simple, transparent pricing</h2>", unsafe_html_allowed=True)

# Build clean responsive pricing display elements 
st.markdown("<div style='background: rgba(255,255,255,0.02); border: 1px solid #9D17F8; border-radius: 18px; padding: 2rem; text-align: center;'><span style='background: #9D17F8; color: #FFFFFF; padding: 2px 14px; font-size: 0.75rem; font-weight: bold; border-radius: 12px;'>Most Popular Plan</span><h3 style='font-size: 1.4rem; margin: 1rem 0 0 0;'>Pro Dashboard</h3><p style='color: #8C8CA3; font-size: 0.9rem; margin: 0 0 1rem 0;'>For growing automated workflows</p><h2 style='font-size: 2.2rem; font-weight: bold; margin: 1rem 0;'>$49 <span style='font-size: 1rem; color: #8C8CA3;'>/ month</span></h2><p style='color: #8C8CA3; font-size: 0.9rem;'>✓ Unlimited data retention panels<br>✓ Seamless Snapchat integration pipelines<br>✓ Priority automated customer support loops</p></div>", unsafe_html_allowed=True)
