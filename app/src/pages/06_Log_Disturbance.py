import logging
logger = logging.getLogger(__name__)

import streamlit as st
import requests
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

st.title("Complaints")

complaints = requests.get(f"http://api:4000/s/{st.session_state['id']}/complaints").json()
for complaint in complaints:

    st.text(complaint["description"])
    if st.button("Remove", key=complaint["compId"]):
        try:
            res = requests.delete(
                f"http://api:4000/s/{st.session_state['id']}/complaints",
                json={"id": complaint["compId"]}
            )
            if res.status_code == 201:
                st.success("Complaint submitted successfully.")
            else:
                st.error("Failed to submit complaint.")
                st.write(res.text)
        except Exception as e:
            st.error(f"Error: {e}")

st.text("🚨 Report a new Complaint")
description = st.text_area("Describe the disturbance")
submit = st.button("Submit")

if submit and description:
    try:
        res = requests.post(
            f"http://api:4000/s/{st.session_state['id']}/complaints",
            json={"description": description}
        )
        if res.status_code == 201:
            st.success("Complaint submitted successfully.")
        else:
            st.error("Failed to submit complaint.")
            st.write(res.text)
    except Exception as e:
        st.error(f"Error: {e}")
