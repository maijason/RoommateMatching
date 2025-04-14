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
# Get all students from the system
@students.route('/students', methods=['GET'])
def get_students():

    cursor = db.get_db().cursor()
    cursor.execute('''
                   select * from student
    ''')
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get student preferences
@students.route('/students/<id>/preferences', methods=['GET'])
def get_student_preferences(id):
    current_app.logger.info(f'GET /students/{id}/preferences route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM preferences WHERE stuId = %s', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response

# Get student complaints
@students.route('/students/<id>/complaints', methods=['GET'])
def get_student_complaints(id):
    current_app.logger.info(f'GET /students/{id}/complaints route')
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM complaints WHERE stuId = %s', (id,))
    
    theData = cursor.fetchall()
    
    the_response = make_response(jsonify(theData))
    the_response.status_code = 200
    return the_response