# All CRUD operations of Experience
from models.experience import Experience
from services.input_validation_service import InputValidator
from database.experience_db import add

class ExperienceService:
    validator = InputValidator()
    def __init__(self):
        self._experiences = []

    def get_experiences_of_an_employee(self, _employee_id):
        # call the method from the database service to get the experiences
        pass

    def add_experience(self, _employee_id):
        _company_name = self.validator.get_input_and_validate(str, "Enter company's name: ")
        _position = self.validator.get_input_and_validate(str, "Enter the job title: ")
        _joining_date = self.validator.get_input_and_validate(str, "Enter joining date (DD-MM-YYYY): ", self.validator.validate_date, "⚠️  Invalid date format")
        _ending_date = self.validator.get_input_and_validate(str, "Enter leaving date (DD-MM-YYYY): ", self.validator.validate_date, "⚠️  Invalid date format")
        _location = self.validator.get_input_and_validate(str, "Enter company's location: ")
    
        experience = Experience(_employee_id, _company_name, _position, _joining_date, _ending_date, _location)
        # Insert into the DB
        

    def delete_experience(self, experience_id):
        pass
    
    def update_experience(self, experience_id):
        pass