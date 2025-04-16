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
    """
)

response = requests.get('http://api:4000/d/roommates')
response.raise_for_status()  # This will raise an exception for HTTP errors
roommates = response.json()
    
st.dataframe(roommates)