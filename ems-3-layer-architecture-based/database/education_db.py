# All the DB operations regarding Education Table;
from database.setup import get_db_connection
from models.education import EducationalDegree

add_degree_query = (
    "INSERT INTO degrees "
    "(name, employee_id, degree_name, institute_name, major, location, gpa, gpa_scale, year_of_passing) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

search_degrees_of_an_employee_query = (
    "SELECT * FROM degrees "
    "WHERE employee_id = %s"
)

update_a_degree_of_an_employee = (
    "UPDATE degrees SET "
    "name=%s, " 
    "employee_id=%s, " 
    "degree_name=%s, " 
    "institute_name=%s, " 
    "major=%s, " 
    "location=%s, " 
    "gpa=%s, " 
    "gpa_scale=%s, " 
    "year_of_passing=%s, "
    "WHERE degree_id=%s"
)

delete_a_degree_of_an_employee_query = (
    "DELETE FROM degrees "
    "WHERE degree_id=%s"
)

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

