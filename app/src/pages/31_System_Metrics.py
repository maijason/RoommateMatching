import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

logger.info("Loading System Metrics page")

st.set_page_config(layout='wide', page_title='RoommateMatching - System Metrics')

SideBarLinks()

st.title("System Metrics Dashboard")

st.write("""
# System Performance Monitoring

This dashboard provides an overview of system performance metrics, alerts, and suspicious activity 
for the Roomies4Life platform.
""")

st.sidebar.header('System Filter Options')

def filter_options():
    time_period = st.sidebar.selectbox('Time Period', 
                                      ['Last 24 Hours', 'Last Week', 'Last Month', 'All Time'])
    alert_level = st.sidebar.selectbox('Alert Level', 
                                      ['All', 'Critical', 'Warning', 'Information'])
    show_resolved = st.sidebar.checkbox('Show Resolved Issues', value=False)
    
    filters = {
        'time_period': time_period,
        'alert_level': alert_level,
        'show_resolved': show_resolved
    }
    return filters

filters = filter_options()

st.subheader('System Overview')
metrics_data = {
    "Metric": ["Uptime", "Active Users", "Response Time"],
    "Value": ["99.9%", "100", "120ms"]
}
metrics_df = pd.DataFrame(metrics_data)
st.dataframe(metrics_df)

st.subheader('Current Alerts')
alerts_data = {
    "Alert Type": ["Backup Warning", "Updates"],
    "Message": ["Last backup was over 48h ago", "Security patch ready"],
    "Severity": ["Warning", "Information"]
}
alerts_df = pd.DataFrame(alerts_data)
st.dataframe(alerts_df)

st.subheader('Alert Resolution')
form1 = st.form(key="resolve_alert_form")
alert_to_resolve = form1.selectbox("Select Alert to Resolve", ["Backup Warning", "Updates"])
resolution_action = form1.text_area("Resolution Action", height=100, 
                                   value="Describe the action taken to resolve this alert...")
resolved = form1.form_submit_button("Mark as Resolved")

if resolved:
    st.success(f"Alert '{alert_to_resolve}' marked as resolved with action: '{resolution_action}'")

st.subheader('Suspicious Activity')
suspicious_data = {
    "Timestamp": ["2025-03-25 20:10:44", "2025-03-25 19:58:10"],
    "IP address": ["192.168.1.45", "10.24.55.82"],
    "Activity": ["Failed Login Attempt", "Unusual Data Access"],
    "Status": ["Flagged", "Blocked"]
}
suspicious_df = pd.DataFrame(suspicious_data)
st.dataframe(suspicious_df)

st.subheader('Handle Suspicious Activity')
form2 = st.form(key="suspicious_activity_form")
activity_to_handle = form2.selectbox("Select Activity to Handle", 
                                   ["Failed Login Attempt (192.168.1.45)", "Unusual Data Access (10.24.55.82)"])
action = form2.selectbox("Action", ["Ignore", "Block IP", "Investigate", "Reset User Account"])
notes = form2.text_area("Notes", height=100, 
                       value="Add notes about this suspicious activity...")
handled = form2.form_submit_button("Submit Action")

if handled:
    st.success(f"Action '{action}' taken for activity: '{activity_to_handle}'")

st.subheader('Resource Usage')
usage_data = {
    "Module": ["Student Portal", "RA Portal", "Housing Admin", "System Admin", "Matching Algorithm"],
    "Usage (%)": [45, 30, 15, 5, 5]
}
usage_df = pd.DataFrame(usage_data)
st.dataframe(usage_df)

st.subheader('Database Performance')
db_data = {
    "Metric": ["Average query response time", "Database size", "Connections"],
    "Value": ["35ms", "1.2 GB", "42 active / 100 maximum"]
}
db_df = pd.DataFrame(db_data)
st.dataframe(db_df)

if st.button('Back to Admin Home', use_container_width=True):
    st.switch_page('pages/30_Administrator_Home.py')