import logging
logger = logging.getLogger(__name__)


import streamlit as st
from modules.nav import SideBarLinks
import requests
import pandas as pd


st.set_page_config(layout='wide')
SideBarLinks()


st.title("🏘️ Manage Dorm Capacity and Availability")
st.write("Below is the current capacity and occupancy of all dorms:")


# --- GET dorm data from backend ---
try:
   response = requests.get("http://localhost:5000/dorms")  # Adjust port/URL as needed


   if response.status_code == 200:
       data = response.json()
       df = pd.DataFrame(data)


       # Add available column
       df["Available"] = df["maxCapacity"] - df["occupancy"]


       # Rename columns for display
       df = df.rename(columns={
           "address": "Dorm Name",
           "maxCapacity": "Capacity",
           "occupancy": "Occupied"
       })


       st.dataframe(df[["Dorm Name", "Capacity", "Occupied", "Available"]])


   else:
       st.error("Failed to load dorm data from server.")


except Exception as e:
   logger.error(f"Error fetching dorm data: {e}")
   st.error("An error occurred while loading dorm data.")
   