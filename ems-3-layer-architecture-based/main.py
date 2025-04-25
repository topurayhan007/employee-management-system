# This is a console based application made using 3-layer architecture
from services.employee_service import EmployeeService

def main():
    print("====================================")
    print("||   Employee Management System   ||")
    print("==================================== \n")

    options = """Select an option to continue: 
1. Add an employee 
2. Show all employees
3. Find employee
4. Update an employee
5. Delete an employee
6. Exit app
help: Help \n"""
    print(options)

    employees = EmployeeService()

    while True: 
        choice = input("=> ")

        match choice:
            case "1":
                print("=> Please give all the information: ")
                employees.add_an_employee()
                print("✅ Employee info saved!")

            case "2":
                print("=> All Employee Details:")
                print(employees.getAllEmployees())

            case "3":
                search_input = input("=> Search for employee: ")
                employees.searchAnEmployee(search_input)

            case "4":
                print("=> Update operation selected: ")
                search_input = input("=> Search for employee: ")
                search_result = employees.searchAnEmployee(search_input.strip())
                employees.selectEmployeeAndPerformUpdateOrDelete(search_result, "update")

            case "5":
                print("=> Delete operation selected:")
                search_input = input("=> Search for employee: ")
                search_result = employees.searchAnEmployee(search_input.strip())
                employees.selectEmployeeAndPerformUpdateOrDelete(search_result, "delete")
                
            case "6":
                print("Exiting the app....")
                break

            case "help":
                print(options)
              
if __name__== "__main__":
    main() 