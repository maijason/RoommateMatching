from flask import Blueprint, jsonify
from backend.db_connection import db
from flask import make_response

ra = Blueprint('ra', __name__)

@ra.route('/residents/<int:ra_id>', methods=['GET'])
def get_residents_for_ra(ra_id):
        cursor = db.get_db().cursor()

        query = """
            SELECT s.firstName, s.lastName, e.email
            FROM student s
            JOIN student_email e ON s.studId = e.studId
            JOIN studentBridgeRA sb ON sb.studId = s.studId
            WHERE sb.raId = %s
        """
        cursor.execute(query)
        data = cursor.fetchall()

        residents = [
            {
                "name": f"{data['firstName']} {data['lastName']}",
                "email": data['email']
            }
            for row in data
        ]

        return jsonify(residents)

@ra.route('/conflicts', methods=['GET'])
def get_conflicts():
        cursor = db.get_db().cursor()

        query = """
            SELECT 
                c.confId,
                c.urgency,
                h.firstName AS haFirstName,
                h.lastName AS haLastName
            FROM conflicts c
            JOIN housingAdmin h ON c.housingAdminId = h.haId
        """

        cursor.execute(query)
        result_data = cursor.fetchall()

        response_data = make_response(jsonify(result_data))
        response_data.status_code = 200

        return response_data