import mysql.connector

#View employee count data per country
def get_employees_country(mycursor):

    #get user input to view country data
    user_choice = input("Enter a country name for specific country or (ALL) to view all countries: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from EmployeesPerCountry"
    else:
        sql_query = f"Select * from EmployeesPerCountry where country_name = '{user_choice}'"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----Number of Employees Per Country-----\n")
    found = False
    for record in query_result:
        #check if the user entered country exists in the database and if not found and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"{record[0]}: {record[1]} employees")
            found = True

    if not found:
        print(f"There are no employees in {user_choice} country")

    return

def get_manager_count_dept(mycursor):
    #get user input to view country data
    user_choice = input("Enter department name for specific department or (ALL) to view all departments: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select department_name, COUNT(department_name) AS 'Number of Managers' From managers group by department_name order by COUNT(department_name) desc"
    else:
        sql_query = f"Select department_name, COUNT(department_name) AS 'Number of Managers' from managers where department_name = '{user_choice}'group by department_name order by COUNT(department_name) desc"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----Managers Per Department-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"{record[0]} Department: {record[1]} managers")
            found = True

    if not found:
        print(f"There are no managers in {user_choice} department")

    return

def get_dependent_data_perjob(mycursor):
    #get user input to view country data
    user_choice = input("Enter job title or (ALL) to view data for all job titles: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from DependentsByJobTitle"
    else:
        sql_query = f"Select * from DependentsByJobTitle where job_title = '{user_choice}'"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----Job Titles with the most Dependents-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"{record[0]}: {record[1]} dependents")
            found = True

    if not found:
        print(f"There are no dependents in {user_choice} job title")

    return

def get_dept_hired_byyear(mycursor):
    #get user input to view country data
    
    user_choice = input("Enter year or (ALL) to view hiring data for all years in departments: ")
    
    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from DepartmentHiresByYear"
    else:
        sql_query = f"Select * from DepartmentHiresByYear where year = '{int(user_choice)}'" #convert user input to int if not it does not work 
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----All hired department by years-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == 'ALL' or int(user_choice) == record[0]:
            print(f"\n{record[0]} {record[1]}: {record[2]} hires")
            found = True

    if not found:
        print(f"There is no hiring data for year {user_choice}")

    return

def get_avg_salary_bytitle(mycursor):
    #get user input to view country data
    user_choice = input("Enter job title or (ALL) for average salary data for all job titles: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from AvgSalaryByJobTitle"
    else:
        sql_query = f"Select * from AvgSalaryByJobTitle where job_title = '{user_choice}'"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----Average salary per job titles-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"\n{record[0]}: ${round(record[1], 2)}")
            found = True

    if not found:
        print(f"There is no salary data for {user_choice} department")

    return

def get_avg_salary_bydept(mycursor):
    #get user input to view country data
    user_choice = input("Enter the department or (ALL) for average salary by department: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from AvgSalaryByDepartment"
    else:
        sql_query = f"Select * from AvgSalaryByDepartment where department_name = '{user_choice}'"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----JAverage Salaries by Department-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"\n{record[0]}: ${round(record[1], 2)}")
            found = True

    if not found:
        print(f"There is no salary data for {user_choice} department")

    return

def get_dependent_data_byemployee(mycursor): 
    #get user input to view country data
    user_choice = input("Enter employee first name and last name or (ALL) to view data for all job titles: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from EmployeeDependents"
    else:
        sql_query = f"Select * from EmployeeDependents where first_name = '{user_choice.split()[0]}' and last_name = '{user_choice.split()[1]}'"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----Employees with Dependents-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == 'ALL' or record[0].upper() == user_choice.split()[0].upper() and record[1].upper() == user_choice.split()[1].upper():
            print(f"\n{record[0]} {record[1]}: {record[4]} dependents")
            found = True

    if not found:
        print(f"There are no dependents data for {user_choice}")

    return

def get_location_data_byregion(mycursor):
    #get user input to view country data
    user_choice = input("Enter a region or (ALL) for location data for all regions: ")

    #create sql query based on user input
    if user_choice.upper() == 'ALL':
        sql_query = "Select * from CountryLocation"
    else:
        sql_query = f"Select * from CountryLocation where region_name = '{user_choice}'"
        

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through the query_result and show the results
    print("\n-----Location data by region-----\n")
    found = False
    for record in query_result:
        #check if the user entered dept name exists in the database and if it doesnt exist and not equal to 'ALL', print the second if statement
        if user_choice.upper() == record[0].upper() or user_choice.upper() == 'ALL':
            print(f"\n{record[0]}: {record[1]}")
            found = True

    if not found:
        print(f"There is no location data for {user_choice} region")

    return


def print_menu():
    print("\nChoose an option")
    print("---------------------")
    print("------------- VIEW DATA -------------")
    print("1. View employee count data per country")
    print("2. View manager count by department")
    print("3. View dependent data per job title")
    print("4. View hiring data by year and department")
    print("5. View average salary data by job title")
    print("6. View average salary data by department")
    print("7. View dependent data by employee")
    print("8. View location data by region")
    print("17. Exit Application")
    return

def get_user_choice():
    print_menu()
    choice = int(input("\nEnter Choice: "))
    return choice

def main():
    #create conection object to connect to database
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

    #create database cursor
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
            elif user_choice == 17:
                print("Bye!!!")
                break
            else:
                print("Error, number must be 1-9")
        except ValueError:
                print("Please enter a number.")


main()