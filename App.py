import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Configuration & Custom CSS Injection for Global Theme
st.set_page_config(page_title="Analytics Starter Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS mimicking the midnight-dark theme with pink/purple gradients
st.markdown("""
    <style>
    /* Background and global text settings */
    .stApp {
        background-color: #030313 !important;
        color: #FFFFFF !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Hide top default streamlit elements for a cleaner SaaS feel */
    header, footer {visibility: hidden;}
    
    /* Premium Header Container */
    .hero-container {
        text-align: center;
        padding: 2.5rem 1rem 1.5rem 1rem;
    }
    .badge {
        background: rgba(157, 23, 248, 0.15);
        color: #D36BFF;
        border: 1px solid rgba(157, 23, 248, 0.3);
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 1rem;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 1rem;
        background: linear-gradient(135deg, #FFFFFF 40%, #FF66C4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-subtitle {
        color: #8C8CA3;
        font-size: 1.05rem;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }
    
    /* Glassmorphism Metric and Feature Cards */
    .card-metric {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        padding: 1.2rem;
        text-align: center;
    }
    .metric-label { color: #8C8CA3; font-size: 0.85rem; margin-bottom: 4px; }
    .metric-value { font-size: 1.8rem; font-weight: 700; color: #FFFFFF; }
    .metric-delta { color: #00E676; font-size: 0.8rem; font-weight: 600; margin-top: 4px; }
    
    .feature-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .feature-title { font-size: 1.15rem; font-weight: 700; color: #FFFFFF; margin-bottom: 0.5rem; }
    .feature-text { font-size: 0.9rem; color: #8C8CA3; line-height: 1.5; }
    
    /* Section Headings */
    .section-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 800;
        margin-top: 3.5rem;
        margin-bottom: 2rem;
        background: linear-gradient(135deg, #FFFFFF 60%, #9D17F8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Modern Pricing Cards */
    .pricing-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 18px;
        padding: 2rem;
        text-align: center;
        height: 100%;
    }
    .pricing-card.pro {
        border: 1px solid #9D17F8;
        position: relative;
    }
    .pricing-badge {
        position: absolute;
        top: -12px;
        left: 50%;
        transform: translateX(-50%);
        background: #9D17F8;
        color: #FFFFFF;
        padding: 2px 14px;
        font-size: 0.75rem;
        font-weight: bold;
        border-radius: 12px;
    }
    
    /* Premium Testimonial Cards */
    .testimonial-card {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid rgba(255, 255, 255, 0.04);
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .avatar {
        width: 36px;
        height: 36px;
        border-radius: 50%;
        background: #9D17F8;
        display: inline-block;
        vertical-align: middle;
        text-align: center;
        line-height: 36px;
        font-weight: bold;
        font-size: 0.85rem;
        margin-right: 10px;
    }
    </style>
""", unsafe_html_allowed=True)

# 2. Hero Header Section
st.markdown("""
    <div class="hero-container">
        <div class="badge">✨ Now with AI-powered insights</div>
        <div class="hero-title">Analytics that<br>actually make sense</div>
        <div class="hero-subtitle">Stop drowning in data. Turn your metrics into actionable insights with AI-powered analytics that your whole team will love.</div>
    </div>
""", unsafe_html_allowed=True)

# File Uploader Styled cleanly
uploaded_file = st.file_uploader("", type=["csv", "xlsx"])

# 3. Dynamic Dashboard Processing Block
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.markdown("<h2 style='text-align: center; font-size: 1.5rem; margin-top: 2rem;'>📈 Your Active Metrics Overview</h2>", unsafe_html_allowed=True)
        
        # Simulated Glossy Live Metrics Row
        m_col1, m_col2, m_col3, m_col4 = st.columns(4)
        with m_col1:
            st.markdown('<div class="card-metric"><div class="metric-label">Total Records</div><div class="metric-value">{:,}</div><div class="metric-delta">↑ 12% growth</div></div>'.format(len(df)), unsafe_html_allowed=True)
        with m_col2:
            st.markdown('<div class="card-metric"><div class="metric-label">Active Columns</div><div class="metric-value">{}</div><div class="metric-delta">↑ 8% optimization</div></div>'.format(len(df.columns)), unsafe_html_allowed=True)
        with m_col3:
            st.markdown('<div class="card-metric"><div class="metric-label">Gross Value</div><div class="metric-value">$48.2K</div><div class="metric-delta">↑ 23% this mo</div></div>', unsafe_html_allowed=True)
        with m_col4:
            st.markdown('<div class="card-metric"><div class="metric-label">Conversion Rate</div><div class="metric-value">3.2%</div><div class="metric-delta">↑ 0.4% trend</div></div>', unsafe_html_allowed=True)
            
        # Chart Display with Dark styling adjustments
        if len(df.columns) >= 2:
            fig_bar = px.bar(df, x=df.columns[0], y=df.columns[1], title="Live Comparison Analysis")
            fig_bar.update_layout(
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                font_color="#FFFFFF", title_font_color="#FFFFFF",
                colorway=['#9D17F8', '#FF66C4']
            )
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.dataframe(df)
            
    except Exception as e:
        st.error(f"Error parsing file: {e}")
else:
    # 4. Fallback Static Visual Showcase (Shows original template look when no file is uploaded yet)
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1:
        st.markdown('<div class="card-metric"><div class="metric-label">Total Users</div><div class="metric-value">24,521</div><div class="metric-delta">↑ 12%</div></div>', unsafe_html_allowed=True)
    with m_col2:
        st.markdown('<div class="card-metric"><div class="metric-label">Active Now</div><div class="metric-value">1,429</div><div class="metric-delta">↑ 8%</div></div>', unsafe_html_allowed=True)
    with m_col3:
        st.markdown('<div class="card-metric"><div class="metric-label">Revenue</div><div class="metric-value">$48.2K</div><div class="metric-delta">↑ 23%</div></div>', unsafe_html_allowed=True)
    with m_col4:
        st.markdown('<div class="card-metric"><div class="metric-label">Conversion</div><div class="metric-value">3.2%</div><div class="metric-delta">↑ 0.4%</div></div>', unsafe_html_allowed=True)

# 5. Core Feature Grid Section
st.markdown('<div class="section-title">Powerful features that help you understand your data</div>', unsafe_html_allowed=True)
f_col1, f_col2, f_col3 = st.columns(3)
with f_col1:
    st.markdown('<div class="feature-card"><div class="feature-title">📊 Real-time Analytics</div><div class="feature-text">Track metrics as they happen with sub-second latency and beautiful visual elements.</div></div>', unsafe_html_allowed=True)
    st.markdown('<div class="feature-card"><div class="feature-title">🔒 Enterprise Security</div><div class="feature-text">SOC 2 Type II certified with SSO protocols, comprehensive audit logging and controls.</div></div>', unsafe_html_allowed=True)
with f_col2:
    st.markdown('<div class="feature-card"><div class="feature-title">✨ AI Insights</div><div class="feature-text">Get actionable business recommendations driven by machine learning pattern models.</div></div>', unsafe_html_allowed=True)
    st.markdown('<div class="feature-card"><div class="feature-title">👥 Team Collaboration</div><div class="feature-text">Share structural views, coordinate alerts, and analyze parameters in real time.</div></div>', unsafe_html_allowed=True)
with f_col3:
    st.markdown('<div class="feature-card"><div class="feature-title">⚡ Lightning Fast</div><div class="feature-text">Queries finish in execution milliseconds, completely independent of total platform scale.</div></div>', unsafe_html_allowed=True)
    st.markdown('<div class="feature-card"><div class="feature-title">📋 Custom Reports</div><div class="feature-text">Build and arrange distribution loops that automatically land in email systems.</div></div>', unsafe_html_allowed=True)

# 6. Simple, Transparent Pricing Section
st.markdown('<div class="section-title">Simple, transparent pricing</div>', unsafe_html_allowed=True)
p_col1, p_col2, p_col3 = st.columns(3)
with p_col1:
