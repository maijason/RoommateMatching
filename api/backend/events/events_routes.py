from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

events = Blueprint("events", __name__)

#Get upcoming events
@events.route("/events/upcoming", methods=["GET"])
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
@events.route('/events/rsvp', methods=['POST'])
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

# Delete an event
@events.route('/events/delete', methods=['DELETE'])
def delete_event():
    data = request.get_json()
    title = data.get('title')
    datetime_val = data.get('datetime')

    current_app.logger.info(f"Deleting event: {title} at {datetime_val}")

    cursor = db.get_db().cursor()
    query = """
        DELETE FROM events
        WHERE title = %s AND datetime = %s
    """
    cursor.execute(query, (title, datetime_val))
    db.get_db().commit()

    return jsonify({"message": "Event deleted"}), 200

