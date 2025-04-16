import logging
logger = logging.getLogger(__name__)

import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks

logger.info("Loading Permissions Dashboard page")

st.set_page_config(layout='wide', page_title='RoommateMatching - Permissions Dashboard')

SideBarLinks()

st.title("Roles and Permissions Dashboard")
st.write("Manage user access and security settings across the Roomies4Life platform")

def get_user_roles():
    data = [
        {"User": "Sam", "Role": "System Admin", "Permissions": "*"},
        {"User": "Bill", "Role": "Housing Admin", "Permissions": "Manages RA and dorms"},
        {"User": "Jane", "Role": "Housing Admin", "Permissions": "Manages RA and dorms"},
        {"User": "Renee", "Role": "RA", "Permissions": "Manages students and events"}
    ]
    return pd.DataFrame(data)

st.subheader("Current User Roles")
roles_df = get_user_roles()
st.dataframe(roles_df, use_container_width=True)

st.subheader("Modify User Role")
st.form_submit_button = st.form("role_form")

username = st.selectbox("Select User", ["Sam", "Bill", "Jane", "Renee", "Alex", "Maria"])
role = st.selectbox("Assign Role", ["System Admin", "Housing Admin", "RA", "Student"])

permissions = ""
if role == "System Admin":
    permissions = "*"
elif role == "Housing Admin":
    permissions = "Manages RA and dorms"
elif role == "RA":
    permissions = "Manages students and events"
else:
    permissions = "Basic user access"

st.write(f"Permissions that will be assigned: **{permissions}**")

submitted = st.form_submit_button("Update Role")
if submitted:
    st.success(f"Updated {username}'s role to {role} with permissions: {permissions}")

st.subheader("Add New User")
new_user_form = st.form("new_user_form")

new_username = st.text_input("Username")
new_email = st.text_input("Email")
new_role = st.selectbox(
    "Role", 
    ["System Admin", "Housing Admin", "RA", "Student"],
    key="new_role"
)

new_permissions = ""
if new_role == "System Admin":
    new_permissions = "*"
elif new_role == "Housing Admin":
    new_permissions = "Manages RA and dorms"
elif new_role == "RA":
    new_permissions = "Manages students and events"
else:
    new_permissions = "Basic user access"

st.write(f"Permissions that will be assigned: **{new_permissions}**")

add_submitted = st.form_submit_button("Add User")
if add_submitted:
    if new_username and new_email:
        st.success(f"Added new user {new_username} with role {new_role}")
    else:
        st.error("Username and email are required")

st.subheader("Recent Permission Changes")
changes_data = [
    {"Timestamp": "2025-04-15 10:23:45", "Changed By": "Sam", "User": "Maria", "Action": "Changed role from Student to RA"},
    {"Timestamp": "2025-04-14 16:42:31", "Changed By": "Sam", "User": "Alex", "Action": "Added new user with Housing Admin role"}
]
changes_df = pd.DataFrame(changes_data)
st.dataframe(changes_df, use_container_width=True)

if st.button('Back to Admin Home', use_container_width=True):
    st.switch_page('pages/30_System_Admin_Home.py')