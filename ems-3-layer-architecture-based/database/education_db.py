# All the DB operations regarding Education Table;
from database.setup import DB_NAME, get_db_connection
from models.education import EducationalDegree

add_degree_query = (
    "INSERT INTO degrees "
    "(employee_id, degree_name, institute_name, major, location, gpa, gpa_scale, year_of_passing) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

search_degrees_of_an_employee_query = (
    "SELECT * FROM degrees "
    "WHERE employee_id = %s"
)

update_a_degree_of_an_employee_query = (
    "UPDATE degrees SET " 
    "employee_id=%s, " 
    "degree_name=%s, " 
    "institute_name=%s, " 
    "major=%s, " 
    "location=%s, " 
    "gpa=%s, " 
    "gpa_scale=%s, " 
    "year_of_passing=%s "
    "WHERE degree_id=%s"
)

delete_a_degree_of_an_employee_query = (
    "DELETE FROM degrees "
    "WHERE degree_id=%s"
)

def add_degree(degree: EducationalDegree):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    degree_data = (
            degree._employee_id,
            degree._degree_name,
            degree._institute_name,
            degree._major,
            degree._location,
            degree._gpa,
            degree._gpa_scale,
            degree._year_of_passing
        )

    try:
        cursor.execute(add_degree_query, degree_data)
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

def search_degrees_of_an_employee(employee_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(f"USE {DB_NAME}")

    try:
        cursor.execute(search_degrees_of_an_employee_query, (employee_id,))
        result = cursor.fetchall()        
        cursor.close()
        db_connection.close()
        return result
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None

def delete_a_degree_of_an_employee(degree_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    try:
        cursor.execute(delete_a_degree_of_an_employee_query, (degree_id,))
        db_connection.commit()
        result = cursor.rowcount
        cursor.close()
        db_connection.close()
        return result
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None

def update_a_degree_of_an_employee(degree):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    try:
        updated_degree_data = (
            degree['employee_id'],
            degree['degree_name'],
            degree['institute_name'],
            degree['major'],
            degree['location'],
            degree['gpa'],
            degree['gpa_scale'],
            degree['year_of_passing'],
            degree['degree_id']
        )

        cursor.execute(update_a_degree_of_an_employee_query, updated_degree_data)
        db_connection.commit()
        result = cursor.rowcount
        cursor.close()
        db_connection.close()
        return result
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None