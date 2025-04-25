# All the DB operations regarding Education Table;
from database.setup import get_db_connection
from models.education import EducationalDegree

add_degree_query = (
    "INSERT INTO degrees "
    "(name, employee_id, degree_name, institute_name, major, location, gpa, gpa_scale, year_of_passing) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

def add_degree(degree: EducationalDegree):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    try:
        cursor.execute(add_degree_query, degree)
        degree_id = cursor.lastrowid
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return degree_id
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None

