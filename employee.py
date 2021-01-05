import datetime
from datetime import datetime
import logging
import csv

from itertools import count


class Employee():
    # initialize the attributes
    _ids = count(1)
    # def __init__(self, employee_id,name, phone,age,role=junior):

    def __init__(self, name, phone, age, role="junior"):
        self.employee_id = next(self._ids)
        self.name = name
        self.phone = phone
        self.age = age
        self.role = role

    # set the attributes
    def set_employee_id(self):
        self.employee_id = next(self._ids)

    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_age(self, age):
        if not (age > 0):
            raise Exception("age must be greater than zero")
        self.age = age

    def set_role(self, role):
        self.role = role

    # return the attributes
    def get_employee_id(self):
        # return Employee.empId
        return self.employee_id

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_age(self):
        return self.age

    def get_role(self):
        return self.role
    # return the objects state as a string

    def __str__(self):
        result = "Employee_id: " + str(self.get_employee_id()) + \
            ", Name: " + self.get_name() + \
            ", Phone: " + self.get_phone() + \
            ", Age: " + str(self.get_age()) + \
            ", Role: " + self.get_role()
        return result

    # Work wth csv file
    # Create Employee.csv with following columns: Employee_id, Name, Phone, Age
    def update_csv_manually(self, employee_file_path):
        """
         This function add a new employee to the Employee file.
         :param employee_file_path: employee file path to the csv file 
         :type employee_file_path: string
         :return: Add a new employee to the Employee file.
         :rtype: None
         """
        with open(employee_file_path, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([self.get_employee_id(), self.get_name(
            ), self.get_phone(), self.get_age(), self.get_role()])


class Manager(Employee):
    def __init__(self, name, phone, age, role="manager"):
        super().__init__(name=name, phone=phone, age=age)
        self.role = role


class Senior(Employee):
    def __init__(self, name, phone, age, role="senior"):
        super().__init__(name=name, phone=phone, age=age)
        self.role = role
