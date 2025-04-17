# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has functions to add role-specific sidebar links to the app

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")

def AboutPageNav():
    st.sidebar.page_link("pages/40_About.py", label="About", icon="🧠")

#### ------------------------ Student Role ------------------------
def StudentNav():
    st.sidebar.page_link("pages/00_Student_Home.py", label="Home", icon="🏠")
    st.sidebar.page_link("pages/01_Survey_Form.py", label="Fill Out Preferences", icon="📝")
    st.sidebar.page_link("pages/04_View_All_Dorms.py", label="View Dorms", icon="🏘️")
    st.sidebar.page_link("pages/06_Log_Disturbance.py", label="Report a Disturbance", icon="🚨")

#### ------------------------ RA Role ------------------------
def RADashboardNav():
    st.sidebar.page_link("pages/11_RA_Dashboard.py", label="Dashboard", icon="🛜")

def EventOrganizerNav():
    st.sidebar.page_link("pages/12_RA_Calendar.py", label="Calendar", icon="📈")

#### ------------------------ HA Role ------------------------
def AnalyticsNav():
    st.sidebar.page_link("pages/21_Analytics.py", label="Analytics", icon="🌺")

def ManagementDashboardNav():
    st.sidebar.page_link("pages/22_Management.py", label="Management", icon="📊")

#### ------------------------ System Admin Role ------------------------
def SystemMetricsNav():
    st.sidebar.page_link("pages/31_System_Metrics.py", label="Metrics", icon="🖥️")

def PermissionsDashboard():
    st.sidebar.page_link("pages/32_Permissions_Dashboard.py", label="Permissions", icon="🏢")

#### ------------------------ Main Sidebar Function ------------------------
def SideBarLinks(show_home=False):
    """
    Adds navigation links to the sidebar based on the user's role.
    """
    st.sidebar.image("assets/logo.png", width=150)

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        HomeNav()

    if st.session_state["authenticated"]:
        role = st.session_state.get("role", "")
        
        if role == "student":
            StudentNav()
        elif role == "ra":
            RADashboardNav()
            EventOrganizerNav()
        elif role == "ha":
            AnalyticsNav()
            ManagementDashboardNav()
        elif role == "administrator":
            SystemMetricsNav()
            PermissionsDashboard()

    AboutPageNav()

    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
