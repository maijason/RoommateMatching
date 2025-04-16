import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

# Show sidebar links based on the student role
SideBarLinks()

# Use session state to greet the logged-in student
first_name = st.session_state.get('first_name', 'Student')

st.title(f"👋 Welcome back, {first_name}!")
st.write("")
st.write("### What would you like to do today?")

# Navigation buttons
if st.button("📝 Fill Out Preferences", type="primary", use_container_width=True):
    st.switch_page("pages/10_User_Preferences.py")

if st.button("📅 View Upcoming Events", type="primary", use_container_width=True):
    st.switch_page("pages/05_Upcoming_Events.py")

if st.button("🚨 Report a Disturbance", type="primary", use_container_width=True):
    st.switch_page("pages/06_Log_Disturbance.py")

if st.button("🏘️ View All Dorms", type="primary", use_container_width=True):
    st.switch_page("pages/04_View_All_Dorms.py")