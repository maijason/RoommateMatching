import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

logger.info("Loading System Admin home page")

st.set_page_config(layout='wide', page_title='RoommateMatching - System Admin')

SideBarLinks()

st.title(f"Welcome System Admin, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View System Metrics', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/31_System_Metrics.py')

if st.button('View Permissions Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/32_Permissions_Dashboard.py')