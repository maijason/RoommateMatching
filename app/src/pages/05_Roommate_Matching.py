import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from modules.nav import SideBarLinks

import pandas as pd

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

# get potential roommate matches 
try:
    response = requests.get(f'http://api:4000/d/roommates?student_id={student_id}')
    if response.status_code == 200:
        matches = response.json()
        
        if matches:
            formatted_matches = []
            for match in matches:
                formatted_matches.append({
                    "Name": f"{match['firstName']} {match['lastName']}",
                    "Sleep Time": f"{match.get('sleepTime', 'Unknown')}:00",
                    "Smoking": "Yes" if match.get('smoking', 0) else "No",
                    "Match Score": match['match_score'],
                    "Notes": match.get('extra_observations', 'No additional notes')
                })
            
            st.subheader("Your Potential Matches")
            
            df = pd.DataFrame(formatted_matches)
            
            def highlight_matches(s):
                if s.name == 'Match Score':
                    return ['background-color: #8eff8e' if v >= 5 else 
                            'background-color: #d6ffb6' if v >= 3 else 
                            'background-color: #ffe0b6' if v >= 1 else 
                            'background-color: #ffb6b6' for v in s]
                return [''] * len(s)
            
            st.dataframe(df.style.apply(highlight_matches), use_container_width=True)
            
            # Add a way to contact potential roommates - but still in process 
            # not sure if this will fully be implemented but its an idea so its the start of its implementation
            st.subheader("Contact a Potential Roommate")
            selected_roommate = st.selectbox(
                "Select a roommate to contact:",
                [f"{match['firstName']} {match['lastName']}" for match in matches]
            )
            
            if st.button("Send Contact Request"):
                st.success(f"Contact request sent to {selected_roommate}! They will receive your contact information.")
        else:
            st.info("No potential roommate matches found at this time.")
    else:
        st.error(f"Failed to retrieve matches: {response.status_code}")
except requests.exceptions.RequestException as e:
    st.error(f"Error retrieving matches: {e}")
