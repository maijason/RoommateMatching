import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout='wide')

SideBarLinks()

# Get RA name safely
name = st.session_state.get('first_name', 'RA')
st.title(f"Welcome RA, {name}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('📊 Open Dashboard', 
             type='primary', 
             use_container_width=True):
    st.switch_page('pages/11_RA_Dashboard.py')

if st.button("📅 Open RA Calendar", 
             type="primary", 
             use_container_width=True):
    st.switch_page("pages/12_RA_Calendar.py")


