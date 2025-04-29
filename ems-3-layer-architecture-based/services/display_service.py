# All work of printing tables are done here
from tabulate import tabulate

def print_employee_table(data, flag):
    headers = ["ID", "Name", "DoB", "NID", "Email", "Phone no.", "Gender", "Marital Status", "Department", "Designation", "Joining Date", "Present Address"]
    dataRow = []
    if flag == "single":
        item = data
        dataRow.append([item['employee_id'], item['name'], item['date_of_birth'], item['nid'], item['email'], item['phone_no'], item['gender'], item['marital_status'], item['dept'], item['designation'], item['joining_date'], item['present_address']])
        return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  
    else:   
        for item in data:
            dataRow.append([item['employee_id'], item['name'], item['date_of_birth'], item['nid'], item['email'], item['phone_no'], item['gender'], item['marital_status'], item['dept'], item['designation'], item['joining_date'], item['present_address']])
        return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  

def print_degree_table(data, flag):
    headers = ["ID", "Employee ID", "Degree Name", "Institute Name", "Major", "Location", "GPA", "GPA Scale", "Year of Passing"]
    dataRow = []
    if flag == "single":
        item = data
        dataRow.append([item['degree_id'], item['employee_id'], item['degree_name'], item['institute_name'], item['major'], item['location'], item['gpa'], item['gpa_scale'], item['year_of_passing']])
        return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  
    else:   
        for item in data:
            dataRow.append([item['degree_id'], item['employee_id'], item['degree_name'], item['institute_name'], item['major'], item['location'], item['gpa'], item['gpa_scale'], item['year_of_passing']])
        return tabulate(dataRow, headers=headers, tablefmt="fancy_grid") 
    
def print_experience_table(data, flag):
    headers = ["ID", "Employee ID", "Company Name", "Position", "Joining Date", "Ending Date", "Location"]
    dataRow = []
    if flag == "single":
        item = data
        dataRow.append([item['experience_id'], item['employee_id'], item['company_name'], item['position'], item['joining_date'], item['ending_date'], item['location']])
        return tabulate(dataRow, headers=headers, tablefmt="fancy_grid")  
    else:   
        for item in data:
            dataRow.append([item['experience_id'], item['employee_id'], item['company_name'], item['position'], item['joining_date'], item['ending_date'], item['location']])
        return tabulate(dataRow, headers=headers, tablefmt="fancy_grid") 