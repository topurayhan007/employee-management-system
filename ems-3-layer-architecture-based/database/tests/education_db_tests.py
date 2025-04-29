# Test cases to test education database operations
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from models.education import EducationalDegree
from database.education_db import add_degree, search_degrees_of_an_employee, delete_a_degree_of_an_employee, update_a_degree_of_an_employee

degree = EducationalDegree(
    2,                 
    "B.Sc Test",       
    "Test Institute",  
    "Testing",         
    "Test City",       
    3.5,               
    4.0,               
    "2020"             
)


updated_degree = {
    'employee_id': 2,
    'degree_name': "B.Sc Test",
    'institute_name': "Test Institute",
    'major': "Quality Assurance",
    'location': "Updated City",
    'gpa': 3.8,
    'gpa_scale': 4.0,
    'year_of_passing': "2020",
    'degree_id': 1
}

result = add_degree(degree)
print(1, result)

result2 = search_degrees_of_an_employee(2)
print(2, result2)

result3 = update_a_degree_of_an_employee(updated_degree)
print(3, result3)

result4 = delete_a_degree_of_an_employee(8)
print(4, result4)








