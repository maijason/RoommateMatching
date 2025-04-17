import logging
logger = logging.getLogger(__name__)
import streamlit as st
import requests
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks


SideBarLinks()

st.write("# View All Dorms")

try:
    response = requests.get('http://api:4000/s/dorms')
    response.raise_for_status()  # This will raise an exception for HTTP errors
    dorms = response.json()
    st.dataframe(dorms)
except requests.exceptions.RequestException as e:
    st.error(f"Could not connect to the API: {str(e)}")
except ValueError as e:
    st.error(f"Error parsing response: {str(e)}")
except Exception as e:
    st.error(f"An unexpected error occurred: {str(e)}")


