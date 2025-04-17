import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd
from modules.nav import SideBarLinks

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- Page Configuration ---
st.set_page_config(page_title="System Metrics", page_icon="📊", layout="wide")
SideBarLinks()

# --- Title & Intro ---
st.title("Roomies4Life System Metrics")
st.markdown("Monitor system performance, track suspicious activity, and manage security alerts.")

# --- API Base URL ---
API_URL = "http://web-api:4000/admin"

# --- Helper Functions ---
def fetch_system_stats():
    try:
        res = requests.get(f"{API_URL}/system/stats")
        res.raise_for_status()
        return res.json()[0]
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching system stats: {e}")
        st.error("Failed to fetch system statistics.")
        return {}

def fetch_suspicious_logins():
    try:
        res = requests.get(f"{API_URL}/security/login-attempts")
        res.raise_for_status()
        return pd.DataFrame(res.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching suspicious logins: {e}")
        st.error("Failed to fetch suspicious login data.")
        return pd.DataFrame()

def fetch_data_access_logs():
    try:
        res = requests.get(f"{API_URL}/audit/data-access")
        res.raise_for_status()
        return pd.DataFrame(res.json())
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data access logs: {e}")
        st.error("Failed to fetch data access logs.")
        return pd.DataFrame()

# --- System Overview Metrics ---
st.subheader("📊 System Overview")

system_stats = fetch_system_stats()
if system_stats:
    col1, col2, col3 = st.columns(3)
    
    total_users = system_stats.get("total_students", 0) + system_stats.get("total_RAs", 0) + system_stats.get("total_admins", 0)
    col1.metric("Total Users", total_users)
    col2.metric("Active Events", system_stats.get("total_events", 0))
    col3.metric("Open Complaints", system_stats.get("total_complaints", 0))
    
    # Additional metrics row
    col1, col2, col3 = st.columns(3)
    col1.metric("Student Users", system_stats.get("total_students", 0))
    col2.metric("RA Users", system_stats.get("total_RAs", 0))
    col3.metric("Admin Users", system_stats.get("total_admins", 0))
else:
    st.info("No system statistics available.")

# --- Suspicious Login Activity ---
st.subheader("🚨 Suspicious Login Activity")
suspicious_logins = fetch_suspicious_logins()

if not suspicious_logins.empty:
    st.warning(f"{len(suspicious_logins)} users have suspicious login activity")
    
    # Add visualization
    fig, ax = plt.subplots(figsize=(10, 5))
    suspicious_logins.sort_values('failed_attempts', ascending=False, inplace=True)
    ax.bar(suspicious_logins['userId'].astype(str), suspicious_logins['failed_attempts'])
    ax.set_xlabel("User ID")
    ax.set_ylabel("Failed Login Attempts")
    ax.set_title("Failed Login Attempts by User")
    plt.xticks(rotation=45)
    st.pyplot(fig)
    
    # Display the data table with suspicious logins
    st.dataframe(suspicious_logins, use_container_width=True)
else:
    st.success("No suspicious login activity detected.")

# --- Data Access Logs ---
st.subheader("📝 Data Access Audit Logs")
data_access_logs = fetch_data_access_logs()

if not data_access_logs.empty:
    # Filter options
    access_types = ["All"] + data_access_logs["accessType"].unique().tolist()
    selected_access_type = st.selectbox("Filter by Access Type:", access_types)
    
    # Apply filter
    if selected_access_type != "All":
        filtered_logs = data_access_logs[data_access_logs["accessType"] == selected_access_type]
    else:
        filtered_logs = data_access_logs
    
    # Show data
    st.dataframe(filtered_logs, use_container_width=True)
    
    # Visualization of data access by type
    if not data_access_logs.empty:
        access_counts = data_access_logs["accessType"].value_counts()
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.pie(access_counts, labels=access_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        ax.set_title("Data Access by Type")
        st.pyplot(fig)
else:
    st.info("No data access logs available.")

if st.button('Back to Admin Home', use_container_width=True):
    st.switch_page('pages/30_Administrator_Home.py')