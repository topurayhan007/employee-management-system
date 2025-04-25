# All the DB operations regarding Experience Table;
from database.setup import get_db_connection
from models.experience import Experience

add_experience_query = (
    "INSERT INTO degrees "
    "(employee_id, company_name, position, joining_date, ending_date, location) "
    "VALUES (%s, %s, %s, %s, %s, %s)")

def add_experience(experience: Experience):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    try:
        cursor.execute(add_experience_query, experience)
        experience_id = cursor.lastrowid
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return experience_id
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None