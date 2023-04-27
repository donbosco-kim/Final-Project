import mysql.connector

#View employee count data per country
def get_employees_country(mycursor):

    #get user input to view country data
    country_choice = input("Enter a country name for specific country or (ALL) to view all countries: ")

    #create sql query based on user input
    if country_choice.lower() == 'all':
        sql_query = f"Select * from EmployeesPerCountry where country_name = '{country_choice}'"
    else:
        sql_query = "Select * from EmployeesPerCountry"

    #execute the query
    mycursor.execute(sql_query)

    #get the query result
    query_result = mycursor.fetchall()

    #loop through results and show the number of employees in UK
    print("\n-----Number of Employees Per Country-----\n")
    for record in query_result:
        print(f"{record[0]}: {record[1]}")

    return

def print_menu():
    print("\nChoose an option")
    print("---------------------")
    print("------------- VIEW DATA -------------")
    print("1. View employee count data per country")
    print("2. Show number of managers per department")
    print("3. Show the job titles with the most dependents")
    print("4. Show number of department hires in 1998")
    print("5. Show average salary for programmers")
    print("6. Show department name with the lowest average salary")
    print("7. Show employees with no dependents")
    print("8. Show regions with no locations")
    print("8. Exit Application")
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
            elif user_choice == 9:
                print("Bye!!!")
                break
            else:
                print("Error, number must be 1-9")
        except ValueError:
                print("Please enter a number.")


main()