import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd

logger.info("Loading RA Calendar")

st.set_page_config(layout='wide', page_title='RoommateMatching - RA Calendar')
SideBarLinks()

st.title("📅 RA Calendar")

with st.form("new_event"):
    st.write("➕ Create New Event")
    title = st.text_input("Title")
    location = st.text_input("Location")
    date = st.date_input("Date")
    time = st.time_input("Time")
    submit = st.form_submit_button("Add")

    if submit:
        from datetime import datetime
        full_datetime = datetime.combine(date, time)

        try:
            res = requests.post("http://api:4000/events/add", json={
                "title": title,
                "location": location,
                "datetime": str(full_datetime),
                "raId": st.session_state['id']
            })
            if res.status_code == 201:
                st.success("Event added.")
            else:
                st.error(res.text)
                
        except:
            st.error("Could not add event.")


# Get event data
try:
    response = requests.get(f"http://api:4000/events/upcoming/{st.session_state['id']}")
    response.raise_for_status()
    events = pd.DataFrame(response.json())
except Exception as e:
    st.error("Could not load events.")
    events = pd.DataFrame(columns=["datetime", "title", "location"])

# Show each event with delete button
if not events.empty:
    for _, event in events.iterrows():
        st.write(f"**{event['datetime']} - {event['title']}**")
        with st.form(f"📍 {event['location']} - {event['datetime']}"):
            st.write("Change Location")
            location = st.text_input("Location", value=event['location'])
            if st.form_submit_button("Change"):
                try:
                    res = requests.put("http://api:4000/events", json={
                        "title": title,
                        "location": location,
                        "datetime": str(full_datetime),
                        "raId": st.session_state['id']
                    })
                    if res.status_code == 201:
                        st.success("Event added.")
                except:
                    st.error("Could not add event.")

        if st.button("🗑️ Delete", key=f"{event['datetime']}-{event['title']}"):
            try:
                res = requests.delete("http://api:4000/events", json={
                    "datetime": str(pd.to_datetime(event["datetime"])),
                    "title": event["title"]
                })
                if res.status_code == 200:
                    st.success("Event deleted.")
                else:
                    st.error("Failed to delete event.")
            except Exception as e:
                st.error("Error deleting event.")
        st.markdown("---")
else:
    st.info("No upcoming events found.")
