import streamlit as st
import requests
from datetime import time

st.set_page_config(page_title="Roommate Preferences Survey", layout="centered")
st.title("Roommate Preferences Survey")

student_id = st.session_state.get("id", 1)

existing_preferences = None
try:
    response = requests.get(f"http://api:4000/s/students/{student_id}/preferences")
    if response.status_code == 200:
        data = response.json()
        if data:
            existing_preferences = data[0]
except requests.exceptions.RequestException as e:
    st.error(f"Error retrieving preferences: {e}")

with st.form("preferences_form"):
    st.write("Input your roommate preferences:")

    default_sleep_time = existing_preferences.get('sleepTime', 23) if existing_preferences else 23
    sleep_time = st.number_input(
        "Preferred bedtime (24-hour format):", 
        min_value=0, 
        max_value=24, 
        value=default_sleep_time
    )
    
    cleanliness = st.number_input("Preferred cleanliness on a scale from 1 (messy) to 5 (very clean)", min_value=1, max_value=5, step=1)
    smoking = st.radio("I would prefer to live with someone who does not smoke", ["No", "Yes"])
    extra_observations = st.text_area("Please write here any extra observations")

    submitted = st.form_submit_button("Submit Preferences")

    if submitted:
        data = {
            "sleepTime": sleep_time,
            "cleanliness": cleanliness,
            "smoking": 1 if smoking == "Yes" else 0,
            "extra_observations": extra_observations
        }

        try:
            response = requests.post(f"http://api:4000/s/students/{student_id}/preferences", json=data)
            if response.status_code == 200:
                st.success("Preferences submitted successfully!")

                if st.button("View Potential Roommate Matches"):
                    st.switch_page("pages/05_Roommate_Matching.py")
            else:
                st.error("Failed to submit preferences.")
        except requests.exceptions.RequestException:
            st.error("An exception occurred")
