import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.title(f'RA Dashboard')

st.header('My Students')

# get students
residents = requests.get(f'http://api:4000/ra/residents/{st.session_state["id"]}').json()
# st.dataframe(residents)
st.dataframe(residents)






  