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

st.write("\n\n")
st.write("## Update Dorm Information")

dorm_names = [dorm["Dorm Name"] for dorm in st.session_state.dorm_data]

selected_dorm = st.selectbox(
    "Select dorm to update",
    options=dorm_names
)

current_dorm = next((item for item in st.session_state.dorm_data if item["Dorm Name"] == selected_dorm), None)
current_capacity = current_dorm["Capacity"] if current_dorm else 0
current_occupied = current_dorm["Occupied"] if current_dorm else 0

selected_dorm_id = next(
    (item.get("dormId", i + 1) for i, item in enumerate(st.session_state.dorm_data) if item["Dorm Name"] == selected_dorm), 1
)

new_capacity = st.number_input("Total Capacity", min_value=0, value=current_capacity)
new_occupied = st.number_input("Occupied Rooms", min_value=0, max_value=new_capacity, value=min(current_occupied, new_capacity))

new_available = new_capacity - new_occupied

st.info(f"Available Rooms: {new_available}")

# update button
if st.button('Update Dorm Information', type='primary', use_container_width=True):
    try:
        response = requests.put(
            f"http://api:5000/dorms/{selected_dorm_id}/availability",
            json={"capacity": new_capacity, "occupied": new_occupied}
        )

        if response.status_code == 200:
            for dorm in st.session_state.dorm_data:
                if dorm["Dorm Name"] == selected_dorm:
                    dorm["Capacity"] = new_capacity
                    dorm["Occupied"] = new_occupied
                    dorm["Available"] = new_available
                    break
            
            st.success(f"Successfully updated information for {selected_dorm}:\n- Capacity: {new_capacity}\n- Occupied: {new_occupied}\n- Available: {new_available}")
        else:
            st.error(f"Failed to update dorm information: {response.status_code} - {response.text}")
            
            for dorm in st.session_state.dorm_data:
                if dorm["Dorm Name"] == selected_dorm:
                    dorm["Capacity"] = new_capacity
                    dorm["Occupied"] = new_occupied
                    dorm["Available"] = new_available
                    break
            
            st.warning("API error")

    except Exception as e:
        logger.error(f"Error updating dorm information: {str(e)}")
        st.error(f"An error occurred while updating dorm information.")
        
        for dorm in st.session_state.dorm_data:
            if dorm["Dorm Name"] == selected_dorm:
                dorm["Capacity"] = new_capacity
                dorm["Occupied"] = new_occupied
                dorm["Available"] = new_available
                break
        
        st.warning("API error")
