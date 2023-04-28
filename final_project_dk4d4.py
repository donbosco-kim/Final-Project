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
            elif user_choice == 9:
                print("Bye!!!")
                break
            else:
                print("Error, number must be 1-9")
        except ValueError:
                print("Please enter a number.")


main()