from application_layer.classes.experience import Experience
from database_layer.setup import DatabaseManager
from database_layer.storage_managers.experience_db_manager import ExperienceDBManager
class ExperienceService:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.experience_db_manager = ExperienceDBManager(db_manager)
        
    def add_experience(self, experince: Experience):
        result = self.experience_db_manager
        return result

    def search_experiences_of_an_employee(self, employee_id):
        experiences = self.experience_db_manager
        return experiences

    def delete_an_experience_of_an_employee(self, experience_id):
        result = self.experience_db_manager
        return result

    def update_an_experience_of_an_employee(self, experience: Experience):
        result = self.experience_db_manager
        return result