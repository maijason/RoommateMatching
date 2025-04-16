import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

logger.info("Loading Housing Admin home page")

st.set_page_config(layout='wide', page_title='RoommateMatching - Housing Admin')

SideBarLinks()

st.title(f"Welcome Housing Admin, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Analytics Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Analytics_Dashboard.py')

if st.button('View Management Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Management.py')