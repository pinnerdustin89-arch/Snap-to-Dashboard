import streamlit as str
import pandas as pd
import plotly.express as px

# Set up the page title and format layout
str.set_page_config(page_title="My Dashboard", layout="wide")
str.title("📊 My Data Dashboard")
str.markdown("Welcome to your live data dashboard. Use the sidebar to upload files.")

# Create a sidebar for user configuration and uploads
str.sidebar.header("Configuration")
uploaded_file = str.sidebar.file_uploader("Upload your Excel or CSV file", type=["csv", "xlsx"])

# Process data and display charts if a file is uploaded
if uploaded_file is not None:
    try:
        # Check file extension and load data safely
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Display raw interactive data table
        str.subheader("📁 Raw Data View")
        str.dataframe(df)
        
        # Build simple charts dynamically based on available columns
        if len(df.columns) >= 2:
            str.subheader("📈 Visual Data Analysis")
            col1, col2 = str.columns(2)
            
            with col1:
                # Column Chart
                fig_bar = px.bar(df, x=df.columns[0], y=df.columns[1], title="Data Comparison")
                str.plotly_chart(fig_bar, use_container_width=True)
                
            with col2:
                # Line Chart
                fig_line = px.line(df, x=df.columns[0], y=df.columns[1], title="Data Trends over Time")
                str.plotly_chart(fig_line, use_container_width=True)
        else:
            str.warning("Please upload a dataset with at least 2 columns to generate visual charts.")
            
    except Exception as e:
        str.error(f"Error loading file: {e}")
else:
    str.info("💡 Awaiting file upload... Please drag and drop or browse for an Excel/CSV file in the sidebar.")
