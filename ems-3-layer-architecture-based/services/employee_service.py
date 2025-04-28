from models.education import EducationalDegree
from models.experience import Experience
from models.employee import Employee
from services.input_validation_service import InputValidator
from tabulate import tabulate
from services.education_service import EducationService
from services.experience_service import ExperienceService
from database.employee_db import add_employee, get_all_employee, search_employee, delete_an_employee

# Employee Service Class
class EmployeeService:
    validator = InputValidator()
    education_service = EducationService()
    experience_service = ExperienceService()

    def __init__(self):
        self._employees = []

    def validate_unique_id(self, input):
        for item in self._employees:
            if item._employee_id == input:
                return False
        return True

    def add_an_employee(self):
        _name = self.validator.get_input_and_validate(str, "Enter name: ")
        _date_of_birth = self.validator.get_input_and_validate(str, "Enter date of birth (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
        _nid = self.validator.get_input_and_validate(int, "Enter NID no: ", self.validator.validate_nid, "⚠️  NID should be between 10 and 17 digits")
        _email = self.validator.get_input_and_validate(str, "Enter email address: ", self.validator.validate_email, "⚠️  Invalid email format")
        _phone_no = self.validator.get_input_and_validate(str, "Enter phone no: ", self.validator.validate_phone_number, "⚠️  Phone no. should be 11 digits")
        _gender = self.validator.get_input_and_validate(str, "Enter gender (Male/Female/Other): ", self.validator.validate_gender, "⚠️  Invalid gender input")
        _father_name = self.validator.get_input_and_validate(str, "Enter father's name: ")
        _mother_name = self.validator.get_input_and_validate(str, "Enter mother's name: ")
        _marital_status = self.validator.get_input_and_validate(str, "Enter marital status (Single/Married): ")
        _dept = self.validator.get_input_and_validate(str, "Enter department name: ")
        _designation = self.validator.get_input_and_validate(str, "Enter designation: ")
        _nationality = self.validator.get_input_and_validate(str, "Enter nationality: ")
        _joining_date = self.validator.get_input_and_validate(str, "Enter joining date (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
        _present_address = self.validator.get_input_and_validate(str, "Enter present address: ")
        _permanent_address = self.validator.get_input_and_validate(str, "Enter permanent address: ")

        employee = Employee(_name, _date_of_birth, _nid, _email, _phone_no, _gender, _father_name, _mother_name, _marital_status, _dept, _designation, _nationality, _joining_date, _present_address, _permanent_address)
        
        # insert into DB
        _employee_id = add_employee(employee)
        if _employee_id is not None:
            print(f"✅ Employee with ID: {_employee_id} added successfully")
            no_of_degrees = int(input("How many educational degress do you want to add? => "))
            for i in range(no_of_degrees):
                self.education_service.add_educational_degree(_employee_id)

            no_of_exp = int(input("How many job experiences do you want to add? => "))
            for i in range(no_of_exp):
                self.experience_service.add_experience(_employee_id)
        
        else:
            print("Something went wrong")
            

    def printDataTable(self, data, flag):
        headers = ["ID", "Name", "DoB", "NID", "Email", "Phone no.", "Gender", "Marital Status", "Department", "Designation", "Joining Date", "Present Address"]
        dataRow = []
        if flag == "single":
            item = data
            dataRow.append([item['employee_id'], item['name'], item['date_of_birth'], item['nid'], item['email'], item['phone_no'], item['gender'], item['marital_status'], item['dept'], item['designation'], item['joining_date'], item['present_address']])
            return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  
        else:   
            for item in data:
                dataRow.append([item['employee_id'], item['name'], item['date_of_birth'], item['nid'], item['email'], item['phone_no'], item['gender'], item['marital_status'], item['dept'], item['designation'], item['joining_date'], item['present_address']])
            return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  

    def getAllEmployees(self):
        employees = get_all_employee()
        if employees is None or len(employees) == 0:
            print("⚠️  No data found!")
            return None
        else: 
            print(self.printDataTable(employees, "multiple"))
            return employees
    
    def searchAnEmployee(self, input_text):
        search_result = search_employee(input_text)
        if search_result is None or len(search_result) == 0:
            print("⚠️  Employee not found!")
            return None
        else: 
            print(self.printDataTable(search_result, "multiple")) 
            return search_result   
            
    def updateEmployeeFields(self, data):
        item = data
        print("=> Employee selected: ")
        print(self.printDataTable(item, "single"))
        print("These are the fields you can update: ")
        print("Phone Number, Marital Status, Department, Designation, Present Address")
        fields = input("From the above fields type the fields you want to update separated by commas: ")
        fields = fields.split(",")

        for field in fields:
            if field.strip().lower() in "Phone Number".lower():
                item._phone_no = input("Enter new phone number: ")
            elif field.strip().lower() in "Marital Status".lower():
                item._marital_status = input("Enter new marital status: ")
            elif field.strip().lower() in "Department".lower(): 
                item._dept = input("Enter new department: ")
            elif field.strip().lower() in "Designation".lower():
                item._designation = input("Enter new designation: ")
            elif field.strip().lower() in "Present Address".lower():
                item._present_address = input("Enter new present address: ")
            else:
                print("⚠️  You entered an invalid field, skipping this field...")
        print("✅ Employee updated successfully!") 
    
    def deleteAnEmployee(self, employee):
        delete_an_employee(employee['employee_id'])
        print("✅ Employee deleted successfully!") 


    def selectEmployeeAndPerformUpdateOrDelete(self, search_result, action):
        if isinstance(search_result, str):
                print(search_result)
        else: 
            if len(search_result) > 1:
                selected_emp = None
                while True:
                    emp_id = input(f"Type the employee ID you want to {action} from the above result: ")
                    for item in search_result:
                        if item['employee_id'] == int(emp_id):
                            selected_emp = item
                            break
                    if selected_emp is not None:
                        break
                    else: 
                        print("⚠️  ID didn't match, please try again")

                self.updateEmployeeFields(selected_emp) if action == "update" else self.deleteAnEmployee(selected_emp) 
            else:
                self.updateEmployeeFields(search_result[0]) if action == "update" else self.deleteAnEmployee(search_result[0])
      
