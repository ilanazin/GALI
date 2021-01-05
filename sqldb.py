import sqlite3
from sqlite3 import Error
import employee
import sqldb
import time
from datetime import datetime
from tabulate import tabulate
import utils

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect(r"C:\Ilana\Python\Final_Project\Employee.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS employees(
             employee_id integer,
             name text,
             phone text,
             age integer,
             role text,
             date text,
             time text
             ) """)

c.execute("""CREATE TABLE IF NOT EXISTS managers(
             employee_id integer,
             name text,
             phone text,
             age integer,
             role text,
             date text,
             time text
             ) """)


def insert_emp(employee):
    with conn:
        c.execute("INSERT INTO employees VALUES (:employee_id, :name, :phone, :age, :role, :date, :time)",
                  {'employee_id': employee.employee_id, 'name': employee.name, 'phone': employee.phone,
                   'age': employee.age, 'role': employee.role, 'date': '2020-01-01', 'time': '01:00:00'})


def insert_manager(employee):
    with conn:
        c.execute("INSERT INTO managers VALUES (:employee_id, :name, :phone, :age, :role, :date, :time)",
                  {'employee_id': employee.employee_id, 'name': employee.name, 'phone': employee.phone,
                   'age': employee.age, 'role': employee.role, 'date': '2020-01-01', 'time': '01:00:00'})


def get_emps_by_id_employee(employee_id):
    c.execute("SELECT * FROM employees WHERE employee_id=:employee_id",
              {'employee_id': employee_id})
    return c.fetchall()


def get_emps_by_id_managers(employee_id):
    c.execute("SELECT * FROM managers WHERE employee_id=:employee_id",
              {'employee_id': employee_id})
    return c.fetchall()


def get_emps_by_name(name):
    c.execute("SELECT * FROM employees WHERE name=:name", {'name': name})
    return c.fetchall()


def get_emps_by_phone(phone):
    c.execute("SELECT * FROM employees WHERE phone=:phone", {'phone': phone})
    return c.fetchall()


def get_emps_by_age(age):
    c.execute("SELECT * FROM employees WHERE age=:age", {'age': age})
    return c.fetchall()


def get_emps_by_role(role):
    c.execute("SELECT * FROM employees WHERE role=:role", {'role': role})
    return c.fetchall()


def update_name(employee, name):
    with conn:
        c.execute("""UPDATE employees SET name=:name
                     WHERE employee_id= :employee_id""",
                  {'employee_id': employee.employee_id, 'name': name, 'phone': employee.phone, 'age': employee.age, 'role': employee.role})


def update_phone(employee, phone):
    with conn:
        c.execute("""UPDATE employees SET phone=:phone
                     WHERE employee_id= :employee_id""",
                  {'employee_id': employee.employee_id, 'name': employee.name, 'phone': phone, 'age': employee.age, 'role': employee.role})


def update_age(employee, age):
    with conn:
        c.execute("""UPDATE employees SET age=:age
                     WHERE employee_id= :employee_id""",
                  {'employee_id': employee.employee_id, 'name': employee.name, 'phone': employee.phone, 'age': age, 'role': employee.role})


def update_role(employee, role):
    with conn:
        c.execute("""UPDATE employees SET role=:role
                     WHERE employee_id= :employee_id""",
                  {'employee_id': employee.employee_id, 'name': employee.name, 'phone': employee.phone, 'age': employee.age, 'role': role})


def remove_emp(employee):
    with conn:
        c.execute("DELETE from employees where employee_id= :employee_id",
                  {'employee_id': employee.employee_id})


def delete_emp(name):
    with conn:
        emps = sqldb.get_emps_by_name(name)
        if emps:
            c.execute("DELETE from employees where name=:name",
                      {'name': name})
            print(name + " deleted from DB")
        else:
            print(name + " does not exist in DB nothing to delete")


def add_employee_attendance_to_DB(employee_id):
    t = datetime.now()
    # t = time.localtime()
    current_date = time.strftime("%Y:%m:%d", t)
    current_time = time.strftime("%H:%M", t)
    with conn:
        if get_emps_by_id_employee(employee_id):
            c.execute(
                "UPDATE employees SET time=current_time WHERE employee_id=:employee_id", {'employee_id': employee_id})
            c.execute(
                "UPDATE employees SET date=current_date WHERE employee_id=:employee_id", {'employee_id': employee_id})
            print("Employee " + employee_id + " attendance updated in DB")
        else:
            print("Employee " + employee_id +
                  " does not exist in DB nothing to update")


def add_managers_to_managers_db():
    """
    This function add managers to managers db.
    :return: Add managers to managers db.
    :rtype: None
    """
    i = 0
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        if row[4] == "manager":
            new_employee = employee.Employee(
                str(row[1]), str(row[2]), int(row[3]), str(row[4]))
            insert_manager(new_employee)
            i += 1

    if i > 0:
        utils.logging.info("Added Manager id: " + str(new_employee.get_employee_id()) +
                           " and manager name: " + str(new_employee.get_name()) + " Managers DB ")
        print(str(i) + " Managers were added to the Managers DB")
    else:
        print("Nothing added to Manager DB")


def generate_attendance_report_db(employee_id):
    """
    This function generate attendance report for employee in the last month.
    :return: Generate attendance report for employee in the last month.
    :rtype: None
    """
    i = 1
    t = time.localtime()
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role", "Date", "Time"]
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees WHERE employee_id=:employee_id",
                {'employee_id': employee_id})
    rows = cur.fetchall()
    for row in rows:
        lines.append(int(row[0]))
        table.append(row)
        i += 1

    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees attendance report created ")
    else:
        print("Nothing added to attendance report")


def generate_attendance_managers_report_db():
    """
    This function generate attendance report for managers in the last month.
    :return: Generate attendance report for managers in the last month.
    :rtype: None
    """
    i = 1
    t = time.localtime()
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role", "Date", "Time"]
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        if row[4] == "manager":
            lines.append(int(row[0]))
            table.append(row)
            i += 1

    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Managers attendance report created ")
    else:
        print("Nothing added to managers attendance report")


def generate_attendance_month_report():
    """
    This function generate attendance report for employee in the last month.
    :return: Generate attendance report for employee in the last month.
    :rtype: None
    """
    i = 1
    t = time.localtime()
    current_month = time.strftime("%m", t)
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role", "Date", "Time"]
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        my_month = row[5][5]+row[5][6]
        if current_month == my_month:
            lines.append(int(row[0]))
            table.append(row)
            i += 1

    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees attendance month report created ")
    else:
        print("Nothing added to month attendance report")


def generate_attendance_late_report_db():
    """
    This function generate attendance report for employee in the last month.
    :return: Generate attendance report for employee in the last month.
    :rtype: None
    """
    i = 1
    nine = "9:30"
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role", "Date", "Time"]
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        hour = row[6][0]+row[6][1]
        minute = row[6][3] + row[6][4]
        if int(hour) > 9 or (int(hour) == 9 and int(minute) > 30):
            lines.append(int(row[0]))
            table.append(row)
            i += 1

    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees late attendance report created ")
    else:
        print("Nothing added to late attendance report")


def generate_attendance_given_date_report(from_date):
    i = 1
    lines = []
    table = []
    headers = ["Employee_id", "Name", "Phone", "Age", "Role", "Date", "Time"]
    cur = conn.cursor()
    cur.execute("SELECT * FROM employees")
    rows = cur.fetchall()
    for row in rows:
        my_date = row[5]
        if my_date == from_date:
            lines.append(int(row[0]))
            table.append(row)
            i += 1

    if i > 1:
        print(tabulate(table, headers, tablefmt="pipe"))
        print("Employees given date attendance report created ")
    else:
        print("Nothing added to given date attendance report")

# conn.close()
