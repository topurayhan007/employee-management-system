# This is a console based application made using 3-layer architecture
from services.employee_service import EmployeeService
from services.education_service import EducationService
from services.experience_service import ExperienceService
from database.setup import initialize_database

def main():
    # Initialize database
    initialize_database()

    print("====================================")
    print("||   Employee Management System   ||")
    print("==================================== \n")

    options = """Select an option to continue: 
1.  Add an employee 
2.  Show all employees
3.  Find employee
4.  Update an employee
5.  Delete an employee
6.  Add degree/experience of an employee
7.  Find degrees/experiences of an employee
8.  Update degree/experience of an employee
9.  Delete degree/experience of an employee
10. Exit app
help: Help \n"""
    print(options)

    employees = EmployeeService()
    education_service = EducationService()
    experience_service = ExperienceService()

    while True: 
        choice = input("=> ")

        match choice:
            case "1":
                print("=> Please give all the information: ")
                employees.add_an_employee()
                print("✅ Employee info saved!")

            case "2":
                print("=> All Employee Details:")
                employees.getAllEmployees()

            case "3":
                search_input = input("=> Search for employee: ")
                employees.searchAnEmployee(search_input.strip())

            case "4":
                print("=> Update operation selected: ")
                search_input = input("=> Search for employee: ")
                search_result = employees.searchAnEmployee(search_input.strip())
                if search_result is not None:
                    employees.selectEmployeeAndPerformUpdateOrDelete(search_result, "update")

            case "5":
                print("=> Delete operation selected:")
                search_input = input("=> Search for employee: ")
                search_result = employees.searchAnEmployee(search_input.strip())
                if search_result is not None:
                    employees.selectEmployeeAndPerformUpdateOrDelete(search_result, "delete")

            case "6":
                print("Add degree/experience operation selected:")
                choice_input = input("=> Type degree/experience that you want to add to an employee: ")
                if choice_input.strip().lower() in "Degree".lower():
                    employee_id = input("=> Type the employee ID: ")
                    education_service.add_educational_degree(employee_id)
                elif choice_input.strip().lower() in "Experience".lower():
                    employee_id = input("=> Type the employee ID: ")
                    experience_service.add_experience(employee_id)
                else:
                    print("⚠️  Invalid, please try again!")
                    pass
                
            case "7":
                print("=> Finding degree/experience operation selected:")
                choice_input = input("=> Type degree/experience that you want to see of an employee: ")
                if choice_input.strip().lower() in "Degree".lower():
                    employee_id = input("=> Type the employee ID: ")
                    education_service.search_educational_degrees_of_an_employee(employee_id)
                elif choice_input.strip().lower() in "Experience".lower():
                    employee_id = input("=> Type the employee ID: ")
                    experience_service.search_experience(employee_id)
                else:
                    print("⚠️  Invalid, please try again!")
                    pass

            case "8":
                print("=> Updating degree/experience operation selected:")
                choice_input = input("=> Type degree/experience that you want to update of an employee: ")
                if choice_input.strip().lower() in "Degree".lower():
                    employee_id = input("=> Type the employee ID: ")
                    degrees = education_service.search_educational_degrees_of_an_employee(employee_id)
                    if degrees is not None:
                        degree_id = int(input("Type the ID that you want to update: "))
                        education_service.update_educational_degree(degrees, degree_id)

                elif choice_input.strip().lower() in "Experience".lower():
                    employee_id = input("=> Type the employee ID: ")
                    experiences = experience_service.search_experience(employee_id)
                    if experiences is not None:
                        experience_id = int(input("Type the ID that you want to update: "))
                        experience_service.update_experience(experiences, experience_id)

                else:
                    print("⚠️  Invalid, please try again!")
                    pass

            case "9":
                print("=> Deleting degree/experience operation selected:")
                choice_input = input("=> Type degree/experience that you want to update of an employee: ")
                if choice_input.strip().lower() in "Degree".lower():
                    employee_id = input("=> Type the employee ID: ")
                    degrees = education_service.search_educational_degrees_of_an_employee(employee_id)
                    if degrees is not None:
                        degree_id = int(input("Type the ID that you want to delete: "))
                        education_service.delete_educational_degree(degree_id)

                elif choice_input.strip().lower() in "Experience".lower():
                    employee_id = input("=> Type the employee ID: ")
                    experiences = experience_service.search_experience(employee_id)
                    if experiences is not None:
                        experience_id = int(input("Type the ID that you want to delete: "))
                        experience_service.delete_experience(experience_id)

                else:
                    print("⚠️  Invalid, please try again!")
                    pass

            case "10":
                print("Exiting the app....")
                break

            case "help":
                print(options)
              
if __name__== "__main__":
    main() 