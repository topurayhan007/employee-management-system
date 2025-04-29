# All CRUD operations of Education
from models.education import EducationalDegree
from services.input_validation_service import InputValidator
from services.display_service import print_degree_table
from database.education_db import add_degree, search_degrees_of_an_employee, update_a_degree_of_an_employee, delete_a_degree_of_an_employee

class EducationService:
    validator = InputValidator()

    def add_educational_degree(self, _employee_id):
        _degree_name = self.validator.get_input_and_validate(str, "Enter educational degree name: ")
        _institute_name = self.validator.get_input_and_validate(str, "Enter educational institute name: ")
        _major = self.validator.get_input_and_validate(str, "Enter educational major: ")
        _location = self.validator.get_input_and_validate(str, "Enter institute location: ")
        _gpa = self.validator.get_input_and_validate(float, "Enter GPA: ")
        _gpa_scale = self.validator.get_input_and_validate(float, "Enter GPA scale: ")
        _year_of_passing = self.validator.get_input_and_validate(str, "Enter year of passing (YYYY): ", self.validator.validate_year, "⚠️  Invalid year format")

        degree = EducationalDegree(_employee_id, _degree_name, _institute_name, _major, _location, _gpa, _gpa_scale, _year_of_passing)
        # Insert into DB by calling the method
        degree_id = add_degree(degree)

        if degree_id is not None:
            print("✅ Saved into database!")
        else:
            print("⚠️  Couldn't add to database!")

    def search_educational_degrees_of_an_employee(self, employee_id):
        degrees = search_degrees_of_an_employee(employee_id)
        if degrees is None or len(degrees) == 0:
            print("⚠️  No educational degrees found for the employee!")
            return None
        else: 
            print(print_degree_table(degrees, "multiple"))
            return degrees


    def delete_educational_degree(self, degree_id):
        result = delete_a_degree_of_an_employee(degree_id)
        if result == 1:
            print("✅ Educational degree deleted from database!")
        else:
            print("⚠️  Couldn't delete from database!")

    def update_degree_fields_and_put_into_db(self, data):
        item = data
        print("=> Degree selected:")
        print(print_degree_table(item, "single"))
        print("These are the fields you can update: ")
        print("Degree Name, Institute Name, Major, Location, GPA, GPA Scale, Year of Passing")
        fields = input("From the above fields type the fields you want to update separated by commas: ")
        fields = fields.split(",")

        for field in fields:
            if field.strip().lower() in "Degree Name".lower():
                item['degree_name'] = self.validator.get_input_and_validate(str, "Enter new degree name: ")
            elif field.strip().lower() in "Institute Name".lower():
                item['institute_name'] = self.validator.get_input_and_validate(str, "Enter new institute name: ")
            elif field.strip().lower() in "Major".lower():
                item['major'] = self.validator.get_input_and_validate(str, "Enter new major: ")
            elif field.strip().lower() in "Location".lower():
                item['location'] = self.validator.get_input_and_validate(str, "Enter new location: ")
            elif field.strip().lower() in "GPA".lower():
                item['gpa'] = self.validator.get_input_and_validate(float, "Enter new gpa: ")
            elif field.strip().lower() in "GPA Scale".lower():
                item['gpa_scale'] = self.validator.get_input_and_validate(float, "Enter new gpa scale: ")
            elif field.strip().lower() in "Year of Passing".lower():
                item['year_of_passing'] = self.validator.get_input_and_validate(str, "Enter new year of passing (YYYY): ", self.validator.validate_year, "⚠️  Invalid year format")
            else:
                print("⚠️  You entered an invalid field, skipping this field...")

        result = update_a_degree_of_an_employee(item)
        if result == 1:
            print("✅ Education degree updated successfully!") 
        else:
            print("✅ Couldn't update degree, please try again!") 

    def update_educational_degree(self, degrees, degree_id):
        for item in degrees:
            if item['degree_id'] == degree_id:
                self.update_degree_fields_and_put_into_db(item)



    