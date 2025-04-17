NAMES: Felipe Vianna, Sunil Williams, Jason Lam, Jason Mai, Emily Quach

Roomies4Life is a web application designed to simplify and improve campus housing for students, Resident Assistants, Housing Admins, and System Administrators. Each user has access to a personalized dashboard that helps them manage relevant tasks — from submitting roommate preferences to addressing community issues.

The app is built with Streamlit for the frontend and Flask for the backend, and uses MySQL for the database to store user, survey, event, and complaint data. We follow a REST API design using Flask blueprints, and use Docker Compose to containerize the backend, frontend, and database services.

Students can fill out preference forms, explore dorms, and report conflicts. RAs can view their residents, manage conflicts, and schedule events. HAs can monitor RA activity and community health trends, while system admins manage permissions and oversee the platform.

To run the app, clone the repo, configure the .env file, and run docker-compose up -d. The codebase is divided into app/ (Streamlit UIs) and api/ (Flask routes), each organized by user roles.

LINK FOR THE VIDEO: https://drive.google.com/file/d/1_dM-tiUm0qopkik8oX963MMSKlOJ-dQy/view?usp=sharing
