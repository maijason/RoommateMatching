import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()
st.title('Complaints')

# get complaints
complaints = requests.get(f'http://api:4000/ra/complaints/{st.session_state["id"]}').json()


st.dataframe(complaints)

st.header('Conflicts')

# get events
events = requests.get(f'http://api:4000/ra/conflicts/{st.session_state["id"]}').json()
st.dataframe(events)




  