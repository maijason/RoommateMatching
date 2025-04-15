import streamlit as st
import requests

st.set_page_config(page_title="RA Dashboard", layout="centered")
st.title("Resident Assistant - Assigned Students")

ra_id = st.number_input("Enter your RA ID to see assigned residents", min_value=1, step=1)

if st.button("Load Residents"):
    try:
        response = requests.get(f"http://localhost:4000/residents/{ra_id}")
        response.raise_for_status()
        residents = response.json()

        if residents:
            st.subheader("Assigned Residents:")
            for r in residents:
                st.write(f"{r['name']} | {r['email']}")
        else:
            st.info("No residents found")

    except requests.exceptions.RequestException:
        st.error("An exception occurred")