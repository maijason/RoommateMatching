########################################################
# Sample dorm blueprint of endpoints
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
# routes.
dorms = Blueprint('dorms', __name__)


#------------------------------------------------------------
# Get all dorms from the system
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


# Get potential roommate matches for a student
@dorms.route('/roommates', methods=['GET'])
def get_potential_roommates():
    student_id = request.args.get('student_id', default=None, type=int)
    
    cursor = db.get_db().cursor()
    
    if student_id:
        cursor.execute('''
            SELECT sleepTime, smoking FROM preferences WHERE stuId = %s
        ''', (student_id,))
        
        student_pref = cursor.fetchone()
        
        if student_pref:
            cursor.execute('''
                SELECT 
                    s.stuId, 
                    s.firstName, 
                    s.lastName, 
                    p.sleepTime, 
                    p.smoking, 
                    p.extra_observations,
                    CASE 
                        WHEN ABS(p.sleepTime - %s) <= 1 THEN 3
                        WHEN ABS(p.sleepTime - %s) <= 2 THEN 2
                        WHEN ABS(p.sleepTime - %s) <= 3 THEN 1
                        ELSE 0
                    END +
                    CASE 
                        WHEN p.smoking = %s THEN 3
                        ELSE 0
                    END AS match_score
                FROM 
                    student s
                JOIN 
                    preferences p ON s.stuId = p.stuId
                WHERE 
                    s.stuId != %s
                ORDER BY 
                    match_score DESC
            ''', (student_pref['sleepTime'], student_pref['sleepTime'], student_pref['sleepTime'], 
                  student_pref['smoking'], student_id))
        else:
            # If student has no preferences, just return all other students
            cursor.execute('''
                SELECT 
                    s.stuId, 
                    s.firstName, 
                    s.lastName, 
                    p.sleepTime, 
                    p.smoking, 
                    p.extra_observations,
                    0 AS match_score
                FROM 
                    student s
                LEFT JOIN 
                    preferences p ON s.stuId = p.stuId
                WHERE 
                    s.stuId != %s
            ''', (student_id,))
    else:
        # If no student ID is provided, return all students with their preferences
        cursor.execute('''
            SELECT 
                s.stuId, 
                s.firstName, 
                s.lastName, 
                p.sleepTime, 
                p.smoking, 
                p.extra_observations,
                0 AS match_score
            FROM 
                student s
            LEFT JOIN 
                preferences p ON s.stuId = p.stuId
        ''')
    
    matches = cursor.fetchall()
    
    the_response = make_response(jsonify(matches))
    the_response.status_code = 200
    return the_response