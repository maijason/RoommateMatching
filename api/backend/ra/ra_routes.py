from flask import Blueprint, jsonify
from backend.db_connection import db

ra_bp = Blueprint('ra', __name__)

@ra_bp.route('/residents/<int:ra_id>', methods=['GET'])
def get_residents_for_ra(ra_id):
        cursor = db.get_db().cursor()

        query = """
            SELECT s.firstName, s.lastName, e.email
            FROM student s
            JOIN student_email e ON s.stuId = e.stuId
            JOIN studentBridgeRA sb ON sb.stuId = s.stuId
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

@ra_bp.route('/complaints/<int:ra_id>', methods=['GET'])
def get_complaints_for_ra(ra_id):
        cursor = db.get_db().cursor()

        query = """
            SELECT compId, description
            FROM complaints
            WHERE stuId IN (
            SELECT stuId FROM studentBridgeRA WHERE raId = %s;
        """
        cursor.execute(query, (ra_id,))
        data = cursor.fetchall()
        cursor.close()

        return jsonify(data)


@ra_bp.route('/events/<int:ra_id>', methods=['GET'])
def get_events_for_ra(ra_id):
        cursor = db.get_db().cursor()

        query = """
            SELECT c.compId, c.description, e.title, e.datetime
            FROM complaints c
            JOIN studentBridgeRA sr ON c.stuId = sr.stuId
            LEFT JOIN RABridgeEvents re ON sr.raId = re.raId
            LEFT JOIN events e ON re.datetime = e.datetime AND re.title = e.title
            WHERE sr.raId = %s;
        """
        cursor.execute(query, (ra_id,))
        data = cursor.fetchall()
        cursor.close()

        return jsonify(data)


