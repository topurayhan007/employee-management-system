# All CRUD operations of Education
from models.education import EducationalDegree
from services.input_validation_service import InputValidator
from database.education_db import add_degree

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

    def delete_educational_degree(self, degree_id):
        pass

    def update_educational_degree(self, degree_id):
        pass
    