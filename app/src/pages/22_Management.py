import streamlit as st
from modules.nav import SideBarLinks
import requests
import logging
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()
Faker.seed(123)

st.set_page_config(layout='wide')
SideBarLinks()

st.title('Manage Dorm Capacity and Availability')

def generate_fake_dorm_data(num_dorms=3):
    dorm_names = ["Speare", "IV", "White Hall", "East Village", "West Village", "International Village"]
    data = []
    for i in range(min(num_dorms, len(dorm_names))):
        capacity = fake.random_int(min=50, max=200)
        occupied = fake.random_int(min=0, max=capacity)
        data.append({
            "dormId": i + 1,
            "Dorm Name": dorm_names[i],
            "Capacity": capacity,
            "Occupied": occupied,
            "Available": capacity - occupied
        })
    return data

if 'dorm_data' not in st.session_state:
    try:
        response = requests.get("http://api:5000/dorms")
        if response.status_code == 200:
            st.session_state.dorm_data = response.json()
        else:
            logger.warning(f"Failed to fetch real data: {response.status_code}. Using generated data.")
            st.session_state.dorm_data = generate_fake_dorm_data()
    except Exception as e:
        logger.error(f"API error: {str(e)}. Using generated data.")
        st.session_state.dorm_data = generate_fake_dorm_data()

st.write("")
st.table(st.session_state.dorm_data)

