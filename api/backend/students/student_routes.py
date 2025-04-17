########################################################
# Sample student blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################
from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db
from backend.ml_models.model01 import predict

#------------------------------------------------------------
# Create a new Blueprint object, which is a collection of 
# routes.4
students = Blueprint('students', __name__)

#------------------------------------------------------------


# Get student preferences
@students.route('/<id>/preferences', methods=['GET'])
def get_student_preferences(id):
    current_app.logger.info(f'GET /students/{id}/preferences route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM preferences WHERE stuId = %s', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


@students.route('/<id>/preferences', methods=['POST'])
def add_preferences(id):
    # Collect data from the request body
    the_data = request.json
    current_app.logger.info(the_data)


    # Build the SQL query using string interpolation 
    query = f'''
        

        INSERT INTO preferences 
        VALUES ({id}, {the_data['sleepTime']}, '{the_data['extra_observations']}', {"true" if the_data['smoking'] == 1 else "false" });
    '''

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(f"DELETE FROM preferences WHERE stuId = {id};")
    db.get_db().commit()


    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    # Send response
    response = make_response("preferences submitted successfully!")
    response.status_code = 200
    return response




# Get student complaints
@students.route('/<id>/complaints', methods=['GET'])
def get_student_complaints(id):
    current_app.logger.info(f'GET /students/{id}/complaints route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM complaints WHERE stuId = %s', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response



@students.route('/<id>/complaints', methods=['DELETE'])
def delete_complaint(id):
    # Collect data from the request body
    the_data = request.json
    current_app.logger.info(the_data)

    cursor = db.get_db().cursor()
    cursor.execute(f"DELETE FROM RABridgeComplaints WHERE compId = {the_data['id']};")
    db.get_db().commit()
    
    cursor = db.get_db().cursor()
    cursor.execute(f"DELETE FROM complaints WHERE compId = {the_data['id']};")
    db.get_db().commit()

    # Send response
    response = make_response("complaints submitted successfully!")
    response.status_code = 201
    return response

@students.route('/<id>/complaints', methods=['POST'])
def add_complaint(id):
    # Collect data from the request body
    the_data = request.json
    current_app.logger.info(the_data)


    # Build the SQL query using string interpolation 
    query = f'''
        INSERT INTO complaints (stuId, description)
        VALUES ({id}, '{the_data['description']}')
    '''

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    # Send response
    response = make_response("complaints submitted successfully!")
    response.status_code = 201
    return response

@dorms.route('/dorms', methods=['GET'])
def get_dorms():

    cursor = db.get_db().cursor()
    cursor.execute('''
                    select * from dormBuilding
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response


