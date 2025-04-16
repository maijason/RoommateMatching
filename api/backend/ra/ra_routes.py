from flask import Blueprint, jsonify
from backend.db_connection import db

ra_bp = Blueprint('ra', __name__)

@ra_bp.route('/residents/<int:ra_id>', methods=['GET'])
def get_residents_for_ra(ra_id):
        cursor = db.get_db().cursor()

        query = """
            SELECT s.firstName, s.lastName, e.email
            FROM student s
            JOIN student_email e ON s.studId = e.studId
            JOIN studentBridgeRA sb ON sb.studId = s.studId
            WHERE sb.raId = %s
        """
        cursor.execute(query, (ra_id,))
        data = cursor.fetchall()
        cursor.close()

        residents = [
            {
                "name": f"{data['firstName']} {data['lastName']}",
                "email": data['email']
            }
            for row in data
        ]

        return jsonify(residents)