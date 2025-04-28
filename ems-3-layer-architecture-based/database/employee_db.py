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
    cursor.execute("USE ems")

    try:
        employee_data = (
            employee._name,
            employee._date_of_birth,
            employee._nid,
            employee._email,
            employee._phone_no,
            employee._gender,
            employee._father_name,
            employee._mother_name,
            employee._marital_status,
            employee._dept,
            employee._designation,
            employee._nationality,
            employee._joining_date,
            employee._present_address,
            employee._permanent_address,
        )
        cursor.execute(add_employee_query, employee_data)
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
