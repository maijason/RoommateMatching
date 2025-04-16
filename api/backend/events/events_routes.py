########################################################
# Sample customers blueprint of endpoints
# Remove this file if you are not using it in your project
########################################################

from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

events_bp = Blueprint("events_bp", __name__)

#Get upcoming events
@events_bp.route("/events/upcoming", methods=["GET"])
def get_upcoming_events():
    query = """
        SELECT datetime, title, location 
        FROM events 
        WHERE datetime >= NOW()
        ORDER BY datetime ASC
    """
    cursor = db.get_db().cursor()

    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response

#  RSVP to an event
@events_bp.route('/events/rsvp', methods=['POST'])
def add_rsvp():
    # Collect data from the request body
    the_data = request.json
    current_app.logger.info(the_data)

    # Extract fields
    stu_id = the_data['stuId']
    datetime = the_data['datetime']
    title = the_data['title']

    # Build the SQL query using string interpolation 
    query = f'''
        INSERT INTO studentBridgeEvents (stuId, datetime, title)
        VALUES ({stu_id}, '{datetime}', '{title}')
    '''

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    # Send response
    return jsonify({"message": "RSVP submitted successfully!"}), 201
