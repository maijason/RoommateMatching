import streamlit as st
import requests

st.set_page_config(page_title="Dorm Building Viewer", layout="centered")
st.title("Dorm Building Viewer")

try:
    response = requests.get("http://localhost:4000/dorms")
    response.raise_for_status()
    dorms = response.json()

    if dorms:
        st.write("Available dorm buildings:")

        for dorm in dorms:
            with st.container():
                st.subheader(dorm["name"])
                st.write(f"Address: {dorm['address']}")
                st.write(f"Capacity: {dorm['maxCapacity']}")
                st.write(f"Room occupancy: {dorm['occupancy']}")
                st.write(f"Amenities: {dorm['amenities']}")
                st.markdown("---")
    else:
        st.info("No dorms found")

except requests.exceptions.RequestException:
    st.error("An exception occurred")