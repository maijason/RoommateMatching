from flask import Blueprint
from flask import request
from flask import jsonify
from flask import make_response
from flask import current_app
from backend.db_connection import db

events = Blueprint("events", __name__)

#Get upcoming events
@events.route("/upcoming/<raId>", methods=["GET"])
def getupcoming_events(raId):
    query = f"""
        SELECT datetime, title, location 
        FROM events 
        WHERE datetime >= NOW() AND raId = {raId}
        ORDER BY datetime ASC
    """
    cursor = db.get_db().cursor()

    cursor.execute(query)
    theData = cursor.fetchall()
    response = make_response(jsonify(theData))
    response.status_code = 200
    return response


#Get upcoming events
@events.route("/", methods=["PUT"])
def change_events_location():
    # Collect data from the request body
    the_data = request.json
    current_app.logger.info(the_data)


    # Build the SQL query using string interpolation 
    query = f'''
        UPDATE events
        SET location = {the_data["location"]}
        WHERE datetime = {the_data["datetime"]} AND title = {the_data["title"]};
    '''

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    # Send response
    response = make_response("location submitted successfully!")
    response.status_code = 201
    return response

#  RSVP to an event
@events.route('/add', methods=['POST'])
def add_():
    # Collect data from the request body
    the_data = request.json
    current_app.logger.info(the_data)


    # Build the SQL query using string interpolation 
    query = f'''
        INSERT INTO events 
        VALUES ('{the_data['datetime']}', '{the_data['title']}', '{the_data['location']}', {the_data['raId']})
    '''

    # Execute the query
    cursor = db.get_db().cursor()
    cursor.execute(query)
    db.get_db().commit()

    # Send response
    response = make_response("RSVP submitted successfully!")
    response.status_code = 201
    return response


# Delete an event
@events.route('/', methods=['DELETE'])
def delete_event():
    the_data = request.json
    title = the_data['title']
    datetime_val = the_data['datetime']

    current_app.logger.info(f"Deleting event: {title} at {datetime_val}")

    cursor = db.get_db().cursor()
    query = """
        DELETE from RABridgeEvents
        WHERE title = %s AND datetime = %s;

    """
    cursor.execute(query, (title, datetime_val))
    db.get_db().commit()

    cursor = db.get_db().cursor()
    query = """
        DELETE FROM events
        WHERE title = %s AND datetime = %s;

    """
    cursor.execute(query, (title, datetime_val))
    db.get_db().commit()
        

    response = make_response("Event deleted")
    response.status_code = 200
    return response

