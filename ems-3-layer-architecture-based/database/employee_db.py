# All the DB operations regarding Employee Table;
from database.setup import get_db_connection
from models.employee import Employee

add_employee_query = (
    "INSERT INTO employees "
    "(name, date_of_birth, nid, email, phone_no, gender, father_name, mother_name, marital_status, dept, designation, nationality, joining_date, present_address, permanent_address) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

def add_employee(employee:Employee):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    try:
        cursor.execute(add_employee_query, employee)
        emp_id = cursor.lastrowid
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return emp_id
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None
