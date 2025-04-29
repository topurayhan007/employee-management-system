# All CRUD operations of Experience
from models.experience import Experience
from services.input_validation_service import InputValidator
from services.display_service import print_experience_table
from database.experience_db import add_experience, search_experiences_of_an_employee, update_an_experience_of_an_employee, delete_an_experience_of_an_employee

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
        _joining_date = self.validator.get_input_and_validate(str, "Enter joining date (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
        _ending_date = self.validator.get_input_and_validate(str, "Enter leaving date (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
        _location = self.validator.get_input_and_validate(str, "Enter company's location: ")
    
        experience = Experience(_employee_id, _company_name, _position, _joining_date, _ending_date, _location)
        # Insert into the DB

        experience_id = add_experience(experience)

        if experience_id is not None:
            print("✅ Saved into database!")
        else:
            print("⚠️  Something went wrong!")        

    def search_experience(self, employee_id):
        experiences = search_experiences_of_an_employee(employee_id)
        if experiences is None or len(experiences) == 0:
            print("⚠️  No experiences found for the employee!")
            return None
        else: 
            print(print_experience_table(experiences, "multiple"))
            return experiences

    def delete_experience(self, experience_id):
        result = delete_an_experience_of_an_employee(experience_id)
        if result == 1:
            print("✅ Experience deleted from database!")
        else:
            print("⚠️  Couldn't delete from database!")

    
    def update_experience_fields_and_put_into_db(self, data):
        item = data
        print("=> Experience selected:")
        print(print_experience_table(item, "single"))
        print("These are the fields you can update: ")
        print("Company Name, Position, Joining Date, Ending Date, Location")
        fields = input("From the above fields type the fields you want to update separated by commas: ")
        fields = fields.split(",")  

        for field in fields:
            if field.strip().lower() in "Company Name".lower():
                item['company_name'] = self.validator.get_input_and_validate(str, "Enter new company's name: ")
            elif field.strip().lower() in "Position".lower():
                item['position'] = self.validator.get_input_and_validate(str, "Enter new job title: ")
            elif field.strip().lower() in "Joining Date".lower():
                item['joining_date'] = self.validator.get_input_and_validate(str, "Enter new joining date (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
            elif field.strip().lower() in "Ending Date".lower():
                item['ending_date'] = self.validator.get_input_and_validate(str, "Enter new leaving date (YYYY-MM-DD): ", self.validator.validate_date, "⚠️  Invalid date format")
            elif field.strip().lower() in "Location".lower():
                item['location'] = self.validator.get_input_and_validate(str, "Enter new company's location: ")
            else:
                print("⚠️  You entered an invalid field, skipping this field...")

        result = update_an_experience_of_an_employee(item)
        if result == 1:
            print("✅ Experience updated successfully!") 
        else:
            print("✅ Couldn't update experience, please try again!")


    def update_experience(self, experiences, experience_id):
        for item in experiences:
            if item['experience_id'] == experience_id:
                self.update_experience_fields_and_put_into_db(item)

