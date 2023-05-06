import mysql.connector

# ____________________________________VIEW DATA____________________________________________

# View employee count data per country


def get_employees_country(mycursor):

    # get user input to view country data
    user_choice = input(
        "Enter a country name for specific country or (ALL) to view all countries: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from EmployeesPerCountry"
    else:
        sql_query = f"Select * from EmployeesPerCountry where country_name = '{user_choice}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----Number of Employees Per Country-----\n")
    found = False
    for record in query_result:
        # check if the user entered country exists in the database and if not found and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"{record[0]}: {record[1]} employees")
            found = True

    if not found:
        print(f"There are no employees in {user_choice} country")

    return


def get_manager_count_dept(mycursor):
    # get user input to view country data
    user_choice = input(
        "Enter department name for specific department or (ALL) to view all departments: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select department_name, COUNT(department_name) AS 'Number of Managers' From managers group by department_name order by COUNT(department_name) desc"
    else:
        sql_query = f"Select department_name, COUNT(department_name) AS 'Number of Managers' from managers where department_name = '{user_choice}'group by department_name order by COUNT(department_name) desc"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----Managers Per Department-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"{record[0]} Department: {record[1]} managers")
            found = True

    if not found:
        print(f"There are no managers in {user_choice} department")

    return


def get_dependent_data_perjob(mycursor):
    # get user input to view country data
    user_choice = input(
        "Enter job title or (ALL) to view data for all job titles: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from DependentsByJobTitle"
    else:
        sql_query = f"Select * from DependentsByJobTitle where job_title = '{user_choice}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----Job Titles with the most Dependents-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"{record[0]}: {record[1]} dependents")
            found = True

    if not found:
        print(f"There are no dependents in {user_choice} job title")

    return


def get_dept_hired_byyear(mycursor):
    # get user input to view country data

    user_choice = input(
        "Enter year or (ALL) to view hiring data for all years in departments: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from DepartmentHiresByYear"
    else:
        # convert user input to int if not it does not work
        sql_query = f"Select * from DepartmentHiresByYear where year = '{int(user_choice)}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----All hired department by years-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == 'ALL' or int(user_choice) == record[0]:
            print(f"\n{record[0]} {record[1]}: {record[2]} hires")
            found = True

    if not found:
        print(f"There is no hiring data for year {user_choice}")

    return


def get_avg_salary_bytitle(mycursor):
    # get user input to view country data
    user_choice = input(
        "Enter job title or (ALL) for average salary data for all job titles: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from AvgSalaryByJobTitle"
    else:
        sql_query = f"Select * from AvgSalaryByJobTitle where job_title = '{user_choice}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----Average salary per job titles-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"\n{record[0]}: ${round(record[1], 2)}")
            found = True

    if not found:
        print(f"There is no salary data for {user_choice} department")

    return


def get_avg_salary_bydept(mycursor):
    # get user input to view country data
    user_choice = input(
        "Enter the department or (ALL) for average salary by department: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from AvgSalaryByDepartment"
    else:
        sql_query = f"Select * from AvgSalaryByDepartment where department_name = '{user_choice}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----JAverage Salaries by Department-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"\n{record[0]}: ${round(record[1], 2)}")
            found = True

    if not found:
        print(f"There is no salary data for {user_choice} department")

    return


def get_dependent_data_byemployee(mycursor):
    # get user input to view country data
    user_choice = input(
        "Enter employee first name and last name or (ALL) to view data for all job titles: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from EmployeeDependents"
    else:
        sql_query = f"Select * from EmployeeDependents where first_name = '{user_choice.split()[0]}' and last_name = '{user_choice.split()[1]}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----Employees with Dependents-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == 'ALL' or record[0].upper() == user_choice.split()[0].upper() and record[1].upper() == user_choice.split()[1].upper():
            print(f"\n{record[0]} {record[1]}: {record[4]} dependents")
            found = True

    if not found:
        print(f"There are no dependents data for {user_choice}")

    return


def get_location_data_byregion(mycursor):
    # get user input to view country data
    user_choice = input(
        "Enter a region or (ALL) for location data for all regions: ")

    # create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from CountryLocation"
    else:
        sql_query = f"Select * from CountryLocation where region_name = '{user_choice}'"

    # execute the query
    mycursor.execute(sql_query)

    # get the query result
    query_result = mycursor.fetchall()

    # loop through the query_result and show the results
    print("\n-----Location data by region-----\n")
    found = False
    for record in query_result:
        # check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"\n{record[0]}: {record[1]}")
            found = True

    if not found:
        print(f"There is no location data for {user_choice} region")

    return
# ____________________________________________VIEW DATA END_____________________________________

# ____________________________________________ADD DATA__________________________________________


def add_dependent(mycursor):
    # get user input
    user_choice_first = input("Enter dependent first name: ")
    user_choice_last = input("Enter dependent last name: ")
    user_choice_relation = input("Enter relationship: ")
    user_choice_employeeId = input("Enter employee ID: ")

    sql_query = f"Insert Into dependents (first_name, last_name, relationship, employee_id) Values ('{user_choice_first}', '{user_choice_last}', '{user_choice_relation}', {user_choice_employeeId});"

    try:
        # execute the query
        mycursor.execute(sql_query)

        print(f"\nSuccess: {mycursor.rowcount} dependent added")
    except mysql.connector.Error as error:
        print(f"\nFailed to insert into dependents table {error}")


def add_job(mycursor):
    # get user input
    job_title = input("Enter new job title: ")
    while (True):
        try:
            min_salary = float(input("Enter minimum salary: "))
            max_salary = float(input("Enter maximum sallary: "))
            if max_salary < min_salary:
                print("Maximum salary can't be less than the minimum salary")
                continue
            else:
                sql_query = f"Insert into jobs (job_title, min_salary, max_salary) Values ('{job_title}', '{min_salary}', '{max_salary}');"
            mycursor.execute(sql_query)
            print(f"\nSuccess: {mycursor.rowcount} job added")
            break
        except mysql.connector.Error as error:
            print(f"\nFailed to insert into dependents table {error}")
            break

# ____________________________________________ADD DATA END______________________________________

# ____________________________________________DELETE DATA__________________________________________


def delete_employee(mycursor):
    try:
        employee_id = int(input("Enter employee ID to be deleted: "))
        delete_query = f"Delete from employees where employee_id = '{employee_id}';"
        mycursor.execute(delete_query)
        print(f"\nSuccess: {mycursor.rowcount} employee was deleted")
    except mysql.connector.Error as error:
        print(f"\nFailed to delete employee from employees table {error}")
        # print("Please enter a number")


def delete_dependent(mycursor):
    try:
        dependent_id = int(input("Enter dependent ID to be deleted: "))
        delete_query = f"Delete from dependents where dependent_id = '{dependent_id}';"
        mycursor.execute(delete_query)
        print(f"\nSuccess: {mycursor.rowcount} dependent was deleted")
    except mysql.connector.Error as error:
        print(f"\nFailed to delete dependent from dependent table {error}")


# ____________________________________________DELETE DATA END______________________________________

# ____________________________________________UPDATE DATA__________________________________________


def update_employee_fname(mycursor):
    try:
        employee_id = int(input("Enter employee ID to be updated: "))
        employee_fname = input("Enter employee's new first name: ")
        update_query = f"Update employees Set first_name = '{employee_fname}' Where employee_id = '{employee_id}';"
        mycursor.execute(update_query)
        print(f"\nSuccess: {mycursor.rowcount} record was updated.")
        print(f"Employee with id {employee_id} name was updated")
    except mysql.connector.Error as error:
        print(f"\nFailed to update employee from employees table {error}")


def update_employee_lname(mycursor):
    try:
        employee_id = int(input("Enter employee ID to be updated: "))
        employee_lname = input("Enter employee's new last name: ")
        update_query = f"Update employees Set last_name = '{employee_lname}' Where employee_id = '{employee_id}';"
        mycursor.execute(update_query)
        print(f"\nSuccess: {mycursor.rowcount} record was updated.")
        print(f"Employee with id {employee_id} name was updated")
    except mysql.connector.Error as error:
        print(f"\nFailed to update employee from employees table {error}")


def update_min_salary(mycursor):
    job_id = int(input("Enter job ID to be updated: "))
    while (True):
        try:
            min_salary = int(input("Enter jobs' new minimum salary: "))
            if min_salary < 0:
                print("Error: This input must be a number greater than 0")
                continue
            else:
                update_query = f"Update jobs Set min_salary = '{min_salary}' Where job_id = '{job_id}';"
                mycursor.execute(update_query)
                print(f"\nSuccess: {mycursor.rowcount} record was updated.")
                print(f"Job id {job_id} min salary was updated")
                break
        except mysql.connector.Error as error:
            print(f"\nFailed to update minimum salary from jobs table {error}")
            break


def update_max_salary(mycursor):
    job_id = int(input("Enter job ID to be updated: "))
    while (True):
        try:
            max_salary = int(input("Enter jobs' new maximum salary: "))
            if max_salary < 0:
                print("Error: This input must be a number greater than 0")
                continue
            else:
                update_query = f"Update jobs Set max_salary = '{max_salary}' Where job_id = '{job_id}';"
                mycursor.execute(update_query)
                print(f"\nSuccess: {mycursor.rowcount} record was updated.")
                print(f"Employee with id {job_id} name was updated")
                break
        except mysql.connector.Error as error:
            print(f"\nFailed to update maximum salary from jobs table {error}")
            break

# ____________________________________________UPDATE DATA END______________________________________


def print_menu():
    print("\nChoose an option")
    print("-------------------------------------")
    print("------------- VIEW DATA -------------")
    print("1. View employee count data per country")
    print("2. View manager count by department")
    print("3. View dependent data per job title")
    print("4. View hiring data by year and department")
    print("5. View average salary data by job title")
    print("6. View average salary data by department")
    print("7. View dependent data by employee")
    print("8. View location data by region")
    print("\n-------- ADD DATA ---------")
    print("9. Add a dependent")
    print("10. Add a job")
    print("\n-------- DELETE DATA ---------")
    print("11. Delete an employee")
    print("12. Delete a dependent")
    print("\n-------- UPDATE DATA ---------")
    print("13. Update employee first name")
    print("14. Update employee last name")
    print("15. Update job minimum salary")
    print("16. Update job maximum salary")
    print("\n-------- EXIT --------")
    print("17. Exit Application")
    return


def get_user_choice():
    print_menu()
    choice = int(input("\nEnter Choice: "))
    return choice


def main():
    # create conection object to connect to database
    try:
        mydb = mysql.connector.connect(
            host="mysql-container",
            user="root",
            password="root",
            database="project2"
        )
        print("Successfully connected to the database!")
    except Exception as err:
        print(f"Error occured: {err}\nExiting program...")
        quit()

    # create database cursor
    mycursor = mydb.cursor()

    while (True):
        try:
            user_choice = get_user_choice()
            if user_choice == 1:
                get_employees_country(mycursor)
            elif user_choice == 2:
                get_manager_count_dept(mycursor)
            elif user_choice == 3:
                get_dependent_data_perjob(mycursor)
            elif user_choice == 4:
                get_dept_hired_byyear(mycursor)
            elif user_choice == 5:
                get_avg_salary_bytitle(mycursor)
            elif user_choice == 6:
                get_avg_salary_bydept(mycursor)
            elif user_choice == 7:
                get_dependent_data_byemployee(mycursor)
            elif user_choice == 8:
                get_location_data_byregion(mycursor)
            elif user_choice == 9:
                add_dependent(mycursor)
                mydb.commit()
            elif user_choice == 10:
                add_job(mycursor)
                mydb.commit()
            elif user_choice == 11:
                delete_employee(mycursor)
                mydb.commit()
            elif user_choice == 12:
                delete_dependent(mycursor)
                mydb.commit()
            elif user_choice == 13:
                update_employee_fname(mycursor)
                mydb.commit()
            elif user_choice == 14:
                update_employee_lname(mycursor)
                mydb.commit()
            elif user_choice == 15:
                update_min_salary(mycursor)
                mydb.commit()
            elif user_choice == 16:
                update_max_salary(mycursor)
                mydb.commit()
            elif user_choice == 17:
                print("Bye!!!")
                break
            else:
                print("Error, number must be 1-9")
        except ValueError:
            print("Please enter a number.")


main()
