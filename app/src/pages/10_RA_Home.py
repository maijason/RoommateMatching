import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome RA, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Open Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_RA_Dashboard.py')

if st.button('View Calendar', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Calendar.py')
