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
            JOIN student_email e ON s.stuId = e.stuId
            JOIN studentBridgeRA sb ON sb.stuId = s.stuId
            WHERE sb.raId = %s
        """
        cursor.execute(query, (ra_id))
        data = cursor.fetchall()

        residents = [
            {
                "name": f"{row['firstName']} {row['lastName']}",
                "email": row['email']
            }
            for row in data
        ]

        # print(data)
        response_data = make_response(jsonify(residents))
        response_data.status_code = 200

        return response_data

@ra.route('/complaints/<int:ra_id>', methods=['GET'])
def get_complaints_for_ra(ra_id):
        cursor = db.get_db().cursor()

        query = """
            SELECT s.firstName, s.lastName, c.description
            FROM complaints c
            JOIN student s
            ON c.stuId = s.stuId
            WHERE c.stuId IN (
                SELECT stuId FROM studentBridgeRA
                WHERE raId = %s
            )

        """
        cursor.execute(query, (ra_id,))
        data = cursor.fetchall()
        cursor.close()

        complaints = [
            {
                "name": f"{row['firstName']} {row['lastName']}",
                "description": row['description']
            }
            for row in data
        ]

        return jsonify(complaints)


@ra.route('/events/<int:ra_id>', methods=['GET'])
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


@ra.route('/conflicts/<int:ra_id>', methods=['GET'])
def get_conflicts(ra_id):
        cursor = db.get_db().cursor()

        # get conflicts connected to my students

        query = """
            SELECT DISTINCT s1.firstName, s1.lastName, s2.firstName, s2.lastName, c.urgency
            
            FROM conflicts c
            JOIN conflicts_student c1 ON c.confId = c1.confId
            JOIN conflicts_student c2 ON c1.confId = c2.confId AND c1.studentId != c2.studentId
            JOIN studentBridgeRA sr ON c1.studentId = sr.stuId OR c2.studentId = sr.stuId
            JOIN student s1 ON c1.studentId = s1.stuId
            JOIN student s2 ON c2.studentId = s2.stuId
            
            WHERE sr.raId = %s
        """

        cursor.execute(query, (ra_id))
        result_data = cursor.fetchall()

        response_data = make_response(jsonify([
            {
                "name1": f"{row['firstName']} {row['lastName']}",
                "name2": f"{row['s2.firstName']} {row['s2.lastName']}",
                "urgency": row['urgency']
            }
            for row in result_data
        ]))
        response_data.status_code = 200

        return response_data
