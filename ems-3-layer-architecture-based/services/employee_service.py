from models.education import EducationalDegree
from models.experience import Experience
from models.employee import Employee
from services.input_validation_service import InputValidator
from services.display_service import print_employee_table
from services.education_service import EducationService
from services.experience_service import ExperienceService
from database.employee_db import add_employee, get_all_employee, search_employee, delete_an_employee, update_an_employee

# Employee Service Class
class EmployeeService:
    validator = InputValidator()
    education_service = EducationService()
    experience_service = ExperienceService()

    def __init__(self):
        self._employees = []

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
            

    def getAllEmployees(self):
        employees = get_all_employee()
        if employees is None or len(employees) == 0:
            print("⚠️  No data found!")
            return None
        else: 
            print(print_employee_table(employees, "multiple"))
            return employees
    
    def searchAnEmployee(self, input_text):
        search_result = search_employee(input_text)
        if search_result is None or len(search_result) == 0:
            print("⚠️  Employee not found!")
            return None
        else: 
            print(print_employee_table(search_result, "multiple")) 
            return search_result   
            
    def updateEmployeeFields(self, data):
        item = data
        print("=> Employee selected: ")
        print(print_employee_table(item, "single"))
        print("These are the fields you can update: ")
        print("Name, Date of Birth, NID, Email, Phone Number, Gender, Father's Name, Mother's Name, Marital Status, Department, Designation, Nationality, Joining Date, Present Address, Permanent Address")
        fields = input("From the above fields type the fields you want to update separated by commas: ")
        fields = fields.split(",")

        for field in fields:
            if field.strip().lower() in "Name".lower():
                item['name'] = self.validator.get_input_and_validate(str, "Enter new name: ")
            elif field.strip().lower() in "Date of Birth".lower():
                item['date_of_birth'] = self.validator.get_input_and_validate(str, "Enter new date of birth (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
            elif field.strip().lower() in "NID".lower():
                item['nid'] = self.validator.get_input_and_validate(int, "Enter new NID no: ", self.validator.validate_nid, "⚠️  NID should be between 10 and 17 digits")
            elif field.strip().lower() in "Email".lower():
                item['email'] = self.validator.get_input_and_validate(str, "Enter new email address: ", self.validator.validate_email, "⚠️  Invalid email format")
            elif field.strip().lower() in "Phone number".lower():
                item['phone_no'] = self.validator.get_input_and_validate(str, "Enter new phone no: ", self.validator.validate_phone_number, "⚠️  Phone no. should be 11 digits")
            elif field.strip().lower() in "Gender".lower():
                item['gender'] = self.validator.get_input_and_validate(str, "Enter new gender (Male/Female/Other): ", self.validator.validate_gender, "⚠️  Invalid gender input")
            elif field.strip().lower() in "Father's Name".lower():
                item['father_name'] = self.validator.get_input_and_validate(str, "Enter new father's name: ")
            elif field.strip().lower() in "Mother's Name".lower():
                item['mother_name'] = self.validator.get_input_and_validate(str, "Enter new mother's name: ")
            elif field.strip().lower() in "Marital Status".lower():
                item['marital_status'] = self.validator.get_input_and_validate(str, "Enter new marital status (Single/Married): ")
            elif field.strip().lower() in "Department".lower():
                item['dept'] = self.validator.get_input_and_validate(str, "Enter new department name: ")
            elif field.strip().lower() in "Designation".lower():
                item['designation'] = self.validator.get_input_and_validate(str, "Enter new designation: ")
            elif field.strip().lower() in "Nationality".lower():
                item['nationality'] = self.validator.get_input_and_validate(str, "Enter new nationality: ")
            elif field.strip().lower() in "Joining Date".lower():
                item['joining_date'] = self.validator.get_input_and_validate(str, "Enter new joining date (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
            elif field.strip().lower() in "Present Address".lower():
                item['present_address'] = self.validator.get_input_and_validate(str, "Enter new present address: ")
            elif field.strip().lower() in "Permanent Address".lower():
                item['permanent_address'] = self.validator.get_input_and_validate(str, "Enter new permanent address: ")
            else:
                print("⚠️  You entered an invalid field, skipping this field...")
        
        update_an_employee(item)
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
      
