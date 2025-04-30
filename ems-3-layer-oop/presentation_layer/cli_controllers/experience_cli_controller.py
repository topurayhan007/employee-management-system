from application_layer.classes.experience import Experience
from application_layer.services.experience_service import ExperienceService
from application_layer.services.input_validator_service import InputValidator
from presentation_layer.table_printer import Printer

class ExperienceCliController:
    def __init__(self, experience_service: ExperienceService):
        self.validator = InputValidator()
        self.printer = Printer()
        self.experience_service = experience_service

        
        