from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

# Create a Blueprint for system admin-related routes
system_admin = Blueprint('system_admin', __name__)

# Get all user roles and permissions
@system_admin.route('/users/roles', methods=['GET'])
def get_user_roles():
    query = '''
        SELECT cl.userId, cl.role, cl.clearance
        FROM clearanceLevels cl
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Update a user's role and permissions
@system_admin.route('/user/role', methods=['PUT'])
def update_user_role():
    the_data = request.json
    current_app.logger.info(the_data)
    
    userId = the_data['userId']
    role = the_data['role']
    clearance = the_data['clearance']
    
    query = f'''
        UPDATE clearanceLevels
        SET role = '{role}',
            clearance = {str(clearance)}
        WHERE userId = {str(userId)}
    '''
    
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully updated user role")
    response.status_code = 200
    return response

# Get system usage statistics
@system_admin.route('/system/stats', methods=['GET'])
def get_system_stats():
    query = '''
        SELECT 
            (SELECT COUNT(*) FROM student) as total_students,
            (SELECT COUNT(*) FROM RA) as total_RAs,
            (SELECT COUNT(*) FROM housingAdmin) as total_admins,
            (SELECT COUNT(*) FROM events) as total_events,
            (SELECT COUNT(*) FROM complaints) as total_complaints,
            (SELECT COUNT(*) FROM conflicts) as total_conflicts
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Add a new staff user
@system_admin.route('/staff', methods=['POST'])
def add_staff_user():
    the_data = request.json
    current_app.logger.info(the_data)
    
    firstName = the_data['firstName']
    lastName = the_data['lastName']
    adminId = the_data['adminId']
    role = the_data['role']
    clearance = the_data['clearance']
    
    query = f'''
        INSERT INTO systemAdmin (firstName, lastName, adminId)
        VALUES ('{firstName}', '{lastName}', {str(adminId)});
        
        INSERT INTO clearanceLevels (userId, role, clearance)
        VALUES ({str(adminId)}, '{role}', {str(clearance)});
    '''
    
    current_app.logger.info(query)
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()
    
    response = make_response("Successfully added staff user")
    response.status_code = 200
    return response

# Get suspicious login activity
@system_admin.route('/security/login-attempts', methods=['GET'])
def get_suspicious_logins():
    query = '''
        SELECT userId, COUNT(*) as failed_attempts, MAX(timestamp) as last_attempt
        FROM login_attempts
        WHERE success = 0
        GROUP BY userId
        HAVING COUNT(*) > 3
        ORDER BY failed_attempts DESC
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

# Get audit log of sensitive data access
@system_admin.route('/audit/data-access', methods=['GET'])
def get_data_access_log():
    query = '''
        SELECT 
            userId, 
            dataResource, 
            accessType, 
            timestamp,
            ipAddress
        FROM data_access_log
        ORDER BY timestamp DESC
        LIMIT 100
    '''
    
    cursor = db.get_db().cursor()
    cursor.execute(query)
    theData = cursor.fetchall()
    
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response