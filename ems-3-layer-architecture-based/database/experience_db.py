# All the DB operations regarding Experience Table;
from database.setup import DB_NAME, get_db_connection
from models.experience import Experience

add_experience_query = (
    "INSERT INTO experiences "
    "(employee_id, company_name, position, joining_date, ending_date, location) "
    "VALUES (%s, %s, %s, %s, %s, %s)")

search_experiences_of_an_employee_query = (
    "SELECT * FROM experiences "
    "WHERE employee_id = %s"
)

update_an_experience_of_an_employee_query = (
    "UPDATE experiences SET " 
    "employee_id=%s, " 
    "company_name=%s, " 
    "position=%s, " 
    "joining_date=%s, " 
    "ending_date=%s, " 
    "location=%s " 
    "WHERE experience_id=%s"
)

delete_an_experience_of_an_employee_query = (
    "DELETE FROM experiences "
    "WHERE experience_id=%s"
)

def add_experience(experience: Experience):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    experience_data = (
            experience._employee_id,
            experience._company_name,
            experience._position,
            experience._joining_date,
            experience._ending_date,
            experience._location
        )

    try:
        cursor.execute(add_experience_query, experience_data)
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

def search_experiences_of_an_employee(employee_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(f"USE {DB_NAME}")

    try:
        cursor.execute(search_experiences_of_an_employee_query, (employee_id,))
        result = cursor.fetchall()        
        cursor.close()
        db_connection.close()
        return result
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None

def delete_an_experience_of_an_employee(experience_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    try:
        cursor.execute(delete_an_experience_of_an_employee_query, (experience_id,))
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

def update_an_experience_of_an_employee(experience):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    try:
        updated_experience_data = (
            experience['employee_id'],
            experience['company_name'],
            experience['position'],
            experience['joining_date'],
            experience['ending_date'],
            experience['location'],
            experience['experience_id']
        )

        cursor.execute(update_an_experience_of_an_employee_query, updated_experience_data)
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