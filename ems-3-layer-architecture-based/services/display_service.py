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
