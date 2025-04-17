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
    try:
        cursor = db.get_db().cursor()
        cursor.execute('SELECT * FROM housingAdmin')
        
        theData = cursor.fetchall()
        
        the_response = make_response(jsonify(theData))
        the_response.status_code = 200
        return the_response
    except Exception as e:
        current_app.logger.error(f"Error fetching housing admins: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

# Get all dorms with capacity and availability
@housing_admin.route('/dorms/capacity', methods=['GET'])
def get_dorm_capacity():
    try:
        query = '''
            SELECT 
                dormId, 
                dormName, 
                numRooms, 
                maxCapacity,
                occupied,
                maxCapacity - occupied as available
            FROM dormBuilding
            ORDER BY dormName
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    except Exception as e:
        current_app.logger.error(f"Error fetching dorm capacity: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

# Update dorm capacity
@housing_admin.route('/dorm/capacity', methods=['PUT'])
def update_dorm_capacity():
    try:
        the_data = request.json
        current_app.logger.info(the_data)
        
        dormId = the_data['dormId']
        maxCapacity = the_data['maxCapacity']
        
        query = 'UPDATE dormBuilding SET maxCapacity = %s WHERE dormId = %s'
        
        cursor = db.get_db().cursor()
        cursor.execute(query, (maxCapacity, dormId))
        db.get_db().commit()
        
        response = make_response(jsonify({"message": "Successfully updated dorm capacity"}))
        response.status_code = 200
        return response
    except Exception as e:
        db.get_db().rollback()
        current_app.logger.error(f"Error updating dorm capacity: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

# Get conflicts by dorm (for heatmap)
@housing_admin.route('/conflicts/by-dorm', methods=['GET'])
def get_conflicts_by_dorm():
    try:
        query = '''
            SELECT 
                dormId,
                dormName,
                conflict_count
            FROM dormBuilding_conflicts
            ORDER BY conflict_count DESC
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    except Exception as e:
        current_app.logger.error(f"Error fetching conflicts by dorm: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

# Get conflicts over time
@housing_admin.route('/conflicts/over-time', methods=['GET'])
def get_conflicts_over_time():
    try:
        query = '''
            SELECT 
                month,
                conflict_count
            FROM conflicts_by_month
            ORDER BY month
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    except Exception as e:
        current_app.logger.error(f"Error fetching conflicts over time: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)

# Get roommate match success rates
@housing_admin.route('/match-success', methods=['GET'])
def get_match_success():
    try:
        query = '''
            SELECT
                match_category,
                room_count
            FROM roommate_match_success
        '''
        
        cursor = db.get_db().cursor()
        cursor.execute(query)
        theData = cursor.fetchall()
        
        response = make_response(jsonify(theData))
        response.status_code = 200
        return response
    except Exception as e:
        current_app.logger.error(f"Error fetching match success rates: {str(e)}")
        return make_response(jsonify({"error": str(e)}), 500)