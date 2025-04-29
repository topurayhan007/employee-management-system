# Test cases to test education database operations
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from models.experience import Experience
from database.experience_db import add_experience, search_experiences_of_an_employee, delete_an_experience_of_an_employee, update_an_experience_of_an_employee

experience = Experience(
    2,                 
    "Test Company",       
    "Test Position",  
    "2022-01-01",         
    "2025-01-01",       
    "Test Location"            
)


updated_experience = {
    'employee_id': 2,
    'company_name': "Update Company",
    'position': "Updated Position",
    'joining_date': "2021-01-01",
    'ending_date': "2024-12-31",
    'location': "Updated Location",
    'experience_id': 1
}

result = add_experience(experience)
print(1, result)

result2 = search_experiences_of_an_employee(2)
print(2, result2)

result3 = update_an_experience_of_an_employee(updated_experience)
print(3, result3)

result4 = delete_an_experience_of_an_employee(1)
print(4, result4)








