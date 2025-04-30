from application_layer.classes.education import EducationalDegree
from database_layer.setup import DatabaseManager

class EducationDBManager:
    def __init__(self, db_manager:DatabaseManager):
        self.db_manager = db_manager
        self.db_connection = db_manager.get_db_connection()
    
