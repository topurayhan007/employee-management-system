from application_layer.classes.experience import Experience
from database_layer.setup import DatabaseManager
from database_layer.storage_managers.experience_db_manager import ExperienceDBManager
class ExperienceService:
    def __init__(self, db_manager: ExperienceDBManager):
        self.db_manager = db_manager
        self.experience_db_manager = ExperienceDBManager(db_manager)
        