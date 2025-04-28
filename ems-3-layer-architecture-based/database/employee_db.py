# All the DB operations regarding Employee Table;
from database.setup import get_db_connection, DB_NAME
from models.employee import Employee

add_employee_query = (
    "INSERT INTO employees "
    "(name, date_of_birth, nid, email, phone_no, gender, father_name, mother_name, marital_status, dept, designation, nationality, joining_date, present_address, permanent_address) "
    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

get_all_employee_query = (
    "SELECT * FROM employees "
)

delete_an_employee_query = (
    "DELETE FROM employees WHERE employee_id=%s;"
)

search_employee_query = (
    "SELECT * FROM employees WHERE "
    "name LIKE %s OR "
    "date_of_birth LIKE %s OR "
    "nid LIKE %s OR "
    "email LIKE %s OR "
    "phone_no LIKE %s OR "
    "gender LIKE %s OR "
    "father_name LIKE %s OR "
    "mother_name LIKE %s OR "
    "marital_status LIKE %s OR "
    "dept LIKE %s OR "
    "designation LIKE %s OR "
    "nationality LIKE %s OR "
    "joining_date LIKE %s OR "
    "present_address LIKE %s OR "
    "permanent_address LIKE %s"
)

def add_employee(employee:Employee):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

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
    
def get_all_employee():
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(f"USE {DB_NAME}")

    try:
        cursor.execute(get_all_employee_query)
        all_employees = cursor.fetchall()
        
        cursor.close()
        db_connection.close()
        return all_employees
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None
    
def search_employee(search_text):
    db_connection = get_db_connection()
    cursor = db_connection.cursor(dictionary=True)
    cursor.execute(f"USE {DB_NAME}")

    params = tuple(["%" + search_text + "%"] * 15)

    try:
        cursor.execute(search_employee_query, params)
        result = cursor.fetchall()
        cursor.close()
        db_connection.close()
        return result
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None

def delete_an_employee(employee_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute(f"USE {DB_NAME}")

    try:
        result = cursor.execute(delete_an_employee_query)
        cursor.close()
        db_connection.close()
        return result
    
    except db_connection.Error as err:
        print(err.msg)
        cursor.close()
        db_connection.close()
        return None