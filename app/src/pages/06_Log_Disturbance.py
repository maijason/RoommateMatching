import streamlit as st
import requests

st.set_page_config(layout="wide")
st.title("🚨 Report a Disturbance")

description = st.text_area("Describe the disturbance")
submit = st.button("Submit")

if submit and description:
    try:
        res = requests.post(
            f"http://localhost:4000/students/{st.session_state['id']}/complaints",
            json={"description": description}
        )
        if res.status_code == 201:
            st.success("Complaint submitted successfully.")
        else:
            st.error("Failed to submit complaint.")
            st.write(res.text)
    except Exception as e:
        st.error(f"Error: {e}")
