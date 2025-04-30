from application_layer.classes.education import EducationalDegree
from database_layer.setup import DatabaseManager
from database_layer.storage_managers.education_db_manager import EducationDBManager

class EducationService:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.education_db_manager = EducationDBManager(db_manager)