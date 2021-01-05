import sqlite3
from sqlite3 import Error
import employee
import sqldb
import constants
# Use colorama module to print in color
import colorama
from colorama import Fore, Back, Style
import utils


def validate_input():
    """
    This function loop over the user input till it is not valid.
    :return: Valid input option
    :rtype: integer
    """

    option = input("\nplease select one of the valid options: ")
    while check_option(option) == False:
        option = input("please select one of the valid options: ")

    return option


def check_option(option):
    """
    This function check validity of user selection
    :param option: user input selection
    :type option: integer
    :return: check selected option is integer number between 0 and 11
    :rtype: Boolean
    """
    if option in constants.OPTIONS:
        result = True
    else:
        result = False
    return result


def add_employee_manually():
    """
    This function add a new employee to the Employee DB if all the data supplied and valid, return an error message to the user if something is wrong
    :return: Add a new employee to the Employee file if all the data supplied and valid, give an error message to the user if something is wrong
    :rtype: None
    """
    print("To add employee you need to provide the following information: name, phone and age")

    name = input("Please enter name: ")
    while utils.check_name(name) == False:
        name = input("Please enter name: ")

    phone = input("Please enter a phone number in the format XXX-XXX-XXXX: ")
    while utils.check_phone(phone) == False:
        phone = input(
            "Please enter a phone number in the format XXX-XXX-XXXX: ")

    age = input("Please enter age: ")
    while utils.check_age(age) == False:
        age = input("Please enter age: ")

    role = input("Please enter role - junior, manager or senior: ")
    while utils.check_role(role) == False:
        role = input("Please enter role - junior, manager or senior: ")

    if role == "junior":
        new_employee = employee.Employee(name, phone, age, role)
    elif role == "manager":
        new_employee = employee.Manager(name, phone, age, role)
    elif role == "senior":
        new_employee = employee.Senior(name, phone, age, role)

    sqldb.insert_emp(new_employee)
    utils.logging.info("Added Employee id: " + str(new_employee.get_employee_id()) +
                       " and employee name: " + str(new_employee.get_name()) + " Employee DB ")
    print("Employee was added to the Employee DB with the following information:")
    emps = sqldb.get_emps_by_name(name)
    print(emps)


def add_employee_from_file(employee_data_file_path):
    """
    This function check csv file data and if the file and data in it is valid, add new employees to Employees DB
    :param employee_data_file_path: file path to the csv file with input data
    :type employee_data_file_path: string
    :return: Add new employees from csv file if the file and data in it is valid
    :rtype: None
    """
    if utils.check_file(employee_data_file_path) and utils.check_csv_header_data(employee_data_file_path) and utils.check_scv_data(employee_data_file_path):
        utils.copy_scv_to_db(employee_data_file_path)


def search_employee():
    """
    This function check that Employees name exist in Employee DB.
    :return: Check that Employees name exist in Employee DB.
    :rtype: None
    """
    name = input("Please enter employee name to check in DB: ")
    while utils.check_name(name) == False:
        name = input("Please enter name to check it in DB: ")

    emps = sqldb.get_emps_by_name(name)
    if emps:
        print(name + " exist in DB")
        print(emps)
    else:
        print(name + " does not exist in DB")


def delete_employee():
    """
    This function get Employee name to delete and if it exist in Employees DB delete it
    :return: Delete employees from Employees DB if the Employee exist
    :rtype: None
    """
    name = input("Please enter employee name to delete : ")
    while utils.check_name(name) == False:
        name = input("Please enter name: ")
    # if utils.check_file(employee_file_path) and utils.check_csv_header(employee_file_path) and utils.check_scv_data(employee_file_path):
    sqldb.delete_emp(name)


def mark_employee_attendance():
    """
    This function mark employee attendance in attendance Employee DB log file if provided employee id exist in Employee DB, else error message is given
    :return: Mark employee attendance in attendance Employee DB log file if provided employee id exist in Employee DB, else error message is given
    :rtype: None0
    """
    employee_id = input(
        "\nPlease enter id of the employee to mark attendance: ")
    while utils.check_employee_id(employee_id) == False:
        employee_id = input(
            "Please enter id of the employee to mark attendance: ")
    sqldb.add_employee_attendance_to_DB(employee_id)


def employee_attendance_report():
    """
    This function generete employee attendance report 
    :return: Generete employee attendance report 
    :rtype: None
    """
    employee_id = input(
        "\nPlease enter id of the employee for report: ")
    while utils.check_employee_id(employee_id) == False:
        employee_id = input(
            "Please enter id of the employee for report: ")
    sqldb.generate_attendance_report_db(employee_id)


def generate_attendance_managers_report():
    """
    This function generete managers attendance report 
    :return: Generete managers attendance report 
    :rtype: None
    """
    sqldb.generate_attendance_managers_report_db()


def generate_attendance_month_report():
    """
    This function print a report for current month for all employees and give an error message to the user if something is wrong.
    :return: Print a report for current month for all employees and give an error message to the user if something is wrong.
    :rtype: None
    """
    sqldb.generate_attendance_month_report()


def attendance_late_report_db():
    """
    This function print a report for all active employees who were late in the last month and give an error message to the user if something is wrong.
    :return: Print a report for all active employees who were late in the last month and give an error message to the user if something is wrong.
    :rtype: None
    """
    sqldb.generate_attendance_late_report_db()


def generate_attendance_date_range_report():
    """
    This function check that date in right format and create attendance report according predefined date.
    :return:Check that that date in right format and create attendance report according predefined date.
    :rtype: None
    """
    print("To create report according given date range you need to provide date. ")
    from_date = input("\nPlease enter from date in format 'YYYY-MM-DD': ")
    while utils.check_date_time(from_date) == False:
        from_date = input("Please enter from date in format 'YYYY-MM-DD': ")

    sqldb.generate_attendance_given_date_report(from_date)


def add_managers_to_db():
    """
    This function add managers to managers db
    :return:Add managers to managers db
    :rtype: None
    """
    sqldb.add_managers_to_managers_db()


def main():
    employee_file_path, employee_data_file_path, employee_delete_file_path, attendance_file_path, attendance_report_path, attendance_month_path, attendance_late_path, attendance_given_date_path, managers_path, users_file_path, log_file = utils.create_files()

    end = 0
    while end == 0:
        option = utils.validate_input()
        if option == "1":
            add_employee_manually()

        elif option == "2":
            add_employee_from_file(employee_data_file_path)

        elif option == "3":
            search_employee()

        elif option == "4":
            delete_employee()

        elif option == "5":
            mark_employee_attendance()

        elif option == "6":
            employee_attendance_report()

        elif option == "7":
            generate_attendance_month_report()

        elif option == "8":
            attendance_late_report_db()

        elif option == "9":
            generate_attendance_date_range_report()

        elif option == "10":
            generate_attendance_managers_report()

        elif option == "11":
            add_managers_to_db()

        elif option == "0":
            end = 1

    # conn.close()


if __name__ == "__main__":
    # Initialize the colorama module

    colorama.init()
    utils.print__wellcome_screen_db()

    main()
