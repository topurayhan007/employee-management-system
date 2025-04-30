# Bridge between CLI controllers and DB managers
from application_layer.classes.employee import Employee
from database_layer.setup import DatabaseManager
from database_layer.storage_managers.employee_db_manager import EmployeeDBManager

class EmployeeService:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.employee_db_manager = EmployeeDBManager(db_manager)
    
    def add_employee(self, employee: Employee):
        employee_data = self.employee_object_to_tuple(employee)
        result = self.employee_db_manager.add_employee(employee_data, flag="add")
        return result
    
    def get_all_employee(self)-> list[Employee]:
        result = self.employee_db_manager.get_all_employee()
        employees = self.db_data_to_employee_list(result)
        return employees
    
    def search_employee(self, input_text):
        result = self.employee_db_manager.search_employee(input_text)
        employees = self.db_data_to_employee_list(result)
        return employees
    
    def delete_an_employee(self, employee_id):
        result = self.employee_db_manager.delete_an_employee(employee_id)
        return result

    def update_an_employee(self, employee: Employee):
        updated_employee_data = self.employee_object_to_tuple(employee, flag="update")
        result = self.employee_db_manager.update_an_employee(updated_employee_data)
        return result

    def employee_object_to_tuple(self, employee: Employee, flag):
        return (
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
            employee._permanent_address
        ) if flag == "add" else (
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
            employee._employee_id
        )
    
    def db_data_to_employee_list(self, data) -> list[Employee]:
        employees: list[Employee] = []
        for row in data:
            employee = Employee(
                row['employee_id'],
                row['name'],
                row['date_of_birth'],
                row['nid'],
                row['email'],
                row['phone_no'],
                row['gender'],
                row['father_name'],
                row['mother_name'],
                row['marital_status'],
                row['dept'],
                row['designation'],
                row['nationality'],
                row['joining_date'],
                row['present_address'],
                row['permanent_address']
            )
            employees.append(employee)
        return employees
        
            



"""
update_employee_data = (
                employee['name'],
                employee['date_of_birth'],
                employee['nid'],
                employee['email'],
                employee['phone_no'],
                employee['gender'],
                employee['father_name'],
                employee['mother_name'],
                employee['marital_status'],
                employee['dept'],
                employee['designation'],
                employee['nationality'],
                employee['joining_date'],
                employee['present_address'],
                employee['permanent_address'],
                employee['employee_id']
            )
"""

    