# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/40_About.py", label="About", icon="🧠")


#### ------------------------ Examples for Role of pol_strat_advisor ------------------------
def SurveyFormNav():
    st.sidebar.page_link(
        "pages/01_Survey_Form.py", label="Survey", icon="👤"
    )


def BuildingViewerNav():
    st.sidebar.page_link(
        "pages/02_Building_Viewer.py", label="Building Viewer", icon="🏦"
    )


def StudentDashboardNav():
    st.sidebar.page_link("pages/06_Log_Disturbance.py", label="Complaints", icon="🗺️")


def StudentGetAllDormsNav():
    st.sidebar.page_link("pages/04_View_All_Dorms.py", label="Get All Dorms", icon="🏠")


def RoommateMatchingNav():
    st.sidebar.page_link("pages/05_Roommate_Matching.py", label="Roommate Matching", icon="🤝")


## ------------------------ Examples for Role of usaid_worker ------------------------
def RADashboardNav():
    st.sidebar.page_link("pages/11_RA_Dashboard.py", label="Dashboard", icon="🛜")

def RAComplaintsNav():
    st.sidebar.page_link("pages/13_RA_Complaints.py", label="Complaints", icon="🛜")


def EventOrganizerNav():
    st.sidebar.page_link(
        "pages/12_RA_Calendar.py", label="Calendar", icon="📈"
    )


#### ------------------------ System Admin Role ------------------------

def AnalyticsNav():
    st.sidebar.page_link(
        "pages/21_Analytics.py", label="Analytics", icon="🌺"
    )

    
def ManagementDashboardNav():
    st.sidebar.page_link(
        "pages/22_Management.py", label="Management", icon="🌺"
    )
    
def Management2DashboardNav():
    st.sidebar.page_link(
        "pages/23_Management2.py", label="Edit ", icon="🌺"
    )


#### ------------------------ System Admin Role ------------------------

def SystemMetricsNav():
    st.sidebar.page_link("pages/31_System_Metrics.py", label="Metrics", icon="🖥️")
    
    
def PermissionsDashboard():
    st.sidebar.page_link(
        "pages/32_Permissions_Dashboard.py", label="Permissions", icon="🏢"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state["role"] == "student":
            SurveyFormNav()
            StudentDashboardNav()
            StudentGetAllDormsNav()
            
        # If the user role is usaid worker, show the Api Testing page
        if st.session_state["role"] == "ra":
            RADashboardNav()
            EventOrganizerNav()
            RAComplaintsNav()

        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "ha":
            AnalyticsNav()
            ManagementDashboardNav()
            Management2DashboardNav()


        # If the user is an administrator, give them access to the administrator pages
        if st.session_state["role"] == "administrator":
            SystemMetricsNav()
            PermissionsDashboard()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
