import streamlit as st
import requests
from datetime import time

st.set_page_config(page_title="Roommate Preferences Survey", layout="centered")
st.title("Roommate Preferences Survey")

with st.form("preferences_form"):
    st.write("Input dorm preferences:")

    sleep_time = st.time_input("Preferred bedtime:", value=time(23, 0))
    cleanliness = st.number_input("Preferred cleanliness on a scale from 1 (messy) to 5 (very clean)", min_value=1, max_value=5, step=1)
    smoking = st.radio("I would prefer to live with someone who does not smoke", ["No", "Yes"])
    extra_observations = st.text_area("Please write here any extra observations")

    submitted = st.form_submit_button("Submit Preferences")

    if submitted:
        data = {
            "sleepTime": sleep_time.strftime("%H:%M"),
            "cleanliness": cleanliness,
            "smoking": 1 if smoking == "No" else 0,
            "extra_observations": extra_observations
        }

        try:
            response = requests.post("http://localhost:4000/students/<id>/preferences", json=data)
            if response.status_code == 200:
                st.success("Preferences submitted successfully!")
            else:
                st.error("Failed to submit preferences.")
        except requests.exceptions.RequestException:
            st.error("An exception occurred")
