import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

logger.info("Loading Roommate Matching page")

st.set_page_config(layout='wide', page_title='RoommateMatching - Find Roommates')

SideBarLinks()

st.write("# Roommate Matching")

st.markdown(
    """
    This page displays potential roommate matches based on your preferences.
    Matches are scored on a scale from 0-6, with 6 being the best possible match.
    """
)

student_id = st.session_state.get("id", 1)

# if the student has set preferences
has_preferences = False
try:
    pref_response = requests.get(f'http://api:4000/s/students/{student_id}/preferences')
    if pref_response.status_code == 200:
        preferences = pref_response.json()
        if preferences:
            has_preferences = True
            st.success(f"Matching based on your preferences: Sleep time: {preferences[0]['sleepTime']}:00, Smoking: {'Yes' if preferences[0]['smoking'] else 'No'}")
except requests.exceptions.RequestException as e:
    st.error(f"Error checking preferences: {e}")

if not has_preferences:
    st.warning("You haven't set your preferences yet. Please fill out the survey form first for better matches.")
    if st.button("Go to Survey Form"):
        st.switch_page("pages/01_Survey_Form.py")
