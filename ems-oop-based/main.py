# This is a console based employee management system
# This system relies on user input from the console to perform CRUD operations

from tabulate import tabulate
import re
from datetime import datetime

# Educational Degree Class
class EducationalDegree:
    def __init__(self, _degree_name, _institute_name, _major, _location, _gpa, _gpa_scale, _year_of_passing):
        self._degree_name = _degree_name
        self._institute_name = _institute_name 
        self._major = _major 
        self._location = _location 
        self._gpa = _gpa
        self._gpa_scale = _gpa_scale
        self._year_of_passing = _year_of_passing

# Experience Class
class Experience:
    def __init__(self, _company_name, _position, _joining_date, _ending_date, _location):
        self._company_name = _company_name
        self._position = _position
        self._joining_date = _joining_date 
        self._ending_date = _ending_date 
        self._location = _location

# Employee Class
class Employee:
    def __init__(self, _employee_id, _name, _dob, _nid, _email, _phone_no, _gender, _father_name, _mother_name, _marital_status, _dept, _designation, _nationality, _joining_date, _present_address, _permanent_address, _educational_degrees: list[EducationalDegree], _experience: list[Experience]):
        self._employee_id = _employee_id
        self._name = _name
        self._dob = _dob
        self._nid = _nid
        self._email = _email
        self._phone_no = _phone_no
        self._gender = _gender
        self._father_name = _father_name
        self._mother_name = _mother_name
        self._marital_status = _marital_status
        self._dept = _dept
        self._designation = _designation
        self._nationality = _nationality
        self._joining_date = _joining_date
        self._present_address = _present_address
        self._permanent_address = _permanent_address
        self._educational_degrees = _educational_degrees
        self._experience = _experience

class EmployeeController:
    def __init__(self):
        self._employees = []

    def getAndValidateInput(self, data_type, input_text, custom_validator=None):
        while True:
            try:
                x = data_type(input(input_text))
                if not x:
                    print("⚠️  Input required")
                    continue
                if custom_validator and not custom_validator(x):
                    print("⚠️  Invalid input format")
                    continue
                else:
                    return x
            except ValueError:
                print("⚠️  Invalid input, please try again")
    
    def validateDate(self, input):
        format = "%d-%m-%Y"
        return datetime.strptime(input, format)
    
    def validate_email(self, input):
        format = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(format, input)
    
    def validate_year(self, input):
        format = "%Y"
        return datetime.strptime(input, format)
    
    def validate_phone_number(self, input):
        length = 11
        return len(input) == length
    
    def validate_gender(self, input):
        return input.lower() == "male" or input.lower() == "female" or input.lower() == "other"
    
    def validate_nid(self, input):
        min_length = 10
        max_length = 17
        return len(str(input)) >= min_length and len(str(input)) <= max_length
    
    def addAnEmployee(self):      
        _employee_id = self.getAndValidateInput(str, "Enter employee ID: ")
        _name = self.getAndValidateInput(str, "Enter name: ")
        _dob = self.getAndValidateInput(str, "Enter date of birth (DD-MM-YYYY): ", self.validateDate)
        _nid = self.getAndValidateInput(int, "Enter NID no: ", self.validate_nid)
        _email = self.getAndValidateInput(str, "Enter email address: ", self.validate_email)
        _phone_no = self.getAndValidateInput(str, "Enter phone no: ", self.validate_phone_number)
        _gender = self.getAndValidateInput(str, "Enter gender (Male/Female/Other): ", self.validate_gender)
        _father_name = self.getAndValidateInput(str, "Enter father's name: ")
        _mother_name = self.getAndValidateInput(str, "Enter mother's name: ")
        _marital_status = self.getAndValidateInput(str, "Enter marital status (Single/Married): ")
        _dept = self.getAndValidateInput(str, "Enter department name: ")
        _designation = self.getAndValidateInput(str, "Enter designation: ")
        _nationality = self.getAndValidateInput(str, "Enter nationality: ")
        _joining_date = self.getAndValidateInput(str, "Enter joining date (DD-MM-YYYY): ", self.validateDate)
        _present_address = self.getAndValidateInput(str, "Enter present address: ")
        _permanent_address = self.getAndValidateInput(str, "Enter permanent address: ")

        _educational_degrees = []
        no_of_degrees = int(input("How many educational degress do you want to add? => "))
        for i in range(no_of_degrees):
            _degree_name = self.getAndValidateInput(str, "Enter educational degree name: ")
            _institute_name = self.getAndValidateInput(str, "Enter educational institute name: ")
            _major = self.getAndValidateInput(str, "Enter educational major: ")
            _location = self.getAndValidateInput(str, "Enter institute location: ")
            _gpa = self.getAndValidateInput(float, "Enter GPA: ")
            _gpa_scale = self.getAndValidateInput(float, "Enter GPA scale: ")
            _year_of_passing = self.getAndValidateInput(str, "Enter year of passing (YYYY): ", self.validate_year)

            degree = EducationalDegree(_degree_name, _institute_name, _major, _location, _gpa, _gpa_scale, _year_of_passing)
            _educational_degrees.append(degree)

        _experience = []
        no_of_exp = int(input("How many job experiences do you want to add? => "))
        for i in range(no_of_exp):
            _company_name = self.getAndValidateInput(str, "Enter company's name: ")
            _position = self.getAndValidateInput(str, "Enter the job title: ")
            _joining_date = self.getAndValidateInput(str, "Enter joining date (DD-MM-YYYY): ", self.validateDate)
            _ending_date = self.getAndValidateInput(str, "Enter leaving date (DD-MM-YYYY): ", self.validateDate)
            _location = self.getAndValidateInput(str, "Enter company's location: ")

            exp = Experience(_company_name,_position, _joining_date, _ending_date, _location)
            _experience.append(exp)

        employee = Employee(_employee_id, _name, _dob, _nid, _email, _phone_no, _gender, _father_name, _mother_name, _marital_status, _dept, _designation, _nationality, _joining_date, _present_address, _permanent_address, _educational_degrees, _experience)
        
        self._employees.append(employee)

    def printDataTable(self, data, flag):
        headers = ["Employee ID", "Name", "Date of Birth", "NID", "Email", "Phone no.", "Gender", "Department","Designation", "Marital Status", "Present Address"]
        dataRow = []
        if flag == "single":
            item = data
            dataRow.append([item._employee_id, item._name, item._dob, item._nid, item._email, item._phone_no, item._gender, item._dept, item._designation, item._marital_status, item._present_address])
            return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  
        else:   
            for item in data:
                dataRow.append([item._employee_id, item._name, item._dob, item._nid, item._email, item._phone_no, item._gender, item._dept, item._designation, item._marital_status, item._present_address])
            return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  

    def getAllEmployees(self):
        emp = self._employees
        return self.printDataTable(emp, "multiple")
    
    def searchAnEmployee(self, input_text):
        search_result = []
        for item in self._employees:
            if input_text == item._employee_id or input_text.lower() in item._name.lower() or input_text in item._dob or input_text == item._nid or input_text.lower() in item._email or input_text in item._phone_no or input_text.lower() in item._gender.lower() or input_text.lower() in item._father_name.lower() or input_text.lower() in item._mother_name.lower() or input_text.lower() in item._marital_status.lower() or input_text.lower() in item._dept.lower() or input_text.lower() in item._designation.lower() or input_text.lower() in item._nationality.lower() or input_text in item._joining_date or input_text.lower() in item._present_address.lower() or input_text.lower() in item._permanent_address.lower():
                search_result.append(item)
        if len(search_result) == 0:
            return "⚠️  Employee not found!"
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
        self._employees.remove(employee)
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
                        if item._employee_id == emp_id:
                            selected_emp = item
                            break
                    if selected_emp is not None:
                        break
                    else: 
                        print("⚠️  ID didn't match, please try again")

                self.updateEmployeeFields(selected_emp) if action == "update" else self.deleteAnEmployee(selected_emp) 
            else:
                self.updateEmployeeFields(search_result[0]) if action == "update" else self.deleteAnEmployee(search_result[0])
    

print("====================================")
print("||   Employee Management System   ||")
print("====================================")
print("\n")

print("Select an option to continue: ")
options = """1. Add an employee 
2. Show all employees
3. Find employee
4. Update an employee
5. Delete an employee
6. Exit app
help: Help"""
print(options)


employees = EmployeeController()

while True: 
    choice = input("=> ")

    match choice:
        case "1":
            print("=> Please give all the information: ")
            employees.addAnEmployee()
            print("✅ Employee info saved!")

        case "2":
            print("=> All Employee Details:")
            print(employees.getAllEmployees())

        case "3":
            search_input = input("=> Search for employee: ")
            employees.searchAnEmployee(search_input)

        case "4":
            print("=> Update operation selected: ")
            search_input = input("=> Search for employee: ")
            search_result = employees.searchAnEmployee(search_input.strip())
            employees.selectEmployeeAndPerformUpdateOrDelete(search_result, "update")

        case "5":
            print("=> Delete operation selected:")
            search_input = input("=> Search for employee: ")
            search_result = employees.searchAnEmployee(search_input.strip())
            employees.selectEmployeeAndPerformUpdateOrDelete(search_result, "delete")
            
        case "6":
            print("Exiting the app....")
            break

        case "help":
            print(options)
            





