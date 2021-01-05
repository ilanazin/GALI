import employee
import os.path
from os import path
from datetime import datetime
import logging
import utils
import csv
# Use colorama module to print in color
import colorama
from colorama import Fore, Back, Style
import constants

# def print__wellcome_screen():

#     """
#     This function print the welcome screen and Employee Attendance Management System options
#     :return: print the welcome screen and Employee Attendance Management System options
#     :rtype: None
#     """
#     utils.print_message_with_color(constants.EMPLOYEE_ASCII_ART, "blue")
#     utils.print_message_with_color("""This program maintain employee attendance for a company. Please select one of the following options:""", "blue" )
#     utils.print_message_with_color("1 - Add employee manually", "blue")
#     utils.print_message_with_color("2 - Add employees from file", "blue")
#     utils.print_message_with_color("3 - Check employee exsit in the system", "blue")
#     utils.print_message_with_color("4 - Delete employee manually", "blue")
#     utils.print_message_with_color("5 - Delete employee from file", "blue")
#     utils.print_message_with_color("6 - Mark Attendance", "blue")
#     utils.print_message_with_color("7 - Generate attendance report of an employee", "blue")
#     utils.print_message_with_color("8 - Print a report for current month for all employees", "blue")
#     utils.print_message_with_color("9 - Print an attendance report for all employees who were late (come after 9:30) ", "blue")
#     utils.print_message_with_color("10 - Print a report for given date for all employees", "blue")
#     utils.print_message_with_color("11 - Print attendance managers report", "blue")
#     utils.print_message_with_color("0 - End program and exit", "blue")
#     utils.print_message_with_color("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ", "blue")

# def validate_input():
#     """
#     This function loop over the user input till it is not valid.
#     :return: Valid input option
#     :rtype: integer
#     """

#     option = input("\nplease select one of the valid options: ")
#     while check_option(option) == False:
#         option = input("please select one of the valid options: ")

#     return option

# def check_option(option):
#     """
#     This function check validity of user selection
#     :param option: user input selection
#     :type option: integer
#     :return: check selected option is integer number between 0 and 11
#     :rtype: Boolean
#     """
#     if option in constants.OPTIONS:
#         result = True
#     else:
#         result = False
#     return result


def add_employee_manually(file_path):
    """
    This function add a new employee to the Employee file if all the data supplied and valid, return an error message to the user if something is wrong
    :param file_path: file path to the csv file 
    :type file_path: string
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

    utils.logging.info("Added Employee id: " + str(new_employee.get_employee_id()) +
                       " and employee name: " + str(new_employee.get_name()) + " to file " + file_path)
    new_employee.update_csv_manually(file_path)
    print("Employee was added to the file " +
          file_path + " with the following information:")
    print(new_employee)


def add_employee_from_file(employee_data_file_path, employee_file_path):
    """
    This function check csv file data and if the file and data in it is valid, add new employees to Employees file
    :param employee_data_file_path: file path to the csv file with input data
    :type employee_data_file_path: string
    :param employee_file_path: file path to the csv file for update 
    :type employee_file_path: string
    :return: Add new employees from csv file if the file and data in it is valid   
    :rtype: None
    """
    if utils.check_file(employee_data_file_path) and utils.check_file(employee_file_path) and utils.check_csv_header(employee_file_path) and utils.check_csv_header_data(employee_data_file_path) and utils.check_scv_data(employee_data_file_path):
        utils.copy_scv(employee_data_file_path, employee_file_path)


def search_employee(employee_file_path):
    """
    This function check that Employees csv file exist under predefined path and have right format and pass it to utility that check that employee exist in it. 
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :return: Check that Employees csv file exist under predefined path and have right format and pass it to utility that check that employee exist in it.
    :rtype: None
    """
    if utils.check_file(employee_file_path) and utils.check_csv_header(employee_file_path):
        utils.check_employee(employee_file_path)


def delete_employee_manually(employee_file_path):
    """
    This function check the Employee id selected manually by the user and delete specified employee from Employees csv file if the Employee id is valid 
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :return: Delete employees from Employees csv file if the Employee id is valid   
    :rtype: None
    """
    if utils.check_file(employee_file_path) and utils.check_csv_header(employee_file_path) and utils.check_scv_data(employee_file_path):
        utils.delete_manually_from_scv(employee_file_path)


def delete_employee_automatic(employee_file_path, employee_delete_file_path):
    """
    This function check file that include employees id to be deleted data. If the file and data both valid, delete employees them from Employees file
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :param employee_delete_file_path: file path to the file with employees id to delete
    :type employee_delete_file_path: string
    :return: Delete employees from Employees csv file if the delete file and data in it valid   
    :rtype: None
    """
    if utils.check_file(employee_file_path) and utils.check_file(employee_delete_file_path) and utils.check_delete_scv(employee_delete_file_path) and utils.check_csv_header(employee_file_path) and utils.check_scv_data(employee_file_path):
        utils.delete_with_file_from_scv(
            employee_file_path, employee_delete_file_path)


def mark_employee_attendance(employee_file_path, attendance_file_path):
    """
    This function mark employee attendance in attendance log file if provided employee id exist in Employee scv file, else error message is given 
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :param attendance_file_path: file path to the csv file with employees
    :type attendance_file_path: string
    :return: Mark employee attendance in attendance log file if provided employee id exist in Employee scv file, else error message is given   
    :rtype: None
    """
    if utils.check_file(employee_file_path) and utils.check_csv_header(employee_file_path) and utils.check_scv_data(employee_file_path) and utils.check_attendance_header(attendance_file_path) and utils.check_file(attendance_file_path):
        utils.add_employee_to_attendance_log(
            employee_file_path, attendance_file_path)


def generate_employee_attendance_report(attendance_report_path, attendance_file_path):
    """
    This function generete employee attendance report Employee scv file, else error message is given 
    :param attendance_file_path: file path to the csv file with employees
    :type attendance_file_path: string
    :param attendance_report_path: file path to the attendance report csv file with output data
    :type attendance_report_path: string
    :return: Generete employee attendance report scv file, else error message is given   
    :rtype: None
    """
    if utils.check_file(attendance_file_path) and utils.check_attendance_header(attendance_file_path) and utils.check_attendance_header(attendance_report_path) and utils.check_file(attendance_report_path):
        utils.update_attendance_report(
            attendance_report_path, attendance_file_path)


def generate_attendance_month_report(attendance_file_path, attendance_month_path):
    """
    This function print a report for current month for all employees and give an error message to the user if something is wrong.
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_month_path: file path to the attendance month Excel report file 
    :type attendance_month_path: string
    :return: Print a report for current month for all employees and give an error message to the user if something is wrong. 
    :rtype: None
    """
    if utils.check_attendance_header(attendance_file_path) and utils.check_file(attendance_file_path):
        utils.generate_attendance_month_report(
            attendance_file_path, attendance_month_path)


def generate_attendance_late_report(attendance_file_path, attendance_late_path):
    """
    This function print a report for all active employees who were late in the last month and give an error message to the user if something is wrong.
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_late_path: file path to the attendance late Excel report file 
    :type attendance_late_path: string
    :return: Print a report for all active employees who were late in the last month and give an error message to the user if something is wrong.
    :rtype: None
    """
    if utils.check_attendance_header(attendance_file_path) and utils.check_file(attendance_file_path):
        utils.generate_attendance_late_report(
            attendance_file_path, attendance_late_path)


def generate_attendance_date_range_report(attendance_file_path, attendance_given_date_path):
    """
    This function check that Attendance csv file exist under predefined path and have right format and pass it to utility that create attendance report according predefined date range. 
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_given_date_path: file path to the attendance given date Excel report file 
    :type attendance_given_date_path: string
    :return:Check that Attendance csv file exist under predefined path and have right format and pass it to utility that create attendance report according predefined date range. 
    :rtype: None
    """
    if utils.check_attendance_header(attendance_file_path) and utils.check_file(attendance_file_path):
        utils.generate_attendance_given_date_report(
            attendance_file_path, attendance_given_date_path)


def generate_managers_report(employee_file_path, managers_path):
    """
    This function check that Employees csv file exist under predefined path and have right format and pass it to utility that create managers report. 
    :param employee_file_path: file path to the file emmployees file
    :type employee_file_path: string
    :param managers_path: file path to managers Excel report file 
    :type managers_path: string
    :return:Check that Attendance csv file exist under predefined path and have right format and pass it to utility that create managers report
    :rtype: None
    """
    if utils.check_csv_header(employee_file_path) and utils.check_file(employee_file_path):
        utils.generate_managers_report(employee_file_path, managers_path)


def main():
    employee_file_path, employee_data_file_path, employee_delete_file_path, attendance_file_path, attendance_report_path, attendance_month_path, attendance_late_path, attendance_given_date_path, managers_path, users_file_path, log_file = utils.create_files()

    end = 0
    while end == 0:
        option = utils.validate_input()
        if option == "1":
            add_employee_manually(employee_file_path)

        elif option == "2":
            add_employee_from_file(employee_data_file_path, employee_file_path)

        elif option == "3":
            search_employee(employee_file_path)

        elif option == "4":
            delete_employee_manually(employee_file_path)

        elif option == "5":
            delete_employee_automatic(
                employee_file_path, employee_delete_file_path)

        elif option == "6":
            mark_employee_attendance(employee_file_path, attendance_file_path)

        elif option == "7":
            generate_employee_attendance_report(
                attendance_report_path, attendance_file_path)

        elif option == "8":
            generate_attendance_month_report(
                attendance_file_path, attendance_month_path)

        elif option == "9":
            generate_attendance_late_report(
                attendance_file_path, attendance_late_path)

        elif option == "10":
            generate_attendance_date_range_report(
                attendance_file_path, attendance_given_date_path)

        elif option == "11":
            generate_managers_report(employee_file_path, managers_path)

        elif option == "0":
            end = 1


if __name__ == "__main__":
    # Initialize the colorama module
    colorama.init()
    utils.print__wellcome_screen()

    main()
