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

st.button('Select Dorm', type='secondary', key='select_dorm_btn')
st.button('Floor Filter', type='secondary', key='floor_filter_btn')


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
            "Available": capacity - occupied,
            "Edit": "Edit"
        })
    return data

try:
    response = requests.get("http://api:5000/dorms")
    if response.status_code == 200:
        dorm_data = response.json()
        for dorm in dorm_data:
            dorm["Edit"] = "Edit"
    else:
        logger.warning(f"Failed to fetch real data: {response.status_code}. Using generated data.")
        dorm_data = generate_fake_dorm_data()
except Exception as e:
    logger.error(f"API error: {str(e)}. Using generated data.")
    dorm_data = generate_fake_dorm_data()

st.write("")
st.table(dorm_data)

st.write("\n\n")
st.write("## Update Dorm Capacity")

dorm_names = [dorm["Dorm Name"] for dorm in dorm_data]

selected_dorm = st.selectbox(
    "Select dorm to update",
    options=dorm_names
)

current_capacity = next(
    (item["Capacity"] for item in dorm_data if item["Dorm Name"] == selected_dorm), 0
)

selected_dorm_id = next(
    (item.get("dormId", i + 1) for i, item in enumerate(dorm_data) if item["Dorm Name"] == selected_dorm), 1
)

new_capacity = st.number_input("New Capacity", min_value=0, value=current_capacity)

# update button
if st.button('Update Capacity', type='primary', use_container_width=True):
    try:
        response = requests.put(
            f"http://api:5000/dorms/{selected_dorm_id}/availability",
            json={"capacity": new_capacity}
        )

        if response.status_code == 200:
            st.success(f"Successfully updated capacity for {selected_dorm} to {new_capacity}")
            st.experimental_rerun()
        else:
            st.error(f"Failed to update capacity: {response.status_code} - {response.text}")

    except Exception as e:
        logger.error(f"Error updating capacity: {str(e)}")
        st.error(f"An error occurred while updating capacity.")

st.write("\n\n")
if st.button('Return to Dashboard', type='primary'):
    st.switch_page('pages/20_HA_Home.py')
