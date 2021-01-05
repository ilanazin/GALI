import os.path
from os import path
import csv
import constants
from datetime import datetime
import time
import employee
import logging
# Use colorama module to print in color
import colorama
from colorama import Fore, Back, Style
# Writing to an excel sheet using Python
import xlwt
from xlwt import Workbook
from tabulate import tabulate
import sqldb


def print__wellcome_screen():
    """
    This function print the welcome screen and Employee Attendance Management System options
    :return: print the welcome screen and Employee Attendance Management System options
    :rtype: None
    """
    print_message_with_color(constants.EMPLOYEE_ASCII_ART, "blue")
    print_message_with_color(
        """This program maintain employee attendance for a company. Please select one of the following options:""", "blue")
    print_message_with_color("1 - Add employee manually", "blue")
    print_message_with_color("2 - Add employees from file", "blue")
    print_message_with_color("3 - Check employee exsit in the system", "blue")
    print_message_with_color("4 - Delete employee manually", "blue")
    print_message_with_color("5 - Delete employee from file", "blue")
    print_message_with_color("6 - Mark Attendance", "blue")
    print_message_with_color(
        "7 - Generate attendance report of an employee", "blue")
    print_message_with_color(
        "8 - Print a report for current month for all employees", "blue")
    print_message_with_color(
        "9 - Print an attendance report for all employees who were late (come after 9:30) ", "blue")
    print_message_with_color(
        "10 - Print a report for given date for all employees", "blue")
    print_message_with_color("11 - Print attendance managers report", "blue")
    print_message_with_color("0 - End program and exit", "blue")
    print_message_with_color("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ", "blue")


def print__wellcome_screen_db():
    """
    This function print the welcome screen and Employee Attendance Management System options
    :return: print the welcome screen and Employee Attendance Management System options
    :rtype: None
    """
    print_message_with_color(constants.EMPLOYEE_ASCII_ART, "blue")
    print_message_with_color(
        """This program maintain employee attendance for a company. Please select one of the following options:""", "blue")
    print_message_with_color("1 - Add employee manually", "blue")
    print_message_with_color("2 - Add employees from file", "blue")
    print_message_with_color("3 - Check employee exsit in the system", "blue")
    print_message_with_color("4 - Delete employee", "blue")
    print_message_with_color("5 - Mark Attendance", "blue")
    print_message_with_color(
        "6 - Generate attendance report of an employee", "blue")
    print_message_with_color(
        "7 - Print a report for current month for all employees", "blue")
    print_message_with_color(
        "8 - Print an attendance report for all employees who were late (come after 9:30) ", "blue")
    print_message_with_color(
        "9 - Print a report for given date for all employees", "blue")
    print_message_with_color("10 - Print attendance managers report", "blue")
    print_message_with_color("11 - Add managers to Managers DB", "blue")
    print_message_with_color("0 - End program and exit", "blue")
    print_message_with_color("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ", "blue")


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


def create_files():
    """
    This function create files under predifined path than needed for Employee Management System
    :return: Create files under predifined patht han needed for Employee Management System
    :rtype: Tuple
    """

    employee_file_path = r'C:\Ilana\Python\Final_Project\Employee.csv'
    employee_data_file_path = r'C:\Ilana\Python\Final_Project\Employee_data.csv'
    employee_delete_file_path = r'C:\Ilana\Python\Final_Project\Employee_delete.csv'
    attendance_file_path = r'C:\Ilana\Python\Final_Project\Attendance_log.csv'
    attendance_report_path = r'C:\Ilana\Python\Final_Project\Attendance_report.csv'
    attendance_month_path = r'C:\Ilana\Python\Final_Project\Attendance_month.xls'
    attendance_late_path = r'C:\Ilana\Python\Final_Project\Attendance_late.xls'
    attendance_given_date_path = r'C:\Ilana\Python\Final_Project\Attendance_given_date.xls'
    managers_path = r'C:\Ilana\Python\Final_Project\Managers.xls'
    users_file_path = r'C:\Ilana\Python\Final_Project\Users.csv'
    log_file = r'C:\Ilana\Python\Final_Project\logging.txt'

    my_logging(log_file)
    create_csv(employee_file_path)
    create_attendance_log(attendance_file_path)
    create_attendance_report(attendance_report_path)
    return employee_file_path, employee_data_file_path, employee_delete_file_path, attendance_file_path, attendance_report_path, attendance_month_path, attendance_late_path, attendance_given_date_path, managers_path, users_file_path, log_file


def print_message_with_color(msg, color="WHITE", back="RESET"):
    """
    This function prints string message to console with different font colors: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET. The default is white.
    :param screen: string to print
    :type screen: string
    :param screen: color of the string to print
    :type screen: string
    :param screen: back color of the string to print
    :type screen: string
    :return: print to console with different font colors
    :rtype: None
    """

    color = getattr(Fore, color.upper())
    back = getattr(Back, back.upper())
    print(color + msg + back + Style.RESET_ALL)


def my_logging(log_file):
    """
    This function define the structure of logger file that include the date, employee_id and name.
    :return: The logger file with prefefined structure
    :rtype: None
    """
    LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format=LOG_FORMAT,
                        filemode='w')
    logger = logging.getLogger()
    # text messages
    logger.debug("Start logger")


def create_csv(employee_file_path):
    """
    This function create csv file with header Employee_id, Name, Phone, Age, Role.
    :param employee_file_path: file path to the csv file
    :type employee_file_path: string
    :return: Crete csv file with header Employee_id, Name, Phone, Age, Role.
    :rtype: None
    """

    if path.isfile(employee_file_path) == False:
        with open(employee_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Employee_id", "Name", "Phone", "Age", "Role"])


def create_users(users_file_path):
    """
    This function create Users csv file with header Username, Password.
    :param users_file_path: file path to the Users csv file
    :type users_file_path: string
    :return: Crete csv file with header Username, Password.
    :rtype: None
    """

    if path.isfile(users_file_path) == False:
        with open(users_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Username", "Password"])


def create_attendance_log(attendance_file_path):
    """
    This function crete csv file for attendance log with header Employee_id, Date, Time, Role.
    :param attendance_file_path: file path to the csv attendance log file
    :type attendance_file_path: string
    :return: Crete csv file for attendance log with header Employee_id, Date, Time, Role.
    :rtype: None
    """
    if path.isfile(attendance_file_path) == False:
        with open(attendance_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Employee_id", "Date", "Time", "Role"])


def create_attendance_report(attendance_report_path):
    """
    This function crete csv file for attendance report with header Employee_id, Date, Time, Role.
    :param attendance_report_path): file path to the csv attendance report file
    :type attendance_report_path): string
    :return: Crete csv file for attendance report with header Employee_id, Date, Time ,Role.
    :rtype: None
    """
    if path.isfile(attendance_report_path) == False:
        with open(attendance_report_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Employee_id", "Date", "Time", "Role"])


def create_attendance_month_report(attendance_month_path):
    """
    This function crete csv file for attendance report with header Employee_id.
    :param attendance_month_path): file path to the csv attendance report file
    :type attendance_month_path): string
    :return: Crete csv file for attendance report with header Employee_id.
    :rtype: None
    """
    if path.isfile(attendance_month_path) == False:
        with open(attendance_month_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Employee_id"])


def check_attendance_header(attendance_file_path):
    """
    This function check that csv attendance report file have predefined header
    :param attendance_file_path: file path to the attendance csv file
    :type attendance_file_path: string
    :return: Check that csv attendance report file have predefined header. If yes return True, else False
    :rtype: Boolean
    """

    with open(attendance_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # the first line is the header
        header = next(reader)

    if header[0] == 'Employee_id' and header[1] == 'Date' and header[2] == 'Time':
        return True
    else:
        print("Wrong csv header file. Please check that " + attendance_file_path +
              " file include the following columns: 'Employee_id', 'Date', 'Time'")
        return False


def create_password(users_file_path):
    """
    This function crete csv file with header Employee_id, Name, Phone, Age, Role.
    :param employee_file_path: file path to the csv file
    :type employee_file_path: string
    :return: Crete csv file with header Employee_id, Name, Phone, Age, Role.
    :rtype: None
    """

    if path.isfile(users_file_path) == False:
        with open(users_file_path, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["User", "Password"])


def validate_input_path():
    """
    This function loop over the user input for file path till it is not valid.
    :return: Valid file path
    :rtype: string
    """

    employee_data_file_path = input(
        "\nPlease enter the valid path to csv file with employees information: ")
    while check_file(employee_data_file_path) == False:
        employee_data_file_path = input(
            "Please enter the valid path to csv file with employees information: ")

    return employee_data_file_path


def check_date(employee_date):
    """
    This function check that date in formt YYYY:MM:DD
    :param employee_date: date
    :type employee_date: integer
    :return: check that date in formt YYYY:MM:DD
    :rtype: Boolean
    """
    isValidDate = True
    try:
        year, month, day = employee_date.split(':')
    except ValueError:
        print("Input date is not valid.")
        isValidDate = False
        return False
    else:
        try:
            datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if(isValidDate):
            for i, c in enumerate(employee_date):
                if i in [4, 7]:
                    if c != ':':
                        print("Date include wrong delimeter")
                        return False
                elif not c.isnumeric():
                    print("Input date is not according date format 'YYYY:MM:DD'.")
                    return False
            if i < 9:
                print("Date include wrong number of digits")
                return False
            return True
        else:
            print("Input date is not valid.")
            return False


def check_date_time(employee_date):
    """
    This function check that date in formt YYYY:MM:DD
    :param employee_date: date
    :type employee_date: integer
    :return: check that date in formt YYYY:MM:DD
    :rtype: Boolean
    """
    isValidDate = True
    try:
        year, month, day = employee_date.split('-')
    except ValueError:
        print("Input date is not valid.")
        isValidDate = False
        return False
    else:
        try:
            datetime(int(year), int(month), int(day))
        except ValueError:
            isValidDate = False

        if(isValidDate):
            for i, c in enumerate(employee_date):
                if i in [4, 7]:
                    if c != '-':
                        print("Date include wrong delimeter")
                        return False
                elif not c.isnumeric():
                    print("Input date is not according date format 'YYYY-MM-DD'.")
                    return False
            if i < 9:
                print("Date include wrong number of digits")
                return False
            return True
        else:
            print("Input date is not valid.")
            return False


def date_difference(date_check1, date_check2):
    """
    This function check if the given time (date_check1) is after date_check2 and return True else return False.
    :param date_check1: time to check difference from date_check2 to date_check1
    :type date_check1: string
    :param date_check2: time to check difference from date_check2 to date_check1
    :type date_check2: string
    :return: Check if the given time (date_check1) is after (date_check2) and return True else return False.
    :rtype: Boolean
    """
    dateA = datetime.strptime(date_check1, "%Y:%M:%d")
    dateB = datetime.strptime(date_check2, "%Y:%M:%d")
    newDate = dateA - dateB
    return dateA >= dateB


def check_file(employee_data_file_path):
    """
    This function check that file exist according given path, not empty and with csv extention
    :param employee_data_file_path: file path to the csv file
    :type employee_data_file_path: string
    :return: check that file exist according given path, not empty and with csv extention. If yes return True, else False
    :rtype: Boolean
    """

    if (path.isfile(employee_data_file_path) and path.getsize(employee_data_file_path) > 0):
        file_link = path.splitext(employee_data_file_path)
        if file_link[1] == ".csv":
            return True
    else:
        print("Please enter path to not emppty .csv file")
        return False


def check_delete_header(employee_delete_file_path):
    """
    This function check that delete file have employee id in header
    :param employee_delete_file_path: file path to the delete file
    :type employee_delete_file_path: string
    :return: Check that delete file have employee id have employee id in header. If yes return True, else False
    :rtype: Boolean
    """

    with open(employee_delete_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # the first line is the header
        header = next(reader)
        if len(header) == 1:
            if header[0] == 'Employee_id':
                return True
            else:
                print("Wrong csv header file. Please check that " + employee_delete_file_path +
                      " file include the following columns: 'Employee_id'")
                return False
        else:
            print("Wrong csv header file. Please check that " + employee_delete_file_path +
                  " file include the following columns: 'Employee_id'")
            return False


def check_delete_scv(employee_delete_file_path):
    """
    This function check that delete file have employee id with valid data to delete from Employee scv file
    :param employee_delete_file_path: file path to the delete file
    :type employee_delete_file_path: string
    :return: Check that delete file have employee id with valid data to delete from Employee scv file. If yes return True, else False
    :rtype: Boolean
    """
    if check_delete_header(employee_delete_file_path) == False:
        return False
    else:
        result = True
        lines = list()
        with open(employee_delete_file_path, 'r') as readFile:
            reader = csv.reader(readFile)
            header = next(reader)
            for row in reader:
                lines.append(row)
                for field in row:
                    if check_employee_id(field) == False:
                        result = False

        return result


def check_employee_id(employee_id):
    """
    This function check validity of employee_id
    :param employee_id: employee id
    :type employee_id: integer
    :return: check that employee_id is integer number bigger then 0
    :rtype: Boolean
    """
    if employee_id == "0":
        print("Employee id need to be greate then zero")
        result = False
    elif employee_id.isdigit() != True:
        print("Employee id need to be integer")
        result = False
    else:
        result = True
    return result


def check_age(age):
    """
    This function check validity of age
    :param age: age
    :type age: integer
    :return: check that age is integer number bigger then 0
    :rtype: Boolean
    """
    if age == "0":
        print("Age need to be greate then zero")
        result = False
    elif age.isdigit() != True:
        print("Age need to be integer bigger then zero")
        result = False
    else:
        result = True
    return result


def check_phone(phone):
    """
    This function check that phone number in formt XXX-XXX-XXXX
    :param phone: phone
    :type phone: integer
    :return: check that phone number in formt XXX-XXX-XXXX
    :rtype: Boolean
    """
    for i, c in enumerate(phone):
        if i in [3, 7]:
            if c != '-':
                print("Phone number include wrong delimeter")
                return False
        elif not c.isnumeric():
            print("Phone number need to include only numbers")
            return False
    if i < 11:
        print("Phone number include wrong number of digits")
        return False
    return True


def check_name(name):
    """
    This function check validity of name
    :param name: name
    :type name: string
    :return: check that name is alfabetic string
    :rtype: Boolean
    """
    if name.isalpha() == False:
        print("Name need to be only alfabetic string")
        result = False
    else:
        result = True
    return result


def check_role(role):
    """
    This function check validity of role
    :param name: role
    :type name: string
    :return: check that role is according predefined values
    :rtype: Boolean
    """
    if role in constants.ROLES:
        return True
    else:
        print("Wrong role")
        return False


def check_csv_header(employee_file_path):
    """
    This function check that csv file have predefined header
    :param employee_file_path: file path to the csv file
    :type employee_file_path: string
    :return: Check that csv file have predefined header. If yes return True, else False
    :rtype: Boolean
    """

    with open(employee_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # the first line is the header
        header = next(reader)

    if header[0] == 'Employee_id' and header[1] == 'Name' and header[2] == 'Phone' and header[3] == 'Age' and header[4] == 'Role':
        return True
    else:
        print("Wrong csv header file. Please check that " + employee_file_path +
              " file include the following columns: 'Employee_id', 'Name', 'Phone', 'Age', 'Role'")
        return False


def check_csv_header_data(employee_data_file_path):
    """
    This function check that csv file have predefined header
    :param employee_data_file_path: file path to the csv file
    :type employee_data_file_path: string
    :return: Check that csv file have predefined header. If yes return True, else False
    :rtype: Boolean
    """
    with open(employee_data_file_path, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        # the first line is the header
        header = next(reader)

    if header[0] == 'Name' and header[1] == 'Phone' and header[2] == 'Age' and header[3] == 'Role':
        return True
    else:
        print("Wrong csv header file. Please check that " + employee_data_file_path +
              " file include the following columns: 'Name', 'Phone', 'Age', 'Role'")
        return False


def check_scv_data(employee_data_file_path):
    """
    This function check that csv file have valid data - no empty columns and data in every column with right type.
    :param employee_data_file_path: file path to the csv file
    :type employee_data_file_path: string
    :return: If csv file does not have no empty columns and data in every column with right type then return true else return false
    :rtype: Boolean
    """

    with open(employee_data_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Name'] == '' or row['Phone'] == '' or row['Age'] == '' or row['Role'] == '':
                print("CSV file " + employee_data_file_path +
                      " have missing empty data in one of the rows")
                return False
            elif check_name(row['Name']) and check_phone(row['Phone']) and check_age(row['Age']) and check_role(row['Role']):
                return True


def check_employee(employee_file_path):
    """
    This function get from the user Employee id, check that it is valid and exist in the Employees csv file, and return True if the id exist, else return False.
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :return: Get from the user Employee id, check that it is valid and exist in the Employees csv file, and return True if the id exist, else return False.
    :rtype: Boolean
    """
    exist = 0
    lines = list()
    employee_id = input(
        "Please enter employee id to check if it is exist in Employees csv file: ")
    while check_employee_id(employee_id) == False:
        employee_id = input(
            "Please enter employee id to check if it is exist in Employees csv file: ")
    with open(employee_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == employee_id:
                    exist++1
                    print("Employee id: " + employee_id +
                          " exist in Employees csv file  " + employee_file_path)
                    logging.info("Employee id: " + employee_id +
                                 " exist in Employees csv file  " + employee_file_path)
                    return True
    if exist == 0:
        print("Employee id: " + employee_id +
              " does not exist in Employees csv file  " + employee_file_path)
        logging.info("Employee id: " + employee_id +
                     " does not exist in Employees csv file  " + employee_file_path)
        return False


def copy_scv(employee_data_file_path, employee_file_path):
    """
    This function read csv file with header Name, Phone, Age, Role.
    :param employee_data_file_path: file path to the csv file with input data
    :type employee_data_file_path: string
    :param employee_file_path: file path to the csv file for update
    :type employee_file_path: string
    :return: Read csv file with header  Name, Phone, Age, Role.
    :rtype: None
    """
    counter = 0
    with open(employee_data_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        with open(employee_file_path, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            for row in csv_reader:
                new_employee = employee.Employee(
                    row['Name'], row['Phone'], row['Age'], row['Role'])
                writer.writerow([new_employee.get_employee_id(
                ), row['Name'], row['Phone'], row['Age'], row['Role']])
                counter += 1
                logging.info("Added Employee id: " + str(new_employee.get_employee_id()) +
                             " and employee name: " + str(new_employee.get_name()) + "  to file path " + employee_file_path)
    print(str(counter) + " employees were coped from " +
          employee_data_file_path + " file to " + employee_file_path + " file")


def copy_scv_to_db(employee_data_file_path):
    """
    This function read csv file with header Name, Phone, Age, Role.
    :param employee_data_file_path: file path to the csv file with input data
    :type employee_data_file_path: string
    :return: Read csv file with header  Name, Phone, Age, Role.
    :rtype: None
    """
    counter = 0
    with open(employee_data_file_path, 'r', newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # with open (employee_file_path,'a',newline='') as csv_file:
        #     writer=csv.writer(csv_file)
        for row in csv_reader:
            new_employee = employee.Employee(
                row['Name'], row['Phone'], row['Age'], row['Role'])
            sqldb.insert_emp(new_employee)
            # writer.writerow([new_employee.get_employee_id(), row['Name'],row['Phone'], row['Age'], row['Role']])
            counter += 1
            logging.info("Added Employee id: " + str(new_employee.get_employee_id()) +
                         " and employee name: " + str(new_employee.get_name()) + "  to Employee DB ")
    print(str(counter) + " employees were coped from " +
          employee_data_file_path + " file to Employee DB")


def delete_manually_from_scv(employee_file_path):
    """
    This function check file that include employees id to be deleted data. If the file and data both valid, delete employees them from Employees file
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :return: Delete employees from Employees csv file if the delete file and data in it valid
    :rtype: None
    """
    deleted = 0
    lines = list()
    employee_id = input("\nPlease enter id of the employee to be deleted: ")
    while check_employee_id(employee_id) == False:
        employee_id = input("Please enter id of the employee to be deleted: ")
    with open(employee_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == employee_id:
                    lines.remove(row)
                    deleted = 1
                    logging.info("Deleted Employee id: " + employee_id +
                                 " from file path " + employee_file_path)

    with open(employee_file_path, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    if deleted != 1:
        print("Selected employee id does not exist in Employee scv file, nothing deleted")
    else:
        print("Selected employee id: " + employee_id +
              " deleted from scv Employee file")


def delete_employee_from_scv(employee_file_path, employee_id):
    """
    This function get employee id to be deleted. If this id exist in Employee file, employee deleted, else return message to the user that employee does not exist and nothing deleted.
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :param employee_id: imployee id to delete
    :type employee_id: integer
    :return: Get employee id to be deleted. If this id exist in Employee file, employee deleted, else return message to the user that employee does not exist and nothing deleted.
    :rtype: None
    """
    deleted = 0
    lines = list()
    with open(employee_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            lines.append(row)
            if row[0][0] == employee_id:
                lines.remove(row)
                deleted = 1
                logging.info("Deleted Employee id: " + employee_id +
                             " from file path " + employee_file_path)

    with open(employee_file_path, 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(lines)
    if deleted != 1:
        print("Selected employee id " + employee_id +
              " does not exist in Employee scv file, nothing deleted")
    else:
        print("Selected employee id: " + employee_id +
              " deleted from scv Employee file")


def delete_with_file_from_scv(employee_file_path, employee_delete_file_path):
    """
    This function read file that include employees id to be deleted and pass the id to function that delete the employee according the id
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :param employee_delete_file_path: file path to the file with employees id to delete
    :type employee_delete_file_path: string
    :return: Read file that include employees id to be deleted and pass the id to function that delete the employee according the id
    :rtype: None
    """
    lines = list()
    with open(employee_delete_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        header = next(reader)
        for row in reader:
            lines.append(row)
            for field in row:
                try:
                    delete_employee_from_scv(employee_file_path, field)
                except ValueError:
                    print("The employee ID " + field + " from " + employee_delete_file_path +
                          " file does not exist in " + employee_file_path + ",so it does not deleted")


def check_employee_exist(employee_file_path, employee_id):
    """
    This function check that employees id exist in Employees scv file
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :param employee_id: Employee id
    :type employee_id: integer
    :return: Check employees id exist in Employees scv file and if yes return True, else return False
    :rtype: Boolean
    """
    result = False
    lines = list()
    with open(employee_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        header = next(reader)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == employee_id:
                    result = True
    return result


def add_employee_to_attendance_log(employee_file_path, attendance_file_path):
    """
    This function get employee id from user and if the value exist in Employees file scv update attendance log with employee id, system date and time. Give an error message to the use if the id is not in the Employees file.
    :param employee_file_path: file path to the csv file with employees
    :type employee_file_path: string
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :return: Get employee id from user and if the value exist in Employees file scv update attendance log with employee id, system date and time. Give an error message to the use if the id is not in the Employees file.
    :rtype: None
    """
    print("To mark employee attendance you need to provide the employee_id")
    employee_id = input("\nPlease enter Enployee id: ")
    while check_employee_id(employee_id) == False:
        employee_id = input("Please enter Enployee id: ")

    t = time.localtime()
    current_date = time.strftime("%Y:%m:%d", t)
    current_time = time.strftime("%H:%M", t)
    if check_employee_exist(employee_file_path, employee_id):
        with open(attendance_file_path, 'a', newline='') as writeFile:
            writer = csv.writer(writeFile)
            line = [employee_id, current_date, current_time]
            print("Employees attendence log updated for Employee id " + employee_id)
            writer.writerow(line)
            logging.info("Mark Employee id: " + employee_id +
                         " in attendence log " + attendance_file_path)
    else:
        print("Employee Id " + employee_id +
              " does not exist in Employee scv file, attendance log file does not updated")


def generate_attendance_month_report(attendance_file_path, attendance_month_path):
    """
    This function generate attendance Excel report of all employees in the last month.
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_month_path: file path to the attendance month Excel file report
    :type attendance_month_path: string
    :return: Generate attendance Excel report of all employees in the last month.
    :rtype: None
    """
    t = time.localtime()
    current_month = time.strftime("%B", t)

    # ws.write_merge(6, 6, 35, 42, "Date", xlwt.easyxf('font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'"borders: top double, bottom double, left dashed, right double;"))
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on;'
                         'alignment: horizontal center;')
    style1 = xlwt.easyxf(
        'font: name Times New Roman, color-index red, bold on')
    style2 = xlwt.easyxf('font: bold True;'
                         'alignment: horizontal left;'
                         "borders: top 1, bottom 1, left 1, right 1;")
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Monthly Report')
    ws.write(0, 0, current_month, style0)
    ws.write(0, 1, "Employeers Attendance Monthly Report", style1)
    ws.write(1, 0, "Employee ID", style2)
    i = 2
    count = 0
    lines = []
    with open(attendance_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        header = next(reader)
        for row in reader:
            if lines.count(int(row[0])) == 0:
                lines.append(int(row[0]))
                ws.write(i, 0, int(row[0]), style2)
                i += 1
                count += 1
                print("Employee_ID: " + row[0])
    wb.save(attendance_month_path)
    if i > 1:
        print("Employees month attendance report created under the following path " +
              attendance_month_path)
        logging.info("Employees month attendance report created " +
                     attendance_month_path)
    else:
        print("Nothing added to month attendance report")


def time_difference(time_check1, time_check2):
    """
    This function check if the given time (time_check1) is after time_check2 and return True else return False.
    :param time_check1: time to check difference from time_check2 to time_check1
    :type time_check1: string
    :param time_check2: time to check difference from time_check2 to time_check1
    :type time_check2: string
    :return: Check if the given time (time_check1) is after (time_check2) and return True else return False.
    :rtype: Boolean
    """
    timeA = datetime.strptime(time_check1, "%H:%M")
    timeB = datetime.strptime(time_check2, "%H:%M")
    newTime = timeA - timeB
    return timeA > timeB


def time_difference_with_sec(time_check1, time_check2):
    """
    This function check if the given time (time_check1) is after time_check2 and return True else return False.
    :param time_check1: time to check difference from time_check2 to time_check1
    :type time_check1: string
    :param time_check2: time to check difference from time_check2 to time_check1
    :type time_check2: string
    :return: Check if the given time (time_check1) is after (time_check2) and return True else return False.
    :rtype: Boolean
    """
    timeA = datetime.strptime(time_check1, "%H:%M:%S")
    timeB = datetime.strptime(time_check2, "%H:%M:%S")
    newTime = timeA - timeB
    return timeA > timeB


def generate_attendance_late_report(attendance_file_path, attendance_late_path):
    """
    This function generate attendance Excel report of all employees in the last month.
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_late_path: file path to the attendance late Excel file report
    :type attendance_late_path: string
    :return: Generate attendance Excel report of all employees in the late month.
    :rtype: None
    """
    t = time.localtime()
    current_month = time.strftime("%B", t)
    nine = "9:30"
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on;'
                         'alignment: horizontal center;')
    style1 = xlwt.easyxf(
        'font: name Times New Roman, color-index red, bold on')
    style2 = xlwt.easyxf('font: bold True;'
                         'alignment: horizontal left;'
                         "borders: top 1, bottom 1, left 1, right 1;")
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Late Report')
    ws.write(0, 0, current_month, style0)
    ws.write(0, 1, "Employeers Attendance late Report", style1)
    ws.write(1, 0, "Employee ID", style2)
    ws.write(1, 1, "Date", style2)
    ws.write(1, 2, "Time", style2)
    i = 2
    lines = []
    table = []
    headers = ["Employee_id", "Date", "Time"]
    with open(attendance_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        header = next(reader)
        for row in reader:
            if time_difference(row[2], '9:30'):
                lines.append(int(row[0]))
                table.append(row)
                ws.write(i, 0, int(row[0]), style2)
                ws.write(i, 1, row[1], style2)
                ws.write(i, 2, row[2], style2)
                i += 1
    wb.save(attendance_late_path)
    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees late attendance report created under the fllowing path " +
              attendance_late_path)
        logging.info("Employees late attendance report created " +
                     attendance_late_path)
    else:
        print("Nothing added to late attendance report")


def month_ago():
    """
    This function find the date one month ago.
    :param None
    :type None
    :return: Find the date one month ago.
    :rtype: None
    """
    today = datetime.today()

    if today.month == 1:
        one_month_ago = today.replace(year=today.year - 1, month=12)
    else:
        extra_days = 0
        while True:
            try:
                one_month_ago = today.replace(
                    month=today.month - 1, day=today.day - extra_days)
                break
            except ValueError:
                extra_days += 1
    print(one_month_ago)


def generate_attendance_given_date_report(attendance_file_path, attendance_given_date_path):
    """
    This function generate attendance Excel report of all employees according given date range.
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_given_date_path: file path to the attendance given date Excel file report
    :type attendance_given_date_path: string
    :return: Generate attendance Excel report of all employees according given date range.
    :rtype: None
    """
    print("To create report according given date range you need to provide from and to dates. ")
    from_date = input("\nPlease enter from date in format 'YYYY:MM:DD': ")
    while check_date(from_date) == False:
        from_date = input("Please enter from date in format 'YYYY:MM:DD': ")

    to_date = input("\nPlease enter to date in format 'YYYY:MM:DD': ")
    while check_date(to_date) == False:
        to_date = input("Please enter to date in format 'YYYY:MM:DD': ")

    t = time.localtime()

    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on;'
                         'alignment: horizontal center;')
    style1 = xlwt.easyxf(
        'font: name Times New Roman, color-index red, bold on')
    style2 = xlwt.easyxf('font: bold True;'
                         'alignment: horizontal left;'
                         "borders: top 1, bottom 1, left 1, right 1;")
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Late Report')
    ws.write(0, 0, "Employeers attendance report according date ranges", style1)
    ws.write(0, 4, from_date, style0)
    ws.write(0, 5, to_date, style0)
    ws.write(1, 0, "Employee ID", style2)
    ws.write(1, 1, "Date", style2)
    ws.write(1, 2, "Time", style2)
    i = 2
    lines = []
    table = []
    headers = ["Employee_id", "Date", "Time"]
    with open(attendance_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        header = next(reader)
        for row in reader:
            if date_difference(row[1], from_date) and date_difference(to_date, row[1]):
                lines.append(int(row[0]))
                ws.write(i, 0, int(row[0]), style2)
                ws.write(i, 1, row[1], style2)
                ws.write(i, 2, row[2], style2)
                i += 1
                table.append(row)
    wb.save(attendance_given_date_path)
    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees attendance report according given dates created under the fllowing path " +
              attendance_given_date_path)
        logging.info(
            "Employees attendance report according given dates created " + attendance_given_date_path)
    else:
        print("Nothing added to attendance report according given dates ")


def update_attendance_report(attendance_report_path, attendance_file_path):
    """
    This function get employee id from user and if the value exist in Attendance log file, create the attendance report for a given employee with all the entries of his attendance.
    :param attendance_file_path: file path to the file attendance log
    :type attendance_file_path: string
    :param attendance_report: file path to the attendance report Excel file
    :type attendance_report: string
    :return: Get employee id from user and if the value exist in Attendance log file, create the attendance report for a given employee with all the entries of his attendance.
    :rtype: None
    """
    print("To create employee attendance report you need to provide the employee_id")
    employee_id = input("\nPlease enter Enployee id: ")
    while check_employee_id(employee_id) == False:
        employee_id = input("\nPlease enter Enployee id: ")

    lines = list()
    added = 0
    count = 0
    if check_employee_exist(attendance_file_path, employee_id):
        with open(attendance_file_path, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                count += 1
                lines.append(row)
                for field in row:
                    if field == employee_id:
                        with open(attendance_report_path, 'w', newline='') as writeFile:
                            writer = csv.writer(writeFile)
                            added += 1
                            writer.writerows(lines)
                        if count == len(row):
                            print(
                                tabulate(lines, headers="firstrow", tablefmt="pipe"))
        if added > 0:
            print("\nEmployee " + employee_id +
                  " added to attendance report " + attendance_report_path)
            logging.info("Employee " + employee_id +
                         " added to attendance report " + attendance_report_path)
    else:
        print("\nEmployee Id " + employee_id +
              " does not exist in Attendence log file, attendance report does not created")


def generate_managers_report(employee_file_path, managers_path):
    """
    This function create managers report Excel file.
    :param employee_file_path: file path to the employee file
    :type employee_file_path: string
    :param managers_path: file path to managers Excel file
    :type managers_path: string
    :return: Create managers report Excel file.
    :rtype: None
    """
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on;'
                         'alignment: horizontal center;')
    style1 = xlwt.easyxf(
        'font: name Times New Roman, color-index red, bold on')
    style2 = xlwt.easyxf('font: bold True;'
                         'alignment: horizontal left;'
                         "borders: top 1, bottom 1, left 1, right 1;")
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Managers Report')
    ws.write(0, 0, "Managers report", style1)
    ws.write(1, 0, "Employee ID", style2)
    ws.write(1, 1, "Name", style2)
    ws.write(1, 2, "Phone", style2)
    ws.write(1, 3, "Age", style2)
    ws.write(1, 4, "Role", style2)
    i = 2
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role"]
    with open(employee_file_path, 'r') as readFile:
        reader = csv.reader(readFile)
        header = next(reader)
        for row in reader:
            if row[4] == "manager":
                lines.append(int(row[0]))
                ws.write(i, 0, int(row[0]), style2)
                ws.write(i, 1, row[1], style2)
                ws.write(i, 2, row[2], style2)
                ws.write(i, 3, row[3], style2)
                ws.write(i, 4, row[4], style2)
                i += 1
                table.append(row)
    wb.save(managers_path)
    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees managers report created " + managers_path)
        logging.info("Employees managers report created " + managers_path)
    else:
        print("Nothing added to managers report file")


def generate_managers_report_screen():
    """
    This function create managers report.
    :return: Create managers report.
    :rtype: None
    """
    style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on;'
                         'alignment: horizontal center;')
    style1 = xlwt.easyxf(
        'font: name Times New Roman, color-index red, bold on')
    style2 = xlwt.easyxf('font: bold True;'
                         'alignment: horizontal left;'
                         "borders: top 1, bottom 1, left 1, right 1;")
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Managers Report')
    ws.write(0, 0, "Managers report", style1)
    ws.write(1, 0, "Employee ID", style2)
    ws.write(1, 1, "Name", style2)
    ws.write(1, 2, "Phone", style2)
    ws.write(1, 3, "Age", style2)
    ws.write(1, 4, "Role", style2)
    i = 2
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role"]

    for row in sqldb.get_emps_by_role('manager'):
        lines.append(int(row[0]))
        ws.write(i, 0, int(row[0]), style2)
        ws.write(i, 1, row[1], style2)
        ws.write(i, 2, row[2], style2)
        ws.write(i, 3, row[3], style2)
        ws.write(i, 4, row[4], style2)
        i += 1
        table.append(row)
    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees managers report created")
        logging.info("Employees managers report created")

    else:
        print("Nothing added to managers report")

    for row in sqldb.get_emps_by_role('manager'):
        manager_employee = employee.Employee(
            row[1], row[2], row[3], row[4])
        # row['Name'], row['Phone'], row['Age'], row['Role'],row['attendance'])
        sqldb.insert_manager(manager_employee)


def generate_managers_report_db():
    """
    This function add managers to managers DB.
    :return: Add managers to managers DB.
    :rtype: None
    """
    added = 0
    for row in sqldb.get_emps_by_role('manager'):
        print(sqldb.get_emps_by_role('manager')[0][1])
        print(sqldb.get_emps_by_role('manager')[0][2])
        print(sqldb.get_emps_by_role('manager')[0][3])
        # print(sqldb.get_emps_by_id_managers(
        #     sqldb.get_emps_by_role('manager')[0][0]))
        # if sqldb.get_emps_by_id_managers(row[0]):
        if sqldb.get_emps_by_role('manager'):
            manager_employee = employee.Manager(
                row[1], row[2], row[3], row[4])
            sqldb.insert_manager(manager_employee)
            added += 1

    if added > 0:
        print("Managers added to Managers DB")
        logging.info("Managers added to Managers DB")

    else:
        print("Nothing added to Managers DB")

    # for row in sqldb.get_emps_by_role('manager'):
    #         manager_employee = employee.Employee(
    #             row[1], row[2], row[3], row[4])
    #         sqldb.insert_manager(manager_employee)
