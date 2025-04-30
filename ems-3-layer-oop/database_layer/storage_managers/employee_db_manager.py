# Database Class with queries, methods to perform queries to DB, retrieve data to class object
from application_layer.classes.employee import Employee
from database_layer.setup import DatabaseManager

class EmployeeDBManager:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.db_connection = db_manager.get_db_connection()

    def add_employee(self, employee_data):
        cursor = self.db_connection.cursor()
        query = (
            "INSERT INTO employees "
            "(name, date_of_birth, nid, email, phone_no, gender, father_name, mother_name, marital_status, dept, designation, nationality, joining_date, present_address, permanent_address) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )

        try:
            cursor.execute(query, employee_data)
            emp_id = cursor.lastrowid
            self.db_connection.commit()
            cursor.close()
            self.db_connection.close()
            return emp_id
        
        except self.db_connection.Error as err:
            print(err.msg)
            cursor.close()
            self.db_connection.close()
            return None
        
    def get_all_employee(self):
        cursor = self.db_connection.cursor(dictionary=True)
        
        query = (
            "SELECT * FROM employees "
        )

        try:
            cursor.execute(query)
            all_employees = cursor.fetchall()
            
            cursor.close()
            self.db_connection.close()
            return all_employees
        
        except self.db_connection.Error as err:
            print(err.msg)
            cursor.close()
            self.db_connection.close()
            return None
        
    def search_employee(self, search_text):
        cursor = self.db_connection.cursor(dictionary=True)

        params = tuple(["%" + search_text + "%"] * 15)
        query = (
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

        try:
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            self.db_connection.close()
            return result
        
        except self.db_connection.Error as err:
            print(err.msg)
            cursor.close()
            self.db_connection.close()
            return None

    def delete_an_employee(self, employee_id):
        cursor = self.db_connection.cursor()

        query = (
            "DELETE FROM employees WHERE employee_id=%s;"
        )
        
        try:
            cursor.execute(query, (employee_id,))
            self.db_connection.commit()
            result = cursor.rowcount
            cursor.close()
            self.db_connection.close()
            return result
        
        except self.db_connection.Error as err:
            print(err.msg)
            cursor.close()
            self.db_connection.close()
            return None
        
    def update_an_employee(self, updated_employee_data):
        cursor = self.db_connection.cursor()
        
        query = (
            "UPDATE employees SET "
            "name=%s, "
            "date_of_birth=%s, "
            "nid=%s, "
            "email=%s, "
            "phone_no=%s, "
            "gender=%s, "
            "father_name=%s, "
            "mother_name=%s, "
            "marital_status=%s, "
            "dept=%s, "
            "designation=%s, "
            "nationality=%s, "
            "joining_date=%s, "
            "present_address=%s, "
            "permanent_address=%s "
            "WHERE employee_id=%s"
        )

        try:
            cursor.execute(query, updated_employee_data)
            self.db_connection.commit()
            result = cursor.rowcount
            cursor.close()
            self.db_connection.close()
            return result
        
        except self.db_connection.Error as err:
            print(err.msg)
            cursor.close()
            self.db_connection.close()
            return None