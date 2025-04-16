########################################################
# Housing Admin blueprint of endpoints
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.
housing_admin = Blueprint('housing_admin', __name__)

#------------------------------------------------------------
# Get all housing admins from the system
@housing_admin.route('/admins', methods=['GET'])
def get_housing_admins():
    cursor = db.get_db().cursor()
    cursor.execute('''
                    select * from housingAdmin
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


# Update dorm availability
@housing_admin.route('/dorms/<int:dorm_id>/availability', methods=['PUT'])
def update_dorm_availability(dorm_id):
    data = request.get_json()
    capacity = data.get('capacity')
    
    cursor = db.get_db().cursor()
    cursor.execute('''
                    UPDATE dormBuilding
                    SET capacity = %s
                    WHERE dormId = %s
    ''', (capacity, dorm_id))
    
    db.get_db().commit()
    
    the_response = make_response(jsonify({"message": "Dorm availability updated successfully"}))
    the_response.status_code = 200
    return the_response 